#!/usr/bin/env python3
"""SQLite source-evidence verifier for Novel OS Reliability Layer v2.

This tool proves only that an Evidence Packet points to one concrete SQLite row
and that its excerpt is present in the declared source field. It does NOT prove
that the evidence semantically entails a claim.
"""
from __future__ import annotations

import argparse
import json
import re
import sqlite3
import sys
import unicodedata
from pathlib import Path
from typing import Any

DB_CANDIDATES = (
    Path("story_database.sqlite3"),
    Path("migration/source_corpus/01_Database/story_database.sqlite3"),
)
IDENTIFIER_RE = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")
ALIASES = {
    "subtask_id": "sub_id",
    "dialogue_id": "id",
    "step_id": "id",
}
REQUIRED_LOCATORS = {
    "tasks": {"task_id"},
    "subtasks": {"task_id", "sub_id"},
    "dialogues": {"sub_id", "phase"},
    "steps": {"sub_id", "step_index"},
}
ALLOWED_MATCH_MODES = {"contains_normalized", "exact_normalized"}


def load_json(path: Path) -> tuple[dict[str, Any] | None, list[str]]:
    if not path.is_file():
        return None, [f"Missing file: {path}"]
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return None, [
            f"{path}: invalid JSON at line {exc.lineno}, column {exc.colno}: {exc.msg}"
        ]
    if not isinstance(data, dict):
        return None, [f"{path}: root must be a JSON object"]
    return data, []


def find_db(explicit: str | Path | None = None) -> Path | None:
    if explicit:
        path = Path(explicit)
        return path if path.is_file() else None
    for candidate in DB_CANDIDATES:
        if candidate.is_file():
            return candidate
    return None


def normalize_text(value: str) -> str:
    value = unicodedata.normalize("NFC", value)
    value = value.replace("\r\n", "\n").replace("\r", "\n")
    return " ".join(value.split())


def quote_identifier(name: str) -> str:
    if not IDENTIFIER_RE.fullmatch(name):
        raise ValueError(f"unsafe SQL identifier: {name!r}")
    return f'"{name}"'


def table_columns(conn: sqlite3.Connection, table: str) -> set[str]:
    qtable = quote_identifier(table)
    return {row[1] for row in conn.execute(f"PRAGMA table_info({qtable})")}


def normalized_locator(
    table: str, locator: dict[str, Any], columns: set[str], where: str
) -> tuple[dict[str, Any], list[str]]:
    errors: list[str] = []
    resolved: dict[str, Any] = {}

    for raw_key, value in locator.items():
        if not isinstance(raw_key, str) or not IDENTIFIER_RE.fullmatch(raw_key):
            errors.append(f"{where}: invalid locator key {raw_key!r}")
            continue
        key = ALIASES.get(raw_key, raw_key)
        if key not in columns:
            errors.append(
                f"{where}: locator field {raw_key!r} resolves to unknown column {key!r}"
            )
            continue
        if isinstance(value, (dict, list)) or value is None:
            errors.append(f"{where}: locator value for {raw_key!r} must be scalar and non-null")
            continue
        if key in resolved and resolved[key] != value:
            errors.append(f"{where}: conflicting locator values for column {key!r}")
            continue
        resolved[key] = value

    required = REQUIRED_LOCATORS.get(table, set())
    missing = sorted(required - set(resolved))
    if missing:
        errors.append(
            f"{where}: locator for sqlite.{table} must include {', '.join(missing)} "
            "(aliases such as subtask_id are accepted)"
        )

    return resolved, errors


