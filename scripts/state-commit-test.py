#!/usr/bin/env python3
"""Regression tests for state-commit-guard.py."""
from __future__ import annotations

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


def init_repo(root: Path) -> str:
    git(root, "init")
    git(root, "config", "user.email", "novel-os-test@example.invalid")
    git(root, "config", "user.name", "Novel OS Test")
    (root / "characters").mkdir(parents=True, exist_ok=True)
    (root / "worldbuilding").mkdir(parents=True, exist_ok=True)
    (root / "plot").mkdir(parents=True, exist_ok=True)
    (root / "revisions").mkdir(parents=True, exist_ok=True)
    (root / "chapters").mkdir(parents=True, exist_ok=True)
    (root / "characters" / "hero.md").write_text("baseline state\n", encoding="utf-8")
    (root / "chapters" / "chapter_10.md").write_text("baseline prose\n", encoding="utf-8")
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


def scenario_prose_only(root: Path) -> None:
    base = init_repo(root)
    (root / "chapters" / "chapter_10.md").write_text("author prose changed\n", encoding="utf-8")
    commit_all(root, "edit prose")
    assert_code("prose-only change does not require canon approval", run_guard(root, base), 0)


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


def scenario_state_approved(root: Path) -> None:
    base = init_repo(root)
    (root / "characters" / "hero.md").write_text("new durable state\n", encoding="utf-8")
    write_diff(root, approved=True)
    commit_all(root, "apply approved state")
    assert_code("checked canon diff authorizes forward state write", run_guard(root, base), 0)


def main() -> int:
    scenarios = [
        scenario_prose_only,
        scenario_state_without_diff,
        scenario_state_unapproved,
        scenario_state_approved,
    ]
    for scenario in scenarios:
        with tempfile.TemporaryDirectory(prefix="novel-os-state-guard-") as temp:
            scenario(Path(temp))

    print("\n[STATE-COMMIT TEST PASS] Forward-only canon approval behavior is locked.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
