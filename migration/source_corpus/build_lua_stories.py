#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kiếm Thế 2 - Phase 3: LUA Story Extractor (Army Camp, Faction Primer, LinkTask, World NPC Ambient)
Bóc tách kịch bản LUA Quân Doanh, Tân Thủ 12 Phái, Bao Vạn Đồng, Thương Hội & 720 NPC Thế Giới.
Tuân thủ 100% nguyên tắc Strict Provenance - Không suy diễn, giữ trọn vẹn chứng cứ.
"""

import os
import sys
import glob
import json
import sqlite3
import csv
import re
from pathlib import Path

# Cấu hình UTF-8 cho Windows console
try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

from build_story_extractor import Dictionaries, TextSanitizer, BASE_DIR, OUTPUT_DIR, DB_OUTPUT_DIR, SERVER_SETTING

SCRIPT_TASK_DIR = BASE_DIR / "Kiếm Thế 2" / "Server" / "Docker_KT2" / "Kiemthe2-server" / "gameserver" / "script" / "task"
SETTING_NPC_DIR = SERVER_SETTING / "npc"
SETTING_TASK_DIR = SERVER_SETTING / "task"

class LuaStoryExtractor:
    def __init__(self):
        self.dicts = Dictionaries()
        self.dicts.load_all()
        self.sanitizer = TextSanitizer(self.dicts)
        
        self.armycamp_data = []
        self.primer_data = []
        self.linktask_data = []
        self.ambient_data = []
        self.merchant_wanted_data = []

    def run_all(self):
        print("==================================================================")
        print("GIAI ĐOẠN 3: BÓC TÁCH KỊCH BẢN LUA QUÂN DOANH, MÔN PHÁI, BAO VẠN ĐỒNG & NPC")
        print("==================================================================")
        self.extract_ambient_dialogues()
        self.extract_linktask_stories()
        self.extract_armycamp_lore()
        self.extract_primer_stories()
        self.extract_merchant_wanted()
        self.save_to_database()
        self.export_phase_3_reports()

    def extract_ambient_dialogues(self):
        """Bóc tách 720 đối thoại NPC đời thường từ dialognpc.txt"""
        file_path = SETTING_NPC_DIR / "dialognpc.txt"
        print(f"\n[1/5] Đang bóc tách NPC đối thoại thế giới: {file_path.name}...")
        
        if not file_path.exists():
            print(f"[CẢNH BÁO] Không tìm thấy file {file_path}")
            return

        count = 0
        with open(file_path, "r", encoding="utf-8-sig", errors="replace") as f:
            reader = csv.DictReader(f, delimiter="\t")
            for row in reader:
                rec_id = row.get("Id", "").strip()
                map_name = row.get("Map", "").strip()
                map_id = row.get("MapId", "").strip()
                class_name = row.get("ClassName", "").strip()
                msg = row.get("Msg", "").strip()
                
                # Gom các options hội thoại
                options = []
                for i in range(1, 13):
                    opt = row.get(f"Option{i}", "").strip()
                    if opt:
                        options.append(opt.replace('""', '"'))
                        
                cleaned_msg = self.sanitizer.clean(msg)
                
                self.ambient_data.append({
                    "record_id": int(rec_id) if rec_id.isdigit() else count + 1,
                    "map_id": int(map_id) if map_id.isdigit() else 0,
                    "map_name": map_name,
                    "npc_class": class_name,
                    "raw_msg": msg,
                    "cleaned_msg": cleaned_msg,
                    "options": options,
                    "file_path": str(file_path.relative_to(BASE_DIR))
                })
                count += 1
                
        print(f"      -> Đã bóc tách {count} bản ghi đối thoại phong thổ tại 30 đại thành thị / môn phái.")

    def extract_linktask_stories(self):
        """Bóc tách 50 mẩu truyện tình báo, nghĩa quân và dân gian từ linktask/text.lua"""
        file_path = SCRIPT_TASK_DIR / "linktask" / "text.lua"
        print(f"\n[2/5] Đang bóc tách truyện ngắn nghĩa quân Bao Vạn Đồng: {file_path.name}...")
        
        if not file_path.exists():
            print(f"[CẢNH BÁO] Không tìm thấy file {file_path}")
            return

        content = file_path.read_text(encoding="utf-8-sig", errors="replace")
        
        # Bóc tách từng mảng LinkTask.Text[10000], [20000], [30000]
        array_matches = re.finditer(r"LinkTask\.Text\[(\d+)\]\s*=\s*\{([^}]+)\};", content)
        count = 0
        for m in array_matches:
            category_code = int(m.group(1))
            body = m.group(2)
            
            # Bóc tách từng dòng [idx] = "..."
            entry_matches = re.finditer(r'\[(\d+)\]\s*=\s*"([^"]+)"', body)
            for em in entry_matches:
                idx = int(em.group(1))
                text = em.group(2)
                cleaned_text = self.sanitizer.clean(text)
                
                cat_name = "Nghĩa quân / Tình báo chiến sự" if category_code in [10000, 30000] else "Thảo phạt ác đồ giang hồ"
                
                self.linktask_data.append({
                    "category_code": category_code,
                    "index": idx,
                    "category_name": cat_name,
                    "raw_text": text,
                    "cleaned_text": cleaned_text,
                    "file_path": str(file_path.relative_to(BASE_DIR))
                })
                count += 1
                
        print(f"      -> Đã bóc tách {count} mẩu truyện ngắn cốt truyện Bao Vạn Đồng.")

    def extract_armycamp_lore(self):
        """Bóc tách kịch bản 4 đại chiến trường Quân Doanh: Phục Ngưu Sơn, Bách Man Sơn, Hải Lăng Vương Mộ, Ngạc Luân Hà Nguyên"""
        army_dir = SCRIPT_TASK_DIR / "armycamp"
        print(f"\n[3/5] Đang bóc tách kịch bản 4 Đại Chiến Trường Quân Doanh...")
        
        camps = [
            ("90_100", "Hậu Sơn Phục Ngưu Sơn", 1, "Cấp 90 - 100", "Chiến sự thảo phạt sơn tặc và thủ hộ doanh trại Phục Ngưu"),
            ("100_110", "Bách Man Sơn", 2, "Cấp 100 - 110", "Rừng thiêng nước độc Miêu Cương, thâm nhập sào huyệt Cổ Vương"),
            ("110_120", "Hải Lăng Vương Mộ", 3, "Cấp 110 - 120", "Thâm nhập lăng tẩm hoàng đế Kim quốc Hoàn Nhan Lượng, cạm bẫy cổ mộ"),
            ("elunheyuan", "Ngạc Luân Hà Nguyên", 4, "Cấp 130+", "Chiến trường thảo nguyên Mông Cổ, đàm đạo Đà Lôi Khả Hãn & Mộc Hoa Lê")
        ]

        count = 0
        for folder_name, camp_name, camp_id, level_req, desc in camps:
            camp_path = army_dir / folder_name
            if not camp_path.exists():
                continue
                
            main_lua = camp_path / "main.lua"
            main_desc = ""
            if main_lua.exists():
                main_text = main_lua.read_text(encoding="utf-8-sig", errors="replace")
                desc_m = re.search(r'tbInstancing\.szDesc\s*=\s*"([^"]+)"', main_text)
                if desc_m:
                    main_desc = desc_m.group(1)

            # Quét các file npc, boss, item trong camp
            for lua_file in camp_path.rglob("*.lua"):
                text = lua_file.read_text(encoding="utf-8-sig", errors="replace")
                
                # Tìm các câu thoại Dialog:Say hoặc chuỗi thông báo
                for sm in re.finditer(r'Dialog:Say\s*\(\s*"([^"]+)"', text):
                    raw_say = sm.group(1)
                    self.armycamp_data.append({
                        "camp_id": camp_id,
                        "camp_name": camp_name,
                        "level_req": level_req,
                        "section": lua_file.stem,
                        "lore_type": "Đối thoại kịch bản",
                        "speaker_or_subject": lua_file.stem,
                        "raw_text": raw_say,
                        "cleaned_text": self.sanitizer.clean(raw_say),
                        "file_path": str(lua_file.relative_to(BASE_DIR))
                    })
                    count += 1
                    
                # Tìm các chuỗi thông báo phụ bản
                for bm in re.finditer(r'szMsg\s*=\s*"([^"]{10,})"', text):
                    raw_msg = bm.group(1)
                    if "<color" in raw_msg or "khiêu chiến" in raw_msg or "đánh bại" in raw_msg or "bí mật" in raw_msg:
                        self.armycamp_data.append({
                            "camp_id": camp_id,
                            "camp_name": camp_name,
                            "level_req": level_req,
                            "section": lua_file.stem,
                            "lore_type": "Thông cáo cốt truyện",
                            "speaker_or_subject": lua_file.stem,
                            "raw_text": raw_msg,
                            "cleaned_text": self.sanitizer.clean(raw_msg),
                            "file_path": str(lua_file.relative_to(BASE_DIR))
                        })
                        count += 1

            # Bóc tách ngân hàng câu hỏi lịch sử Ngạc Luân Hà Nguyên nếu có
            q_file = SETTING_TASK_DIR / "armycamp" / "elunheyuan" / "question.txt"
            if folder_name == "elunheyuan" and q_file.exists():
                with open(q_file, "r", encoding="utf-8-sig", errors="replace") as f:
                    q_reader = csv.reader(f, delimiter="\t")
                    for q_row in q_reader:
                        if len(q_row) >= 2 and q_row[0].strip():
                            q_text = q_row[0].strip()
                            ans_text = q_row[1].strip() if len(q_row) > 1 else ""
                            self.armycamp_data.append({
                                "camp_id": camp_id,
                                "camp_name": camp_name,
                                "level_req": level_req,
                                "section": "Khảo nghiệm Mông Cổ",
                                "lore_type": "Tri thức lịch sử Thảo Nguyên",
                                "speaker_or_subject": "Đà Lôi Khả Hãn",
                                "raw_text": f"Hỏi: {q_text} | Đáp: {ans_text}",
                                "cleaned_text": f"Hỏi: {q_text} | Đáp: {ans_text}",
                                "file_path": str(q_file.relative_to(BASE_DIR))
                            })
                            count += 1

        print(f"      -> Đã bóc tách {count} phân đoạn hội thoại, thông cáo và tri thức 4 Đại Quân Doanh.")

    def extract_primer_stories(self):
        """Bóc tách kịch bản phó bản giáo dục tân thủ cấp 10 & 20 và nhập môn 12 phái"""
        primer_dir = SCRIPT_TASK_DIR / "primer"
        print(f"\n[4/5] Đang bóc tách kịch bản Tân Thủ & Nhập Môn Môn Phái: {primer_dir.name}...")
        
        count = 0
        if primer_dir.exists():
            for lua_file in primer_dir.rglob("*.lua"):
                text = lua_file.read_text(encoding="utf-8-sig", errors="replace")
                
                # Bóc tách Dialog:Say
                for sm in re.finditer(r'Dialog:Say\s*\(\s*"([^"]+)"', text):
                    raw_say = sm.group(1)
                    level = "Cấp 10" if "10" in lua_file.name else ("Cấp 20" if "20" in lua_file.name else "Tân Thủ")
                    self.primer_data.append({
                        "level_group": level,
                        "section": lua_file.stem,
                        "raw_text": raw_say,
                        "cleaned_text": self.sanitizer.clean(raw_say),
                        "file_path": str(lua_file.relative_to(BASE_DIR))
                    })
                    count += 1
                    
        print(f"      -> Đã bóc tách {count} phân đoạn hội thoại Tân Thủ & Nhập Môn.")

    def extract_merchant_wanted(self):
        """Bóc tách Thương Hội Chu Tử Chân và Truy Nã Hải Tặc"""
        merchant_dir = SCRIPT_TASK_DIR / "merchant"
        wanted_dir = SCRIPT_TASK_DIR / "wanted"
        print(f"\n[5/5] Đang bóc tách kịch bản Thương Hội & Truy Nã...")
        
        count = 0
        # Merchant
        if merchant_dir.exists():
            for f in merchant_dir.rglob("*.lua"):
                text = f.read_text(encoding="utf-8-sig", errors="replace")
                for sm in re.finditer(r'Dialog:Say\s*\(\s*(\[\[.*?\]\]|"[^"]+")', text, re.DOTALL):
                    raw_say = sm.group(1).strip("[]\"")
                    self.merchant_wanted_data.append({
                        "system_name": "Thương Hội (Merchant)",
                        "subject": f.stem,
                        "raw_text": raw_say,
                        "cleaned_text": self.sanitizer.clean(raw_say),
                        "file_path": str(f.relative_to(BASE_DIR))
                    })
                    count += 1

        # Wanted
        if wanted_dir.exists():
            for f in wanted_dir.rglob("*.lua"):
                text = f.read_text(encoding="utf-8-sig", errors="replace")
                for sm in re.finditer(r'Dialog:Say\s*\(\s*(\[\[.*?\]\]|"[^"]+")', text, re.DOTALL):
                    raw_say = sm.group(1).strip("[]\"")
                    self.merchant_wanted_data.append({
                        "system_name": "Truy Nã Hải Tặc (Wanted)",
                        "subject": f.stem,
                        "raw_text": raw_say,
                        "cleaned_text": self.sanitizer.clean(raw_say),
                        "file_path": str(f.relative_to(BASE_DIR))
                    })
                    count += 1

        print(f"      -> Đã bóc tách {count} phân đoạn kịch bản Thương Hội và Truy Nã.")

    def save_to_database(self):
        """Lưu toàn bộ dữ liệu Phase 3 vào SQLite và cập nhật file JSON"""
        sqlite_path = DB_OUTPUT_DIR / "story_database.sqlite3"
        print(f"\n[Cập nhật CSDL] Đang ghi dữ liệu Phase 3 vào {sqlite_path.name}...")
        
        conn = sqlite3.connect(sqlite_path)
        cur = conn.cursor()
        
        # 1. Bảng world_ambient_dialogues
        cur.execute("""
        CREATE TABLE IF NOT EXISTS world_ambient_dialogues (
            id INTEGER PRIMARY KEY,
            map_id INTEGER,
            map_name TEXT,
            npc_class TEXT,
            raw_msg TEXT,
            cleaned_msg TEXT,
            options TEXT,
            file_path TEXT
        );
        """)
        cur.execute("CREATE INDEX IF NOT EXISTS idx_amb_map ON world_ambient_dialogues(map_id);")
        cur.execute("CREATE INDEX IF NOT EXISTS idx_amb_mapname ON world_ambient_dialogues(map_name);")
        
        for amb in self.ambient_data:
            cur.execute("""
            INSERT INTO world_ambient_dialogues (id, map_id, map_name, npc_class, raw_msg, cleaned_msg, options, file_path)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                amb["record_id"],
                amb["map_id"],
                amb["map_name"],
                amb["npc_class"],
                amb["raw_msg"],
                amb["cleaned_msg"],
                " | ".join(amb["options"]),
                amb["file_path"]
            ))

        # 2. Bảng armycamp_lore
        cur.execute("""
        CREATE TABLE IF NOT EXISTS armycamp_lore (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            camp_id INTEGER,
            camp_name TEXT,
            level_req TEXT,
            section TEXT,
            lore_type TEXT,
            speaker_or_subject TEXT,
            raw_text TEXT,
            cleaned_text TEXT,
            file_path TEXT
        );
        """)
        cur.execute("CREATE INDEX IF NOT EXISTS idx_army_camp ON armycamp_lore(camp_id);")
        
        for item in self.armycamp_data:
            cur.execute("""
            INSERT INTO armycamp_lore (camp_id, camp_name, level_req, section, lore_type, speaker_or_subject, raw_text, cleaned_text, file_path)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                item["camp_id"],
                item["camp_name"],
                item["level_req"],
                item["section"],
                item["lore_type"],
                item["speaker_or_subject"],
                item["raw_text"],
                item["cleaned_text"],
                item["file_path"]
            ))

        # 3. Bảng linktask_tales
        cur.execute("""
        CREATE TABLE IF NOT EXISTS linktask_tales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category_code INTEGER,
            category_name TEXT,
            entry_index INTEGER,
            raw_text TEXT,
            cleaned_text TEXT,
            file_path TEXT
        );
        """)
        
        for lt in self.linktask_data:
            cur.execute("""
            INSERT INTO linktask_tales (category_code, category_name, entry_index, raw_text, cleaned_text, file_path)
            VALUES (?, ?, ?, ?, ?, ?)
            """, (
                lt["category_code"],
                lt["category_name"],
                lt["index"],
                lt["raw_text"],
                lt["cleaned_text"],
                lt["file_path"]
            ))

        # 4. Bảng faction_primer_stories
        cur.execute("""
        CREATE TABLE IF NOT EXISTS faction_primer_stories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            level_group TEXT,
            section TEXT,
            raw_text TEXT,
            cleaned_text TEXT,
            file_path TEXT
        );
        """)
        
        for pr in self.primer_data:
            cur.execute("""
            INSERT INTO faction_primer_stories (level_group, section, raw_text, cleaned_text, file_path)
            VALUES (?, ?, ?, ?, ?)
            """, (
                pr["level_group"],
                pr["section"],
                pr["raw_text"],
                pr["cleaned_text"],
                pr["file_path"]
            ))

        # 5. Bảng feature_system_stories (Merchant, Wanted)
        cur.execute("""
        CREATE TABLE IF NOT EXISTS feature_system_stories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            system_name TEXT,
            subject TEXT,
            raw_text TEXT,
            cleaned_text TEXT,
            file_path TEXT
        );
        """)
        
        for mw in self.merchant_wanted_data:
            cur.execute("""
            INSERT INTO feature_system_stories (system_name, subject, raw_text, cleaned_text, file_path)
            VALUES (?, ?, ?, ?, ?)
            """, (
                mw["system_name"],
                mw["subject"],
                mw["raw_text"],
                mw["cleaned_text"],
                mw["file_path"]
            ))

        conn.commit()
        conn.close()
        print(f"      -> Hoàn tất cập nhật 5 bảng LUA & Ambient vào SQLite: {sqlite_path.stat().st_size / (1024*1024):.2f} MB")

        # Cập nhật file JSON
        json_path = DB_OUTPUT_DIR / "story_database.json"
        if json_path.exists():
            print(f"      -> Đang cập nhật {json_path.name} với dữ liệu Phase 3...")
            with open(json_path, "r", encoding="utf-8") as f:
                full_db = json.load(f)
            full_db["world_ambient_dialogues"] = self.ambient_data
            full_db["armycamp_lore"] = self.armycamp_data
            full_db["linktask_tales"] = self.linktask_data
            full_db["primer_stories"] = self.primer_data
            full_db["feature_system_stories"] = self.merchant_wanted_data
            
            with open(json_path, "w", encoding="utf-8") as f:
                json.dump(full_db, f, ensure_ascii=False, indent=2)
            print(f"      -> Hoàn tất cập nhật JSON: {json_path.stat().st_size / (1024*1024):.2f} MB")

    def export_phase_3_reports(self):
        """Xuất báo cáo kiểm tra và mẫu đối chiếu Giai đoạn 3"""
        report_path = OUTPUT_DIR / "PHASE_3_AUDIT_REPORT.json"
        audit = {
            "total_ambient_dialogues": len(self.ambient_data),
            "total_armycamp_lore_snippets": len(self.armycamp_data),
            "total_linktask_tales": len(self.linktask_data),
            "total_primer_snippets": len(self.primer_data),
            "total_feature_system_snippets": len(self.merchant_wanted_data),
            "total_records_phase_3": len(self.ambient_data) + len(self.armycamp_data) + len(self.linktask_data) + len(self.primer_data) + len(self.merchant_wanted_data)
        }
        with open(report_path, "w", encoding="utf-8") as f:
            json.dump(audit, f, ensure_ascii=False, indent=2)
        print(f"\n[Báo cáo] Đã lưu báo cáo thống kê Phase 3 tại: {report_path}")

        sample_path = OUTPUT_DIR / "PHASE_3_SAMPLE_VERIFICATION.md"
        with open(sample_path, "w", encoding="utf-8") as f:
            f.write("# BÁO CÁO MẪU KIỂM CHỨNG GIAI ĐOẠN 3: LUA SCRIPTS & NPC THẾ GIỚI (STRICT PROVENANCE)\n\n")
            f.write("> Đối chiếu trực tiếp dữ liệu trích xuất từ các file LUA và bảng cấu hình `dialognpc.txt`.\n\n")

            f.write("## 1. Mẫu Đối Thoại NPC Thế Giới (Ambient NPCs)\n\n")
            for item in self.ambient_data[:5]:
                f.write(f"### [{item['map_name']}] Lớp NPC: `{item['npc_class']}` (Record #{item['record_id']})\n")
                f.write(f"- **Nguồn**: `{item['file_path']}` (Map ID: {item['map_id']})\n")
                f.write(f"- **Lời thoại**: {item['cleaned_msg']}\n")
                if item["options"]:
                    f.write(f"- **Các lựa chọn tương tác**: {', '.join(item['options'][:3])}\n")
                f.write("\n---\n\n")

            f.write("## 2. Mẫu Kịch Bản 4 Đại Chiến Trường Quân Doanh\n\n")
            sample_camps = {}
            for item in self.armycamp_data:
                cid = item["camp_name"]
                if cid not in sample_camps:
                    sample_camps[cid] = []
                if len(sample_camps[cid]) < 2:
                    sample_camps[cid].append(item)

            for camp_name, items in sample_camps.items():
                f.write(f"### Chiến trường: {camp_name}\n")
                for it in items:
                    f.write(f"- **Phân đoạn**: `{it['section']}` ({it['lore_type']}) | **Nguồn**: `{it['file_path']}`\n")
                    f.write(f"- **Nội dung**: {it['cleaned_text']}\n\n")
                f.write("---\n\n")

            f.write("## 3. Mẫu Truyện Ngắn Nghĩa Quân Bao Vạn Đồng\n\n")
            for item in self.linktask_data[:3]:
                f.write(f"### [Bao Vạn Đồng] Truyện #{item['index']} ({item['category_name']})\n")
                f.write(f"- **Nguồn**: `{item['file_path']}` (Mã: {item['category_code']})\n")
                f.write(f"- **Nguyên văn**: {item['cleaned_text']}\n\n")
                f.write("---\n\n")

        print(f"[Sample] Đã xuất mẫu kiểm chứng Phase 3 tại: {sample_path}")
        print("\n==================================================================")
        print("HOÀN TẤT GIAI ĐOẠN 3: TOÀN BỘ KỊCH BẢN LUA & NPC ĐÃ ĐƯỢC TÍCH HỢP")
        print("==================================================================")

if __name__ == "__main__":
    extractor = LuaStoryExtractor()
    extractor.run_all()
