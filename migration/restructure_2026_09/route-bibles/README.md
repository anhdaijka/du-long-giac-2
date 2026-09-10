# Route Arc Bibles — pilot Quyển I

Trạng thái: `AUTHOR-APPROVED PLANNING / VOLUME I PILOT / NOT CANON`.

Tác giả xác nhận “Duyệt toàn bộ theo đề xuất” ngày 2026-09-09, chốt V1PQ-01–04 và BFCQ-01–04 trong phạm vi đã trình (R-27–R-34 / D-026–D-027). RABQ/LWCQ là quyền triển khai trước đó. Phê duyệt này không tự mở phân chương, văn xuôi, canon promotion hoặc nội dung Quyển II–V.

## Đọc gì trước

- [Tiêu Phùng](tieu-phung.md): cộng đồng, xuất hành, bước đầu vào thiết chế Cái Bang.
- [Tĩnh Xuyên](tinh-xuyen.md): quân lệnh, hộ tống và cái giá rời phòng tuyến.
- [Hạ Nương](ha-nuong.md): cứu người trong một thất bại của tổ chức, rồi gánh việc hồi phục.
- [Convergence matrix](convergence-matrix.md): tin tức/hậu quả nối ba tuyến; không gặp trực tiếp trong Quyển I.
- [World coverage](../world-coverage/README.md): đủ 465 task có disposition sơ bộ, không có nghĩa đủ 465 task đã chuyển thể hoặc đọc sâu.
- [Khảo sát khả thi Bridge](../bridge-feasibility-volume-i.md): BFCQ-01–04 đã duyệt; CDQ-01–05 sau đó quy định không nêu người/cách cứu Lục trong Quyển I, chọn relay theo chức năng và giữ lịch/custody mở.
- [Continuity-detail spec](../continuity-detail-spec-volume-i.md): CDQ-01–05 đã duyệt; người cứu Lục được chủ ý không nêu, relay chọn theo chức năng, chronology chỉ dùng partial order và custody hậu trường vẫn mở.
- [Chapter-architecture phase spec](../chapter-architecture-phase-spec-volume-i.md): CAPQ-01–06 đã duyệt. [Bộ architecture](../chapter-architecture/README.md) sau đó được duyệt qua V1CAQ-01–06; 25 function mặc định là planning authority, V1-CAND-020 deferred và bước proposal tên/số chương cùng brief đã mở.

Đây là sơ đồ áp lực và lựa chọn, không phải thứ tự cảnh. Mỗi nấc nhân vật là `AUTHOR-APPROVED NOVELIZATION BRIDGE — PILOT SCOPE`; trục lựa chọn, PB-01–06 và bốn Bridge khả thi đã được duyệt. Lục Trầm Châu là người đấu Thôi; thông cáo tới Thạch rồi chỉ phần công khai có thể tới Tiêu Phùng qua La Phong hoặc Cầu Chỉ Thủy. Người/cách cứu Lục, người relay cụ thể, lịch hành trình, custody thật, từng đòn đánh và kết quả y khoa vẫn chưa chọn.

## Quy ước bằng chứng

`GAME FACT` nghĩa là nguồn game ghi proposition đó, có giữ người nói/phương tiện truyền đạt. Một lời tố cáo, dự đoán hay thông cáo trong game không mặc nhiên là sự thật khách quan của thế giới. Không có `HISTORICAL FACT` mới nào được xác lập trong pilot. Quan chức, biến cố và niên hiệu xuất hiện trong nguồn vẫn là lớp game, chờ historical ledger.

`AUTHOR-APPROVED NOVELIZATION BRIDGE` chỉ áp dụng cho quyết định trong [author-decisions.md](../author-decisions.md). `PROTECTED FOUNDATION / AUDIT REQUIRED` không được gắn nhãn direct source. PB-01–06 bên dưới đã được duyệt với đúng giới hạn đã trình; mọi bổ sung bền vững ngoài phạm vi đó vẫn là `BRIDGE-CANDIDATE / AUTHOR APPROVAL REQUIRED`.

Mã `T157/S320/E1432` nghĩa là Task 157, subtask 320, step có id 1432; không phải số thứ tự cảnh. Với step được dẫn trong pilot, lời thoại/lệnh nối nằm trong `target_params` (trường `instruction` có thể rỗng). `T12/S90` mặc định trỏ `describe_cleaned` của subtask, trừ khi ghi trường khác. Evidence ledger dùng chính các packet lưu đủ query, bind và kết quả sau:

| Task | Packet kết quả | Bộ tham số |
| --- | --- | --- |
| 1, 2 | [arc_00.json](../evidence/source-packets/arc_00.json) | `task=(1)` hoặc `(2)`; `subtasks=(task_id)`; `steps/dialogues=(sub_id)` |
| 12 | [arc_01.json](../evidence/source-packets/arc_01.json) | `task=(12)`; `subtasks=(12)`; `steps/dialogues=(sub_id)` |
| 157, 158, 159, 160 | [arc_06.json](../evidence/source-packets/arc_06.json) | `task=(task_id)`; `subtasks=(task_id)`; `steps/dialogues=(sub_id)` |

