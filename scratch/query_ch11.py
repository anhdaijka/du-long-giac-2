import sqlite3
import sys

sys.stdout.reconfigure(encoding='utf-8')

conn = sqlite3.connect('story_database.sqlite3')
cur = conn.cursor()

print("=== TASK 12 SUBTASKS 86 to 95 ===")
for r in cur.execute("SELECT sub_id, name, describe_cleaned, dialog_npc_name FROM subtasks WHERE task_id = 12"):
    print(f"Subtask {r[0]}: {r[1]} (NPC: {r[3]})")
    print(f"  Desc: {r[2][:160]}...\n")
