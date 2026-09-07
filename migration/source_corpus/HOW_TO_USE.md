# CẨM NANG HƯỚNG DẪN DÀNH CHO AGENT / DEVELOPER
## Tra Cứu, Sử Dụng & Khai Thác Cơ Sở Dữ Liệu Cốt Truyện Kiếm Thế 2 (Strict Provenance)

> **Dành cho bất kỳ Agent / AI Assistant / Developer nào tiếp nhận dự án**:  
> Thư mục này chứa toàn bộ cơ sở dữ liệu cốt truyện, nhiệm vụ, lời thoại và kịch bản của game **Kiếm Thế 2** được trích xuất trực tiếp từ mã nguồn gốc máy chủ và dữ liệu gói của trò chơi.  
> **TÔN CHỈ TỐI CAO**: **Dữ liệu là sự thật duy nhất (Ground Truth First). Tuyệt đối KHÔNG tự suy diễn, KHÔNG tự bịa lời thoại, KHÔNG tự kết luận mối quan hệ khi chưa có liên kết mã nguồn xác thực.**

---

## 1. Bản Đồ Thư Mục & Tổng Quan Tài Nguyên

```text
D:\Games\Server Client\Server KT\Kiếm Thế 2\Stories_Exported\
├── HOW_TO_USE.md                         <-- TÀI LIỆU BẠN ĐANG ĐỌC (Hướng dẫn cho Agent)
├── PHASE_1_AUDIT_REPORT.json             <-- Báo cáo đối soát liên kết Task - Sub và các điểm đứt gãy
├── PHASE_1_SAMPLE_VERIFICATION.md        <-- Mẫu đối chiếu văn bản trích xuất với XML gốc
├── build_story_extractor.py              <-- Script trích xuất và giải mã thực thể gốc
├── export_database.py                    <-- Script xuất CSDL SQLite, JSON, CSV và Manifest
│
├── 01_Database/                          <-- KHO CƠ SỞ DỮ LIỆU CẤU TRÚC (ƯU TIÊN DÙNG CHO AGENT)
│   ├── story_database.sqlite3            <-- CSDL SQLite3 quan hệ có index (Nhanh nhất, tiện truy vấn SQL)
│   ├── story_database.json               <-- Cây dữ liệu JSON hoàn chỉnh (Dành cho load nguyên cây)
│   ├── tasks_catalog.csv                 <-- Bảng danh mục 465 nhiệm vụ dạng Excel / CSV
│   └── provenance_manifest.json          <-- Bảng kê khai mã băm SHA-256 từng file nguồn gốc
│
├── 02_Narrative_Book/                    <-- (Đang phát triển) Bộ sách kịch bản kịch tính Markdown
└── 03_Web_Reader/                        <-- (Đang phát triển) Giao diện đọc offline trực quan HTML/CSS
```

---

## 2. Cấu Trúc Bảng Dữ Liệu SQLite (`story_database.sqlite3`)

Đường dẫn: `01_Database/story_database.sqlite3`  
Đây là file **khuyên dùng hàng đầu** cho Agent khi cần trả lời câu hỏi, tra cứu nhiệm vụ, kiểm tra điều kiện hoặc trích xuất lời thoại của nhân vật.

### 2.1. Bảng `tasks` (465 nhiệm vụ cha)
Chứa thông tin tổng quan của các nhiệm vụ chính/quân doanh/phó bản:
| Tên cột | Kiểu dữ liệu | Ý nghĩa | Ví dụ |
| :--- | :--- | :--- | :--- |
| `task_id` | `INTEGER PRIMARY KEY` | ID nhiệm vụ dạng số thập phân | `1`, `226`, `425` |
| `task_id_hex` | `TEXT` | ID nhiệm vụ dạng hex 16 ký tự | `'0000000000000001'` |
| `name` | `TEXT` | Tên nhiệm vụ tiếng Việt có dấu | `'Tứ Diện Sở Ca'`, `'Hậu Sơn Phục Ngưu Sơn'` |
| `describe_raw` | `TEXT` | Miêu tả bối cảnh gốc từ XML | *Chuỗi gốc chưa làm sạch thẻ* |
| `describe_cleaned`| `TEXT` | Miêu tả bối cảnh đã giải mã NPC/Map | *Chuỗi sạch, dễ đọc* |
| `category` | `TEXT` | Phân loại từ `task_def.txt` | `'Nhiệm vụ chính tuyến'`, `'Nhiệm vụ quân doanh'` |
| `category_desc` | `TEXT` | Chi tiết phân loại | `'Loại editor nhiệm vụ thông dụng'`, `'Cốt truyện'` |
| `order_type` | `TEXT` | Thứ tự thực hiện | `'linear'` (tuần tự), `'random'` (ngẫu nhiên) |
| `repeat` | `INTEGER` | Cho phép làm lại không | `0` (Không), `1` (Có - Hằng ngày) |
| `task_type_code`| `TEXT` | Mã loại nhiệm vụ hệ thống | `'1'` |
| `file_path` | `TEXT` | Đường dẫn tương đối đến file XML gốc | `'Stories\\task_publish\\task\\0000000000000001.xml'` |

