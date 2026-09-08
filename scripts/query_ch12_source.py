#!/usr/bin/env python3
import sqlite3
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
DB = Path("story_database.sqlite3")
conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row
cur = conn.cursor()

print("=== CH12 SOURCE PROBE ===")
print("DB:", DB)

print("\n-- roadmap locators 130, 133 --")
cur.execute("SELECT task_id, sub_id, name, dialog_npc_name, describe_cleaned FROM subtasks WHERE sub_id IN (130,133) ORDER BY sub_id")
for row in cur.fetchall():
    print(dict(row))

print("\n-- task rows 0, 19, 157 --")
for task_id in (0, 19, 157):
    cur.execute("SELECT task_id, name, describe_cleaned, file_path FROM tasks WHERE task_id=?", (task_id,))
    row = cur.fetchone()
    print(task_id, dict(row) if row else "NO TASK ROW")

TERMS = [
    "Yến Tử Ổ",
    "Yến Tử",
    "tiến cử",
    "Điềm Tửu",
    "bầu rượu",
    "rượu nếp",
    "tiễn",
    "xuất sơn",
    "Cái Bang",
]

for term in TERMS:
    print(f"\n-- subtask search: {term} --")
    like = f"%{term}%"
    cur.execute(
        """
        SELECT task_id, sub_id, name, dialog_npc_name, describe_cleaned
        FROM subtasks
        WHERE name LIKE ? OR dialog_npc_name LIKE ? OR describe_cleaned LIKE ?
        ORDER BY task_id, sub_id
        LIMIT 40
        """,
        (like, like, like),
    )
    rows = cur.fetchall()
    if not rows:
        print("NO SUBTASK HITS")
    for row in rows:
        print(dict(row))

    print(f"-- dialogue search: {term} --")
    cur.execute(
        """
        SELECT id, sub_id, phase, cleaned_text
        FROM dialogues
        WHERE cleaned_text LIKE ?
        ORDER BY sub_id, id
        LIMIT 40
        """,
        (like,),
    )
    rows = cur.fetchall()
    if not rows:
        print("NO DIALOGUE HITS")
    for row in rows:
        print(dict(row))

conn.close()
