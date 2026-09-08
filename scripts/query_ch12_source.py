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
print("\n-- subtasks 130, 133 --")
cur.execute("SELECT task_id, sub_id, name, dialog_npc_name, describe_cleaned FROM subtasks WHERE sub_id IN (130,133) ORDER BY sub_id")
rows = cur.fetchall()
for row in rows:
    print(dict(row))
if not rows:
    print("NO ROWS")

print("\n-- task rows 0 and 157 --")
for task_id in (0, 157):
    cur.execute("SELECT * FROM tasks WHERE task_id=?", (task_id,))
    row = cur.fetchone()
    print(task_id, dict(row) if row else "NO TASK ROW")

print("\n-- dialogue rows for subtask 130, 133 --")
cur.execute("PRAGMA table_info(dialogues)")
print("dialogue columns:", [r[1] for r in cur.fetchall()])
cur.execute("SELECT * FROM dialogues WHERE sub_id IN (130,133) ORDER BY sub_id, rowid")
for row in cur.fetchall():
    print(dict(row))

print("\n-- nearby subtasks 125-138 --")
cur.execute("SELECT task_id, sub_id, name, dialog_npc_name, describe_cleaned FROM subtasks WHERE sub_id BETWEEN 125 AND 138 ORDER BY sub_id")
for row in cur.fetchall():
    print(dict(row))

conn.close()
