import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import sqlite3

conn = sqlite3.connect('story_database.sqlite3')
cur = conn.cursor()

print("=== MENTIONS IN TASKS ===")
cur.execute("SELECT task_id, name, describe_cleaned FROM tasks WHERE describe_cleaned LIKE '%Hàm Yên%' OR describe_cleaned LIKE '%Tiêu Vũ%' OR name LIKE '%Hàm Yên%' OR name LIKE '%Tiêu Vũ%'")
for r in cur.fetchall():
    print(f"Task {r[0]} | {r[1]}")
    if r[2]:
        print(f"   Desc: {r[2]}")

print("\n=== MENTIONS IN SUBTASKS ===")
cur.execute("SELECT sub_id, task_id, name, dialog_npc_name, describe_cleaned FROM subtasks WHERE describe_cleaned LIKE '%Hàm Yên%' OR describe_cleaned LIKE '%Tiêu Vũ%' OR name LIKE '%Hàm Yên%' OR name LIKE '%Tiêu Vũ%' OR dialog_npc_name LIKE '%Hàm Yên%' OR dialog_npc_name LIKE '%Tiêu Vũ%'")
for r in cur.fetchall():
    print(f"Subtask {r[0]} | Task {r[1]} | {r[2]} | NPC: {r[3]}")
    if r[4]:
        print(f"   Desc: {r[4][:200]}...")

print("\n=== DIALOGUES WITH DOAN HAM YEN / TIEU VU ===")
cur.execute("SELECT d.id, d.sub_id, s.name, d.raw_text, d.cleaned_text FROM dialogues d JOIN subtasks s ON d.sub_id = s.sub_id WHERE d.cleaned_text LIKE '%Hàm Yên%' OR d.cleaned_text LIKE '%Tiêu Vũ%' OR d.raw_text LIKE '%Hàm Yên%' OR d.raw_text LIKE '%Tiêu Vũ%'")
rows = cur.fetchall()
print(f"Total dialogues: {len(rows)}")
for r in rows:
    txt = r[4] if r[4] else r[3]
    print(f"Dialog {r[0]} (Subtask {r[1]}: {r[2]}): {txt[:300]}")

print("\n=== NPC NAMES ===")
cur.execute("SELECT DISTINCT dialog_npc_name FROM subtasks WHERE dialog_npc_name LIKE '%Doãn%' OR dialog_npc_name LIKE '%Hàm Yên%' OR dialog_npc_name LIKE '%Tiêu Vũ%'")
for r in cur.fetchall():
    print("NPC:", r[0])