### 2.2. Bảng `subtasks` (657 nhiệm vụ con)
Mỗi nhiệm vụ cha quản lý một danh sách các subtasks:
| Tên cột | Kiểu dữ liệu | Ý nghĩa |
| :--- | :--- | :--- |
| `sub_id` | `INTEGER PRIMARY KEY` | ID nhiệm vụ con |
| `sub_id_hex` | `TEXT` | ID nhiệm vụ con dạng hex |
| `task_id` | `INTEGER` | Khóa ngoại trỏ về `tasks(task_id)` |
| `name` | `TEXT` | Tên nhiệm vụ con (ví dụ: `'Anh Cô Trở Về'`, `'Thông Địch Phản Bang'`) |
| `describe_cleaned`| `TEXT` | Miêu tả nhiệm vụ con kèm hướng dẫn từng bước |
| `dialog_npc_id` | `INTEGER` | ID của NPC giao nhiệm vụ mở đầu |
| `dialog_npc_name`| `TEXT` | Tên tiếng Việt của NPC giao (ví dụ: `'Quý Thúc Ban'`, `'Dương Anh'`) |
| `file_path` | `TEXT` | Đường dẫn file XML gốc (`Stories\task_publish\sub\...`) |

### 2.3. Bảng `dialogues` (839 phân cảnh hội thoại)
Toàn bộ lời thoại kịch bản giữa người chơi và các NPC:
| Tên cột | Kiểu dữ liệu | Ý nghĩa |
| :--- | :--- | :--- |
| `id` | `INTEGER PRIMARY KEY` | Khóa tự tăng |
| `sub_id` | `INTEGER` | Khóa ngoại trỏ về `subtasks(sub_id)` |
| `phase` | `TEXT` | Giai đoạn thoại: `'pop'`, `'start'`, `'procedure'`, `'prize'`, `'end'` |
| `raw_text` | `TEXT` | Lời thoại thô (còn thẻ `<npc=...>`, `<end>`) |
| `cleaned_text` | `TEXT` | Lời thoại sạch: đã thay NPC thành `[Tên NPC]`, phân dòng chuẩn |

*Ý nghĩa các giai đoạn (`phase`):*
- `pop`: Lời thoại bong bóng nói chuyện nổi trên đầu NPC khi người chơi đến gần.
- `start`: Lời thoại mở đầu khi tiếp nhận nhiệm vụ.
- `procedure`: Lời thoại nhắc nhở hoặc diễn biến giữa chừng.
- `prize`: Lời thoại khi báo cáo hoàn thành và nhận phần thưởng.
- `end`: Lời thoại kết thúc sau khi trả nhiệm vụ xong.

### 2.4. Bảng `steps` (2,947 bước hành động)
Mục tiêu hành động của người chơi trong từng nhiệm vụ con:
| Tên cột | Kiểu dữ liệu | Ý nghĩa |
| :--- | :--- | :--- |
| `id` | `INTEGER PRIMARY KEY` | Khóa tự tăng |
| `sub_id` | `INTEGER` | Khóa ngoại trỏ về `subtasks(sub_id)` |
| `step_index` | `INTEGER` | Số thứ tự bước (1, 2, 3...) |
| `target_function`| `TEXT` | Hàm hành động game (ví dụ: `Send2Aim`, `KillNpc`, `OpenItem`) |
| `target_params` | `TEXT` | Tham số mục tiêu (toạ độ, ID NPC mục tiêu, ID vật phẩm) |

---

## 3. Agent Cookbook: Các Mẫu Truy Vấn SQL Thông Dụng

Khi bạn (Agent) nhận được câu hỏi từ người dùng, hãy dùng công cụ chạy command `python -c "import sqlite3..."` để truy vấn CSDL:

### Mẫu 1: Tìm kiếm mọi nhiệm vụ liên quan đến một nhân vật cụ thể
*Ví dụ*: Tìm xem nhân vật **Dương Thiết Tâm** xuất hiện trong những nhiệm vụ nào:
```sql
SELECT t.task_id, t.name AS task_name, s.sub_id, s.name AS sub_name, s.dialog_npc_name
FROM tasks t
JOIN subtasks s ON t.task_id = s.task_id
WHERE s.dialog_npc_name LIKE '%Dương Thiết Tâm%' 
   OR t.describe_cleaned LIKE '%Dương Thiết Tâm%'
ORDER BY t.task_id;
```

### Mẫu 2: Lấy toàn bộ kịch bản lời thoại của một Nhiệm vụ cụ thể
*Ví dụ*: Lấy kịch bản thoại của **Task #1 (Tứ Diện Sở Ca)**:
```sql
SELECT s.sub_id, s.name AS sub_name, d.phase, d.cleaned_text
FROM subtasks s
JOIN dialogues d ON s.sub_id = d.sub_id
WHERE s.task_id = 1
ORDER BY s.sub_id, 
  CASE d.phase 
    WHEN 'pop' THEN 1 
    WHEN 'start' THEN 2 
    WHEN 'procedure' THEN 3 
    WHEN 'prize' THEN 4 
    WHEN 'end' THEN 5 
  END;
```

