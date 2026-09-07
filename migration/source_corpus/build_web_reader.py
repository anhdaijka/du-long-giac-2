#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kiếm Thế 2 - Phase 5: Web Reader Builder
Tạo giao diện Web Reader đọc offline trực quan (HTML/CSS/JS thuần, không cần server).
"""

import os
import sys
import sqlite3
import json
from pathlib import Path

# Cấu hình UTF-8 cho Windows console
try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

BASE_DIR = Path(r"D:\Games\Server Client\Server KT")
EXPORT_DIR = BASE_DIR / "Kiếm Thế 2" / "Stories_Exported"
WEB_DIR = EXPORT_DIR / "03_Web_Reader"
DB_PATH = EXPORT_DIR / "01_Database" / "story_database.sqlite3"

def build_web_assets():
    print("==================================================================")
    print("GIAI ĐOẠN 5: XÂY DỰNG GIAO DIỆN WEB READER ĐỌC OFFLINE TRỰC QUAN")
    print("==================================================================")
    WEB_DIR.mkdir(parents=True, exist_ok=True)
    
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    
    # 1. Đóng gói story_data.js
    print("\n[1/3] Đang đóng gói dữ liệu sang story_data.js (đọc offline không bị lỗi CORS)...")
    
    arcs_def = [
        ("arc_00", "Hồi 00: Khởi Nguyên Nghĩa Quân & Tân Thủ Thôn", 1, 9, "Bối cảnh Ba Lăng Huyện, Tân Thủ Thôn, Long Ngũ, Bạch Thu Lâm."),
        ("arc_01", "Hồi 01: Nhập Môn Xuất Sơn & 12 Đại Phái", 10, 25, "Gia nhập 12 môn phái, tu luyện võ công căn bản, nhận mật tịch sư môn và ngựa chiến."),
        ("arc_02", "Hồi 02: Giang Hồ Sơ Khởi & Binh Qua Trung Nguyên", 26, 49, "Xuống núi hành hiệp, đối mặt giặc cỏ, tình báo Tống - Kim và mật thư chiến sự."),
        ("arc_03", "Hồi 03: Tứ Diện Sở Ca & Biến Cố Thiên Vương Đảo", 50, 75, "Dương Anh vân du trở về, Dương Thiết Tâm so tài, Triệu Nhữ Nhu khuếch trương thế lực, Hàn Thác Trụ trốn chạy."),
        ("arc_04", "Hồi 04: Du Long Giác Xuất Thế & Tranh Đoạt Bảo Vật", 76, 110, "Bảo vật Du Long Giác tái xuất giang hồ, Thúy Yên, Đường Môn, Ngũ Độc tranh giành đẫm máu."),
        ("arc_05", "Hồi 05: Nam Bắc Đối Đầu & Nghĩa Khí Giang Hồ", 111, 150, "Bạch Thu Lâm hiệu triệu quần hùng, nghĩa quân lập phân đà, đối đầu cao thủ Kim quốc."),
        ("arc_06", "Hồi 06: Thạch Hiên Viên & Cổ Yên Nhiên", 151, 190, "Ân oán Cái Bang, tấm lòng ái quốc của Thạch bang chủ và mối tình oan trái với Cổ Yên Nhiên."),
        ("arc_07", "Hồi 07: Khánh Nguyên Chi Biến & Khói Lửa Phục Ngưu", 191, 225, "Nghĩa quân phân đà đại chiến, thăm dò động thái quân Kim tại sườn nam Phục Ngưu."),
        ("arc_08", "Hồi 08: Man Thiên Quá Hải & Đột Kích Kim Quốc", 228, 270, "Kế sách qua mặt quân Kim, đột nhập phòng tuyến phương bắc thu thập tình báo cơ mật."),
        ("arc_09", "Hồi 09: Đại Lý Sơn Trang & Thiên Quỳnh Cung Kỳ Án", 271, 320, "Tây Nam phong vân, bí mật cung cấm Đại Lý Đoạn Thị và cạm bẫy Thiên Quỳnh Cung."),
        ("arc_10", "Hồi 10: Vọng Long Sơn & Quyết Nghị Bắc Phạt", 321, 370, "Quần hùng hội tụ Vọng Long Sơn, triều đình Nam Tống dấy binh Bắc Phạt thu phục giang sơn."),
        ("arc_11", "Hồi 11: Trận Chiến Linh Bích & Thân Thế Đại Hiệp", 371, 420, "Huyết chiến Linh Bích, tàn phá đại quân Kim, mở ra sự thật về thân thế phụ mẫu nhân vật chính."),
        ("arc_12", "Hồi 12: Thái Tổ Bảo Khố & Những Bí Mật Còn Bỏ Ngỏ", 421, 465, "Truy tìm bí bảo Thái Tổ, kết cục đại hiệp và các manh mối dang dở chưa có lời kết trong game.")
    ]
    
    story_data = {
        "arcs": [],
        "armycamps": [],
        "factions": [],
        "linktask": [],
        "ambient_maps": []
    }
    
    for arc_key, arc_title, start_id, end_id, summary in arcs_def:
        tasks = cur.execute(
            "SELECT * FROM tasks WHERE task_id >= ? AND task_id <= ? AND category NOT LIKE '%quân doanh%' AND category NOT LIKE '%phó bản%' ORDER BY task_id",
            (start_id, end_id)
        ).fetchall()
        
        arc_tasks = []
        for t in tasks:
            subs = cur.execute("SELECT * FROM subtasks WHERE task_id = ? ORDER BY sub_id", (t["task_id"],)).fetchall()
            sub_list = []
            for s in subs:
                dials = cur.execute("SELECT phase, cleaned_text FROM dialogues WHERE sub_id = ? ORDER BY id", (s["sub_id"],)).fetchall()
                sub_list.append({
                    "sub_id": s["sub_id"],
                    "name": s["name"],
                    "dialog_npc_name": s["dialog_npc_name"],
                    "describe_cleaned": s["describe_cleaned"],
                    "file_path": s["file_path"],
                    "dialogues": [{"phase": d["phase"], "text": d["cleaned_text"]} for d in dials]
                })
            arc_tasks.append({
                "task_id": t["task_id"],
                "name": t["name"],
                "describe_cleaned": t["describe_cleaned"],
                "category": t["category"],
                "file_path": t["file_path"],
                "subs": sub_list
            })
            
        story_data["arcs"].append({
            "key": arc_key,
            "title": arc_title,
            "summary": summary,
            "tasks": arc_tasks
        })

    # Quân Doanh
    camps_meta = [
        ("camp_1", "Hậu Sơn Phục Ngưu Sơn (Cấp 90 - 100)", 1, [226, 227], "Thảo phạt sào huyệt sơn tặc, khai thác mỏ đá, vượt Loạn Thạch Than tiêu diệt Quách Tuấn Cương và Đồ Nhất Ngột."),
        ("camp_2", "Bách Man Sơn (Cấp 100 - 110)", 2, [337, 338], "Vượt rừng thiêng nước độc Miêu Cương, phá Đào Hoa Chướng, trảm Linh Xà, khiêu chiến Cổ Vương."),
        ("camp_3", "Hải Lăng Vương Mộ (Cấp 110 - 120)", 3, [363, 364], "Thâm nhập lăng tẩm hoàng gia Đại Kim của bạo chúa Hoàn Nhan Lượng, vượt Kinh Cức Mật Lâm và Hồng Liên Địa Ngục."),
        ("camp_4", "Ngạc Luân Hà Nguyên (Cấp 130+)", 4, [365, 366, 367, 368], "Chiến trường thảo nguyên phương bắc, khảo nghiệm tri thức Mông Cổ, so tài cùng Đà Lôi Khả Hãn và Mộc Hoa Lê.")
    ]
    for c_key, c_title, camp_id, t_ids, c_summary in camps_meta:
        tasks = []
        for tid in t_ids:
            t = cur.execute("SELECT * FROM tasks WHERE task_id = ?", (tid,)).fetchone()
            if t:
                subs = cur.execute("SELECT * FROM subtasks WHERE task_id = ? ORDER BY sub_id", (tid,)).fetchall()
                sub_list = []
                for s in subs:
                    dials = cur.execute("SELECT phase, cleaned_text FROM dialogues WHERE sub_id = ? ORDER BY id", (s["sub_id"],)).fetchall()
                    sub_list.append({
                        "sub_id": s["sub_id"],
                        "name": s["name"],
                        "dialog_npc_name": s["dialog_npc_name"],
                        "describe_cleaned": s["describe_cleaned"],
                        "file_path": s["file_path"],
                        "dialogues": [{"phase": d["phase"], "text": d["cleaned_text"]} for d in dials]
                    })
                tasks.append({
                    "task_id": t["task_id"],
                    "name": t["name"],
                    "describe_cleaned": t["describe_cleaned"],
                    "category": t["category"],
                    "file_path": t["file_path"],
                    "subs": sub_list
                })
        lores = cur.execute("SELECT * FROM armycamp_lore WHERE camp_id = ? ORDER BY id", (camp_id,)).fetchall()
        story_data["armycamps"].append({
            "key": c_key,
            "title": c_title,
            "summary": c_summary,
            "tasks": tasks,
            "lores": [{"section": lr["section"], "type": lr["lore_type"], "text": lr["cleaned_text"], "file": lr["file_path"]} for lr in lores]
        })

    # Bao Vạn Đồng
    lt_rows = cur.execute("SELECT * FROM linktask_tales ORDER BY id").fetchall()
    story_data["linktask"] = [{
        "index": r["entry_index"],
        "cat_name": r["category_name"],
        "text": r["cleaned_text"],
        "file": r["file_path"]
    } for r in lt_rows]

    # Ambient maps
    maps = cur.execute("SELECT DISTINCT map_id, map_name FROM world_ambient_dialogues ORDER BY map_id").fetchall()
    for m in maps:
        dials = cur.execute("SELECT * FROM world_ambient_dialogues WHERE map_id = ? ORDER BY id", (m["map_id"],)).fetchall()
        story_data["ambient_maps"].append({
            "map_id": m["map_id"],
            "map_name": m["map_name"],
            "dialogues": [{
                "id": d["id"],
                "npc_class": d["npc_class"],
                "msg": d["cleaned_msg"],
                "options": d["options"]
            } for d in dials]
        })

    conn.close()

    js_file = WEB_DIR / "story_data.js"
    with open(js_file, "w", encoding="utf-8") as f:
        f.write("// Dữ liệu cốt truyện Kiếm Thế 2 được đóng gói tự động - Chạy offline 100%\n")
        f.write("window.STORY_DATA = ")
        json.dump(story_data, f, ensure_ascii=False)
        f.write(";\n")
    print(f"      -> Hoàn tất ghi {js_file.name} ({js_file.stat().st_size / (1024*1024):.2f} MB)")

    # 2. Tạo style.css
    print("\n[2/3] Đang tạo style.css giao diện cổ trang kiếm hiệp...")
    css_file = WEB_DIR / "style.css"
    with open(css_file, "w", encoding="utf-8") as f:
        f.write("""/* Kiếm Thế 2 - Web Reader Style */
