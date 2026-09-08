import sqlite3
import sys

sys.stdout.reconfigure(encoding='utf-8')

conn = sqlite3.connect('story_database.sqlite3')
cur = conn.cursor()

def search_exact(table, cols, term):
    for col in cols:
        cur.execute(f"SELECT * FROM [{table}] WHERE [{col}] LIKE ?", (f"%{term}%",))
        rows = cur.fetchall()
        if rows:
            print(f"Table [{table}] Column [{col}] found {len(rows)} rows for '{term}'")
            for r in rows:
                print("  ", r)

for term in ["Bạch Cương", "Bach Cuong", "Thu Di", "Bạch Thu Lâm", "Tiêu Lăng Phong", "Dương Anh", "Dương Thiết Tâm", "Doãn Hàm Yên", "Lệ Thu Thủy", "Đường Nhất Trần", "Đường Hiểu", "Doãn Tiêu Vũ"]:
    print(f"\n==================== SEARCH: {term} ====================")
    search_exact("tasks", ["name", "describe_cleaned"], term)
    search_exact("subtasks", ["name", "describe_cleaned", "dialog_npc_name"], term)
    search_exact("dialogues", ["cleaned_text"], term)
    search_exact("world_ambient_dialogues", ["cleaned_msg", "npc_class"], term)
    search_exact("armycamp_lore", ["cleaned_text", "speaker_or_subject"], term)
    search_exact("faction_primer_stories", ["cleaned_text"], term)
    search_exact("feature_system_stories", ["cleaned_text", "subject"], term)
