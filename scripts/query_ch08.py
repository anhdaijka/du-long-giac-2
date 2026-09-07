import sqlite3
import sys

sys.stdout.reconfigure(encoding='utf-8')

conn = sqlite3.connect('story_database.sqlite3')
cur = conn.cursor()

print("=== TASK 12 ===")
for r in cur.execute("SELECT task_id, name, describe_cleaned FROM tasks WHERE task_id = 12").fetchall():
    print(f"Task ID: {r[0]} | Name: {r[1]}")
    print(f"Describe: {r[2]}\n")

print("=== SUBTASKS FOR TASK 12 ===")
for r in cur.execute("SELECT sub_id, name, describe_cleaned, dialog_npc_name FROM subtasks WHERE task_id = 12").fetchall():
    print(f"Subtask ID: {r[0]} | Name: {r[1]} | NPC: {r[3]}")
    print(f"Describe: {r[2]}\n")

print("=== SUBTASK 85 & 86 DETAILS ===")
for sub_id in [85, 86, 87]:
    print(f"\n--- Subtask {sub_id} Steps ---")
    for s in cur.execute("SELECT step_index, instruction, target_function, target_params FROM steps WHERE sub_id = ?", (sub_id,)).fetchall():
        print(f"Step {s[0]}: {s[1]} | func: {s[2]} | params: {s[3]}")
    
    print(f"\n--- Subtask {sub_id} Dialogues ---")
    for d in cur.execute("SELECT phase, cleaned_text FROM dialogues WHERE sub_id = ?", (sub_id,)).fetchall():
        print(f"[{d[0]}]:\n{d[1]}\n")
