import sqlite3
import sys

sys.stdout.reconfigure(encoding='utf-8')
conn = sqlite3.connect('story_database.sqlite3')
cur = conn.cursor()

print("=== MAX/MIN SUB_ID IN TASK 157 ===")
cur.execute("SELECT min(sub_id), max(sub_id), count(*) FROM subtasks WHERE task_id = 157")
print(cur.fetchone())

print("\n=== SEARCH ALL SUBTASKS CONTAINING 'Vô Danh' OR 'Bí tịch' OR 'Miếu' OR 'cướp' ===")
for r in cur.execute("SELECT task_id, sub_id, name, describe_cleaned, dialog_npc_name FROM subtasks WHERE name LIKE '%Vô Danh%' OR name LIKE '%Bảo Vệ%' OR describe_cleaned LIKE '%Bảo Vệ%'"):
    print(f"Task {r[0]}, Sub {r[1]}: {r[2]} (NPC: {r[4]})\n  Desc: {r[3][:150]}\n")
