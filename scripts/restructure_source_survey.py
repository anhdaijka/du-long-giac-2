#!/usr/bin/env python3
"""Build non-canonical, repeatable source-survey artifacts for the 2026 restructure.

The Narrative Book is used only as a locator of its task inclusions. The script
does not treat its Arc titles or prose summaries as source truth; SQLite rows
remain the evidence source for the reported task/subtask/step counts.
"""

from __future__ import annotations

import csv
import hashlib
import json
import re
import sqlite3
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "story_database.sqlite3"
BOOK_DIR = ROOT / "migration" / "source_corpus" / "02_Narrative_Book" / "01_Chinh_Tuyen"
OUT = ROOT / "migration" / "restructure_2026_09" / "evidence"


PACKET_QUERIES = {
    "task": (
        "SELECT task_id, task_id_hex, name, describe_cleaned, category, category_desc, "
        "order_type, repeat, task_type_code, file_path FROM tasks WHERE task_id = ?"
    ),
    "subtasks": (
        "SELECT sub_id, sub_id_hex, task_id, name, describe_cleaned, file_path, "
        "dialog_npc_id, dialog_npc_name FROM subtasks WHERE task_id = ? ORDER BY sub_id"
    ),
    "steps": (
        "SELECT id, sub_id, step_index, instruction, target_function, target_params "
        "FROM steps WHERE sub_id = ? ORDER BY step_index, id"
    ),
    "dialogues": (
        "SELECT id, sub_id, phase, cleaned_text FROM dialogues "
        "WHERE sub_id = ? ORDER BY id"
    ),
}

KEY_TERMS = [
    "Du Long Giác",
    "Thái Tổ Bảo Khố",
    "Hán Thủy",
    "Tiêu Lăng Phong",
    "Lệ Thu Thủy",
    "Lịch Thu Thủy",
]

KEY_MENTION_QUERY = """
WITH narrative_fields AS (
    SELECT task_id, NULL AS sub_id, 'tasks' AS source_table,
           task_id AS row_id, 'name' AS source_field, name AS source_text
      FROM tasks
    UNION ALL
    SELECT task_id, NULL, 'tasks', task_id, 'describe_cleaned', describe_cleaned
      FROM tasks
    UNION ALL
    SELECT task_id, sub_id, 'subtasks', sub_id, 'name', name
      FROM subtasks
    UNION ALL
    SELECT task_id, sub_id, 'subtasks', sub_id, 'describe_cleaned', describe_cleaned
      FROM subtasks
    UNION ALL
    SELECT s.task_id, st.sub_id, 'steps', st.id, 'instruction', st.instruction
      FROM steps AS st JOIN subtasks AS s ON s.sub_id = st.sub_id
    UNION ALL
    SELECT s.task_id, st.sub_id, 'steps', st.id, 'target_params', st.target_params
      FROM steps AS st JOIN subtasks AS s ON s.sub_id = st.sub_id
    UNION ALL
    SELECT s.task_id, d.sub_id, 'dialogues', d.id, 'cleaned_text', d.cleaned_text
      FROM dialogues AS d JOIN subtasks AS s ON s.sub_id = d.sub_id
)
SELECT task_id, sub_id, source_table, row_id, source_field, source_text
  FROM narrative_fields
 WHERE COALESCE(source_text, '') LIKE ?
 ORDER BY task_id, sub_id, source_table, row_id, source_field
""".strip()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def source_packet(cur: sqlite3.Cursor, task_ids: list[int], label: str) -> dict[str, object]:
    """Return every narrative-bearing SQLite field for a bounded task collection."""
    packet: dict[str, object] = {
        "label": label,
        "provenance": {
            "sqlite_path": DB.relative_to(ROOT).as_posix(),
            "sqlite_sha256": sha256(DB),
            "query_parameters": {"task_ids": task_ids},
            "query_templates": PACKET_QUERIES,
            "result_container": "tasks",
        },
        "task_ids": task_ids,
        "tasks": [],
    }
    for task_id in task_ids:
        task = cur.execute(
            """
            SELECT task_id, task_id_hex, name, describe_cleaned, category, category_desc,
                   order_type, repeat, task_type_code, file_path
              FROM tasks WHERE task_id = ?
            """,
            (task_id,),
        ).fetchone()
        if task is None:
            packet["tasks"].append({"task_id": task_id, "missing_from_sqlite": True})
            continue
        task_data = dict(task)
        task_data["subtasks"] = []
        subtasks = cur.execute(
            """
            SELECT sub_id, sub_id_hex, task_id, name, describe_cleaned, file_path,
                   dialog_npc_id, dialog_npc_name
              FROM subtasks WHERE task_id = ? ORDER BY sub_id
            """,
            (task_id,),
        ).fetchall()
        for subtask in subtasks:
            subtask_data = dict(subtask)
            subtask_id = subtask_data["sub_id"]
            subtask_data["steps"] = [
                dict(row)
                for row in cur.execute(
                    """
                    SELECT id, sub_id, step_index, instruction, target_function, target_params
                      FROM steps WHERE sub_id = ? ORDER BY step_index, id
                    """,
                    (subtask_id,),
                )
            ]
            subtask_data["dialogues"] = [
                dict(row)
                for row in cur.execute(
                    """
                    SELECT id, sub_id, phase, cleaned_text
                      FROM dialogues WHERE sub_id = ? ORDER BY id
                    """,
                    (subtask_id,),
                )
            ]
            task_data["subtasks"].append(subtask_data)
        packet["tasks"].append(task_data)
    return packet


