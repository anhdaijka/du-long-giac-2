#!/usr/bin/env python3
"""Verifier-owned execution completion for Novel OS Reliability Layer v2.

Execution manifests describe deliverables and deterministic acceptance checks. They
never store completion status. This guard computes COMPLETE / INCOMPLETE / BLOCKED
at runtime and rejects self-certified status fields.

The manifest is intentionally not a general workflow engine: arbitrary shell
commands are forbidden. Only a small allowlist of check types is supported.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
ALLOWED_CHECKS = {"file_exists", "file_nonempty", "evidence", "claim", "review"}
FORBIDDEN_STATUS_KEYS = {"status", "state", "done", "complete", "completed"}


def load_manifest(path: Path) -> tuple[dict[str, Any] | None, list[str]]:
    if not path.is_file():
        return None, [f"Missing execution manifest: {path}"]
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return None, [
            f"{path}: invalid JSON at line {exc.lineno}, column {exc.colno}: {exc.msg}"
        ]
    if not isinstance(data, dict):
        return None, [f"{path}: root must be a JSON object"]
    return data, []


def schema_errors(path: Path, data: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    forbidden_root = sorted(FORBIDDEN_STATUS_KEYS.intersection(data))
    if forbidden_root:
        errors.append(
            f"{path}: completion is verifier-owned; remove self-certified field(s): "
            + ", ".join(forbidden_root)
        )

    manifest_id = data.get("manifest_id")
    if not isinstance(manifest_id, str) or not manifest_id.strip():
        errors.append(f"{path}: manifest_id must be a non-empty string")

    deliverables = data.get("deliverables")
    if not isinstance(deliverables, list) or not deliverables:
        return errors + [f"{path}: deliverables must be a non-empty array"]

    ids: set[str] = set()
    for idx, item in enumerate(deliverables, 1):
        where = f"{path}: deliverables[{idx}]"
        if not isinstance(item, dict):
            errors.append(f"{where} must be an object")
            continue

        forbidden = sorted(FORBIDDEN_STATUS_KEYS.intersection(item))
        if forbidden:
            errors.append(
                f"{where}: completion is verifier-owned; remove self-certified field(s): "
                + ", ".join(forbidden)
            )

        did = item.get("id")
        if not isinstance(did, str) or not did.strip():
            errors.append(f"{where}: id must be a non-empty string")
        elif did in ids:
            errors.append(f"{where}: duplicate deliverable id {did!r}")
        else:
            ids.add(did)

        description = item.get("description")
        if not isinstance(description, str) or not description.strip():
            errors.append(f"{where}: description must be a non-empty string")

        requires = item.get("requires", [])
        if not isinstance(requires, list) or any(not isinstance(x, str) for x in requires):
            errors.append(f"{where}: requires must be an array of deliverable IDs")

        checks = item.get("checks")
        if not isinstance(checks, list) or not checks:
            errors.append(f"{where}: checks must be a non-empty array")
            continue

        for cidx, check in enumerate(checks, 1):
            cwhere = f"{where}.checks[{cidx}]"
            if not isinstance(check, dict):
                errors.append(f"{cwhere} must be an object")
                continue
            ctype = check.get("type")
            if ctype not in ALLOWED_CHECKS:
                errors.append(
                    f"{cwhere}: type must be one of {sorted(ALLOWED_CHECKS)}, got {ctype!r}"
                )
                continue
            if ctype in {"file_exists", "file_nonempty"}:
                value = check.get("path")
                if not isinstance(value, str) or not value.strip():
                    errors.append(f"{cwhere}: {ctype} requires non-empty path")
            if ctype in {"evidence", "claim", "review"}:
                chapter = check.get("chapter")
                if not isinstance(chapter, str) or not chapter.strip():
                    errors.append(f"{cwhere}: {ctype} requires non-empty chapter")
            if ctype == "review" and "require_approval" in check and not isinstance(
                check.get("require_approval"), bool
            ):
                errors.append(f"{cwhere}: require_approval must be boolean when present")

    # Dependency validation is separate so forward references are allowed.
    for idx, item in enumerate(deliverables, 1):
        if not isinstance(item, dict):
            continue
        did = item.get("id")
        requires = item.get("requires", [])
        if not isinstance(requires, list):
            continue
        for dep in requires:
            if not isinstance(dep, str):
                continue
            if dep not in ids:
                errors.append(
                    f"{path}: deliverable {did!r} requires unknown deliverable {dep!r}"
                )
            if dep == did:
                errors.append(f"{path}: deliverable {did!r} cannot require itself")

    # Detect dependency cycles without introducing a workflow engine.
    graph = {
        item["id"]: list(item.get("requires", []))
        for item in deliverables
        if isinstance(item, dict) and isinstance(item.get("id"), str)
        and isinstance(item.get("requires", []), list)
    }
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str) -> bool:
        if node in visiting:
            return True
        if node in visited:
            return False
        visiting.add(node)
        for dep in graph.get(node, []):
            if dep in graph and visit(dep):
                return True
        visiting.remove(node)
        visited.add(node)
        return False

    if any(visit(node) for node in graph):
        errors.append(f"{path}: deliverable dependency graph contains a cycle")

    return errors


def run_check(check: dict[str, Any]) -> tuple[bool, str]:
    ctype = check["type"]
    if ctype == "file_exists":
        path = Path(check["path"])
        ok = path.is_file()
        return ok, f"file exists: {path}" if ok else f"missing file: {path}"

    if ctype == "file_nonempty":
        path = Path(check["path"])
        ok = path.is_file() and path.stat().st_size > 0
        return ok, f"file non-empty: {path}" if ok else f"missing/empty file: {path}"

    chapter = check["chapter"]
    if ctype == "evidence":
        args = [sys.executable, str(SCRIPT_DIR / "evidence_guard.py"), "--chapter", chapter]
    elif ctype == "claim":
        args = [sys.executable, str(SCRIPT_DIR / "claim-guard.py"), "--chapter", chapter]
    else:
        args = [
            sys.executable,
            str(SCRIPT_DIR / "review-guard.py"),
            "--chapter-number",
            chapter,
        ]
        review_path = check.get("review")
        if isinstance(review_path, str) and review_path.strip():
            args.extend(["--review", review_path])
        if check.get("require_approval", False):
            args.append("--require-approval")

    result = subprocess.run(args, text=True, capture_output=True, check=False)
    if result.returncode == 0:
        return True, f"{ctype} verifier PASS for chapter {chapter}"
    detail = (result.stdout + "\n" + result.stderr).strip()
    return False, f"{ctype} verifier FAIL for chapter {chapter}: {detail}"


def evaluate(data: dict[str, Any]) -> tuple[list[dict[str, Any]], bool]:
    deliverables = data["deliverables"]
    by_id = {item["id"]: item for item in deliverables}
    results: dict[str, dict[str, Any]] = {}
    remaining = set(by_id)

    # Schema validation already guarantees an acyclic graph. Resolve in dependency order.
    while remaining:
        progress = False
        for did in list(remaining):
            item = by_id[did]
            deps = item.get("requires", [])
            if any(dep not in results for dep in deps):
                continue

            failed_deps = [dep for dep in deps if results[dep]["computed_status"] != "COMPLETE"]
            if failed_deps:
                result = {
                    "id": did,
                    "description": item["description"],
                    "computed_status": "BLOCKED",
                    "details": [f"blocked by incomplete dependency: {dep}" for dep in failed_deps],
                }
            else:
                details: list[str] = []
                checks_ok = True
                for check in item["checks"]:
                    ok, detail = run_check(check)
                    details.append(detail)
                    checks_ok = checks_ok and ok
                result = {
                    "id": did,
                    "description": item["description"],
                    "computed_status": "COMPLETE" if checks_ok else "INCOMPLETE",
                    "details": details,
                }
            results[did] = result
            remaining.remove(did)
            progress = True
        if not progress:
            # Defensive fallback; cycles should already have been rejected.
            for did in remaining:
                results[did] = {
                    "id": did,
                    "description": by_id[did]["description"],
                    "computed_status": "BLOCKED",
                    "details": ["dependency graph could not be resolved"],
                }
            break

    ordered = [results[item["id"]] for item in deliverables]
    all_complete = all(item["computed_status"] == "COMPLETE" for item in ordered)
    return ordered, all_complete


def print_report(path: Path, results: list[dict[str, Any]], all_complete: bool) -> None:
    print(f"=== EXECUTION MANIFEST: {path} ===")
    for item in results:
        print(f"  [{item['computed_status']}] {item['id']}: {item['description']}")
        for detail in item["details"]:
            print(f"    - {detail}")
    verdict = "COMPLETE" if all_complete else "INCOMPLETE"
    print(f"  => COMPUTED EXECUTION STATUS: {verdict}")


def discover_manifests() -> list[Path]:
    root = Path("execution")
    if not root.exists():
        return []
    return sorted(root.glob("*.json"))


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Compute execution completion from deliverables and allowlisted deterministic checks. "
            "Manifest status fields and arbitrary commands are forbidden."
        )
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--manifest", help="Execution manifest JSON path")
    group.add_argument("--all", action="store_true", help="Validate/report execution/*.json")
    parser.add_argument(
        "--require-complete",
        action="store_true",
        help="Return non-zero when any valid manifest has incomplete/blocked deliverables",
    )
    args = parser.parse_args()

    paths = [Path(args.manifest)] if args.manifest else discover_manifests()
    if not paths:
        print("[EXECUTION-GUARD] No execution manifests found; nothing to validate.")
        return 0

    schema_failed = False
    incomplete = False
    for path in paths:
        data, errors = load_manifest(path)
        if errors or data is None:
            schema_failed = True
            for error in errors:
                print(f"[EXECUTION-GUARD FAIL] {error}")
            continue

        errors = schema_errors(path, data)
        if errors:
            schema_failed = True
            for error in errors:
                print(f"[EXECUTION-GUARD FAIL] {error}")
            continue

        results, all_complete = evaluate(data)
        print_report(path, results, all_complete)
        incomplete = incomplete or not all_complete

    if schema_failed:
        print("\n[EXECUTION-GUARD FAILED] Invalid execution manifest contract.")
        return 1
    if args.require_complete and incomplete:
        print(
            "\n[EXECUTION-GUARD INCOMPLETE] One or more deliverables are not verifier-complete. "
            "The agent must not report the execution plan as finished."
        )
        return 1

    print(
        "\n[EXECUTION-GUARD PASS] Manifest contracts are valid. "
        + ("All deliverables are verifier-complete." if not incomplete else "Incomplete work is reported but not self-certified as done.")
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