:root {
  --bg-main: #0c0f14;
  --bg-sidebar: #121720;
  --bg-card: #181f2a;
  --bg-card-hover: #1f2837;
  --border-color: #2b3547;
  --text-main: #e2e8f0;
  --text-muted: #94a3b8;
  --gold-primary: #d4af37;
  --gold-glow: rgba(212, 175, 55, 0.25);
  --cyan-accent: #38bdf8;
  --red-accent: #f43f5e;
  --font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  background-color: var(--bg-main);
  color: var(--text-main);
  font-family: var(--font-family);
  display: flex;
  height: 100vh;
  overflow: hidden;
}

/* Sidebar */
#sidebar {
  width: 320px;
  background-color: var(--bg-sidebar);
  border-right: 1px solid var(--border-color);
  display: flex;
  flex-direction: column;
  flex-shrink: 0;
}

.brand {
  padding: 18px 20px;
  border-bottom: 1px solid var(--border-color);
  display: flex;
  align-items: center;
  gap: 12px;
}
.brand-icon { font-size: 26px; }
.brand-title { font-size: 17px; font-weight: 700; color: var(--gold-primary); }
.brand-sub { font-size: 11px; color: var(--text-muted); }

.search-box {
  padding: 12px 16px;
  border-bottom: 1px solid var(--border-color);
}
.search-box input {
  width: 100%;
  padding: 8px 14px;
  background-color: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 6px;
  color: var(--text-main);
  font-size: 13px;
  outline: none;
  transition: all 0.2s;
}
.search-box input:focus {
  border-color: var(--gold-primary);
  box-shadow: 0 0 8px var(--gold-glow);
}

