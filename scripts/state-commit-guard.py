#!/usr/bin/env python3
"""Forward-only durable-state approval guard for Novel OS.

This guard does not audit historical repository state. It inspects a git changeset
(base -> head) and blocks NEW durable-state writes unless the same changeset also
contains at least one author-approved chapter Canon Diff.

It proves only that an approval checkbox is recorded in the changed Canon Diff.
It does not authenticate who ticked that checkbox and does not validate semantic
alignment between every ledger line and the Canon Diff.
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

DURABLE_PREFIXES = (
    "characters/",
    "worldbuilding/",
    "plot/",
)

CANON_DIFF_RE = re.compile(r"^revisions/chapter_(\d+[a-z]?)_canon_diff\.md$")
APPROVAL_RE = re.compile(
    r"^-\s*\[x\]\s+.*Phê\s+chuẩn.*Canon\s+Diff.*$",
    re.IGNORECASE | re.MULTILINE,
)


def run_git(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        text=True,
        capture_output=True,
        check=False,
    )


def changed_files(base: str, head: str) -> tuple[list[str], list[str]]:
    result = run_git(["diff", "--name-only", base, head])
    if result.returncode != 0:
        detail = result.stderr.strip() or result.stdout.strip() or "git diff failed"
        return [], [f"Unable to inspect changeset {base}..{head}: {detail}"]
    files = [line.strip() for line in result.stdout.splitlines() if line.strip()]
    return files, []


def is_durable_state(path: str) -> bool:
    return path.startswith(DURABLE_PREFIXES)


def approval_errors(diff_path: Path) -> list[str]:
    if not diff_path.is_file():
        return [f"Changed Canon Diff is missing from working tree: {diff_path}"]
    text = diff_path.read_text(encoding="utf-8")
    if not APPROVAL_RE.search(text):
        return [
            f"{diff_path}: missing checked author approval line "
            "(`- [x] ... Phê chuẩn ... Canon Diff ...`)."
        ]
    return []


def validate_changeset(base: str, head: str = "HEAD") -> list[str]:
    files, errors = changed_files(base, head)
    if errors:
        return errors

    durable = sorted(path for path in files if is_durable_state(path))
    if not durable:
        return []

    changed_diffs = sorted(path for path in files if CANON_DIFF_RE.match(path))
    if not changed_diffs:
        return [
            "Durable canon/state files changed without a chapter Canon Diff in the same changeset. "
            f"Changed durable files: {', '.join(durable)}"
        ]

    for path in changed_diffs:
        errors.extend(approval_errors(Path(path)))

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Block new durable-state writes unless the same git changeset includes "
            "an author-approved chapter Canon Diff. Historical state is not audited."
        )
    )
    parser.add_argument("--base", required=True, help="Base commit/ref for forward-only diff")
    parser.add_argument("--head", default="HEAD", help="Head commit/ref (default: HEAD)")
    args = parser.parse_args()

    errors = validate_changeset(args.base, args.head)
    if errors:
        print("[STATE-COMMIT-GUARD FAILED]")
        for error in errors:
            print(f"  - {error}")
        return 1

    print(
        "[STATE-COMMIT-GUARD PASS] No unapproved durable-state write was detected "
        "in the selected changeset. Historical state was not re-audited."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
