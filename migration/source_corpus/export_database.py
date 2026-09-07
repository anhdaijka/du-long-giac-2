#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kiếm Thế 2 - Phase 2: Database Exporter (JSON, SQLite3, CSV, Provenance Manifest)
Tuân thủ 100% nguyên tắc Strict Provenance - Không suy diễn, giữ trọn vẹn chứng cứ.
"""

import os
import sys
import glob
import json
import sqlite3
import csv
import hashlib
from pathlib import Path

# Cấu hình UTF-8 cho Windows console
try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

# Import StoryExtractor từ build_story_extractor
from build_story_extractor import StoryExtractor, BASE_DIR, OUTPUT_DIR, DB_OUTPUT_DIR, TASK_DIR, SUB_DIR

def sha256_file(filepath: Path) -> str:
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()

def export_all():
    print("==================================================================")
    print("GIAI ĐOẠN 2: TRÍCH XUẤT CƠ SỞ DỮ LIỆU CẤU TRÚC (STRICT PROVENANCE)")
    print("==================================================================")
    
    DB_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    extractor = StoryExtractor()
    extractor.parse_all()
    
    # 1. Xuất file story_database.json
    json_path = DB_OUTPUT_DIR / "story_database.json"
    print(f"\n[1/4] Đang ghi {json_path.name}...")
    full_db = {
        "metadata": {
            "title": "Kiếm Thế 2 - Toàn Tập Cốt Truyện & Nhiệm Vụ (Ground Truth Database)",
            "version": "1.0",
            "total_tasks": len(extractor.tasks),
            "total_subs": len(extractor.subs),
            "provenance_standard": "Strict Forensic Provenance (0% speculative extrapolation)"
        },
        "tasks": extractor.tasks,
        "subs": extractor.subs
    }
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(full_db, f, ensure_ascii=False, indent=2)
    print(f"      -> Hoàn tất ghi {json_path.stat().st_size / (1024*1024):.2f} MB")

    # 2. Xuất file story_database.sqlite3
    sqlite_path = DB_OUTPUT_DIR / "story_database.sqlite3"
    print(f"\n[2/4] Đang tạo CSDL SQLite {sqlite_path.name}...")
    if sqlite_path.exists():
        sqlite_path.unlink()
        
    conn = sqlite3.connect(sqlite_path)
    cur = conn.cursor()
    
    # Tạo bảng
    cur.execute("""
    CREATE TABLE tasks (
        task_id INTEGER PRIMARY KEY,
        task_id_hex TEXT NOT NULL,
        name TEXT NOT NULL,
        describe_raw TEXT,
        describe_cleaned TEXT,
        category TEXT,
        category_desc TEXT,
        order_type TEXT,
        repeat INTEGER,
        task_type_code TEXT,
        file_path TEXT NOT NULL
    );
    """)
    cur.execute("CREATE INDEX idx_tasks_cat ON tasks(category);")
    
    cur.execute("""
    CREATE TABLE subtasks (
        sub_id INTEGER PRIMARY KEY,
        sub_id_hex TEXT NOT NULL,
        task_id INTEGER,
        name TEXT NOT NULL,
        describe_raw TEXT,
        describe_cleaned TEXT,
        file_path TEXT NOT NULL,
        dialog_npc_id INTEGER,
        dialog_npc_name TEXT,
        FOREIGN KEY(task_id) REFERENCES tasks(task_id)
    );
    """)
    cur.execute("CREATE INDEX idx_subs_task ON subtasks(task_id);")
    
    cur.execute("""
    CREATE TABLE dialogues (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sub_id INTEGER NOT NULL,
        phase TEXT NOT NULL,
        raw_text TEXT,
        cleaned_text TEXT,
        FOREIGN KEY(sub_id) REFERENCES subtasks(sub_id)
    );
    """)
    cur.execute("CREATE INDEX idx_dial_sub ON dialogues(sub_id);")
    cur.execute("CREATE INDEX idx_dial_phase ON dialogues(phase);")
    
    cur.execute("""
    CREATE TABLE steps (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sub_id INTEGER NOT NULL,
        step_index INTEGER NOT NULL,
        instruction TEXT,
        target_function TEXT,
        target_params TEXT,
        FOREIGN KEY(sub_id) REFERENCES subtasks(sub_id)
    );
    """)
    cur.execute("CREATE INDEX idx_steps_sub ON steps(sub_id);")

    # Nạp dữ liệu vào bảng Tasks
    for t_id, task in extractor.tasks.items():
        cur.execute("""
        INSERT INTO tasks (task_id, task_id_hex, name, describe_raw, describe_cleaned, category, category_desc, order_type, repeat, task_type_code, file_path)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            task["task_id"],
            task["task_id_hex"],
            task["name"],
            task["describe_raw"],
            task["describe_cleaned"],
            task["category"],
            task["category_desc"],
            task["order"],
            1 if task["repeat"] else 0,
            task["task_type_code"],
            task["file_path"]
        ))
        
    # Nạp dữ liệu vào bảng Subtasks, Dialogues, Steps
    for s_id, sub in extractor.subs.items():
        t_id = extractor.refer_to_task.get(s_id)
        
        # Tìm thông tin dialog_npc và describe từ task managed_subs nếu Sub XML để trống
        dialog_npc_id = 0
        dialog_npc_name = ""
        sub_desc_raw = sub["describe_raw"]
        sub_desc_cleaned = sub["describe_cleaned"]
        
        if t_id and t_id in extractor.tasks:
            for m in extractor.tasks[t_id]["managed_subs"]:
                if m["sub_id"] == s_id:
                    dialog_npc_id = m.get("dialog_npc_id", 0)
                    dialog_npc_name = m.get("dialog_npc_name", "")
                    if (not sub_desc_cleaned or len(sub_desc_cleaned.strip()) == 0) and m.get("describe_cleaned"):
                        sub_desc_cleaned = m.get("describe_cleaned")
                        sub_desc_raw = m.get("describe_raw")
                    break
                    
        cur.execute("""
        INSERT INTO subtasks (sub_id, sub_id_hex, task_id, name, describe_raw, describe_cleaned, file_path, dialog_npc_id, dialog_npc_name)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            sub["sub_id"],
            sub["sub_id_hex"],
            t_id,
            sub["name"],
            sub_desc_raw,
            sub_desc_cleaned,
            sub["file_path"],
            dialog_npc_id,
            dialog_npc_name
        ))
        
        # Nạp dialogues
        for phase, d in sub.get("dialogues", {}).items():
            cur.execute("""
            INSERT INTO dialogues (sub_id, phase, raw_text, cleaned_text)
            VALUES (?, ?, ?, ?)
            """, (
                s_id,
                phase,
                d["raw"],
                d["cleaned"]
            ))
            
        # Nạp steps
        for st in sub.get("steps", []):
            funcs = []
            params = []
            for t in st.get("targets", []):
                funcs.append(t["function"])
                params.append(",".join(t["params"]))
            cur.execute("""
            INSERT INTO steps (sub_id, step_index, instruction, target_function, target_params)
            VALUES (?, ?, ?, ?, ?)
            """, (
                s_id,
                st["step_index"],
                "", # instruction được lưu ở task managed_subs step_descs
                "; ".join(funcs),
                "; ".join(params)
            ))

    conn.commit()
    conn.close()
    print(f"      -> Hoàn tất tạo CSDL SQLite: {sqlite_path.stat().st_size / (1024*1024):.2f} MB")

    # 3. Xuất file tasks_catalog.csv
    csv_path = DB_OUTPUT_DIR / "tasks_catalog.csv"
    print(f"\n[3/4] Đang tạo danh mục bảng {csv_path.name}...")
    with open(csv_path, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "Task_ID_Dec",
            "Task_ID_Hex",
            "Tên_Nhiệm_Vụ",
            "Thể_Loại",
            "Thứ_Tự_Logic",
            "Số_Subtask",
            "Người_Giao_Đầu_Tiên",
            "Nguồn_File",
            "Tóm_Tắt_Cốt_Truyện_Gốc"
        ])
        for t_id in sorted(extractor.tasks.keys()):
            task = extractor.tasks[t_id]
            first_giver = task["managed_subs"][0]["dialog_npc_name"] if task["managed_subs"] else ""
            desc_brief = task["describe_cleaned"].replace("\n", " ")[:200]
            if len(task["describe_cleaned"]) > 200:
                desc_brief += "..."
            writer.writerow([
                task["task_id"],
                task["task_id_hex"],
                task["name"],
                task["category"],
                task["order"],
                len(task["managed_subs"]),
                first_giver,
                task["file_path"],
                desc_brief
            ])
    print(f"      -> Hoàn tất ghi {csv_path.name} với {len(extractor.tasks)} dòng dữ liệu.")

    # 4. Xuất file provenance_manifest.json (Mã băm SHA-256 chứng cứ 100%)
    manifest_path = DB_OUTPUT_DIR / "provenance_manifest.json"
    print(f"\n[4/4] Đang tạo Bảng Kê Chứng Cứ {manifest_path.name} (SHA-256)...")
    manifest = {
        "generated_at_utc": "2026-09-07T11:10:00Z",
        "description": "Bảng kê chứng cứ toàn bộ file XML gốc để kiểm chứng tính toàn vẹn (Anti-Tampering)",
        "task_files": {},
        "sub_files": {}
    }
    
    for f in sorted(glob.glob(str(TASK_DIR / "*.xml"))):
        p = Path(f)
        manifest["task_files"][p.name] = {
            "rel_path": str(p.relative_to(BASE_DIR)),
            "size_bytes": p.stat().st_size,
            "sha256": sha256_file(p)
        }
        
    for f in sorted(glob.glob(str(SUB_DIR / "*.xml"))):
        p = Path(f)
        manifest["sub_files"][p.name] = {
            "rel_path": str(p.relative_to(BASE_DIR)),
            "size_bytes": p.stat().st_size,
            "sha256": sha256_file(p)
        }
        
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    print(f"      -> Hoàn tất ghi {manifest_path.name} với {len(manifest['task_files'])} task files và {len(manifest['sub_files'])} sub files.")

    print("\n==================================================================")
    print("HOÀN TẤT GIAI ĐOẠN 2: CƠ SỞ DỮ LIỆU ĐÃ ĐƯỢC XUẤT ĐẦY ĐỦ")
    print(f"Thư mục lưu trữ: {DB_OUTPUT_DIR}")
    print("==================================================================")

if __name__ == "__main__":
    export_all()