.nav-tree {
  flex: 1;
  overflow-y: auto;
  padding: 10px 8px;
}
.nav-group-title {
  font-size: 11px;
  text-transform: uppercase;
  color: var(--gold-primary);
  padding: 10px 12px 6px;
  letter-spacing: 0.5px;
  font-weight: 700;
}
.nav-item {
  display: flex;
  align-items: center;
  padding: 8px 12px;
  border-radius: 6px;
  color: var(--text-muted);
  font-size: 13px;
  cursor: pointer;
  transition: all 0.15s;
  user-select: none;
  margin-bottom: 2px;
}
.nav-item:hover {
  background-color: var(--bg-card);
  color: var(--text-main);
}
.nav-item.active {
  background: linear-gradient(90deg, rgba(212, 175, 55, 0.18), transparent);
  color: var(--gold-primary);
  font-weight: 600;
  border-left: 3px solid var(--gold-primary);
}

/* Main Container */
#main-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  overflow: hidden;
  background-color: var(--bg-main);
}

.top-bar {
  height: 56px;
  border-bottom: 1px solid var(--border-color);
  background-color: var(--bg-sidebar);
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 24px;
  flex-shrink: 0;
}
.current-title {
  font-size: 16px;
  font-weight: 600;
  color: var(--gold-primary);
}
.top-controls {
  display: flex;
  align-items: center;
  gap: 12px;
}
.control-btn {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  color: var(--text-muted);
  padding: 6px 12px;
  border-radius: 6px;
  font-size: 12px;
  cursor: pointer;
  transition: all 0.2s;
}
.control-btn:hover {
  border-color: var(--gold-primary);
  color: var(--gold-primary);
}

