import sqlite3
import sys

sys.stdout.reconfigure(encoding='utf-8')

conn = sqlite3.connect('story_database.sqlite3')
cursor = conn.cursor()

cursor.execute("SELECT task_id, name, describe_cleaned FROM tasks WHERE task_id=1;")
for r in cursor.fetchall():
    print("Task 1:", r)

cursor.execute("SELECT sub_id, name, describe_cleaned, dialog_npc_name FROM subtasks WHERE task_id=1;")
for r in cursor.fetchall():
    print("Subtask:", r)

# Also check dialogues related to task 1
cursor.execute("SELECT dialog_id, npc_name, text_cleaned FROM dialogues WHERE task_id=1 LIMIT 10;")
for r in cursor.fetchall():
    print("Dialogue:", r)

conn.close()
