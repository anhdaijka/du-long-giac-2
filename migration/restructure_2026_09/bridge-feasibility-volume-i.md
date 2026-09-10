# Khảo sát khả thi Bridge — Quyển I

Trạng thái: `AUTHOR-APPROVED PLANNING / BFCQ-01–04 / NOT CANON`.

Phạm vi được tác giả cho phép sau D-026: khảo sát người giao đấu thay, đường truyền tin, partial order và custody của Du Long Giác cho đúng pilot Quyển I. Tài liệu không phân chương, không khóa ngày/thời lượng di chuyển, không tạo nhân vật mới và không mở Quyển II–V.

Ngày 2026-09-09, Tác giả duyệt toàn bộ BFCQ-01–04 theo đề xuất. Phê duyệt chỉ nâng bốn Bridge dưới đây thành planning authority Quyển I; các chi tiết được ghi là còn mở vẫn chưa được chọn.

## Provenance dùng cho mọi GAME FACT bên dưới

SQLite: `story_database.sqlite3`, SHA-256 `b5c30040c9449f2223cf40bfec9866216423a60a82e2333b5cedb4fb5261bdb0`.

| Cụm | Query nguyên văn / bind | Kết quả lưu nguyên văn |
| --- | --- | --- |
| T1, T2 | `SELECT task_id, task_id_hex, name, describe_cleaned, category, category_desc, order_type, repeat, task_type_code, file_path FROM tasks WHERE task_id = ?` bind `(1)` / `(2)`; các query `subtasks`, `steps`, `dialogues` theo chuẩn packet | [arc_00.json](evidence/source-packets/arc_00.json), `tasks[task_id=1]` và `tasks[task_id=2]` |
| T12 | Cùng query trên, bind `(12)` | [arc_01.json](evidence/source-packets/arc_01.json), `tasks[task_id=12]` |
| T157 | Cùng query trên, bind `(157)` | [arc_06.json](evidence/source-packets/arc_06.json), `tasks[task_id=157]` |
| T2 text-search đối chiếu | `SELECT sub_id, task_id, name, dialog_npc_name, describe_cleaned FROM subtasks WHERE name LIKE ? OR describe_cleaned LIKE ? ORDER BY task_id, sub_id`, bind `('%Thôi Xuất Trần%', '%Thôi Xuất Trần%')` | Một hàng duy nhất: `T2/S13`, `Đông Sơn Tái Khởi`; không có dialogue row nào chứa tên này. Kết quả này được trích ngày 2026-09-09 trong lượt khảo sát. |

Các “query chuẩn packet” là:

```sql
SELECT sub_id, sub_id_hex, task_id, name, describe_cleaned, file_path, dialog_npc_id, dialog_npc_name FROM subtasks WHERE task_id = ? ORDER BY sub_id;
SELECT id, sub_id, step_index, instruction, target_function, target_params FROM steps WHERE sub_id = ? ORDER BY step_index, id;
SELECT id, sub_id, phase, cleaned_text FROM dialogues WHERE sub_id = ? ORDER BY id;
```

Packet lưu query, bind và toàn bộ rows/steps/dialogues; trích dẫn mã như `T2/S12/E60` trỏ một proposition cụ thể, không lấy nhan đề Arc làm bằng chứng. `GAME FACT` giữ nguyên speaker scope. Nhận định khả thi ở cột sau là `SOURCE-SUPPORTED INFERENCE` hoặc `BRIDGE-CANDIDATE`, không đổi nhãn source.

## 1. Người thay trận Thôi Xuất Trần

