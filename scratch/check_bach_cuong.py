import sqlite3
import sys

sys.stdout.reconfigure(encoding='utf-8')

conn = sqlite3.connect('story_database.sqlite3')
cur = conn.cursor()

def check_term(term):
    print(f"=== CHECKING TERM: {term} ===")
    for table in ["tasks", "subtasks", "dialogues", "world_ambient_dialogues", "armycamp_lore", "faction_primer_stories", "feature_system_stories", "linktask_tales"]:
        cur.execute(f"PRAGMA table_info([{table}])")
        cols = [c[1] for c in cur.fetchall()]
        text_cols = [c for c in cols if 'text' in c or 'name' in c or 'msg' in c or 'cleaned' in c or 'desc' in c]
        for col in text_cols:
            cur.execute(f"SELECT * FROM [{table}] WHERE [{col}] LIKE ?", (f"%{term}%",))
            rows = cur.fetchall()
            if rows:
                print(f"  [{table}].[{col}] ({len(rows)} matches):")
                for r in rows:
                    print("   -->", r)

check_term("Bạch Cương")
check_term("Bach Cuong")
check_term("bạch cương")
check_term("白刚")
check_term("白罡")
check_term("白")
