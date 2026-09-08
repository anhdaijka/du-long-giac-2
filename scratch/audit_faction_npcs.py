import sqlite3
import sys

sys.stdout.reconfigure(encoding='utf-8')

conn = sqlite3.connect('story_database.sqlite3')
cur = conn.cursor()

def get_npc_mentions(npc_names):
    results = {}
    for name in npc_names:
        results[name] = {"subtasks": [], "dialogues": [], "ambient": []}
        cur.execute("SELECT sub_id, task_id, name, dialog_npc_name, describe_cleaned FROM subtasks WHERE dialog_npc_name LIKE ? OR describe_cleaned LIKE ?", (f"%{name}%", f"%{name}%"))
        results[name]["subtasks"] = cur.fetchall()
        cur.execute("SELECT sub_id, phase, cleaned_text FROM dialogues WHERE cleaned_text LIKE ?", (f"%{name}%",))
        results[name]["dialogues"] = cur.fetchall()
    return results

print("=== AUDITING THIEN VUONG & THUY YEN & NGHIA QUAN NPCS ===")

# Check Thien Vuong NPCs
tv_npcs = ["Dương Anh", "Dương Thiết Tâm", "Cầu Chỉ Thủy", "Bùi Dực Phi", "Lâu Nhất Quan", "Quý Thúc Ban"]
tv_data = get_npc_mentions(tv_npcs)
for k, v in tv_data.items():
    print(f"NPC: {k} -> {len(v['subtasks'])} subtasks, {len(v['dialogues'])} dialogues")

# Check Thuy Yen NPCs
ty_npcs = ["Doãn Hàm Yên", "Lệ Thu Thủy", "Đan Bích Tú", "Chung Linh Tú", "Doãn Tiêu Vũ", "Ma Y Thần Tướng"]
ty_data = get_npc_mentions(ty_npcs)
for k, v in ty_data.items():
    print(f"NPC: {k} -> {len(v['subtasks'])} subtasks, {len(v['dialogues'])} dialogues")

# Check Nghia Quan NPCs
nq_npcs = ["Bạch Thu Lâm", "Bạch Cương", "Long Ngũ", "Trâu Đức Khoái", "Giới Sơn Tông", "Bất Động", "Điềm Tửu", "Thẩm Thiết Thạch", "Thẩm Hà Diệp"]
nq_data = get_npc_mentions(nq_npcs)
for k, v in nq_data.items():
    print(f"NPC: {k} -> {len(v['subtasks'])} subtasks, {len(v['dialogues'])} dialogues")
