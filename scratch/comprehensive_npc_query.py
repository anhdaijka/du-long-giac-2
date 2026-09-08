import sqlite3
import sys

sys.stdout.reconfigure(encoding='utf-8')

conn = sqlite3.connect('story_database.sqlite3')
cur = conn.cursor()

characters = [
    "Bạch Thu Lâm", "Bạch Cương", "Long Ngũ", "Bất Động", "Điềm Tửu", "Thẩm Thiết Thạch", "Thẩm Hà Diệp",
    "Giới Sơn Tông", "Cao Thăng", "Thôi Kiếm", "Dương Anh", "Dương Thiết Tâm", "Cầu Chỉ Thủy",
    "Lâu Nhất Quan", "Quý Thúc Ban", "Bùi Dực Phi", "Diệp Mẫu", "Khang Diên Chi", "Tiêu Lăng Phong",
    "Thạch Hiên Viên", "Bạch Doanh Doanh", "Bạch Hiên Viên", "Dương Hồ Điệp", "Dương Ma"
]

print("=== COMPREHENSIVE NPC AUDIT FROM SQLITE ===")

for char in characters:
    print(f"\n" + "="*60)
    print(f"TARGET: {char}")
    print("="*60)
    
    # 1. Dialogues where character speaks or is mentioned
    cur.execute("SELECT sub_id, cleaned_text FROM dialogues WHERE cleaned_text LIKE ?", (f"%{char}%",))
    d_rows = cur.fetchall()
    print(f"Dialogues ({len(d_rows)}):")
    for r in d_rows[:5]:
        # print snippet containing char
        text = r[1]
        idx = text.find(char)
        start = max(0, idx - 100)
        end = min(len(text), idx + 200)
        snippet = text[start:end].replace('\n', ' ')
        print(f"  [Sub {r[0]}]: ...{snippet}...")
    if len(d_rows) > 5:
        print(f"  ... and {len(d_rows)-5} more dialogues")

    # 2. Subtasks where char appears
    cur.execute("SELECT sub_id, task_id, name, dialog_npc_name, describe_cleaned FROM subtasks WHERE name LIKE ? OR dialog_npc_name LIKE ? OR describe_cleaned LIKE ?", (f"%{char}%", f"%{char}%", f"%{char}%"))
    st_rows = cur.fetchall()
    print(f"Subtasks ({len(st_rows)}):")
    for r in st_rows[:3]:
        desc = r[4][:150].replace('\n', ' ') if r[4] else ""
        print(f"  [Sub {r[0]} - Task {r[1]} - {r[2]} | NPC: {r[3]}]: {desc}")
    if len(st_rows) > 3:
        print(f"  ... and {len(st_rows)-3} more subtasks")

    # 3. Lore / tales / ambient
    for tbl in ["armycamp_lore", "feature_system_stories", "faction_primer_stories", "linktask_tales"]:
        cur.execute(f"SELECT * FROM [{tbl}] WHERE cleaned_text LIKE ?", (f"%{char}%",))
        l_rows = cur.fetchall()
        if l_rows:
            print(f"Table {tbl} ({len(l_rows)}):")
            for r in l_rows[:2]:
                print(f"  {r}")
