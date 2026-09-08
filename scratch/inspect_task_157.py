import sqlite3
import sys

sys.stdout.reconfigure(encoding='utf-8')

conn = sqlite3.connect('story_database.sqlite3')
cur = conn.cursor()

# Get tasks around 157
cur.execute("SELECT task_id, name, describe_cleaned FROM tasks WHERE task_id BETWEEN 150 AND 165")
for t in cur.fetchall():
    print(f"Task {t[0]}: {t[1]}\n  Desc: {t[2]}\n")

# Get subtasks and dialogues for task 157
cur.execute("SELECT sub_id, task_id, name, describe_cleaned, dialog_npc_name FROM subtasks WHERE task_id = 157")
for st in cur.fetchall():
    print(f"Subtask {st[0]} (Task {st[1]}): {st[2]} | NPC: {st[4]}")
    print(f"  Desc: {st[3]}")
    cur.execute("SELECT phase, cleaned_text FROM dialogues WHERE sub_id = ?", (st[0],))
    for d in cur.fetchall():
        print(f"    Dialogue ({d[0]}):\n{d[1]}")
    print("-"*40)