.reading-area {
  flex: 1;
  overflow-y: auto;
  padding: 32px 40px;
}
.reader-container {
  max-width: 960px;
  margin: 0 auto;
}

/* Arc / Chapter Header */
.chapter-header {
  margin-bottom: 32px;
  padding-bottom: 20px;
  border-bottom: 1px solid var(--border-color);
}
.chapter-title {
  font-size: 26px;
  color: var(--gold-primary);
  margin-bottom: 10px;
}
.chapter-summary {
  font-size: 14px;
  color: var(--text-muted);
  font-style: italic;
  line-height: 1.6;
  background: rgba(212, 175, 55, 0.05);
  padding: 12px 16px;
  border-left: 3px solid var(--gold-primary);
  border-radius: 0 6px 6px 0;
}

/* Task Card */
.task-card {
  background-color: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 8px;
  margin-bottom: 28px;
  overflow: hidden;
  transition: all 0.2s;
}
.task-card:hover {
  border-color: rgba(212, 175, 55, 0.4);
}
.task-header {
  padding: 16px 20px;
  background-color: rgba(255, 255, 255, 0.02);
  border-bottom: 1px solid var(--border-color);
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.task-title {
  font-size: 17px;
  font-weight: 700;
  color: var(--cyan-accent);
}
.task-badges {
  display: flex;
  gap: 8px;
}
.badge {
  font-size: 11px;
  padding: 3px 8px;
  border-radius: 4px;
  background-color: #243042;
  color: #cbd5e1;
}
.badge-gold {
  background-color: rgba(212, 175, 55, 0.15);
  color: var(--gold-primary);
  border: 1px solid rgba(212, 175, 55, 0.3);
}

.task-body {
  padding: 20px;
}
.task-desc {
  font-size: 14px;
  line-height: 1.7;
  color: #cbd5e1;
  margin-bottom: 20px;
  padding: 12px 16px;
  background: rgba(0, 0, 0, 0.2);
  border-left: 3px solid var(--cyan-accent);
  border-radius: 0 6px 6px 0;
}

/* Subtask */
.subtask-box {
  margin-top: 18px;
  padding: 16px;
  background-color: rgba(0, 0, 0, 0.25);
  border: 1px solid var(--border-color);
  border-radius: 6px;
}
.subtask-title {
  font-size: 15px;
  font-weight: 600;
  color: var(--gold-primary);
  margin-bottom: 6px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.subtask-giver {
  font-size: 12px;
  color: var(--text-muted);
  font-weight: 400;
}
.subtask-steps {
  font-size: 13.5px;
  line-height: 1.6;
  color: #94a3b8;
  margin: 10px 0;
  white-space: pre-line;
}

/* Dialogue Bubble */
.dialogue-section {
  margin-top: 12px;
  padding-top: 12px;
  border-top: 1px dashed var(--border-color);
}
.dialogue-title {
  font-size: 12px;
  text-transform: uppercase;
  color: var(--gold-primary);
  margin-bottom: 8px;
  font-weight: 600;
}
.dialogue-bubble {
  background: #111620;
  border-left: 3px solid var(--gold-primary);
  padding: 10px 14px;
  margin-bottom: 8px;
  border-radius: 0 6px 6px 0;
  font-size: 13.5px;
  line-height: 1.6;
  color: #e2e8f0;
  white-space: pre-line;
}

.provenance-tag {
  font-size: 11px;
  color: #64748b;
  margin-top: 8px;
  font-family: monospace;
}
""")
    print(f"      -> Đã xuất: {css_file.name}")

    # 3. Tạo index.html & app.js
    print("\n[3/3] Đang tạo index.html và app.js...")
    html_file = WEB_DIR / "index.html"
    with open(html_file, "w", encoding="utf-8") as f:
        f.write("""<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Kiếm Thế 2 - Toàn Tập Cốt Truyện Võ Lâm (Offline Web Reader)</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <!-- Sidebar -->
  <aside id="sidebar">
    <div class="brand">
      <div class="brand-icon">⚔️</div>
      <div>
        <div class="brand-title">Kiếm Thế 2</div>
        <div class="brand-sub">Toàn Tập Cốt Truyện & Lời Thoại</div>
      </div>
    </div>
    
    <div class="search-box">
      <input type="text" id="searchInput" placeholder="🔍 Tìm nhân vật, bảo vật, nhiệm vụ...">
    </div>
    
    <nav class="nav-tree" id="navTree">
      <!-- Generated by app.js -->
    </nav>
  </aside>

  <!-- Main Reader -->
  <main id="main-content">
    <header class="top-bar">
      <div class="current-title" id="currentViewTitle">Hồi 00: Khởi Nguyên Nghĩa Quân & Tân Thủ Thôn</div>
      <div class="top-controls">
        <button class="control-btn" id="btnZoomIn">A+</button>
        <button class="control-btn" id="btnZoomOut">A-</button>
        <button class="control-btn" id="btnZenMode">📖 Zen Mode</button>
      </div>
    </header>

    <div class="reading-area" id="readingArea">
      <div class="reader-container" id="contentContainer">
        <!-- Rendered by app.js -->
      </div>
    </div>
  </main>

  <script src="story_data.js"></script>
  <script src="app.js"></script>
</body>
</html>
""")

    app_js_file = WEB_DIR / "app.js"
    with open(app_js_file, "w", encoding="utf-8") as f:
        f.write("""// Kiếm Thế 2 - Web Reader App Logic
let currentFontSize = 14;
let activeItemKey = 'arc_00';

document.addEventListener('DOMContentLoaded', () => {
  initNav();
  renderCurrentView();
  bindEvents();
});

function initNav() {
  const navTree = document.getElementById('navTree');
  if (!window.STORY_DATA) return;
  
  let html = '';
  
  // 1. Chính tuyến
  html += '<div class="nav-group-title">📜 13 Hồi Chính Tuyến</div>';
  window.STORY_DATA.arcs.forEach(arc => {
    html += `<div class="nav-item ${arc.key === activeItemKey ? 'active' : ''}" data-type="arc" data-key="${arc.key}">${arc.title}</div>`;
  });

  // 2. Quân Doanh
  html += '<div class="nav-group-title">⚔️ 4 Đại Quân Doanh</div>';
  window.STORY_DATA.armycamps.forEach(camp => {
    html += `<div class="nav-item" data-type="camp" data-key="${camp.key}">${camp.title}</div>`;
  });

  // 3. Phụ Tuyến
  html += '<div class="nav-group-title">🍃 Phụ Tuyến & Giang Hồ</div>';
  html += `<div class="nav-item" data-type="linktask" data-key="linktask">Truyện Ngắn Bao Vạn Đồng</div>`;
  html += `<div class="nav-item" data-type="ambient" data-key="ambient">Phong Thổ 30 Thành Thị (720 NPC)</div>`;

  navTree.innerHTML = html;

  // Click handler
  navTree.querySelectorAll('.nav-item').forEach(item => {
    item.addEventListener('click', () => {
      navTree.querySelectorAll('.nav-item').forEach(i => i.classList.remove('active'));
      item.classList.add('active');
      activeItemKey = item.getAttribute('data-key');
      const itemType = item.getAttribute('data-type');
      renderView(itemType, activeItemKey);
    });
  });
}

function renderCurrentView() {
  renderView('arc', activeItemKey);
}

function renderView(type, key) {
  const container = document.getElementById('contentContainer');
  const titleElem = document.getElementById('currentViewTitle');
  document.getElementById('readingArea').scrollTop = 0;

  if (type === 'arc') {
    const arc = window.STORY_DATA.arcs.find(a => a.key === key);
    if (!arc) return;
    titleElem.textContent = arc.title;
    
    let html = `
      <div class="chapter-header">
        <h1 class="chapter-title">${arc.title}</h1>
        <div class="chapter-summary">${arc.summary}</div>
      </div>
    `;

    arc.tasks.forEach(t => {
      html += `
        <div class="task-card">
          <div class="task-header">
            <div class="task-title">[Nhiệm Vụ #${String(t.task_id).padStart(4, '0')}] ${t.name}</div>
            <div class="task-badges">
              <span class="badge badge-gold">${t.category}</span>
              <span class="badge">${t.subs.length} phân đoạn</span>
            </div>
          </div>
          <div class="task-body">
            <div class="task-desc">${t.describe_cleaned}</div>
            ${t.subs.map(s => `
              <div class="subtask-box">
                <div class="subtask-title">
                  <span>Phân đoạn #${String(s.sub_id).padStart(4, '0')}: ${s.name}</span>
                  <span class="subtask-giver">Người giao: ${s.dialog_npc_name || 'Hệ thống'}</span>
                </div>
                <div class="subtask-steps">${s.describe_cleaned}</div>
                ${s.dialogues && s.dialogues.length > 0 ? `
                  <div class="dialogue-section">
                    <div class="dialogue-title">Kịch bản lời thoại:</div>
                    ${s.dialogues.map(d => `<div class="dialogue-bubble"><strong>[${d.phase.toUpperCase()}]:</strong><br>${d.text}</div>`).join('')}
                  </div>
                ` : ''}
                <div class="provenance-tag">Nguồn: ${s.file_path}</div>
              </div>
            `).join('')}
            <div class="provenance-tag" style="margin-top:14px;">Task file: ${t.file_path}</div>
          </div>
        </div>
      `;
    });
    container.innerHTML = html;
  } else if (type === 'camp') {
    const camp = window.STORY_DATA.armycamps.find(c => c.key === key);
    if (!camp) return;
    titleElem.textContent = camp.title;

    let html = `
      <div class="chapter-header">
        <h1 class="chapter-title">${camp.title}</h1>
        <div class="chapter-summary">${camp.summary}</div>
      </div>
      <h2 style="color:var(--gold-primary); margin: 24px 0 16px;">1. Các Nhiệm Vụ Quân Doanh (XML Tasks)</h2>
    `;
    
    camp.tasks.forEach(t => {
      html += `
        <div class="task-card">
          <div class="task-header">
            <div class="task-title">[Nhiệm Vụ #${String(t.task_id).padStart(4, '0')}] ${t.name}</div>
            <span class="badge badge-gold">${t.category}</span>
          </div>
          <div class="task-body">
            <div class="task-desc">${t.describe_cleaned}</div>
            ${t.subs.map(s => `
              <div class="subtask-box">
                <div class="subtask-title">${s.name}</div>
                <div class="subtask-steps">${s.describe_cleaned}</div>
              </div>
            `).join('')}
          </div>
        </div>
      `;
    });

    html += `<h2 style="color:var(--gold-primary); margin: 32px 0 16px;">2. Kịch Bản Lời Thoại Boss & Cạm Bẫy (LUA)</h2>`;
    camp.lores.forEach(l => {
      html += `
        <div class="task-card">
          <div class="task-header">
            <div class="task-title">${l.section}</div>
            <span class="badge">${l.type}</span>
          </div>
          <div class="task-body">
            <div class="dialogue-bubble">${l.text}</div>
            <div class="provenance-tag">Nguồn: ${l.file}</div>
          </div>
        </div>
      `;
    });
    container.innerHTML = html;
  } else if (type === 'linktask') {
    titleElem.textContent = 'Truyện Ngắn Nghĩa Quân Bao Vạn Đồng';
    let html = `
      <div class="chapter-header">
        <h1 class="chapter-title">Truyện Ngắn Nghĩa Quân Bao Vạn Đồng</h1>
        <div class="chapter-summary">50 mẩu truyện ngắn ghi nhận tình hình chiến sự, nghĩa cử giang hồ và đời sống bá tánh thời Tống - Kim.</div>
      </div>
    `;
    window.STORY_DATA.linktask.forEach(lt => {
      html += `
        <div class="task-card">
          <div class="task-header">
            <div class="task-title">Truyện #${lt.index}: ${lt.cat_name}</div>
            <span class="badge badge-gold">Nghĩa Quân</span>
          </div>
          <div class="task-body">
            <div class="dialogue-bubble">${lt.text}</div>
            <div class="provenance-tag">Nguồn: ${lt.file}</div>
          </div>
        </div>
      `;
    });
    container.innerHTML = html;
  } else if (type === 'ambient') {
    titleElem.textContent = 'Phong Thổ Võ Lâm: 720 Đối Thoại Đời Thường Khắp 30 Thành Thị';
    let html = `
      <div class="chapter-header">
        <h1 class="chapter-title">Phong Thổ Võ Lâm: 720 Đối Thoại Đời Thường</h1>
        <div class="chapter-summary">Đàm đạo của các chủ quán, thương gia, tiếp dẫn môn phái tại 30 thành thị lớn thời Nam Tống.</div>
      </div>
    `;
    window.STORY_DATA.ambient_maps.forEach(m => {
      html += `
        <h2 style="color:var(--gold-primary); margin: 28px 0 14px;">Bản Đồ: ${m.map_name} (Map ID: ${m.map_id})</h2>
        <div style="display:grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-bottom: 24px;">
          ${m.dialogues.map(d => `
            <div class="subtask-box">
              <div class="subtask-title">Lớp NPC: ${d.npc_class}</div>
              <div style="font-size:13.5px; color:#e2e8f0; line-height:1.5; margin-bottom:8px;">${d.msg}</div>
              ${d.options ? `<div style="font-size:12px; color:#94a3b8;"><em>Tương tác: ${d.options}</em></div>` : ''}
            </div>
          `).join('')}
        </div>
      `;
    });
    container.innerHTML = html;
  }
}

function bindEvents() {
  document.getElementById('btnZoomIn').addEventListener('click', () => {
    if (currentFontSize < 22) {
      currentFontSize += 1.5;
      document.getElementById('contentContainer').style.fontSize = currentFontSize + 'px';
    }
  });

  document.getElementById('btnZoomOut').addEventListener('click', () => {
    if (currentFontSize > 12) {
      currentFontSize -= 1.5;
      document.getElementById('contentContainer').style.fontSize = currentFontSize + 'px';
    }
  });

  document.getElementById('btnZenMode').addEventListener('click', () => {
    const sidebar = document.getElementById('sidebar');
    const isHidden = sidebar.style.display === 'none';
    sidebar.style.display = isHidden ? 'flex' : 'none';
  });

  // Tìm kiếm tức thì
  const searchInput = document.getElementById('searchInput');
  searchInput.addEventListener('input', (e) => {
    const q = e.target.value.trim().toLowerCase();
    if (!q) {
      renderCurrentView();
      return;
    }

    const container = document.getElementById('contentContainer');
    document.getElementById('currentViewTitle').textContent = `Kết quả tìm kiếm: "${q}"`;

    let hits = [];
    window.STORY_DATA.arcs.forEach(arc => {
      arc.tasks.forEach(t => {
        const matchTitle = t.name.toLowerCase().includes(q);
        const matchDesc = t.describe_cleaned.toLowerCase().includes(q);
        const matchSub = t.subs.some(s => s.name.toLowerCase().includes(q) || s.describe_cleaned.toLowerCase().includes(q) || (s.dialog_npc_name && s.dialog_npc_name.toLowerCase().includes(q)));
        if (matchTitle || matchDesc || matchSub) {
          hits.push({ arcTitle: arc.title, task: t });
        }
      });
    });

    if (hits.length === 0) {
      container.innerHTML = `<div style="padding: 40px; text-align: center; color: #94a3b8;">Không tìm thấy kết quả nào khớp với "${q}".</div>`;
      return;
    }

    let html = `<div style="margin-bottom: 20px; color: var(--gold-primary); font-size: 15px;">Tìm thấy <strong>${hits.length}</strong> nhiệm vụ phù hợp:</div>`;
    hits.forEach(({ arcTitle, task: t }) => {
      html += `
        <div class="task-card">
          <div class="task-header">
            <div class="task-title">[Nhiệm Vụ #${String(t.task_id).padStart(4, '0')}] ${t.name}</div>
            <span class="badge badge-gold">${arcTitle}</span>
          </div>
          <div class="task-body">
            <div class="task-desc">${t.describe_cleaned}</div>
            ${t.subs.map(s => `
              <div class="subtask-box">
                <div class="subtask-title">${s.name} (Người giao: ${s.dialog_npc_name || 'Hệ thống'})</div>
                <div class="subtask-steps">${s.describe_cleaned}</div>
              </div>
            `).join('')}
          </div>
        </div>
      `;
    });
    container.innerHTML = html;
  });
}
""")
    print(f"      -> Đã xuất: {html_file.name} và {app_js_file.name}")

    # 4. Tạo file shortcut .bat mở Web Reader tiện lợi
    bat_file = BASE_DIR / "Kiếm Thế 2" / "DOC_COT_TRUYEN_KIEM_THE_2.bat"
    with open(bat_file, "w", encoding="utf-8") as f:
        f.write(f'@echo off\n')
        f.write(f'title Kiem The 2 - Web Reader Cot Truyen\n')
        f.write(f'start "" "{html_file}"\n')
    print(f"\n[Shortcut] Đã tạo file kích hoạt nhanh 1-click: {bat_file.name}")

    print("\n==================================================================")
    print("HOÀN TẤT GIAI ĐOẠN 5: GIAO DIỆN WEB READER ĐÃ SẴN SÀNG SỬ DỤNG")
    print(f"Mở file: {html_file}")
    print("==================================================================")

if __name__ == "__main__":
    build_web_assets()
