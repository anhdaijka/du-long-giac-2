import sqlite3
import sys

sys.stdout.reconfigure(encoding='utf-8')

conn = sqlite3.connect('story_database.sqlite3')
cur = conn.cursor()

cur.execute("SELECT sub_id, task_id, name, describe_cleaned, dialog_npc_name FROM subtasks WHERE sub_id BETWEEN 640 AND 645")
for st in cur.fetchall():
    print(f"Subtask {st[0]} (Task {st[1]}): {st[2]} | NPC: {st[4]}")
    print(f"Desc:\n{st[3]}\n")
    cur.execute("SELECT phase, cleaned_text FROM dialogues WHERE sub_id = ?", (st[0],))
    for d in cur.fetchall():
        print(f"Dialogue ({d[0]}):\n{d[1]}\n")
    print("="*60)
