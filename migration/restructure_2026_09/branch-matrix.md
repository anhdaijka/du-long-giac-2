# Branch matrix — source routes, variants và reliability

Trạng thái: `COMPLETE INVENTORY / AQ-01–05 RESOLVED`. Ma trận đủ cho các branch family phát hiện trong khảo sát 13 Arc; các condition chưa chứng minh giữ mặc định `DO NOT LINEARIZE`.

| ID | Source family | Kiểu | Có thể đồng hiện mặc định? | Giá trị có thể giữ | Trạng thái |
| --- | --- | --- | --- | --- | --- |
| BR-001 | Tasks 4/5, sub 26–51 | Nam/nữ song song | Không | Cấu trúc sự kiện chung; tên/NPC khác phải theo route | Cần đọc condition XML |
| BR-002 | Tasks 1–25 qua nhiều môn phái | Avatar xuyên faction | Không trong novel | Phân cluster theo ba POV; không gán hết cho một người | Author chose `CURATED THREE-POV DISTRIBUTION` |
| BR-003 | Tasks 158/159/160 | Ba cổng xuất hành | Không | Một cổng chính hoặc phân phối có bridge cho nhiều POV | Open |
| BR-004 | Tasks 203–214 | 12 tuyến tiếp dẫn môn phái | Không | Texture môn phái và một route được chọn | Open |
| BR-005 | Repeat tasks trong Arc 06–08 | Gameplay loop | Không như biến cố bền vững | Lore/NPC/địa điểm có provenance | Filtered by default |
| BR-006 | Task 157 player-avatar | Identity mapping | N/A | Lõi thân thế và bài sấm | Author maps to Tiêu Phùng, age 18; Bridge |
| BR-007 | Task 352, sub 527–536 | Mega-task tuyến phương Bắc | Có nội bộ theo linear task; không đại diện toàn Arc 10 | Doãn Tiêu Vũ–Gia Luật Sở Tài–Hoàn Nhan Tương và tình báo | Cần predecessor/successor conditions |
| BR-008 | Tasks 383–394, 405–428, 430–441 | 12 phái theo cấp/kỹ năng | Không | Võ học/NPC nếu có giá trị novel | Gameplay by default |
| BR-009 | Unclassified 333–338, 363–368 | Main/daily/level variants | Không đếm thành nhiều event | Một event-family và premise lore | Cần chọn representative source row |
| BR-010 | Tasks 450–451 | Vision/alternate backstory | Hợp nhất bằng Bridge, không đổi nhãn source | Minh Dương–Tố Trinh–Nhạc-family profile | `RELIABILITY_LOCK` + author-selected novel truth |
| BR-011 | Missing Task ID 463 | Numeric gap | N/A | Không có | Closed unless new source artifact |

## Quy tắc sử dụng

1. `repeat=1` không đủ để loại mọi lore, nhưng cấm biến mỗi lần lặp thành một mốc chronology.
2. Nhan đề task/Arc là locator; muốn khẳng định sự kiện phải đọc subtask, step và dialogue.
3. Một branch chưa rõ điều kiện được mặc định không đồng hiện với branch song song.
4. Phân phối route cho Tiêu Phùng/Tĩnh Xuyên/Hạ Nương là Novelization Bridge, không phải fact game.
5. Mọi quyết định làm thay đổi profile được khóa phải chuyển sang author question; ma trận này không tự quyết.

## Quyết định đã đóng và việc còn mở

- PA route đã chốt theo `CURATED THREE-POV DISTRIBUTION`.
- Task 450–451 được chọn là thân thế thật trong novel, nhưng source vẫn mang `RELIABILITY_LOCK`.
- Chọn representative event cho Cổ Họa và Hải Lăng Vương Mộ variants nếu đưa vào novel.
- Phép ánh xạ Task 157 sang Tiêu Phùng và tuổi mở truyện 18 đã được chốt.
