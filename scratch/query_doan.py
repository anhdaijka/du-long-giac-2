import sqlite3
import sys

sys.stdout.reconfigure(encoding='utf-8')

conn = sqlite3.connect('story_database.sqlite3')
cur = conn.cursor()

print("=== ALL MENTIONS OF DOÃN HÀM YÊN IN SUBTASKS ===")
for r in cur.execute("SELECT task_id, sub_id, name, describe_cleaned, dialog_npc_name FROM subtasks WHERE describe_cleaned LIKE '%Hàm Yên%' OR name LIKE '%Hàm Yên%' OR dialog_npc_name LIKE '%Hàm Yên%'"):
    print(f"Task {r[0]}, Subtask {r[1]}: {r[2]} (NPC: {r[4]})")
    print(f"  Desc: {r[3]}\n")

print("=== ALL MENTIONS OF DOÃN TIÊU VŨ IN SUBTASKS ===")
for r in cur.execute("SELECT task_id, sub_id, name, describe_cleaned, dialog_npc_name FROM subtasks WHERE describe_cleaned LIKE '%Tiêu Vũ%' OR name LIKE '%Tiêu Vũ%' OR dialog_npc_name LIKE '%Tiêu Vũ%'"):
    print(f"Task {r[0]}, Subtask {r[1]}: {r[2]} (NPC: {r[4]})")
    print(f"  Desc: {r[3]}\n")

print("=== ALL DIALOGUES WITH 'Hàm Yên' OR 'Tiêu Vũ' ===")
for r in cur.execute("SELECT sub_id, phase, cleaned_text FROM dialogues WHERE cleaned_text LIKE '%Hàm Yên%' OR cleaned_text LIKE '%Tiêu Vũ%'"):
    print(f"Subtask {r[0]} [{r[1]}]:\n{r[2]}\n")