Query nguyên bản lưu tại `provenance.query_templates` trong mỗi packet:

```sql
-- task: bind task_id
SELECT task_id, task_id_hex, name, describe_cleaned, category, category_desc, order_type, repeat, task_type_code, file_path FROM tasks WHERE task_id = ?;
-- subtasks: bind task_id
SELECT sub_id, sub_id_hex, task_id, name, describe_cleaned, file_path, dialog_npc_id, dialog_npc_name FROM subtasks WHERE task_id = ? ORDER BY sub_id;
-- steps: bind sub_id
SELECT id, sub_id, step_index, instruction, target_function, target_params FROM steps WHERE sub_id = ? ORDER BY step_index, id;
-- dialogues: bind sub_id
SELECT id, sub_id, phase, cleaned_text FROM dialogues WHERE sub_id = ? ORDER BY id;
```

Kết quả trích xuất nằm trong `tasks[task_id=…].subtasks[sub_id=…]`, không phải ở nhan đề Arc. Mỗi hàng [ledger.json](../world-coverage/ledger.json) còn có JSON pointer theo vị trí thật của task trong packet. `python scripts/build_world_coverage.py --check` tái chạy query read-only và so toàn bộ kết quả. Query replay chứng minh dữ liệu, không thay thế review diễn giải văn học.

## Bridge register — đã duyệt trong phạm vi pilot

Theo V1PQ-01–04, tất cả PB dưới đây có trạng thái `AUTHOR-APPROVED NOVELIZATION BRIDGE — PILOT SCOPE`. Không một PB nào được ghi là fact game.

| ID | Đề xuất cụ thể | Chỗ lệch khỏi avatar nguồn / giá phải giữ |
| --- | --- | --- |
| PB-01 | Tĩnh Xuyên giữ việc mang hai thư tới đầu mối Cái Bang; Tiêu Phùng đến trong cửa sổ khác, chỉ nhận phần việc/tri thức được La Phong hoặc Cầu Chỉ Thủy truyền đạt. Không gặp nhau. | T1/S8/E41 và T2/S9/E43, T2/S9/E44 nối cùng avatar. E43 còn nói thư Dương yêu cầu người đưa thư ở lại Cái Bang rèn luyện: đề xuất bỏ yêu cầu này khỏi thư trong bản chuyển thể, giữ chức năng cầu viện/liên lạc; việc Tiêu Phùng nhập Cái Bang dùng PB-02 riêng. Đây là thay đổi nội dung thư có nguồn, không phải chỉ đổi tên avatar. Không chép tiền sử Thiên Vương sang Tiêu Phùng. Chưa chọn người trao từng tin, giờ/ngày hoặc hành trình tiếp của Tĩnh Xuyên. |
| PB-02 | Dùng La Tuấn ở bước tìm hiểu môn phái làm đầu mối dẫn Tiêu Phùng tới Cái Bang; việc rời quê vẫn phát sinh từ khủng hoảng và sấm thi. | T157/S310 có lựa chọn môn phái; T157/S323 dẫn xuất hành. T158/S314, T159/S315, T160/S316 là các cổng Thiên Vương/Côn Lôn/Nga My, không có cổng Cái Bang. Đường giới thiệu mới là Bridge, không giả làm lựa chọn sẵn có. Chưa chốt bến, thời gian hoặc thư giới thiệu. |
| PB-03 | Với đoạn Cái Bang đầu, Tiêu Phùng tham dự đời sống, chứng kiến xét xử và nhận phần việc phù hợp; không là người hạ Thôi Xuất Trần. BFCQ-01 đã chọn Lục Trầm Châu giao đấu. | T2/S13 giao trận đấu cho avatar; việc đổi sang Lục là Bridge đã duyệt nhờ evidence T2/S10, S12–S13. Giữ hậu quả xử lý nội bộ, không dùng chiến thắng đó để cấp võ công cho Tiêu Phùng. Người/cách cứu Lục và chi tiết trận chưa chọn. Các subtask 15–24 chưa được đưa vào pilot, cũng chưa bị loại khỏi series. |
| PB-04 | Hạ Nương tập trung cứu nạn, chuyển thương và hồi phục; lực lượng môn phái cùng cao thủ trợ chiến giữ trọng lượng quân sự. Lựa chọn của nàng là theo người bị thương thay vì truy dấu ngọc. | T12/S88, T12/S90, T12/S91, T12/S92 đã có cứu nạn, phu phụ Đường Nhất Trần trợ chiến, Tam Muội đi tìm đại phu và tái thiết. Đổi người làm các đòn của avatar vẫn là Bridge. Không thêm kỳ tích chữa trị hoặc bảo đảm mọi bệnh nhân sống. |
| PB-05 | Cuối Quyển I, dùng mạng thư/tin môn phái cho các tuyến chịu tác động gián tiếp; mỗi người chỉ biết bản tin thật sự đến tay mình. BFCQ-02 đã duyệt thông cáo tới Thạch và phần công khai có thể tới Tiêu Phùng qua La Phong hoặc Cầu Chỉ Thủy; không cần đưa bản tin này tới Tĩnh Xuyên trong Quyển I. | T12/S92 có thông cáo tới năm chưởng môn, gồm Cái Bang. Dialogue nguồn cho thấy công bố “bị cướp” là nước cờ có chủ ý; nó không xác lập custody thật. Người relay cho Tiêu Phùng chưa chọn; tin đi tiếp vẫn là Bridge, không phải source edge. Tin Du Long ở T1/S2 là bản tin nguồn riêng, không mặc định do thông cáo này sinh ra. |
| PB-06 | Trong pilot, giữ tên và vai trò phòng thủ của Huyền Nguyệt Đại Trận nhưng treo giải thích công năng; chưa hiện thực hóa hoặc hợp lý hóa “năng lượng mặt trăng”. | T12/S89 mô tả cơ chế phản chiếu năng lượng mặt trăng; Hiến chương cấm huyền huyễn. Đây là `INTERIM HANDLING APPROVED / MECHANISM DEFERRED`, không phải giấy phép tự sửa nguồn. Chỉ được dựng chi tiết vận hành sau khi tác giả chọn mức chuyển thể. |

