import sqlite3
import sys

# Ensure UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

conn = sqlite3.connect('story_database.sqlite3')
cur = conn.cursor()

def search_text(query):
    print(f"=== SEARCHING FOR: {query} ===")
    
    # 1. search in subtasks
    cur.execute("SELECT sub_id, task_id, name, describe_cleaned, dialog_npc_name FROM subtasks WHERE name LIKE ? OR describe_cleaned LIKE ? OR dialog_npc_name LIKE ?", (f'%{query}%', f'%{query}%', f'%{query}%'))
    rows = cur.fetchall()
    print(f"--- Subtasks ({len(rows)}) ---")
    for r in rows:
        print(f"  Subtask {r[0]} (Task {r[1]}): {r[2]} | NPC: {r[4]}")
        desc = r[3][:200] if r[3] else ""
        print(f"    Desc: {desc}")

    # 2. search in dialogues
    cur.execute("SELECT id, sub_id, phase, cleaned_text FROM dialogues WHERE cleaned_text LIKE ?", (f'%{query}%',))
    rows = cur.fetchall()
    print(f"--- Dialogues ({len(rows)}) ---")
    for r in rows[:10]:
        print(f"  Dialogue {r[0]} (Sub {r[1]}, Phase {r[2]}): {r[3][:200]}")
    if len(rows) > 10:
        print(f"  ... and {len(rows)-10} more dialogues")

    # 3. search in tasks
    cur.execute("SELECT task_id, name, describe_cleaned FROM tasks WHERE name LIKE ? OR describe_cleaned LIKE ?", (f'%{query}%', f'%{query}%'))
    rows = cur.fetchall()
    print(f"--- Tasks ({len(rows)}) ---")
    for r in rows:
        print(f"  Task {r[0]}: {r[1]}")
        desc = r[2][:200] if r[2] else ""
        print(f"    Desc: {desc}")

    # 4. search in world_ambient_dialogues
    cur.execute("SELECT id, map_name, npc_class, cleaned_msg FROM world_ambient_dialogues WHERE cleaned_msg LIKE ? OR npc_class LIKE ?", (f'%{query}%', f'%{query}%'))
    rows = cur.fetchall()
    print(f"--- World Ambient ({len(rows)}) ---")
    for r in rows[:10]:
        print(f"  Ambient {r[0]} (Map {r[1]}, NPC {r[2]}): {r[3][:200]}")

    # 5. search in armycamp_lore
    cur.execute("SELECT id, camp_name, speaker_or_subject, cleaned_text FROM armycamp_lore WHERE cleaned_text LIKE ? OR speaker_or_subject LIKE ?", (f'%{query}%', f'%{query}%'))
    rows = cur.fetchall()
    print(f"--- Armycamp Lore ({len(rows)}) ---")
    for r in rows:
        print(f"  Camp {r[0]} ({r[1]} - {r[2]}): {r[3][:200]}")

    # 6. search in feature_system_stories
    cur.execute("SELECT id, system_name, subject, cleaned_text FROM feature_system_stories WHERE cleaned_text LIKE ? OR subject LIKE ?", (f'%{query}%', f'%{query}%'))
    rows = cur.fetchall()
    print(f"--- Feature System Stories ({len(rows)}) ---")
    for r in rows:
        print(f"  Feature {r[0]} ({r[1]} - {r[2]}): {r[3][:200]}")

    print("\n" + "="*50 + "\n")

search_text("Bạch Thu Lâm")
search_text("Bạch Cương")
search_text("Thu Di")
search_text("Tiêu Phùng")
search_text("Tiêu Lăng Phong")