| Phát hiện | Lớp | Hệ quả |
| --- | --- | --- |
| T2/S13/E65 cho Thạch Hiên Viên nói không đệ tử phạm lỗi nào võ công cao hơn Thôi Xuất Trần, hoặc nếu có cũng không dám dùng hết sức. Nguồn giao trận cho avatar. | `GAME FACT` | Không được tự nói một đệ tử phạm lỗi vô danh đã đấu thay chỉ vì tiện kể. |
| T2/S10/E50: Thạch Hiên Viên hỏi võ nghệ Lục Trầm Châu; avatar đáp “rất cao cường”. T2/S12/E59–E60: sau khi Diêm Bang truy sát, Lục chọn theo Thạch; E60 dẫn thẳng tới mã `000…000D`, tức S13. | `GAME FACT` | Lục là người duy nhất có nguồn vừa xác nhận võ nghệ vừa có trạng thái đến Cái Bang trước S13 trong partial order source. |
| Việc avatar cứu Lục khỏi Tô Hữu Tưởng và trận Thôi đều là hành động avatar source. | `GAME FACT` | Nếu Lục nhận trận Thôi, cần giải riêng ai/cách nào giữ ông sống qua T2/S12; không thể “tặng” cả hai chiến công của avatar cho một người mới. |

### BFC-01 — phương án đã duyệt

`AUTHOR-APPROVED NOVELIZATION BRIDGE — VOLUME I FEASIBILITY SCOPE`: **Lục Trầm Châu** thay Thôi Xuất Trần tại lôi đài. Ông phù hợp hơn một “đệ tử Cái Bang vô danh” vì nguồn đã xác nhận võ nghệ, tính thẳng và quyết định đoạn tuyệt Diêm Bang trước S13.

Giới hạn phải giữ: đây là trận bị Thạch Hiên Viên dùng để tái lập bang quy trước anh hùng thiên hạ, không phải một màn Lục chứng minh trung thành hay Tiêu Phùng học tuyệt kỹ. Không viết Lục trở thành “người hùng cứu bang”; trận thắng chỉ thực hiện quyết định tổ chức. Việc giữ Lục sống qua vụ Tô Hữu Tưởng được duyệt ở mức **Cái Bang tự xử lý ngoài màn**; người cứu cụ thể, phương thức và cảnh thực hiện vẫn chưa chọn, và không được gọi đó là fact game.

`REJECTED AS UNSUPPORTED`: gán trận cho Thạch Hiên Viên, Cầu Chỉ Thủy, La Phong, Củng Thiếu Trăn hoặc Lãnh Thu Vân. Source có chức vị/hoạt động cho họ, nhưng không có proposition cho thấy họ là người có thể hoặc được phép đấu Thôi tại thời điểm S13. Lãnh/Củng chỉ xuất hiện sau S14 trong chuỗi source nên càng không là chứng cứ cho lôi đài S13.

## 2. Đường truyền tin

| Đường | GAME FACT có thể dùng | Điều không được tự suy ra |
| --- | --- | --- |
| Thanh Loa → Cái Bang | T1/S8/E37: Dương Thiết Tâm giao hai thư cho avatar; T1/S8/E41: người này gặp La Phong. T2/S9/E43–E44: Thạch Hiên Viên và Cầu Chỉ Thủy nhận/nói về thư; Thạch cho biết ba phân đà Cái Bang gần Thanh Loa hồi viện. | Sau PB-01 chỉ Tĩnh Xuyên mang thư, không ở lại rèn luyện. Source không nói chàng đi đâu sau khi giao, cũng không nói Tiêu Phùng nhận thư riêng. |
| Bách Hoa → Thạch Hiên Viên | T12/S92/E516: sứ giả của Doãn Hàm Yên trực tiếp báo Thạch Hiên Viên rằng Du Long Giác “bị cướp”; Thạch đáp Cái Bang sẽ hỗ trợ. | Câu công khai không phải báo cáo trung tính về custody. Cũng không tự chứng minh Tiêu Phùng hoặc Tĩnh Xuyên nghe được. |
| Thạch → môi trường Tiêu Phùng | T2/S9/S14 đặt La Phong làm người tiếp dẫn/hộ tống và T2/S13/E69 nói thuộc hạ La Phong theo dõi tình hình Hàn Thác Trụ. | Không có row nào nói La Phong chuyển thông cáo Thúy Yên cho Tiêu Phùng. Đó là một relay Bridge, không phải fact. |

