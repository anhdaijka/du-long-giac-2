# World Event Coverage Ledger — bảng sơ bộ

Trạng thái: `PRELIMINARY COMPLETE / NOT CANON / NOT SCENE COVERAGE`.

Đã kiểm kê 465 task thành 390 nhóm lưu trữ; 27 nhóm nhiều task.
Nhóm lưu trữ không khẳng định các thành viên là cùng một biến cố. Chưa chọn representative hoặc gộp outcome.

Bảng phân loại sơ bộ dùng metadata và khảo sát đã lưu. Kiểm tra tái chạy toàn bộ query chứng minh dữ liệu trùng SQLite; không chứng minh đã đọc sâu mọi proposition.

Phạm vi: bảng tasks và subtasks/steps/dialogues liên kết. Các bảng NPC/map/item/lore độc lập và XML flags chưa được kiểm kê toàn bộ ở đây.

## Kết quả

| Kênh chính đề xuất | Task |
| --- | ---: |
| DIRECT_TRIO | 6 |
| DOCUMENT_TRACE | 50 |
| EXCLUDE_GAMEPLAY | 11 |
| LEGENDARY_ECHO | 16 |
| LIVING_LORE | 326 |
| WITNESS_RELAY | 56 |

A = ưu tiên bảo toàn biến cố/hồi cố; B = kho truyện chờ chọn; C = gameplay/routine cần tách lore. Đây là độ ưu tiên biên tập, không phải mức tin cậy fact.

## Cách đọc và tái kiểm

- [ledger.tsv](ledger.tsv): một dòng cho mỗi task, dễ lọc theo kênh/POV.
- [ledger.json](ledger.json): thêm family, NPC liên hệ nguồn, subtask IDs, evidence pointer và giới hạn tri thức.
- [editorial-notes.md](editorial-notes.md): ba cụm mẫu và các rủi ro cần xử lý.
- `python scripts/build_world_coverage.py --check`: mở SQLite read-only, chạy lại query task/subtasks/steps/dialogues, so toàn bộ kết quả với packet và so artifact sinh ra.

Query, bind task_ids và toàn bộ kết quả nằm trong source packet được trỏ ở từng dòng; `json_pointer` chọn chính xác task. NPC liên hệ nguồn không đồng nghĩa người gây biến cố hoặc POV đã chọn.

SQLite SHA-256: `b5c30040c9449f2223cf40bfec9866216423a60a82e2333b5cedb4fb5261bdb0`.

Giữ đủ 19 task ngoài Arc locator. Task thiếu subtask: [288].

Không tự chuyển kiến thức độc giả sang trio. Satellite POV là kênh ứng viên; mỗi cảnh vẫn phải thỏa sáu tiêu chí đã duyệt.

Quyền nguồn, family và sự kiện phải kiểm chứng trước khi chuyển một hàng sơ bộ thành cảnh. Cột OPEN là khoảng chưa quyết định, không phải nội dung bị bỏ quên.
