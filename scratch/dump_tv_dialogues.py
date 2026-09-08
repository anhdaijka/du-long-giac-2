import sqlite3
import sys

sys.stdout.reconfigure(encoding='utf-8')

conn = sqlite3.connect('story_database.sqlite3')
cur = conn.cursor()

def dump_dialogues(title, npc_list):
    print(f"\n{'='*30} {title} {'='*30}")
    for npc in npc_list:
        print(f"\n--- NPC: {npc} ---")
        cur.execute("SELECT sub_id, phase, cleaned_text FROM dialogues WHERE cleaned_text LIKE ?", (f"%{npc}%",))
        rows = cur.fetchall()
        for r in rows:
            print(f"[Sub {r[0]} - Phase {r[1]}]:")
            # print lines that mention npc or around it
            lines = r[2].splitlines()
            for l in lines:
                print(f"   {l}")

dump_dialogues("THIÊN VƯƠNG BANG", ["Dương Anh", "Dương Thiết Tâm", "Cầu Chỉ Thủy", "Bùi Dực Phi"])