### BFC-02 — relay tối thiểu đã duyệt

`AUTHOR-APPROVED NOVELIZATION BRIDGE — VOLUME I FEASIBILITY SCOPE`: không tạo một sứ giả mới. Để **bản thông cáo đến Thạch Hiên Viên** (T12/S92/E516) trở thành `DOCUMENT_TRACE` tại Cái Bang; Tiêu Phùng chỉ biết phần công khai khi được La Phong hoặc Cầu Chỉ Thủy giao một việc/hỏi ý. Người trực tiếp chuyển phần tin này cho Tiêu Phùng vẫn chưa chọn. Không cần cho Tĩnh Xuyên nhận bản thông cáo này trong Quyển I.

Điều đó giữ ba tầng tri thức: Hạ Nương biết cảnh cứu nạn và ý định truyền tin của tổ chức; Thạch biết bản thông cáo; Tiêu Phùng chỉ biết lời công khai cùng hệ quả Cái Bang. Không có người nào mặc nhiên biết custody thật hay động cơ riêng của người khác.

## 3. Partial order khả thi — không phải chronology tuyệt đối

| Cạnh | Cơ sở | Nhận định sử dụng |
| --- | --- | --- |
| T157/S320/E1432 → T157/S312 | E1432 có mã chuyển `000…0138` (hex 138 = subtask 312) sau việc giao 20 chìa khóa cho Thu Di. | Giữ việc làng/chìa khóa trước một phần khủng hoảng tiếp theo; không chốt ngày hay số người bị nạn. |
| T1/S8/E41 → T2/S9 | E41 có mã chuyển `000…0009`, và S9 mở bằng người mang thư tới Cái Bang/La Phong. | Đây là cạnh source trực tiếp cho tuyến Tĩnh Xuyên–thư; PB-01 chỉ thay người mang, không xóa chức năng liên lạc. |
| T2/S12/E60 → T2/S13 | E60 có mã chuyển `000…000D` (hex D = subtask 13), sau khi Lục đồng ý theo Thạch. | BFC-01 đã duyệt cho phép Lục đứng trước lôi đài mà không đảo chuỗi source của riêng T2. |
| T12/S86 → S87 → S88 → S89 → S90 → S91 → S92 | Các subtask/transition source nối chuỗi đo đạc–ngọc–báo động–tập kích–phòng thủ–chuyển thương–thông cáo. | Chỉ là local order của Task 12; không chứng minh nó trước/sau Thanh Loa hay Bạch Thu Lâm. |

`NO SOURCE EDGE`: T157 xuất hành → ngày Tiêu Phùng vào Cái Bang; T12/S92 → thời điểm Thạch nhận/cho lan thông cáo trong T2; thứ tự toàn cục T12 so với T1. Không dựng lịch di chuyển từ task number, vị trí bản đồ game hay cấp độ.

### BFC-03 — bố cục tương đối đã duyệt

`AUTHOR-APPROVED NOVELIZATION BRIDGE — VOLUME I FEASIBILITY SCOPE`: đặt ba dải song hành sau đây, không ghi ngày:

1. Tĩnh Xuyên hoàn tất T1/S8 và giao thư, rồi rời Cái Bang theo PB-01.
2. Tại Cái Bang, S10–S13 diễn ra; theo BFC-01, Lục thay trận Thôi. Tiêu Phùng chỉ đến sau khi tuyến T157 đã mở cửa xuất hành; không cần dự toàn bộ các nấc S9–S13.
3. Hạ Nương trải qua local chain T12/S85–S92; thông cáo của S92 có thể đến Thạch như một **dư chấn cuối Quyển I**, không cần xác định đến trước hay sau lôi đài nếu chưa làm chronology.

