#!/usr/bin/env python3
"""Regression tests for state-commit-guard.py."""
from __future__ import annotations

import json
import sqlite3
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GUARD = ROOT / "scripts" / "state-commit-guard.py"


def cmd(args: list[str], cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, cwd=cwd, text=True, capture_output=True, check=False)


def git(root: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return cmd(["git", *args], root)


def write_source_and_claim_contract(root: Path) -> None:
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
                "claim_id": "CL-10-001",
                "claim": "A source-backed observation exists.",
                "epistemic_status": "DIRECT_SOURCE",
                "evidence": ["EV-10-001"],
                "durability": "durable",
                "promotion": "author_approval_required",
                "reasoning": "",
            }
        ],
    }
    (root / "research" / "evidence" / "chapter_10.json").write_text(
        json.dumps(evidence, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    (root / "research" / "claims" / "chapter_10.json").write_text(
        json.dumps(claims, ensure_ascii=False, indent=2), encoding="utf-8"
    )


def chapter_text(prefix: str = "Line") -> str:
    return "\n".join(f"{prefix} {i} concrete manuscript text." for i in range(1, 31)) + "\n"


def init_repo(root: Path, *, baseline_review: bool = False) -> str:
    git(root, "init")
    git(root, "config", "user.email", "novel-os-test@example.invalid")
    git(root, "config", "user.name", "Novel OS Test")
    for path in ["characters", "worldbuilding", "plot", "revisions", "chapters", "reviews"]:
        (root / path).mkdir(parents=True, exist_ok=True)

    (root / "characters" / "hero.md").write_text("baseline state\n", encoding="utf-8")
    (root / "chapters" / "chapter_10.md").write_text(chapter_text(), encoding="utf-8")
    write_source_and_claim_contract(root)
    if baseline_review:
        write_review(root, approved=True)

    git(root, "add", ".")
    git(root, "commit", "-m", "baseline")
    return git(root, "rev-parse", "HEAD").stdout.strip()


def commit_all(root: Path, message: str) -> None:
    git(root, "add", ".")
    result = git(root, "commit", "-m", message)
    if result.returncode != 0:
        print(result.stdout)
        print(result.stderr)
        raise SystemExit(1)


def run_guard(root: Path, base: str) -> subprocess.CompletedProcess[str]:
    return cmd([sys.executable, str(GUARD), "--base", base], root)


def assert_code(label: str, result: subprocess.CompletedProcess[str], expected: int) -> None:
    if result.returncode != expected:
        print(f"[FAIL] {label}: expected exit {expected}, got {result.returncode}")
        print(result.stdout)
        print(result.stderr)
        raise SystemExit(1)
    print(f"[PASS] {label}")


def write_diff(root: Path, approved: bool) -> None:
    mark = "x" if approved else " "
    text = f"""# Canon Diff\n\n## 9. Quyết Định & Chỉ Thị Của Tác Giả (Cổng Dừng Cứng 3)\n\n- [{mark}] Phê chuẩn toàn văn Đề xuất Canon Diff Chương 10.\n"""
    (root / "revisions" / "chapter_10_canon_diff.md").write_text(text, encoding="utf-8")


def write_review(root: Path, *, approved: bool) -> None:
    verdict = "APPROVED" if approved else "REVISE_REQUIRED"
    gate_e = "PASS" if approved else "FAIL"
    review = f"""# Review v2\n\n## Full-Read Coverage\n\n- `L1-L10` — Opening setup and POV were read concretely.\n- `L11-L20` — Middle causality and action were read concretely.\n- `L21-L30` — Ending payoff and closure were read concretely.\n\n### Gate A: Provenance\n- **PASS**\n\n### Gate B: Pacing\n- **PASS**\n\n### Gate C: Character\n- **PASS**\n\n### Gate D: Voice\n- **PASS**\n\n### Gate E: Substantiality\n- **{gate_e}**\n\n## Evidence\n\n1.\n- **Vị trí**: `L1-L2`\n- **Trích đoạn**: Line 1 concrete manuscript text.\n\n2.\n- **Vị trí**: `L3-L4`\n- **Trích đoạn**: Line 3 concrete manuscript text.\n\n3.\n- **Vị trí**: `L5-L6`\n- **Trích đoạn**: Line 5 concrete manuscript text.\n\n4.\n- **Vị trí**: `L29-L30`\n- **Trích đoạn**: Line 29 concrete manuscript text.\n\n## Verdict\n\n- **{verdict}**\n"""
    (root / "reviews" / "chapter_10_review_v2.md").write_text(review, encoding="utf-8")


def scenario_prose_only(root: Path) -> None:
    base = init_repo(root)
    (root / "chapters" / "chapter_10.md").write_text(chapter_text("Edited"), encoding="utf-8")
    commit_all(root, "edit prose")
    assert_code("prose-only change does not require canon promotion", run_guard(root, base), 0)


def scenario_state_without_diff(root: Path) -> None:
    base = init_repo(root)
    (root / "characters" / "hero.md").write_text("new durable state\n", encoding="utf-8")
    commit_all(root, "mutate state")
    assert_code("durable state without canon diff is rejected", run_guard(root, base), 1)


def scenario_state_unapproved(root: Path) -> None:
    base = init_repo(root)
    (root / "characters" / "hero.md").write_text("new durable state\n", encoding="utf-8")
    write_diff(root, approved=False)
    commit_all(root, "propose unapproved state")
    assert_code("unchecked canon diff cannot authorize state write", run_guard(root, base), 1)


def scenario_approved_diff_missing_review(root: Path) -> None:
    base = init_repo(root)
    (root / "characters" / "hero.md").write_text("new durable state\n", encoding="utf-8")
    write_diff(root, approved=True)
    commit_all(root, "approved diff without full review")
    assert_code("approved canon diff cannot skip v2 full-read review", run_guard(root, base), 1)


def scenario_review_not_approved(root: Path) -> None:
    base = init_repo(root)
    (root / "characters" / "hero.md").write_text("new durable state\n", encoding="utf-8")
    write_diff(root, approved=True)
    write_review(root, approved=False)
    commit_all(root, "state with revise-required review")
    assert_code("REVISE_REQUIRED review blocks state promotion", run_guard(root, base), 1)


def scenario_changed_chapter_stale_review(root: Path) -> None:
    base = init_repo(root, baseline_review=True)
    (root / "chapters" / "chapter_10.md").write_text(chapter_text("Edited"), encoding="utf-8")
    (root / "characters" / "hero.md").write_text("new durable state\n", encoding="utf-8")
    write_diff(root, approved=True)
    commit_all(root, "change prose and state without refreshing review")
    assert_code("changed manuscript cannot reuse unchanged v2 review", run_guard(root, base), 1)


def scenario_state_approved(root: Path) -> None:
    base = init_repo(root)
    (root / "characters" / "hero.md").write_text("new durable state\n", encoding="utf-8")
    write_diff(root, approved=True)
    write_review(root, approved=True)
    commit_all(root, "apply reviewed approved state")
    assert_code(
        "checked canon diff + approved full review + claim contract authorize state promotion",
        run_guard(root, base),
        0,
    )


def main() -> int:
    scenarios = [
        scenario_prose_only,
        scenario_state_without_diff,
        scenario_state_unapproved,
        scenario_approved_diff_missing_review,
        scenario_review_not_approved,
        scenario_changed_chapter_stale_review,
        scenario_state_approved,
    ]
    for scenario in scenarios:
        with tempfile.TemporaryDirectory(prefix="novel-os-state-guard-") as temp:
            scenario(Path(temp))

    print("\n[STATE-COMMIT TEST PASS] Forward-only reviewed canon-promotion behavior is locked.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
