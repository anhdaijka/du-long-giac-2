#!/usr/bin/env python3
"""Regression tests for SQLite Evidence Guard and Claim/Evidence integration."""
from __future__ import annotations

import json
import sqlite3
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EVIDENCE_GUARD = ROOT / "scripts" / "evidence_guard.py"
CLAIM_GUARD = ROOT / "scripts" / "claim-guard.py"


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


def make_db(root: Path) -> None:
    conn = sqlite3.connect(root / "story_database.sqlite3")
    cur = conn.cursor()
    cur.executescript(
        """
        CREATE TABLE tasks (
            task_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            describe_cleaned TEXT
        );
        CREATE TABLE subtasks (
            sub_id INTEGER PRIMARY KEY,
            task_id INTEGER,
            name TEXT NOT NULL,
            describe_cleaned TEXT,
            dialog_npc_name TEXT
        );
        CREATE TABLE dialogues (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sub_id INTEGER NOT NULL,
            phase TEXT NOT NULL,
            cleaned_text TEXT
        );
        CREATE TABLE steps (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sub_id INTEGER NOT NULL,
            step_index INTEGER NOT NULL,
            instruction TEXT
        );
        """
    )
    cur.execute(
        "INSERT INTO tasks(task_id, name, describe_cleaned) VALUES (?, ?, ?)",
        (157, "Bảo Vệ Mật Tịch", "Nhiệm vụ bảo vệ mật tịch tại Ba Lăng."),
    )
    cur.execute(
        """
        INSERT INTO subtasks(sub_id, task_id, name, describe_cleaned, dialog_npc_name)
        VALUES (?, ?, ?, ?, ?)
        """,
        (320, 157, "Cơ Quan Đại Sư", "Source-backed observation from subtask 320.", "Bạch Thu Lâm"),
    )
    cur.execute(
        "INSERT INTO dialogues(sub_id, phase, cleaned_text) VALUES (?, ?, ?)",
        (320, "accept", "Đây là lời thoại xác nhận từ nguồn game."),
    )
    cur.execute(
        "INSERT INTO steps(sub_id, step_index, instruction) VALUES (?, ?, ?)",
        (320, 1, "Bảo vệ chiếc tráp."),
    )
    conn.commit()
    conn.close()


def write_packet(
    root: Path,
    *,
    task_id: int | None = 157,
    subtask_id: int = 320,
    excerpt: str = "Source-backed observation from subtask 320.",
    field: str = "describe_cleaned",
) -> None:
    (root / "research" / "evidence").mkdir(parents=True, exist_ok=True)
    locator: dict[str, object] = {"subtask_id": subtask_id}
    if task_id is not None:
        locator["task_id"] = task_id

    evidence = {
        "chapter": "10",
        "evidence": [
            {
                "evidence_id": "EV-10-001",
                "source_kind": "sqlite.subtasks",
                "locator": locator,
                "field": field,
                "excerpt": excerpt,
                "match": "contains_normalized",
                "notes": "Task lineage retained in the locator.",
            }
        ],
    }
    (root / "research" / "evidence" / "chapter_10.json").write_text(
        json.dumps(evidence, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def write_claims(root: Path) -> None:
    (root / "research" / "claims").mkdir(parents=True, exist_ok=True)
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
            }
        ],
    }
    (root / "research" / "claims" / "chapter_10.json").write_text(
        json.dumps(claims, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="novel-os-evidence-") as temp:
        root = Path(temp)
        make_db(root)
        write_claims(root)

        write_packet(root)
        result = run(EVIDENCE_GUARD, ["--chapter", "10"], root)
        assert_code("valid SQLite locator and excerpt", result, 0)

        write_packet(root, task_id=999)
        result = run(EVIDENCE_GUARD, ["--chapter", "10"], root)
        assert_code("wrong source row is rejected", result, 1)

        write_packet(root, excerpt="A plausible sentence that is not in source.")
        result = run(EVIDENCE_GUARD, ["--chapter", "10"], root)
        assert_code("fabricated excerpt is rejected", result, 1)

        write_packet(root, task_id=None)
        result = run(EVIDENCE_GUARD, ["--chapter", "10"], root)
        assert_code("missing subtask task-lineage context is rejected", result, 1)

        write_packet(root, field="name", excerpt="Source-backed observation from subtask 320.")
        result = run(EVIDENCE_GUARD, ["--chapter", "10"], root)
        assert_code("excerpt cannot drift into the wrong declared field", result, 1)

        write_packet(root)
        result = run(CLAIM_GUARD, ["--chapter", "10"], root)
        assert_code("claim guard accepts source-verified evidence", result, 0)

        write_packet(root, excerpt="Invented evidence text.")
        result = run(CLAIM_GUARD, ["--chapter", "10"], root)
        assert_code("claim guard fails when source evidence fails", result, 1)

    print("\n[EVIDENCE TEST PASS] SQLite evidence provenance behavior is locked.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