Đây là cấu hình ít tạo va chạm nhất với R-17: cùng tổ chức/tin tức nhưng không gặp trực tiếp. Nó không trả lời thời gian di chuyển hay đồng bộ năm lịch, vì source chưa đủ.

## 4. Du Long Giác: custody và vai Hạ Nương

| Row nguồn | GAME FACT với scope đúng |
| --- | --- |
| T12/S86/E483 | Hệ thống task ghi avatar lấy một Du Long Giác; S86 mô tả mục tiêu mang về Lệ Thu Thủy. |
| T12/S86/E484 và T12/S87 | E484 lại có avatar báo e ngọc đã bị mang đi, trong khi S87 mô tả avatar đã đưa ngọc cho Lệ Thu Thủy. Đây là **mâu thuẫn nội bộ source**, không được tự sửa. |
| T12/S92 dialogue và E516 | Doãn Tiêu Vũ đề nghị “tương kế tựu kế”, công bố ngọc đã bị cướp để thăm dò/huy động; Chung, Lệ và Doãn đồng ý. Sứ giả sau đó nói câu công khai ấy với Thạch Hiên Viên. |

### Kết luận custody

`GAME FACT`: **nguồn xác nhận thông cáo “bị cướp” là một nước cờ có chủ ý**, không phải báo cáo trung tính. `UNRESOLVED SOURCE CONTRADICTION`: source không đủ để xác lập ai giữ ngọc thật ngay sau S86–S92, hay dòng custody đầy đủ.

### BFC-04 — phân vai an toàn đã duyệt cho Hạ Nương

`AUTHOR-APPROVED NOVELIZATION BRIDGE — VOLUME I FEASIBILITY SCOPE`: Hạ Nương không lấy, giao, xác nhận nơi giữ hoặc giải công năng ngọc trong Quyển I. Nàng chọn cứu đệ tử bị cháy/chuyển Tam Muội đi chữa, trong khi Lệ Thu Thủy, Chung Linh Tú, Doãn Hàm Yên, Đường Nhất Trần và tổ chức tự xử lý phòng thủ–thông cáo–tái thiết theo source. Cách này thực hiện PB-04 và không buộc một lời giải custody giả.

## Kết quả BFCQ-01–04 — APPROVED 2026-09-09

Tác giả đã duyệt cả bốn đề xuất. Không quyết định nào mở chapter plan, scene prose, chronology tuyệt đối, Quyển II–V, Legendary Shadow hay canon promotion.

| ID | Quyết định đã duyệt | Giới hạn còn mở |
| --- | --- | --- |
| BFCQ-01 | Lục Trầm Châu là người đấu Thôi Xuất Trần; Cái Bang giữ ông sống qua vụ Tô Hữu Tưởng ngoài màn. | Chưa thêm cảnh cứu/đấu, chưa chọn người cứu hoặc cách cứu, không trao chiến công cho Tiêu Phùng. |
| BFCQ-02 | Thông cáo Thúy Yên tới Thạch; Tiêu Phùng chỉ biết bản công khai qua La Phong hoặc Cầu Chỉ Thủy khi có chức năng cảnh. | Không tạo sứ giả mới; chưa chọn La hay Cầu là người relay; không cho trio biết custody thật. |
| BFCQ-03 | Ba dải song hành ở mục 3 là partial order của Quyển I. | Không khóa ngày, độ trễ, cửa sổ di chuyển hoặc vị trí chương. |
| BFCQ-04 | Custody Du Long để mở trong Quyển I; Hạ Nương ở tuyến cứu người. Thông cáo “bị cướp” là nước cờ thông tin có chủ ý. | Không xác lập ai giữ ngọc, không để Hạ Nương lấy/giao/xác nhận custody hoặc giải cơ chế. |

Continuity-detail spec kế tiếp đã được duyệt qua CDQ-01–05. Bước sau chỉ được đề xuất chapter-architecture phase spec; không coi chuỗi phê duyệt này là quyền tự phân chương, chọn lịch tuyệt đối, custody hoặc hung khí Ân Đồng.