## Kết quả V1PQ-01–04 — APPROVED 2026-09-09

### V1PQ-01 — tách avatar Thiên Vương–Cái Bang

**Đã duyệt** hướng PB-01–03 và trục lựa chọn trong hai bible: Tĩnh Xuyên giữ vai người đưa thư; bỏ yêu cầu trong thư rằng chính người đưa thư phải lưu lại rèn luyện. Tiêu Phùng tới Cái Bang qua đầu mối La Tuấn, không thừa hưởng tiền sử Thiên Vương hoặc chiến thắng trước Thôi Xuất Trần. BFCQ-01 sau đó chọn Lục Trầm Châu giao đấu; người/cách cứu ông và chi tiết trận vẫn để mở.

### V1PQ-02 — vai Hạ Nương trong đại nạn

**Đã duyệt** PB-04: nàng có lựa chọn cứu người thực sự quan trọng, còn cao thủ và môn phái tự đánh trận của họ. Chưa chọn kết quả y khoa hoặc chia từng đòn chiến đấu.

### V1PQ-03 — độ hội tụ cuối quyển

**Đã duyệt** PB-05 và convergence matrix ở mức quan hệ nhân quả: mạng thư Thiên Vương–Cái Bang nối Tĩnh Xuyên với môi trường Tiêu Phùng; thông cáo/hậu quả Thúy Yên nối tuyến Hạ Nương với hai tuyến còn lại. Không cùng một cuộc gặp, không cùng biết mọi bí mật; chưa khóa lịch truyền tin.

### V1PQ-04 — xung đột cơ chế Huyền Nguyệt

**Đã duyệt** PB-06 như một giới hạn tạm: giữ biến cố phòng thủ và tên trận, để cơ chế chưa giải thích; không tự chọn SQLite hay Foundation thắng. Khi cần cảnh trực tiếp phải trình phương án fidelity riêng; phê duyệt pilot không tự phê duyệt cơ chế mới.

## Kiểm tra và giới hạn

- Ba route có opening state, pressure chain, lựa chọn, cái giá, tri thức, việc NPC tự làm và phần chưa dùng.
- Các node là tập ứng viên có quan hệ logic, không chia chương/beat/scene.
- Ba bible giữ Quyển II–V ở trạng thái placeholder; chỉ nêu hậu quả mang ra khỏi Quyển I, chưa thiết kế cách trả ở quyển sau.
- Chưa tạo satellite scene hoặc Legendary Shadow profile. Nhu cầu những hình thức đó được giữ ở World Spine; không ép pilot phải có một nhân vật mới.
- Kiểm tra tự động kiểm evidence locator, cấu trúc và trạng thái. Chất lượng nhân quả, giới hạn POV và mức chuyển vai vẫn cần review của người đọc, không được gọi là đã được máy chứng minh.
- BFCQ-01–04, CDQ-01–05, CAPQ-01–06, V1CAQ-01–06, V1CBQ-01–06 và SPQ-01–06 đã duyệt. [Chapter Plan Quyển I](../chapter-plan-volume-i/README.md) có 25 chương, 25 tên làm việc và bounded briefs là planning authority. [Scene-plan phase spec](../scene-plan-phase-spec-volume-i.md) mở candidate implementation; chưa candidate scene nào được duyệt và prose, chronology tuyệt đối, canon promotion vẫn đóng.