### Mẫu 3: Lọc toàn bộ nhiệm vụ Quân Doanh (Army Camp)
```sql
SELECT task_id, name, describe_cleaned, file_path 
FROM tasks 
WHERE category LIKE '%quân doanh%'
ORDER BY task_id;
```

### Mẫu 4: Tìm kiếm theo từ khoá bảo vật / địa danh / âm mưu
*Ví dụ*: Tìm kiếm nơi xuất hiện của bảo vật **"Du Long Giác"**:
```sql
SELECT t.task_id, t.name AS task_name, s.name AS sub_name, d.cleaned_text
FROM subtasks s
JOIN tasks t ON s.task_id = t.task_id
JOIN dialogues d ON s.sub_id = d.sub_id
WHERE d.cleaned_text LIKE '%Du Long Giác%' 
   OR s.describe_cleaned LIKE '%Du Long Giác%'
   OR t.describe_cleaned LIKE '%Du Long Giác%';
```

---

## 4. Mẫu Python Script Cho Agent Tự Chạy Trong Shell

Nếu Agent cần viết script một lần để phân tích phức tạp, đây là khuôn mẫu chuẩn:

```python
import sqlite3
import sys

# Cấu hình UTF-8 cho console Windows
sys.stdout.reconfigure(encoding='utf-8')

db_path = r"D:\Games\Server Client\Server KT\Kiếm Thế 2\Stories_Exported\01_Database\story_database.sqlite3"
conn = sqlite3.connect(db_path)
cur = conn.cursor()

# Ví dụ: Lấy 5 nhiệm vụ chính tuyến đầu tiên
cur.execute("""
    SELECT task_id, name, describe_cleaned 
    FROM tasks 
    WHERE category = 'Nhiệm vụ chính tuyến' 
    ORDER BY task_id LIMIT 5
""")

for task_id, name, desc in cur.fetchall():
    print(f"=== [Task #{task_id:04d}] {name} ===")
    print(f"Bối cảnh: {desc[:150]}...\n")

conn.close()
```

---

## 5. Quy Tắc Ứng Xử Dữ Liệu Bắt Buộc Đối Với Agent

> [!CAUTION]
> **5 NGUYÊN TẮC CẤM KỴ - KHÔNG ĐƯỢC VI PHẠM:**
>
> 1. **KHÔNG tự sáng tác thêm chi tiết**: Nếu nhiệm vụ trong CSDL chỉ ghi đến việc Hàn Thác Trụ rời thuyền, KHÔNG ĐƯỢC tự suy đoán Hàn Thác Trụ sau đó đi đâu nếu không có task tiếp theo xác nhận.
> 2. **BẮT BUỘC ghi rõ nguồn gốc (Provenance)**: Khi trả lời người dùng về một tình tiết, luôn kèm theo mã Task/Sub ID hoặc tên file XML (Ví dụ: *"Theo kịch bản tại Subtask #0001 (Nguồn: sub/0000000000000001.xml)..."*).
> 3. **Phân biệt rạch ròi giữa Lời thoại và Miêu tả**:
>    - `describe_cleaned`: Là lời dẫn chuyện của hệ thống (Narrator).
>    - `dialogues`: Là lời thoại trực tiếp của nhân vật (In-character dialogue).
> 4. **Tôn trọng khoảng trống (Acknowledge Gaps)**: Khi chuỗi nhiệm vụ kết thúc đột ngột hoặc thiếu file sub liên kết (ví dụ trường hợp báo cáo trong `PHASE_1_AUDIT_REPORT.json`), Agent phải thông báo rõ cho người dùng: *"Tại điểm này mã nguồn trò chơi không có nhiệm vụ nối tiếp (No Explicit Next)"*.
> 5. **Kiểm chứng toàn vẹn**: File `01_Database/provenance_manifest.json` chứa mã SHA-256 của toàn bộ 466 task files và 658 sub files. Nếu nghi ngờ dữ liệu bị sửa đổi, hãy băm lại file XML nguồn để đối soát.

---

## 6. Trạng Thái & Roadmap Dự Án

- [x] **Giai đoạn 1**: Xây dựng Engine bóc tách, chuẩn hóa thực thể và Text Sanitizer.
- [x] **Giai đoạn 2**: Xuất CSDL hoàn chỉnh (`story_database.sqlite3`, `story_database.json`, `tasks_catalog.csv`, `provenance_manifest.json`).
- [ ] **Giai đoạn 3**: Trích xuất kịch bản LUA Quân Doanh (`armycamp`), Tân thủ môn phái (`primer`), Bao Vạn Đồng (`linktask`) và đối thoại NPC (`dialognpc.txt`).
- [ ] **Giai đoạn 4**: Biên soạn bộ sách kịch bản Markdown (`02_Narrative_Book/`) theo 14 Arcs Chính Tuyến + 4 Đại Chiến Trường + 12 Phái.
- [ ] **Giai đoạn 5**: Xây dựng giao diện Web Reader đọc offline (`03_Web_Reader/`) và Báo cáo thẩm định toàn diện.
