#!/usr/bin/env python3
"""Structural epistemic verifier for Novel OS Reliability Layer v2.

Validates Evidence Packet / Claim Ledger structure and requires SQLite evidence
to pass Evidence Guard. It deliberately does NOT claim that cited evidence
semantically proves a claim.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

from evidence_guard import validate_packet_data

ALLOWED_STATUSES = {
    "DIRECT_SOURCE",
    "SOURCE_SUPPORTED_INFERENCE",
    "UNRESOLVED",
    "ADAPTATION_DECISION",
    "NOVELIZATION_BRIDGE",
}
ALLOWED_DURABILITY = {"ephemeral", "durable"}
ALLOWED_PROMOTION = {"author_approval_required", "author_approved", "blocked"}
EV_ID_RE = re.compile(r"^EV-[A-Za-z0-9_-]+$")
CL_ID_RE = re.compile(r"^CL-[A-Za-z0-9_-]+$")
APPROVAL_RE = re.compile(
    r"^-\s*\[x\]\s+.*Phê\s+chuẩn.*Canon\s+Diff.*$",
    re.IGNORECASE | re.MULTILINE,
)


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


def validate_evidence_structure(
    path: Path, data: dict[str, Any]
) -> tuple[set[str], list[str]]:
    items = data.get("evidence")
    if not isinstance(items, list):
        return set(), [f"{path}: 'evidence' must be an array"]

    ids: set[str] = set()
    errors: list[str] = []
    for idx, item in enumerate(items, 1):
        where = f"{path}: evidence[{idx}]"
        if not isinstance(item, dict):
            errors.append(f"{where} must be an object")
            continue

        evid = item.get("evidence_id")
        if not isinstance(evid, str) or not evid.strip():
            errors.append(f"{where}: missing non-empty evidence_id")
        elif not EV_ID_RE.match(evid):
            errors.append(f"{where}: invalid evidence_id '{evid}' (expected EV-...)")
        elif evid in ids:
            errors.append(f"{where}: duplicate evidence_id '{evid}'")
        else:
            ids.add(evid)

        source_kind = item.get("source_kind")
        if not isinstance(source_kind, str) or not source_kind.strip():
            errors.append(f"{where}: source_kind must be a non-empty string")

        locator = item.get("locator")
        if not isinstance(locator, dict) or not locator:
            errors.append(f"{where}: locator must be a non-empty object")

        field = item.get("field")
        if not isinstance(field, str) or not field.strip():
            errors.append(f"{where}: field must be a non-empty string")

        excerpt = item.get("excerpt")
        if not isinstance(excerpt, str) or not excerpt.strip():
            errors.append(f"{where}: excerpt must be a non-empty string")

    return ids, errors


def validate_approval_ref(where: str, approval_ref: Any) -> list[str]:
    errors: list[str] = []
    if not isinstance(approval_ref, str) or not approval_ref.strip():
        return [f"{where}: promotion='author_approved' requires non-empty approval_ref"]

    path = Path(approval_ref)
    if path.is_absolute() or ".." in path.parts:
        return [f"{where}: approval_ref must be a repository-relative path"]
    if not path.is_file():
        return [f"{where}: approval_ref does not exist: {approval_ref}"]

    text = path.read_text(encoding="utf-8")
    if not APPROVAL_RE.search(text):
        errors.append(
            f"{where}: approval_ref {approval_ref} does not contain a checked "
            "author Canon Diff approval line"
        )
    return errors


def validate_claims(
    path: Path,
    data: dict[str, Any],
    evidence_ids: set[str],
) -> list[str]:
    items = data.get("claims")
    if not isinstance(items, list):
        return [f"{path}: 'claims' must be an array"]

    ids: set[str] = set()
    errors: list[str] = []
    for idx, item in enumerate(items, 1):
        where = f"{path}: claims[{idx}]"
        if not isinstance(item, dict):
            errors.append(f"{where} must be an object")
            continue

        claim_id = item.get("claim_id")
        if not isinstance(claim_id, str) or not claim_id.strip():
            errors.append(f"{where}: missing non-empty claim_id")
        elif not CL_ID_RE.match(claim_id):
            errors.append(f"{where}: invalid claim_id '{claim_id}' (expected CL-...)")
        elif claim_id in ids:
            errors.append(f"{where}: duplicate claim_id '{claim_id}'")
        else:
            ids.add(claim_id)

        proposition = item.get("claim")
        if not isinstance(proposition, str) or not proposition.strip():
            errors.append(f"{where}: claim must be an explicit non-empty proposition")

        status = item.get("epistemic_status")
        if status not in ALLOWED_STATUSES:
            errors.append(
                f"{where}: epistemic_status must be one of "
                f"{sorted(ALLOWED_STATUSES)}, got {status!r}"
            )

        refs = item.get("evidence", [])
        if not isinstance(refs, list) or any(not isinstance(x, str) for x in refs):
            errors.append(f"{where}: evidence must be an array of evidence IDs")
            refs = []
        else:
            for ref in refs:
                if ref not in evidence_ids:
                    errors.append(f"{where}: references unknown evidence_id '{ref}'")

        durability = item.get("durability")
        if durability not in ALLOWED_DURABILITY:
            errors.append(
                f"{where}: durability must be one of "
                f"{sorted(ALLOWED_DURABILITY)}, got {durability!r}"
            )

        promotion = item.get("promotion")
        if promotion not in ALLOWED_PROMOTION:
            errors.append(
                f"{where}: promotion must be one of "
                f"{sorted(ALLOWED_PROMOTION)}, got {promotion!r}"
            )

        reasoning = item.get("reasoning", "")
        if reasoning is not None and not isinstance(reasoning, str):
            errors.append(f"{where}: reasoning must be a string when present")
            reasoning = ""

        if promotion == "author_approved":
            errors.extend(validate_approval_ref(where, item.get("approval_ref")))
        elif item.get("approval_ref"):
            errors.append(
                f"{where}: approval_ref is only valid when promotion='author_approved'"
            )

        if status == "DIRECT_SOURCE":
            if not refs:
                errors.append(f"{where}: DIRECT_SOURCE requires at least one evidence ID")
            if promotion not in {"author_approval_required", "author_approved"}:
                errors.append(
                    f"{where}: DIRECT_SOURCE requires author approval before durable canon promotion"
                )

        if status == "SOURCE_SUPPORTED_INFERENCE":
            if not refs:
                errors.append(f"{where}: SOURCE_SUPPORTED_INFERENCE requires evidence")
            if not isinstance(reasoning, str) or not reasoning.strip():
                errors.append(
                    f"{where}: SOURCE_SUPPORTED_INFERENCE requires non-empty reasoning"
                )
            if promotion not in {"author_approval_required", "author_approved"}:
                errors.append(
                    f"{where}: SOURCE_SUPPORTED_INFERENCE requires author approval"
                )

        if status == "UNRESOLVED" and promotion != "blocked":
            errors.append(f"{where}: UNRESOLVED claims must use promotion='blocked'")

        if status in {"ADAPTATION_DECISION", "NOVELIZATION_BRIDGE"}:
            if promotion not in {"author_approval_required", "author_approved"}:
                errors.append(
                    f"{where}: {status} requires author approval before durable canon promotion"
                )

        if durability == "durable" and status == "UNRESOLVED":
            errors.append(f"{where}: unresolved material cannot be declared durable truth")

    return errors


def validate_pair(
    evidence_path: Path,
    claims_path: Path,
    db_path: str | Path | None = None,
) -> list[str]:
    errors: list[str] = []
    evidence_data, errs = load_json(evidence_path)
    errors.extend(errs)
    claims_data, errs = load_json(claims_path)
    errors.extend(errs)
    if evidence_data is None or claims_data is None:
        return errors

    ev_ch = str(evidence_data.get("chapter", "")).strip()
    cl_ch = str(claims_data.get("chapter", "")).strip()
    if not ev_ch:
        errors.append(f"{evidence_path}: missing chapter")
    if not cl_ch:
        errors.append(f"{claims_path}: missing chapter")
    if ev_ch and cl_ch and ev_ch != cl_ch:
        errors.append(
            f"Chapter mismatch: evidence packet is {ev_ch!r}, claim ledger is {cl_ch!r}"
        )

    evidence_ids, evidence_errors = validate_evidence_structure(
        evidence_path, evidence_data
    )
    errors.extend(evidence_errors)

    if not evidence_errors:
        errors.extend(
            validate_packet_data(
                evidence_path,
                evidence_data,
                db_path=db_path,
            )
        )

    errors.extend(validate_claims(claims_path, claims_data, evidence_ids))
    return errors


def paths_for_chapter(chapter: str) -> tuple[Path, Path]:
    return (
        Path("research") / "evidence" / f"chapter_{chapter}.json",
        Path("research") / "claims" / f"chapter_{chapter}.json",
    )


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Validate Evidence Packet / Claim Ledger structure, SQLite source locators, "
            "and recorded author approval refs. Does not prove semantic entailment."
        )
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--chapter", help="Chapter suffix, e.g. 10, 08a")
    group.add_argument("--all", action="store_true", help="Validate every research/claims/chapter_*.json")
    parser.add_argument("--evidence", help="Override Evidence Packet path (only with --chapter)")
    parser.add_argument("--claims", help="Override Claim Ledger path (only with --chapter)")
    parser.add_argument("--db", help="Override story_database.sqlite3 path")
    args = parser.parse_args()

    pairs: list[tuple[Path, Path]] = []
    if args.chapter:
        evidence_path, claims_path = paths_for_chapter(args.chapter)
        if args.evidence:
            evidence_path = Path(args.evidence)
        if args.claims:
            claims_path = Path(args.claims)
        pairs.append((evidence_path, claims_path))
    else:
        claim_dir = Path("research") / "claims"
        if not claim_dir.exists():
            print("[CLAIM-GUARD] No research/claims directory; nothing to validate.")
            return 0
        for claims_path in sorted(claim_dir.glob("chapter_*.json")):
            suffix = claims_path.stem.removeprefix("chapter_")
            evidence_path, _ = paths_for_chapter(suffix)
            pairs.append((evidence_path, claims_path))

    if not pairs:
        print("[CLAIM-GUARD] No claim ledgers found; nothing to validate.")
        return 0

    all_errors: list[str] = []
    for evidence_path, claims_path in pairs:
        print(f"=== CLAIM CONTRACT: {claims_path} ===")
        errors = validate_pair(evidence_path, claims_path, args.db)
        if errors:
            all_errors.extend(errors)
            for err in errors:
                print(f"  [FAIL] {err}")
        else:
            print(
                "  [PASS] Evidence/claim structure, SQLite source locators, and any "
                "recorded author approval refs are consistent. Semantic entailment "
                "still requires source-aware review."
            )

    if all_errors:
        print(f"\n[CLAIM-GUARD FAILED] {len(all_errors)} epistemic/source issue(s).")
        return 1

    print("\n[CLAIM-GUARD PASS] Structural/source/recorded-approval contracts satisfied.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
