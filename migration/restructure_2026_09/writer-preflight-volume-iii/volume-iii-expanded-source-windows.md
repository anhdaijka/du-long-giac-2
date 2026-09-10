# Quyển III — expanded source windows cho allocation đầy đủ

Trạng thái: `AUTHOR-DEFAULTED PLANNING / D58-R84 / SOURCE-BOUND / NOT PROSE / NOT CANON`.

Tài liệu này mở rộng baseline bảy chức năng D-055 thành source map đủ mật độ cho Quyển III. Phạm vi chỉ gồm Arc 08 và lát cắt **Phục Ngưu–quân doanh** của Arc 09. Phần Đại Lý/địa-chính trị của Arc 09 vẫn thuộc Quyển IV; Task ID không được dùng thay chronology.

## Source windows được dùng

| Window | SQLite packet receipt | Công dụng chapter-level | Trần suy diễn |
| --- | --- | --- | --- |
| `V3-EW-01` | Arc 08: T228/S403; T231/S406 | Từ thao luyện tân quân sang hợp luyện nghĩa quân–triều đình: cỗ máy huy động bắt đầu có học thuyết, quân nhu và chính danh. | Không biến book/item/game training thành cơ chế tiểu thuyết; không gán avatar/trio làm người chọn quân, truyền lệnh hay chỉ huy. |
| `V3-EW-02` | Arc 08: T232–T240 / S407–S415 | Chuỗi game-narrative về Gia Vương, Chu Hy, triều đình, điều tra, đàn hặc, cách chức và đảng cấm. | Toàn bộ giữ `GAME ALT-HISTORY / GAME NARRATIVE`; không tự gọi là lịch sử thật, không ép avatar route cho Tĩnh hoặc xác lập khách quan ai chính/ai tà. |
| `V3-EW-03` | Arc 08: T241/S416; T242/S417 | Trường Ca Lục và ba danh sĩ làm living-wulin/cultural-memory, cho thấy học giả và môn phái tự có đời sống. | Không biến bản thảo, mặc bảo hoặc mọi lời kể thành historical fact; bỏ objective thu thập/đánh NPC. |
| `V3-EW-04` | Arc 08: T243–T250 / S418–S425 | Chuỗi tin phương Bắc: thảo nguyên, sứ giả, Cố Liêu, giới hào, thế công–thủ và kỵ binh. | Đây là intelligence/report/inference trong game; không canon hóa lịch sử Mông Cổ–Kim, danh tính, ý đồ, công nghệ hay chiến thắng của trio. |
| `V3-EW-05` | Arc 08: T251–T256 / S426–S431 | Tình báo Tây Hạ: tân chủ, người kế vị, ký ức dân chúng, quân bí mật, mã tặc và lời đồn dược–đạo sĩ. | Không biến điều tra/avatar inference thành chân tướng; không xác nhận dã tâm, thư, phe, y thuật hoặc công hiệu Hoàn Đồng Đơn. |
| `V3-EW-06` | Arc 08: T257/S432; T258/S433 | Xe sách rời kinh và cuộc tiễn người học trò bị đày: cái giá con người/học thuật sau chính biến. | Không lấy “hơn 10 ngày” làm chronology tiểu thuyết; không gán hộ tống/chăm sóc cho trio hoặc suy bệnh trạng. |
| `V3-EW-07` | Arc 08: T259–T262 / S434–S437 | Quan hưởng lạc → rương đồng/cắt quân hưởng → binh biến → tìm người hòa giải. | Phân biệt đánh giá của narrator/NPC với objective fact; không cho trio chôn rương, bắt quân hoặc quyết kết cục binh biến. |
| `V3-EW-08` | Arc 08: T263–T266 / S438–S441 | Tất Tái Ngộ dùng mưu, huấn luyện nguy hiểm và thu nạp người giang hồ: quân đội hấp thụ kỹ nghệ/vũ lực ngoài chính quy. | Không xác nhận thuốc, “một địch trăm”, danh tướng tương lai hay chiến công avatar; không để trio tự tuyển cả lực lượng. |
| `V3-EW-09` | Arc 08: T267/S442 | Tin Triệu Nhữ Nhu mất và phản ứng của Tất Tái Ngộ; Khẩn Thân Ngọc chỉ là object/effect claim trong game task. | Không tự xác lập historical death/date/cause, hiệu lực ngọc, tang lễ hoặc người lấy/giao. |
| `V3-EW-10` | Arc 09: T271/S446; T273/S448; T274/S449; T275/S450; T276/S451 | Repeatable camp texture: bạo lực mỏ, cáo buộc cấu kết, mùa đông/quân nhu và người phu mất liên hệ gia đình. | Chỉ dùng như recurring social condition/report, không dựng thành năm sự kiện tuyến tính, không xác nhận cáo buộc hoặc trao objective gameplay cho trio. |

## Không dùng trong baseline này

- T229–230 và T268–270 là repeatable/game-training hoặc kill-loop; chỉ được coi là system/context đã hấp thụ vào EW-01/EW-07, không thành chương riêng.
- T272 và T277–290 là repeatable gameplay/collection/local tale. T281–289 có nhiều lời đồn vật phẩm/y hiệu nhưng không đủ quyền biến thành công năng thật; T288 không có subtask row.
- T291–300 là cụm Chu Hy–Trường Ca tiếp theo nhưng nằm ngoài lát cắt Arc 09 quân doanh đã khóa cho lượt này. Chúng giữ reservoir để review volume boundary riêng, không tự nhập Quyển III và cũng không tự đẩy sang Quyển IV.
- Task 303 trở đi thuộc cửa sổ chiến lược/Đại Lý cần giữ cho Quyển IV; tuyệt đối không dùng để tăng density Quyển III.

## Writer rule

Các chapter chính trị và tình báo phải giữ nguồn phát ngôn: chiếu, thư, lời quan, lời gián điệp, lời dân hoặc suy luận của game avatar. Gemini không được hợp nhất chúng thành giọng kể toàn tri. Với repeatable Arc 09, chỉ được diễn giải thành điều kiện xã hội tái diễn; muốn dựng một biến cố cụ thể, người thực hiện hoặc kết quả bền vững phải hỏi Tác giả.
