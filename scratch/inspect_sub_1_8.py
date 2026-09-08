import sqlite3
import sys

sys.stdout.reconfigure(encoding='utf-8')

conn = sqlite3.connect('story_database.sqlite3')
cur = conn.cursor()

for sub_id in [1, 2, 6, 7, 8]:
    cur.execute("SELECT sub_id, task_id, name, describe_cleaned, dialog_npc_name FROM subtasks WHERE sub_id = ?", (sub_id,))
    st = cur.fetchone()
    if st:
        print(f"Subtask {st[0]} (Task {st[1]}): {st[2]} | NPC: {st[4]}")
        print(f"Desc: {st[3]}")
        cur.execute("SELECT phase, cleaned_text FROM dialogues WHERE sub_id = ?", (sub_id,))
        for d in cur.fetchall():
            print(f"Dialogue ({d[0]}):\n{d[1]}")
        print("="*60)
