#!/usr/bin/env python3
"""
Lore Guard: Programmatic enforcement of Novel-OS Lore Provenance & Anti-Hallucination.
Ensures zero surface-level guessing of factions, black ops, and sect alignments.
Queries SQLite `story_database.sqlite3` across all 8 tables to provide verified canonical truth.
"""
import os
import sys
import sqlite3
import argparse
import re

sys.stdout.reconfigure(encoding='utf-8')

DB_PATH = "story_database.sqlite3"
if not os.path.exists(DB_PATH):
    DB_PATH = "migration/source_corpus/01_Database/story_database.sqlite3"

TABLES_TO_SEARCH = [
    ("tasks", ["name", "describe_cleaned"]),
    ("subtasks", ["name", "describe_cleaned", "dialog_npc_name"]),
    ("dialogues", ["cleaned_text"]),
    ("armycamp_lore", ["camp_name", "speaker_or_subject", "cleaned_text"]),
    ("linktask_tales", ["category_name", "cleaned_text"]),
    ("faction_primer_stories", ["cleaned_text"]),
    ("feature_system_stories", ["system_name", "subject", "cleaned_text"]),
    ("world_ambient_dialogues", ["map_name", "cleaned_msg"])
]

# Known verified canonical factions & organizations mapping
KNOWN_FACTIONS = {
    "FAC-TVB": "Thiên Vương Bang",
    "FAC-TYM": "Thúy Yên Môn",
    "FAC-CB": "Cái Bang",
    "FAC-NDG": "Ngũ Độc Giáo",
    "FAC-TNG": "Thiên Nhẫn Giáo",
    "FAC-DM": "Đường Môn",
    "FAC-TL": "Thiếu Lâm",
    "FAC-VD": "Võ Đang",
    "FAC-NM": "Nga My",
    "FAC-CL": "Côn Lôn",
    "FAC-DT": "Đoàn Thị",
    "FAC-MG": "Minh Giáo"
}

KNOWN_ORGANIZATIONS = {
    "ORG-CB-ANHXA": "Ảnh Xã",
    "ORG-TH-NHATPHAM": "Nhất Phẩm Đường",
    "ORG-TV-CAPXA": "Cáp Xá",
    "ORG-KIM-OSOSA": "Ô Sơ Sa",
    "ORG-MAY-PHAI": "Ma Y Phái",
    "ORG-NGHIA-QUAN": "Nghĩa Quân"
}

# Forbidden hallucination patterns
HALLUCINATION_PATTERNS = [
    (r"sát thủ Ảnh Xã", "Ảnh Xã là tử sĩ tình báo Cái Bang chống Kim, KHÔNG PHẢI sát thủ đối nghịch!"),
    (r"Ảnh Xã.*tràn xuống phương Nam", "Ảnh Xã hoạt động tại Bạch Thạch Sơn Trường và cài cắm sang Kim quốc, không tràn xuống phương Nam cướp ngọc!"),
    (r"Cầu Chỉ Thủy.*phản bội.*Thiên Nhẫn", "Cầu Chỉ Thủy bị vu cáo mớm cung, KHÔNG PHẢI phản đồ thực sự!"),
    (r"Doãn Hàm Yên.*(mới ngoài đôi mươi|hai mươi hai tuổi|22 tuổi|chưởng môn trẻ tuổi)", "Doãn Hàm Yên 40 tuổi, Lục đại cựu môn chủ, mẹ Doãn Tiêu Vũ (17 tuổi), KHÔNG PHẢI mới ngoài đôi mươi!"),
    (r"Chưởng môn sư tỷ.*Doãn Hàm Yên|Doãn Hàm Yên.*Chưởng môn sư tỷ", "Doãn Hàm Yên là tiền bối thế hệ Lục đại, Hạ Nương (16 tuổi) không gọi là Chưởng môn sư tỷ!"),
    (r"Doãn Hàm Yên.*Lệ sư bá|Lệ sư bá.*Doãn Hàm Yên", "Doãn Hàm Yên và Lệ Thu Thủy là đồng bối sư muội - sư tỷ, Doãn Hàm Yên KHÔNG ĐƯỢC gọi Lệ Thu Thủy là sư bá!"),
    (r"Bạch Cương\s+(là|chính là|vốn là)\s+(phụ thân|cha|bố)\s+(của\s+)?Bạch Thu Lâm|Bạch Thu Lâm\s+(là|vốn là)\s+(con gái|nữ nhi)\s+(của\s+)?Bạch Cương|(con gái|nữ nhi)\s+(của\s+)?Bạch Cương.*Bạch Thu Lâm|(phụ thân|cha|bố)\s+của\s+Bạch Thu Lâm\s+(là|chính là)\s+Bạch Cương", "Bạch Cương KHÔNG PHẢI cha Bạch Thu Lâm! Trong baijiang.lua Bạch Cương gọi 'Thu Lâm tỷ' và tự xưng 'đệ'! Thân phụ Bạch Thu Lâm là Tướng quân Bạch Phụ tại Biện Kinh (Task 450)."),
    (r"Thu Di.*(giấu con|cho di ăn|con đi cùng Di|di định đợi)|di giấu con|cho di ăn lót dạ", "Tiêu Phùng (17 tuổi) và Bạch Thu Lâm (24 tuổi) chênh lệch 7 tuổi, quan hệ là TỶ - ĐỆ (xưng Thu Di / Tỷ — Đệ). Tuyệt đối KHÔNG xưng Di - con phi logic sinh học!"),
    (r"Tĩnh Xuyên.*(18 tuổi|mười tám tuổi)|(18 tuổi|mười tám tuổi).*Tĩnh Xuyên", "Tĩnh Xuyên sinh năm 1171 (Tân Mão), debut Quyển 1 (năm 1191) đúng tròn 20 tuổi (tuổi nhược quán), KHÔNG PHẢI 18 tuổi!"),
]

