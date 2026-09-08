#!/usr/bin/env python3
"""Regression tests for author_approved Claim Ledger state."""
from __future__ import annotations

import json
import sqlite3
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CLAIM_GUARD = ROOT / "scripts" / "claim-guard.py"


def run(root: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(CLAIM_GUARD), "--chapter", "10"],
        cwd=root,
        text=True,
        capture_output=True,
        check=False,
    )


def assert_code(label: str, result: subprocess.CompletedProcess[str], expected: int) -> None:
    if result.returncode != expected:
        print(f"[FAIL] {label}: expected exit {expected}, got {result.returncode}")
        print(result.stdout)
        print(result.stderr)
        raise SystemExit(1)
    print(f"[PASS] {label}")


def make_fixture(root: Path) -> None:
    conn = sqlite3.connect(root / "story_database.sqlite3")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE subtasks (sub_id INTEGER PRIMARY KEY, task_id INTEGER, name TEXT, describe_cleaned TEXT)"
    )
    cur.execute(
        "INSERT INTO subtasks(sub_id, task_id, name, describe_cleaned) VALUES (?, ?, ?, ?)",
        (320, 157, "Source Row", "Verified source observation."),
    )
    conn.commit()
    conn.close()

    (root / "research" / "evidence").mkdir(parents=True, exist_ok=True)
    (root / "research" / "claims").mkdir(parents=True, exist_ok=True)
    (root / "revisions").mkdir(parents=True, exist_ok=True)

    evidence = {
        "chapter": "10",
        "evidence": [
            {
                "evidence_id": "EV-10-001",
                "source_kind": "sqlite.subtasks",
                "locator": {"task_id": 157, "subtask_id": 320},
                "field": "describe_cleaned",
                "excerpt": "Verified source observation.",
                "match": "contains_normalized",
                "notes": "",
            }
        ],
    }
    claims = {
        "chapter": "10",
        "claims": [
            {
                "claim_id": "CL-10-ADAPT-001",
                "claim": "The novel canon intentionally adds a durable adaptation detail.",
                "epistemic_status": "ADAPTATION_DECISION",
                "evidence": [],
                "durability": "durable",
                "promotion": "author_approved",
                "approval_ref": "revisions/chapter_10_canon_diff.md",
                "reasoning": "This is novel canon by author decision, not a raw-source assertion.",
            }
        ],
    }

    (root / "research" / "evidence" / "chapter_10.json").write_text(
        json.dumps(evidence, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    (root / "research" / "claims" / "chapter_10.json").write_text(
        json.dumps(claims, ensure_ascii=False, indent=2), encoding="utf-8"
    )


def write_diff(root: Path, approved: bool) -> None:
    mark = "x" if approved else " "
    (root / "revisions" / "chapter_10_canon_diff.md").write_text(
        f"# Canon Diff\n\n- [{mark}] Phê chuẩn toàn văn Đề xuất Canon Diff Chương 10.\n",
        encoding="utf-8",
    )


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="novel-os-claim-approval-") as temp:
        root = Path(temp)
        make_fixture(root)

        result = run(root)
        assert_code("author_approved claim requires approval_ref target", result, 1)

        write_diff(root, approved=False)
        result = run(root)
        assert_code("unchecked approval_ref cannot certify adaptation", result, 1)

        write_diff(root, approved=True)
        result = run(root)
        assert_code("checked approval_ref records approved adaptation", result, 0)

    print("\n[CLAIM-APPROVAL TEST PASS] Source truth and approved adaptation remain distinct.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