def verify_item(
    conn: sqlite3.Connection,
    path: Path,
    item: dict[str, Any],
    index: int,
) -> list[str]:
    where = f"{path}: evidence[{index}]"
    errors: list[str] = []

    source_kind = item.get("source_kind")
    if not isinstance(source_kind, str) or not source_kind.startswith("sqlite."):
        return [f"{where}: Evidence Guard currently supports source_kind='sqlite.<table>' only"]

    table = source_kind.removeprefix("sqlite.")
    if not IDENTIFIER_RE.fullmatch(table):
        return [f"{where}: invalid SQLite table name {table!r}"]

    exists = conn.execute(
        "SELECT 1 FROM sqlite_master WHERE type='table' AND name=?",
        (table,),
    ).fetchone()
    if not exists:
        return [f"{where}: SQLite table {table!r} does not exist"]

    columns = table_columns(conn, table)
    locator = item.get("locator")
    if not isinstance(locator, dict) or not locator:
        return [f"{where}: locator must be a non-empty object"]

    resolved, locator_errors = normalized_locator(table, locator, columns, where)
    errors.extend(locator_errors)
    if locator_errors:
        return errors

    field = item.get("field")
    if not isinstance(field, str) or not field.strip():
        errors.append(
            f"{where}: sqlite evidence requires a non-empty 'field' so excerpt matching "
            "cannot drift across unrelated columns"
        )
        return errors
    field = ALIASES.get(field.strip(), field.strip())
    if field not in columns:
        errors.append(f"{where}: field {field!r} does not exist in sqlite.{table}")
        return errors

    clauses = [f"{quote_identifier(key)} = ?" for key in resolved]
    params = [resolved[key] for key in resolved]
    query = (
        f"SELECT * FROM {quote_identifier(table)} WHERE "
        + " AND ".join(clauses)
        + " LIMIT 2"
    )

    rows = conn.execute(query, params).fetchall()
    if not rows:
        errors.append(
            f"{where}: locator resolved to 0 rows in sqlite.{table}: {locator!r}"
        )
        return errors
    if len(rows) > 1:
        errors.append(
            f"{where}: locator is ambiguous (>1 row) in sqlite.{table}: {locator!r}"
        )
        return errors

    row = rows[0]
    source_value = row[field]
    if not isinstance(source_value, str):
        errors.append(
            f"{where}: declared excerpt field {field!r} is not textual for the resolved row"
        )
        return errors

    excerpt = item.get("excerpt")
    if not isinstance(excerpt, str) or not excerpt.strip():
        errors.append(f"{where}: excerpt must be a non-empty string")
        return errors

    match_mode = item.get("match", "contains_normalized")
    if match_mode not in ALLOWED_MATCH_MODES:
        errors.append(
            f"{where}: match must be one of {sorted(ALLOWED_MATCH_MODES)}, got {match_mode!r}"
        )
        return errors

    normalized_source = normalize_text(source_value)
    normalized_excerpt = normalize_text(excerpt)
    matched = (
        normalized_excerpt == normalized_source
        if match_mode == "exact_normalized"
        else normalized_excerpt in normalized_source
    )
    if not matched:
        errors.append(
            f"{where}: excerpt does not match sqlite.{table}.{field} at locator {locator!r}"
        )

    return errors


def validate_packet_data(
    path: Path,
    data: dict[str, Any],
    db_path: str | Path | None = None,
) -> list[str]:
    items = data.get("evidence")
    if not isinstance(items, list):
        return [f"{path}: 'evidence' must be an array"]

    resolved_db = find_db(db_path)
    if resolved_db is None:
        requested = str(db_path) if db_path else " or ".join(str(p) for p in DB_CANDIDATES)
        return [f"{path}: source database not found ({requested})"]

    errors: list[str] = []
    try:
        conn = sqlite3.connect(resolved_db)
        conn.row_factory = sqlite3.Row
        for idx, item in enumerate(items, 1):
            if not isinstance(item, dict):
                errors.append(f"{path}: evidence[{idx}] must be an object")
                continue
            errors.extend(verify_item(conn, path, item, idx))
    except sqlite3.Error as exc:
        errors.append(f"{path}: SQLite verification error: {exc}")
    finally:
        try:
            conn.close()
        except UnboundLocalError:
            pass
    return errors


def validate_packet_against_db(
    path: Path,
    db_path: str | Path | None = None,
    data: dict[str, Any] | None = None,
) -> list[str]:
    if data is None:
        data, errors = load_json(path)
        if data is None:
            return errors
    return validate_packet_data(path, data, db_path)


def path_for_chapter(chapter: str) -> Path:
    return Path("research") / "evidence" / f"chapter_{chapter}.json"


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Verify that Evidence Packet locators resolve to concrete SQLite rows and "
            "their excerpts match declared source fields. Does not prove claim entailment."
        )
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--chapter", help="Chapter suffix, e.g. 09, 08a")
    group.add_argument("--all", action="store_true", help="Verify every research/evidence/chapter_*.json")
    group.add_argument("--evidence", help="Verify one explicit Evidence Packet path")
    parser.add_argument("--db", help="Override story_database.sqlite3 path")
    args = parser.parse_args()

    if args.chapter:
        targets = [path_for_chapter(args.chapter)]
    elif args.evidence:
        targets = [Path(args.evidence)]
    else:
        evidence_dir = Path("research") / "evidence"
        if not evidence_dir.exists():
            print("[EVIDENCE-GUARD] No research/evidence directory; nothing to verify.")
            return 0
        targets = sorted(evidence_dir.glob("chapter_*.json"))

    if not targets:
        print("[EVIDENCE-GUARD] No Evidence Packets found; nothing to verify.")
        return 0

    all_errors: list[str] = []
    for path in targets:
        print(f"=== SOURCE EVIDENCE: {path} ===")
        errors = validate_packet_against_db(path, args.db)
        if errors:
            all_errors.extend(errors)
            for error in errors:
                print(f"  [FAIL] {error}")
        else:
            print(
                "  [PASS] Every SQLite locator resolves uniquely and each excerpt matches "
                "its declared source field. Claim meaning is not evaluated here."
            )

    if all_errors:
        print(f"\n[EVIDENCE-GUARD FAILED] {len(all_errors)} source-evidence issue(s).")
        return 1

    print("\n[EVIDENCE-GUARD PASS] SQLite locator/excerpt contract satisfied.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
