import sqlite3
import sys

sys.stdout.reconfigure(encoding='utf-8')


conn = sqlite3.connect(r'migration/source_corpus/01_Database/story_database.sqlite3')
cur = conn.cursor()

print("=== SEARCH FOR DIEM TUU ===")
cur.execute("SELECT task_id, sub_id, name, dialog_npc_name, describe_cleaned FROM subtasks WHERE name LIKE '%Điềm Tửu%' OR dialog_npc_name LIKE '%Điềm Tửu%' OR describe_cleaned LIKE '%Điềm Tửu%'")
for r in cur.fetchall():
    print(r)

print("\n=== SEARCH FOR TAN THU THON OR BAC THU LAM ===")
cur.execute("SELECT task_id, sub_id, name, dialog_npc_name, describe_cleaned FROM subtasks WHERE name LIKE '%Bạch Thu Lâm%' OR dialog_npc_name LIKE '%Bạch Thu Lâm%' OR describe_cleaned LIKE '%Bạch Thu Lâm%' LIMIT 10")
for r in cur.fetchall():
    print(r)

print("\n=== SEARCH FOR TASK 157 ===")
cur.execute("SELECT task_id, sub_id, name, dialog_npc_name, describe_cleaned FROM subtasks WHERE task_id=157 LIMIT 10")
for r in cur.fetchall():
    print(r)
