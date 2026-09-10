# Source graph — tái dựng quan hệ nguồn

Trạng thái: `RECONSTRUCTED / NON_CANONICAL`. Graph này mô tả các quan hệ được phát biểu hoặc được phân loại từ nguồn game; nó không phải volume map.

## Quy ước cạnh

- `EXPLICIT`: quan hệ trước–sau/nhân quả được nội dung source nói trực tiếp.
- `INTRA_TASK`: thứ tự step/subtask trong cùng task linear.
- `CANDIDATE`: quan hệ hợp lý cần kiểm tra thêm condition/XML; không được dùng làm fact bền vững.
- `CONTEXT_ONLY`: cùng chủ đề hoặc locator, không hàm ý chronology.
- `RELIABILITY_LOCK`: nguồn tự đặt tính thật/giả chưa xác định.

Toàn bộ node dùng SQLite SHA-256 `b5c30040c9449f2223cf40bfec9866216423a60a82e2333b5cedb4fb5261bdb0`. Query và result nằm trong source packets; chỉ mục literal ở `evidence/key-mentions.tsv` cùng query đầy đủ ở `evidence/key-mentions-report.md`.

## Spine A — player-avatar và route

| Node | Source | Nội dung game-source | Nhãn |
| --- | --- | --- | --- |
| PA-01 | Task 157, sub 306–323 | Thiếu chủ trưởng thành, biết một phần thân thế, gặp Bạch Cương, ghép bài sấm và rời nơi lớn lên. | `GAME_EVENT` |
| PA-02A | Task 158 | Cổng đi Thiên Vương/Giang Nam. | `ROUTE_CANDIDATE` |
| PA-02B | Task 159 | Cổng đi Côn Lôn/Trung Nguyên. | `ROUTE_CANDIDATE` |
| PA-02C | Task 160 | Cổng đi Nga My/Tây Nam. | `ROUTE_CANDIDATE` |
| PA-03 | Tasks 1–25 | Nhiều cluster Thiên Vương, Cái Bang, Ngũ Độc, Thúy Yên, Đường Môn, triều đình và Đại Lý cùng dùng player-avatar. | `ROUTE_BANK` |
| PA-04 | Task 352, sub 527–536 | Chuyến do thám phương Bắc với Doãn Tiêu Vũ/Đan Bích Tú; Gia Luật Sở Tài và Hoàn Nhan Tương. | `GAME_EVENT_CHAIN` |
| PA-05 | Task 382, sub 566–575; Tasks 395–404 | Chuỗi triều chính và huy động thế lực cho Bắc phạt. | `GAME_EVENT_CHAIN` |
| PA-06 | Task 442–449 | Source ghi mốc 1205 và mở chiến dịch Linh Bích. | `GAME_DATE_AND_EVENT_CHAIN` |
| PA-07 | Task 450–451 | Player-avatar vào Huyễn Cảnh thân thế khi trọng thương; nguồn không xác nhận thật/giả. | `RELIABILITY_LOCK` |
| PA-08 | Task 452–462 | Trở lại chiến trường, đưa thông tin Du Long vào quyết sách và bảo vệ bảo khố. | `GAME_EVENT_CHAIN` |

Quan hệ:

- `PA-01 -> {PA-02A | PA-02B | PA-02C}`: `INTRA_TASK/ROUTE_CANDIDATE`; không chạy cả ba route cho một avatar nếu chưa có condition proof.
- `PA-04 -> PA-05`: `CANDIDATE`; task descriptions cho thấy trở về từ phương Bắc, nhưng cần XML/condition để chốt đường vào.
- `PA-06 -> PA-07 -> PA-08`: `INTRA_TASK/EXPLICIT` ở Task 450–452; riêng nội dung nhìn thấy trong PA-07 bị `RELIABILITY_LOCK`.
- Không có cạnh direct-source `PA-01 = Tiêu Phùng`. Tác giả đã duyệt phép đồng nhất này là `NOVELIZATION_BRIDGE`; Tiêu Phùng 18 tuổi ở điểm mở truyện.

## Spine B — Du Long Giác