def mention_context(text: str, term: str, radius: int = 110) -> str:
    """Return a compact, single-line context while preserving the full row in SQLite."""
    clean = re.sub(r"\s+", " ", text).strip()
    index = clean.casefold().find(term.casefold())
    if index < 0:
        return clean[: radius * 2]
    start = max(0, index - radius)
    end = min(len(clean), index + len(term) + radius)
    prefix = "…" if start else ""
    suffix = "…" if end < len(clean) else ""
    return prefix + clean[start:end] + suffix


def write_key_mentions(cur: sqlite3.Cursor, db_hash: str) -> None:
    """Persist selected source-term hits with their exact query and parameters."""
    rows: list[dict[str, object]] = []
    for term in KEY_TERMS:
        for row in cur.execute(KEY_MENTION_QUERY, (f"%{term}%",)):
            item = dict(row)
            item["term"] = term
            item["context"] = mention_context(item.pop("source_text") or "", term)
            rows.append(item)

    with (OUT / "key-mentions.tsv").open("w", encoding="utf-8", newline="") as file:
        fieldnames = [
            "term", "task_id", "sub_id", "source_table", "row_id",
            "source_field", "context",
        ]
        writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)

    counts = Counter(row["term"] for row in rows)
    task_counts = {
        term: len({row["task_id"] for row in rows if row["term"] == term})
        for term in KEY_TERMS
    }
    lines = [
        "# Key source mentions — generated evidence",
        "",
        "Status: non-canonical locator evidence. A hit preserves where text occurs; it does not make a speaker claim objectively true.",
        "",
        f"- SQLite: `story_database.sqlite3` ({db_hash})",
        "- Result rows: `key-mentions.tsv`",
        "- Query parameter for each run: `%<term>%`",
        "",
        "## Query",
        "",
        "```sql",
        KEY_MENTION_QUERY,
        "```",
        "",
        "## Results",
        "",
        "| Term | Matching rows | Distinct tasks |",
        "| --- | ---: | ---: |",
    ]
    for term in KEY_TERMS:
        lines.append(f"| {term} | {counts[term]} | {task_counts[term]} |")
    lines.extend([
        "",
        "Every result row records task/subtask, source table, source row ID, field and bounded context. Read the complete source row from SQLite or its Arc packet before interpreting the claim.",
    ])
    (OUT / "key-mentions-report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    db_hash = sha256(DB)
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    arc_sources: list[dict[str, object]] = []
    assigned: dict[int, str] = {}
    duplicate_assignments: list[tuple[int, str, str]] = []
    for path in sorted(BOOK_DIR.glob("Arc_*.md")):
        text = path.read_text(encoding="utf-8")
        heading = re.search(r"^# (.+)$", text, re.MULTILINE)
        task_ids = [int(value) for value in re.findall(r"### \[Nhiệm Vụ #(\d+)\]", text)]
        arc_id = path.stem.split("_", 2)[1]
        for task_id in task_ids:
            if task_id in assigned:
                duplicate_assignments.append((task_id, assigned[task_id], arc_id))
            else:
                assigned[task_id] = arc_id
        arc_sources.append(
            {
                "arc_id": arc_id,
                "arc_heading": heading.group(1) if heading else "",
                "locator_path": path.relative_to(ROOT).as_posix(),
                "locator_sha256": sha256(path),
                "task_ids": task_ids,
            }
        )

    task_rows = cur.execute(
        """
        SELECT t.task_id, t.task_id_hex, t.name, t.category_desc, t.repeat,
               COUNT(DISTINCT s.sub_id) AS subtask_count,
               COUNT(DISTINCT st.id) AS step_count,
               COUNT(DISTINCT d.id) AS dialogue_count
          FROM tasks AS t
          LEFT JOIN subtasks AS s ON s.task_id = t.task_id
          LEFT JOIN steps AS st ON st.sub_id = s.sub_id
          LEFT JOIN dialogues AS d ON d.sub_id = s.sub_id
         GROUP BY t.task_id
         ORDER BY t.task_id
        """
    ).fetchall()
    task_ids = {row["task_id"] for row in task_rows}
    missing_from_book = sorted(task_ids - set(assigned))
    unknown_in_db = sorted(set(assigned) - task_ids)

    with (OUT / "arc-membership.tsv").open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "task_id", "task_id_hex", "task_name", "category", "repeat",
                "membership_status", "arc_locator_id", "arc_locator_path",
                "subtask_count", "step_count", "dialogue_count",
            ],
            delimiter="\t",
        )
        writer.writeheader()
        path_by_arc = {item["arc_id"]: item["locator_path"] for item in arc_sources}
        for row in task_rows:
            arc_id = assigned.get(row["task_id"])
            writer.writerow(
                {
                    "task_id": row["task_id"],
                    "task_id_hex": row["task_id_hex"],
                    "task_name": row["name"],
                    "category": row["category_desc"],
                    "repeat": row["repeat"],
                    "membership_status": "LOCATOR_LISTED" if arc_id else "UNCLASSIFIED",
                    "arc_locator_id": arc_id or "",
                    "arc_locator_path": path_by_arc.get(arc_id, ""),
                    "subtask_count": row["subtask_count"],
                    "step_count": row["step_count"],
                    "dialogue_count": row["dialogue_count"],
                }
            )

    subtasks_without_task = cur.execute(
        """
        SELECT s.sub_id, s.sub_id_hex, s.task_id, s.name
          FROM subtasks AS s
          LEFT JOIN tasks AS t ON t.task_id = s.task_id
         WHERE t.task_id IS NULL
         ORDER BY s.sub_id
        """
    ).fetchall()
    referenced_missing_subtasks = cur.execute(
        """
        SELECT t.task_id, t.name AS task_name, s.sub_id, s.name AS subtask_name
          FROM tasks AS t
          LEFT JOIN subtasks AS s ON s.task_id = t.task_id
         WHERE s.sub_id IS NULL
         ORDER BY t.task_id
        """
    ).fetchall()

    lines = [
        "# Arc membership survey — generated evidence",
        "",
        "Status: non-canonical reconstruction input. SQLite is the source evidence; Narrative Book files are membership locators only.",
        "",
        f"- SQLite: `story_database.sqlite3` ({db_hash})",
        f"- Tasks: {len(task_rows)}",
        f"- Tasks listed once by Arc locators: {len(assigned)}",
        f"- Tasks not listed by Arc locators: {len(missing_from_book)}",
        f"- Duplicate locator assignments: {len(duplicate_assignments)}",
        f"- Locator task IDs missing from SQLite: {len(unknown_in_db)}",
        "",
        "## Arc locators",
        "",
        "| Arc locator | Narrative Book file | Listed tasks | SQLite tasks verified |",
        "| --- | --- | ---: | ---: |",
    ]
    for item in arc_sources:
        listed = item["task_ids"]
        verified = len([task_id for task_id in listed if task_id in task_ids])
        lines.append(
            f"| {item['arc_id']} | `{item['locator_path']}` | {len(listed)} | {verified} |"
        )
    lines.extend([
        "",
        "## Unclassified tasks",
        "",
        "The following tasks are present in SQLite but omitted from the Narrative Book's 13 Arc locator files. They require classification during the semantic survey; do not force them into an Arc by numeric range.",
        "",
        "| Task ID | Name | Category | Repeat |",
        "| ---: | --- | --- | ---: |",
    ])
    task_lookup = {row["task_id"]: row for row in task_rows}
    for task_id in missing_from_book:
        row = task_lookup[task_id]
        lines.append(f"| {task_id} | {row['name']} | {row['category_desc']} | {row['repeat']} |")
    lines.extend([
        "",
        "## Referential irregularities",
        "",
        f"- SQLite subtasks without a parent task: {len(subtasks_without_task)}.",
        f"- SQLite tasks without a matching subtask row: {len(referenced_missing_subtasks)}.",
    ])
    if referenced_missing_subtasks:
        lines.append("- Task rows without a matching subtask: " + ", ".join(str(row["task_id"]) for row in referenced_missing_subtasks) + ".")
    (OUT / "arc-membership-report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    packets_dir = OUT / "source-packets"
    packets_dir.mkdir(exist_ok=True)
    for item in arc_sources:
        packet = source_packet(cur, item["task_ids"], f"Arc locator {item['arc_id']}")
        packet["locator"] = {
            "path": item["locator_path"],
            "sha256": item["locator_sha256"],
            "role": "membership locator only",
        }
        (packets_dir / f"arc_{item['arc_id']}.json").write_text(
            json.dumps(packet, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
    (packets_dir / "unclassified.json").write_text(
        json.dumps(source_packet(cur, missing_from_book, "Unclassified tasks"), ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_key_mentions(cur, db_hash)
    conn.close()


if __name__ == "__main__":
    main()
