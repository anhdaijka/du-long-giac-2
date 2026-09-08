#!/usr/bin/env python3
"""Forward-only durable-state promotion guard for Novel OS Reliability v2.

This guard does not re-audit historical repository state. It inspects one git
changeset (base -> head) and blocks NEW durable-state writes unless the relevant
chapter promotion has the lightweight prerequisites already required by the
workflow:

1. a changed Author-approved chapter Canon Diff;
2. a current v2 full-read review with reviewer verdict APPROVED;
3. a valid Evidence Packet + Claim Ledger pair;
4. when the chapter manuscript changed in this same changeset, its v2 review must
   also have changed, preventing an unchanged old review from authorizing new prose.

The guard deliberately does not use manuscript hashes or immutable revisions.
It proves recorded workflow prerequisites, not semantic truth and not the human
identity behind an approval checkbox.
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


def run(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, text=True, capture_output=True, check=False)


def run_git(args: list[str]) -> subprocess.CompletedProcess[str]:
    return run(["git", *args])


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


def find_v2_review(chapter: str) -> tuple[Path | None, list[str]]:
    preferred = Path("reviews") / f"chapter_{chapter}_review_v2.md"
    if preferred.is_file():
        return preferred, []

    root = Path("reviews")
    candidates = sorted(root.glob(f"**/chapter_{chapter}_review_v2.md")) if root.exists() else []
    if not candidates:
        return None, [
            f"Chapter {chapter} durable promotion requires a current v2 review "
            f"(`reviews/**/chapter_{chapter}_review_v2.md`)."
        ]
    if len(candidates) > 1:
        rendered = ", ".join(str(path) for path in candidates)
        return None, [
            f"Chapter {chapter} has multiple v2 review candidates ({rendered}). "
            f"Keep the promotion review unambiguous, preferably reviews/chapter_{chapter}_review_v2.md."
        ]
    return candidates[0], []


def verify_review(chapter: str, review_path: Path) -> list[str]:
    script = Path("scripts") / "review-guard.py"
    if not script.is_file():
        return ["Missing scripts/review-guard.py required for state promotion verification"]
    result = run(
        [
            sys.executable,
            str(script),
            "--chapter-number",
            chapter,
            "--review",
            str(review_path),
            "--require-approval",
        ]
    )
    if result.returncode == 0:
        return []
    detail = (result.stdout + "\n" + result.stderr).strip()
    return [
        f"Chapter {chapter} v2 review is not structurally APPROVED by Review Guard: "
        f"{review_path}\n{detail}"
    ]


def verify_claim_contract(chapter: str) -> list[str]:
    script = Path("scripts") / "claim-guard.py"
    if not script.is_file():
        return ["Missing scripts/claim-guard.py required for state promotion verification"]
    result = run([sys.executable, str(script), "--chapter", chapter])
    if result.returncode == 0:
        return []
    detail = (result.stdout + "\n" + result.stderr).strip()
    return [
        f"Chapter {chapter} Evidence/Claim contract does not pass Claim Guard.\n{detail}"
    ]


def chapter_prerequisite_errors(chapter: str, changed: set[str]) -> list[str]:
    errors: list[str] = []
    review_path, review_errors = find_v2_review(chapter)
    errors.extend(review_errors)
    if review_path is None:
        return errors

    chapter_path = f"chapters/chapter_{chapter}.md"
    review_rel = review_path.as_posix()
    if chapter_path in changed and review_rel not in changed:
        errors.append(
            f"{chapter_path} changed in this promotion changeset but {review_rel} did not. "
            "Re-read the current manuscript and update its v2 review before canon/state promotion."
        )

    errors.extend(verify_review(chapter, review_path))
    errors.extend(verify_claim_contract(chapter))
    return errors


def validate_changeset(base: str, head: str = "HEAD") -> list[str]:
    files, errors = changed_files(base, head)
    if errors:
        return errors

    changed = set(files)
    durable = sorted(path for path in files if is_durable_state(path))
    if not durable:
        return []

    changed_diff_pairs = sorted(
        (path, match.group(1))
        for path in files
        if (match := CANON_DIFF_RE.match(path))
    )
    if not changed_diff_pairs:
        return [
            "Durable canon/state files changed without a chapter Canon Diff in the same changeset. "
            f"Changed durable files: {', '.join(durable)}"
        ]

    chapters: list[str] = []
    for path, chapter in changed_diff_pairs:
        errors.extend(approval_errors(Path(path)))
        chapters.append(chapter)

    # Only run downstream promotion prerequisites after every changed Canon Diff
    # has a recorded checked approval marker. This keeps failure output focused.
    if errors:
        return errors

    for chapter in sorted(set(chapters)):
        errors.extend(chapter_prerequisite_errors(chapter, changed))

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Block new durable-state promotion unless the changeset contains an "
            "approved Canon Diff and the corresponding v2 review + claim contract pass. "
            "Historical state is not re-audited."
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
        "[STATE-COMMIT-GUARD PASS] Forward durable-state promotion prerequisites "
        "are recorded and verifier-backed for the selected changeset. Historical "
        "state was not re-audited; semantic truth is not implied."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
