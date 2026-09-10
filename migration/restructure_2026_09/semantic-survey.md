# Semantic survey — tổng hợp đủ 13 Arc locator

Trạng thái: `LOCATOR_LEVEL_SURVEY_COMPLETE / AQ-01–05 RESOLVED / SOURCE REPORT NON-CANONICAL`.

Tài liệu tổng hợp này xác nhận đã đọc semantic cả 13 Arc locator và 19 task unclassified trước khi phân quyển. Nó không duyệt route, không canonize fact và không cho phép viết chapter plan/prose.

## Hồ sơ bằng chứng

- Arc membership: `evidence/arc-membership.tsv` và `evidence/arc-membership-report.md`.
- Query/result packets: `evidence/source-packets/arc_00.json` đến `arc_12.json`, cùng `unclassified.json`.
- Key-term query ledger: `evidence/key-mentions-report.md` và `evidence/key-mentions.tsv`.
- Báo cáo đọc: `semantic-survey-arc-00-03.md`, `semantic-survey-arc-04-08.md`, `semantic-survey-arc-09-12-unclassified.md`.

SQLite được khóa theo SHA-256 `b5c30040c9449f2223cf40bfec9866216423a60a82e2333b5cedb4fb5261bdb0` cho lượt khảo sát này.

## Kết quả toàn cục

1. Narrative Book phân 446/465 task vào 13 locator; 19 task không được gán, không có assignment trùng và không có locator ID thiếu trong SQLite.
2. Tên Arc không phải chronology đáng tin. Nhiều locator trộn main story, vignette địa phương, tutorial, route môn phái, task lặp và live-event.
3. Task 157 là lõi thân thế mạnh của player-avatar; việc gọi nhân vật đó là Tiêu Phùng là adaptation/Foundation mapping, không phải tên trực tiếp trong game row.
4. Task 12 là lõi Bách Hoa Trận/Du Long Giác mạnh; các task 1, 6–8, 11, 16–24, 146, 150, 231, 332, 450–452, 456 và 462 cung cấp những lớp rumor, pursuit, aftermath, secret, vision và vault-state khác nhau.
5. Task 450–451 vẫn là Huyễn Cảnh có reliability không được source giải thích. Tác giả đã chọn profile Minh Dương–Tố Trinh–Nhạc gia làm thân thế thật của Tiêu Phùng trong novel; lựa chọn đó là Novelization Bridge, không làm đổi nhãn nguồn.
6. Các mega-task 12, 157, 352 và 382 cần được giữ như chuỗi nội bộ; không được san phẳng thành một hàng ngang với task gameplay một-subtask.
7. Các family route lớn gồm giới tính Task 4/5, cổng xuất hành 158–160, tiếp dẫn môn phái 203–214, family cấp 20/30/40/110 và các biến thể main/daily/cấp độ unclassified.
8. Các nhân vật/sự kiện mang tên lịch sử trong SQLite vẫn là **fact game** cho tới khi có nguồn lịch sử độc lập. Khoảng nối để thành tiểu thuyết phải ghi **Novelization Bridge**.
9. Query ledger ghi 160 matching rows thuộc 26 task có literal `Du Long Giác`; 0 matching row có `Tiêu Lăng Phong`; và nguồn có cả `Lệ Thu Thủy` lẫn `Lịch Thu Thủy`. Đây là locator result, không tự quyết định canon.

## Điều kiện khi đề xuất phân quyển

- Dùng `source-graph.md` làm quan hệ nguồn, không dùng thứ tự Arc/Task làm niên biểu mặc định.
- Dùng `branch-matrix.md` để loại gameplay loop, variant và mutually-exclusive candidate trước khi chọn tuyến.
- Mọi xung đột mới với ba profile được khóa phải đi vào `foundation-contradictions.md` và chờ Tác giả quyết định.
- Adaptation contract đã được Tác giả duyệt ngày 2026-09-08. Volume architecture được phép đề xuất nhưng chưa được canon hóa; route bible, chapter plan và prose vẫn ở cổng sau.
