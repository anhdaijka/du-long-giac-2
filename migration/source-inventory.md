# BẢN KIỂM KÊ NGUỒN DỮ LIỆU (SOURCE INVENTORY)
## Dự án: ĐẠI TIỂU THUYẾT VÕ LÂM KIẾM THẾ (DU LONG GIÁC)
**Đường dẫn kho lưu trữ:** `migration/source_corpus/`  
**Ngày kiểm kê:** 07/09/2026

---

## 1. TỔNG QUAN TÀI NGUYÊN NGUỒN (CORPUS OVERVIEW)

Kho dữ liệu `source_corpus` được bóc tách nguyên bản từ engine game Kiếm Thế 2 (server & client) và bảo lưu toàn bộ dấu vết xuất xứ:

| Phân hệ dữ liệu | Đường dẫn chi tiết | Nội dung & Số lượng | Tình trạng kiểm định |
| :--- | :--- | :--- | :--- |
| **Cơ sở dữ liệu SQLite** | `01_Database/story_database.sqlite3` | 465 Tasks, 657 Subtasks, 720 thoại ambient, 5,728 NPCs, 1,057 Maps | Indexing hoàn chỉnh, tra cứu SQL O(1) |
| **Dữ liệu phân cấp JSON** | `01_Database/story_database.json` | Toàn bộ cây phả hệ cốt truyện nhiệm vụ (9.19 MB) | JSON Schema hợp lệ |
| **Danh mục bảng tính CSV** | `01_Database/tasks_catalog.csv` | Bảng tra cứu phẳng 465 dòng | Sẵn sàng cho bảng tính |
| **Chứng chỉ đối soát Hash** | `01_Database/provenance_manifest.json` | Bảng mã băm SHA-256 của từng file XML nguồn | Chống giả mạo 100% |
| **Kịch bản Markdown** | `02_Narrative_Book/` | 22 chương kịch bản trích xuất nguyên bản (Chính tuyến, Quân doanh, 12 Môn phái, Phong thổ) | Văn bản sạch không lỗi tag |
| **Web Reader Offline** | `03_Web_Reader/` | Giao diện đọc offline trực quan kèm công cụ Live Search | Đã kiểm nghiệm trên trình duyệt |

---

## 2. QUY CHUẨN TRA CỨU O(1) CHO AGENT
Khi một Agent sáng tác hoặc thẩm định cần kiểm tra bất kỳ chi tiết nào:
- **Tuyệt đối không đọc toàn bộ file JSON hay nạp toàn bộ SQLite vào prompt.**
- Chỉ chạy các câu lệnh truy vấn SQL ngắn gọn vào `story_database.sqlite3`:
  ```sql
  -- Tra cứu hội thoại gốc của một Subtask
  SELECT phase, cleaned_text FROM dialogues WHERE sub_id = ?;

  -- Tra cứu thông tin một NPC
  SELECT npc_id, npc_name, map_name FROM npcs WHERE npc_name LIKE ?;

  -- Tra cứu thoại môi trường tại một bản đồ
  SELECT npc_name, cleaned_msg FROM world_ambient_dialogues WHERE map_name LIKE ?;
  ```

---

## 3. CÁC TÀI LIỆU HƯỚNG DẪN ĐÍNH KÈM
- [`HOW_TO_USE.md`](file:///D:/Games/Server%20Client/Server%20KT/Ki%E1%BA%BFm%20Th%E1%BA%BF%202/Server/du-long-giac-2/migration/source_corpus/HOW_TO_USE.md): Sổ tay hướng dẫn chi tiết cách khai thác database cho các Agent.
- [`PHASE_1_SAMPLE_VERIFICATION.md`](file:///D:/Games/Server%20Client/Server%20KT/Ki%E1%BA%BFm%20Th%E1%BA%BF%202/Server/du-long-giac-2/migration/source_corpus/PHASE_1_SAMPLE_VERIFICATION.md): Báo cáo đối soát mẫu 10 Tasks và Subtasks.
- [`PHASE_3_SAMPLE_VERIFICATION.md`](file:///D:/Games/Server%20Client/Server%20KT/Ki%E1%BA%BFm%20Th%E1%BA%BF%202/Server/du-long-giac-2/migration/source_corpus/PHASE_3_SAMPLE_VERIFICATION.md): Báo cáo đối soát mẫu các kịch bản LUA Quân doanh và 30 thành thị.