def query_lore(term):
    if not os.path.exists(DB_PATH):
        print(f"[LORE-GUARD ERROR] Database not found at {DB_PATH}")
        return 1

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    print(f"\n=======================================================")
    print(f"🔍 [LORE-GUARD] SEARCHING SQLITE FOR: '{term}'")
    print(f"=======================================================")

    total_matches = 0
    for table, cols in TABLES_TO_SEARCH:
        table_matches = []
        for col in cols:
            try:
                query = f"SELECT rowid, {col} FROM {table} WHERE {col} LIKE ?"
                rows = cur.execute(query, (f"%{term}%",)).fetchall()
                for r in rows:
                    table_matches.append((r[0], col, r[1]))
            except sqlite3.OperationalError:
                continue
        
        if table_matches:
            print(f"\n📁 Bảng: `{table}` ({len(table_matches)} kết quả)")
            for rowid, col, text in table_matches[:4]:
                snippet = text.replace('\n', ' ')
                if len(snippet) > 180:
                    snippet = snippet[:180] + "..."
                print(f"   - [ID {rowid} | {col}]: {snippet}")
            if len(table_matches) > 4:
                print(f"     ... và {len(table_matches) - 4} kết quả khác.")
            total_matches += len(table_matches)

    print(f"\n--> Tổng số kết quả tìm thấy: {total_matches}")
    return 0

def check_file(filepath):
    if not os.path.exists(filepath):
        print(f"[LORE-GUARD ERROR] File not found: {filepath}")
        return 1

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    errors = []
    # 1. Check known hallucination patterns
    for pat, explanation in HALLUCINATION_PATTERNS:
        match = re.search(pat, content, re.IGNORECASE)
        if match:
            errors.append(f"Phát hiện suy diễn sai lệch: '{match.group(0)}' -> {explanation}")

    if errors:
        print(f"\n❌ [LORE-GUARD FAIL] {filepath}")
        for err in errors:
            print(f"   - {err}")
        return 1

    print(f"✅ [LORE-GUARD PASS] {filepath}: 0 lỗi lore / Zero Hallucination.")
    return 0

def scan_all():
    print("\n=======================================================")
    print("🛡️ [LORE-GUARD] SCANNING ALL PROJECT FILES FOR LORE INTEGRITY")
    print("=======================================================")
    
    scan_dirs = ["briefs", "chapters", "plot", "worldbuilding/factions"]
    failed = 0
    checked = 0

    for sdir in scan_dirs:
        if not os.path.exists(sdir):
            continue
        for root, _, files in os.walk(sdir):
            for file in files:
                if file.endswith(".md"):
                    fpath = os.path.join(root, file)
                    res = check_file(fpath)
                    checked += 1
                    if res != 0:
                        failed += 1

    print(f"\n--> Quét hoàn tất: {checked} tệp, {failed} tệp vi phạm.")
    return 1 if failed > 0 else 0

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Novel-OS Lore Guard & Anti-Hallucination Tool")
    parser.add_argument("--query", "-q", type=str, help="Tra cứu từ khóa trên toàn bộ 8 bảng CSDL SQLite")
    parser.add_argument("--check", "-c", type=str, help="Quét kiểm tra 1 file markdown cụ thể")
    parser.add_argument("--scan", "-s", action="store_true", help="Quét kiểm tra toàn bộ thư mục truyện")

    args = parser.parse_args()

    if args.query:
        sys.exit(query_lore(args.query))
    elif args.check:
        sys.exit(check_file(args.check))
    elif args.scan:
        sys.exit(scan_all())
    else:
        # Default: scan all
        sys.exit(scan_all())
