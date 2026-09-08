#!/usr/bin/env python3
"""Deterministic regression tests for Reliability Layer v2 guards."""
from __future__ import annotations

import json
import sqlite3
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CLAIM_GUARD = ROOT / "scripts" / "claim-guard.py"
REVIEW_GUARD = ROOT / "scripts" / "review-guard.py"


def run(script: Path, args: list[str], cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(script), *args],
        cwd=cwd,
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


def make_source_fixture(root: Path) -> None:
    conn = sqlite3.connect(root / "story_database.sqlite3")
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE subtasks (
            sub_id INTEGER PRIMARY KEY,
            task_id INTEGER,
            name TEXT NOT NULL,
            describe_cleaned TEXT
        )
        """
    )
    cur.execute(
        "INSERT INTO subtasks(sub_id, task_id, name, describe_cleaned) VALUES (?, ?, ?, ?)",
        (320, 157, "Cơ Quan Đại Sư", "Source-backed observation."),
    )
    conn.commit()
    conn.close()


def write_claim_fixture(root: Path, *, inference_promotion: str = "author_approval_required") -> None:
    (root / "research" / "evidence").mkdir(parents=True, exist_ok=True)
    (root / "research" / "claims").mkdir(parents=True, exist_ok=True)

    evidence = {
        "chapter": "10",
        "evidence": [
            {
                "evidence_id": "EV-10-001",
                "source_kind": "sqlite.subtasks",
                "locator": {"task_id": 157, "subtask_id": 320},
                "field": "describe_cleaned",
                "excerpt": "Source-backed observation.",
                "match": "contains_normalized",
                "notes": "",
            }
        ],
    }
    claims = {
        "chapter": "10",
        "claims": [
            {
                "claim_id": "CL-10-001",
                "claim": "A source-backed event occurred.",
                "epistemic_status": "DIRECT_SOURCE",
                "evidence": ["EV-10-001"],
                "durability": "durable",
                "promotion": "author_approval_required",
                "reasoning": "",
            },
            {
                "claim_id": "CL-10-002",
                "claim": "A source-supported inference may follow.",
                "epistemic_status": "SOURCE_SUPPORTED_INFERENCE",
                "evidence": ["EV-10-001"],
                "durability": "durable",
                "promotion": inference_promotion,
                "reasoning": "This is explicitly an inference rather than a direct source statement.",
            },
        ],
    }

    (root / "research" / "evidence" / "chapter_10.json").write_text(
        json.dumps(evidence, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    (root / "research" / "claims" / "chapter_10.json").write_text(
        json.dumps(claims, ensure_ascii=False, indent=2), encoding="utf-8"
    )


def make_review(root: Path, *, gap: bool = False, bad_quote: bool = False) -> None:
    (root / "chapters").mkdir(parents=True, exist_ok=True)
    (root / "reviews").mkdir(parents=True, exist_ok=True)

    chapter_lines = [f"Line {i} concrete manuscript text." for i in range(1, 31)]
    (root / "chapters" / "chapter_10.md").write_text(
        "\n".join(chapter_lines), encoding="utf-8"
    )

    second_start = 12 if gap else 11
    quote = "This quote is not in the chapter." if bad_quote else "Line 1 concrete manuscript text."
    review = f"""# Review

## 1. Scope

Current manuscript reviewed.

## 2. Full-Read Coverage — Bắt Buộc

- `L1-L10` — Opening POV and scene setup checked concretely.
- `L{second_start}-L20` — Middle causality and character action checked concretely.
- `L21-L30` — Ending payoff and closure checked concretely.

## 3. Gates

### Gate A: Provenance
- **Trạng thái**: **PASS**

### Gate B: Pacing
- **Trạng thái**: **PASS**

### Gate C: Character
- **Trạng thái**: **PASS**

### Gate D: Voice
- **Trạng thái**: **PASS**

### Gate E: Substantiality
- **Trạng thái**: **PASS**

## 4. Evidence

1.
- **Vị trí**: `L1-L2`
- **Trích đoạn**: {quote}
- **Phân tích**: concrete observation

2.
- **Vị trí**: `L3-L4`
- **Trích đoạn**: Line 3 concrete manuscript text.
- **Phân tích**: concrete observation

3.
- **Vị trí**: `L5-L6`
- **Trích đoạn**: Line 5 concrete manuscript text.
- **Phân tích**: concrete observation

4.
- **Vị trí**: `L29-L30`
- **Trích đoạn**: Line 29 concrete manuscript text.
- **Phân tích**: concrete observation

## 6. Verdict

- **Phán quyết**: **APPROVED**
"""
    (root / "reviews" / "chapter_10_review.md").write_text(review, encoding="utf-8")


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="novel-os-reliability-") as temp:
        root = Path(temp)
        make_source_fixture(root)

        write_claim_fixture(root)
        result = run(CLAIM_GUARD, ["--chapter", "10"], root)
        assert_code("valid claim/evidence contract", result, 0)

        write_claim_fixture(root, inference_promotion="blocked")
        result = run(CLAIM_GUARD, ["--chapter", "10"], root)
        assert_code("inference cannot bypass author approval", result, 1)

        make_review(root)
        result = run(
            REVIEW_GUARD,
            ["--chapter-number", "10", "--require-approval"],
            root,
        )
        assert_code("full current-manuscript review coverage", result, 0)

        make_review(root, gap=True)
        result = run(REVIEW_GUARD, ["--chapter-number", "10"], root)
        assert_code("coverage gap is rejected", result, 1)

        make_review(root, bad_quote=True)
        result = run(REVIEW_GUARD, ["--chapter-number", "10"], root)
        assert_code("stale/fabricated evidence quote is rejected", result, 1)

    print("\n[RELIABILITY TEST PASS] Reliability Layer v2 deterministic guards behave as expected.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