| Node | Source | Vai trò nguồn | Reliability |
| --- | --- | --- | --- |
| DL-01 | Tasks 1, 6–8, 11 | Tin đồn, tranh đoạt và lời kể phân tán giữa các phe. | Speaker/claim scoped |
| DL-02 | Task 12, sub 85–95 | La bàn, Bách Hoa Trận, Du Long xuất thế, tập kích, phòng thủ và hậu quả. | Strong intra-task event chain |
| DL-03 | Tasks 16–24 | Điều tra, vận chuyển, cướp đoạt và tiến tới Thái Tổ Bảo Khố. | Multi-task chain candidate |
| DL-04 | Tasks 33, 37 | Echo địa phương có literal mentions. | Context only pending read |
| DL-05 | Tasks 146, 150 | Bạch Thu Lâm điều động đối phó nhóm từng tranh đoạt Du Long Giác. | Character report + action |
| DL-06 | Task 225 | Sau trận Thái Tổ Bảo Khố, chuyển sang dựng quân doanh Phục Ngưu. | Explicit transition |
| DL-07 | Task 231 | Source nói chuyện Du Long Giác đã đến hồi kết rồi chuyển sang quốc phòng. | Explicit phase marker; ending unspecified |
| DL-08 | Task 332 | Cẩm nang nêu bí mật thứ hai và phần kho báu chưa phát hiện. | Character/document claim |
| DL-09 | Tasks 450–451 | Huyễn Cảnh đưa ra Thư/Hùng giác và backstory khác. | Truth unresolved by source |
| DL-10 | Task 452 | Player-avatar kể Huyễn Cảnh; Bạch Thu Lâm cảnh báo giới hạn và hậu quả tranh đoạt. | Report of vision + response |
| DL-11 | Tasks 456–457, 462 | Du Long Bảo Khố có người giữ, quân lực, bí sử và tài nguyên dùng cho quân bị. | Later game-state claims |

Các cạnh được phép dùng:

1. `DL-02[sub85] -> ... -> DL-02[sub95]`: `INTRA_TASK`.
2. `DL-03[Task24] -> DL-06[Task225]`: `EXPLICIT`; Task 225 mở bằng việc nhìn lại trận Thái Tổ Bảo Khố.
3. `DL-06 -> quân doanh Phục Ngưu (Tasks 228–230)`: `EXPLICIT` theo nội dung xây dựng/thao luyện.
4. `DL-09 -> DL-10`: `EXPLICIT`, nhưng không tháo `RELIABILITY_LOCK` của Huyễn Cảnh.
5. `DL-10 -> DL-11`: `CANDIDATE`; source cho thấy kho báu được đưa vào chiến cuộc sau đó, nhưng cần kiểm tra condition/transition chính xác.

Không được tự nối:

- Không nối `DL-07 -> DL-08` chỉ vì số task tăng; “kết” và “bí mật thứ hai” có thể là giai đoạn nội dung khác.
- Không relabel `DL-09` thành direct-source truth. Tác giả đã chọn Minh Dương–Tố Trinh–Nhạc-family profile là novel truth qua `NOVELIZATION_BRIDGE`.
- Không biến lời của NPC về công năng ngọc, long mạch hay “xoay chuyển càn khôn” thành quy luật vật lý khách quan.

## Spine C — chính trị/quân sự trong game

| Node | Source | Cụm |
| --- | --- | --- |
| PM-01 | Tasks 225, 228–231 | Phục Ngưu, tân quân, hợp luyện nghĩa quân–triều đình. |
| PM-02 | Tasks 232–242 | Gia Vương/Ninh Tông, Chu Hy, Triệu Nhữ Nhu, Hàn Thác Trụ, Khánh Nguyên. |
| PM-03 | Tasks 243–256 | Tình báo Thát Đát, Kim, Tây Hạ. |
| PM-04 | Tasks 257–267 | Hậu chính biến và quân doanh Phục Ngưu. |
| PM-05 | Tasks 291–300 | Chu Hy/Trường Ca/Hàn Thác Trụ. |
| PM-06 | Tasks 303–332 | Biên cương, Phục Ngưu và Đại Lý. |
| PM-07 | Task 382; Tasks 395–404 | Chuẩn bị Bắc phạt và huy động giang hồ. |
| PM-08 | Tasks 442–462 | Bắc phạt 1205, Linh Bích và hậu quả. |

Tất cả node PM hiện mang nhãn `GAME_FACT_CLUSTER`. Tên người, năm và biến cố chỉ được nâng thành `HISTORICAL_FACT` sau một ledger sử liệu độc lập. Quan hệ giữa các cụm ngoài cạnh explicit trong task vẫn là `CANDIDATE`.

## Lớp loại khỏi chronology mặc định

- Task `repeat=1`: event occurrence không bền vững; chỉ trích lore nếu cần.
- Family môn phái cấp 20/30/40/110 và tiếp dẫn 203–214: route/gameplay.
- Unclassified 333–338 và 363–368: main/daily/level variants.
- Task 466–469: seasonal, marriage, skill hoặc live-event content.
- Missing numeric IDs: không tạo node “sự kiện mất” nếu không có artifact nguồn khác.
