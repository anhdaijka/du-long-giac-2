import sqlite3
import sys

sys.stdout.reconfigure(encoding='utf-8')

conn = sqlite3.connect('migration/source_corpus/01_Database/story_database.sqlite3')
cursor = conn.cursor()

print("=== TASK ARC 00 & TASK 157 SUBTASKS ===")
cursor.execute('''
    SELECT sub_id, task_id, name, describe_cleaned, dialog_npc_name 
    FROM subtasks 
    WHERE sub_id IN (320, 321, 322, 323, 324, 325) OR (task_id = 0 OR task_id = 157)
    ORDER BY task_id, sub_id
''')
for r in cursor.fetchall():
    print(f"Subtask {r[0]} (Task {r[1]}): {r[2]} | NPC: {r[4]}")
    if r[3]:
        print(f"   Desc: {r[3]}")
    print("-" * 50)
