# Rule 11: Prose Quality Contract & Literary Standards

Bắt nguồn và kế thừa trực tiếp từ hệ thống chất lượng văn học của repository gốc `du-long-giac` (`02_BIBLES/creative_runtime/literary-quality-kernel-r1.md`, `prose-quality-contract-r1.md`, `02_BIBLES/craft/rhetorical-naturalness-guard-r1.md`, `vietnamese-wuxia-prose-guide-reboot-r1.md`, `chapter-substantiality-floor-r1.md`).

Mọi bản thảo (manuscript) khi draft và review BẮT BUỘC tuân thủ các chuẩn mực sau:

---

## 1. Luật Tối Cao (North Laws)

1. `VĂN PHONG KHÔNG THỂ THAY THẾ CHO CỐT TRUYỆN` (Style cannot substitute for story).
2. `NHÂN VẬT THEO ĐUỔI MỤC TIÊU; KHÔNG PHẢI ĐÓNG VAI CHỨC NĂNG` (Characters pursue; they do not perform functions).
3. `LẶP LẠI PHẢI CHUYỂN HÓA` (Repetition must transform).
4. `SỬA LỖI LỚN NHẤT ĐỐI VỚI ĐỘC GIẢ TRƯỚC TIÊN` (The biggest reader-facing failure is fixed first: Macro → Meso → Micro).

---

## 2. Triệt Tiêu 3 Bệnh Kể Lể (Pure Show, Don't Tell)

1. **Bệnh 1: Tóm tắt hồi cố (Expository Recap) — CẤM TUYỆT ĐỐI**:
   - Không để người kể chuyện tóm tắt lại diễn biến vừa xảy ra ở đoạn trước (ví dụ: *"Chàng đã vượt qua... chỉ với suy nghĩ... nhưng không ngờ rằng..."*). Độc giả đã chứng kiến cảnh trước, không cần thuyết minh lại.
2. **Bệnh 2: Dán nhãn tâm lý & Phỏng đoán toàn tri (Psychological Labeling & Omniscient Guessing) — CẤM TUYỆT ĐỐI**:
   - Cấm dùng danh từ/tính từ trừu tượng để dán nhãn cảm xúc (*"sự thất vọng sâu sắc"*, *"cảm giác đắng chát"*, *"dường như đã lường trước"*, *"chàng hiểu rằng"*).
   - BẮT BUỘC miêu tả vi biểu cảm, ánh mắt, nhịp thở, độ run rẩy của cơ bắp, sự im lặng hoặc phản ứng thể chất cụ thể.
3. **Bệnh 3: Giảng giải bài học & Triết lý giáo điều (Thematic Preaching & Moralizing / Trailer Cadence) — CẤM TUYỆT ĐỐI**:
   - Cấm đúc kết bài học đường đời, triết lý số phận, hay báo trước tương lai ở cuối cảnh/cuối chương (*"Và chàng biết rằng chuỗi ngày bình yên đã chính thức khép lại..."*).
   - Cảnh và chương BẮT BUỘC kết thúc bằng hành động vật lý khách quan, hình ảnh không gian dư ba (Cảnh ngụ tình / Dư ba).

---

## 3. Giới Hạn Góc Máy Khách Quan (Third-Person Objective Limited POV)

- Ống kính trần thuật chỉ ghi lại những gì nhân vật trung tâm (POV) nhìn thấy bằng mắt, nghe thấy bằng tai và cảm nhận bằng xúc giác.
- **CẤM Head-Hopping (nhảy cóc tâm lý)**: Đang ở POV nhân vật A tuyệt đối không nhảy sang suy nghĩ, toan tính nội tâm của nhân vật B (ví dụ: trong POV Tiêu Phùng, không được chen vào *"Thu Di biết rõ trong huyết quản đứa trẻ kia..."*).

---

## 4. Zero-Tolerance AI Scaffolding & Cliché Bans (Lọc sạch 7 nhóm sạn)

Được quét và cưỡng chế tự động bởi `npm run lint:prose`:

1. **Thuật ngữ Meta / Lập trình / Planning**:
   - Cấm: `route`, `arc`, `beat`, `aperture`, `civic-martial`, `writer_packet`, `provenance`, `envelope`, `disposition`, `status`, `draft`, `task`, `subtask`.
2. **Khung thuyết minh / Dán nhãn AI (Explanatory / Telling Scaffolds)**:
   - Cấm trong lời dẫn: `đó chính là`, `đây chính là`, `đó là`, `đây là`, `chính là`, `ấy là`, `vốn là`, `thực chất là`, `thực ra là`, `có nghĩa là`, `nói cách khác`, `nơi ấy là`, `nơi đó chính là`, `chàng chính là`, `người thanh niên đó chính là`, `chàng hiểu rằng`, `không ngờ rằng`, `thực chất chỉ là một mắt xích`, `món nợ đạo đức`, `bàn cờ chính trị`.
3. **Mô-típ kết thúc sáo rỗng (AI Cliché Closures & Trailer Cadence)**:
   - Cấm: `bánh xe số phận`, `bàn cờ ân oán`, `bắt đầu chuyển động`, `chính thức lún sâu`, `bước chân.*chính thức`, `phong ba bão táp của chốn võ lâm`, `sóng gió giang hồ chính thức`, `hành trình.*chính thức bắt đầu`, `đã chính thức khép lại`.
4. **Liên từ nghị luận / Văn luận hiện đại (Modern Essay Connectives)**:
   - Cấm trong văn phong kiếm hiệp: `tuy nhiên`, `mặc dù vậy`, `đáng chú ý là`, `có thể thấy rằng`, `không thể phủ nhận rằng`, `hơn thế nữa`, `rõ ràng là`, `về cơ bản`, `trên thực tế`.
   - Thay thế bằng khẩu khí cổ phong tự nhiên: `song`, `nhưng`, `nào ngờ đâu`, `ngặt nỗi`, `ngờ đâu`, `đích thị`, v.v.
5. **Cường điệu võ hiệp huyền huyễn vô căn cứ (Inflated Clichés)**:
   - Cấm: `xé toạc không gian`, `chấn động càn khôn`, `uy lực khủng khiếp`, `bài sơn hải đảo`.
6. **Ngoại ngữ / Từ tiếng Anh rò rỉ**:
   - Cấm xuất hiện từ ngữ tiếng Anh trong văn bản truyện kiếm hiệp.
7. **Rò rỉ cú pháp / Định dạng code**:
   - Cấm thẻ chú thích HTML (`<!--`), thẻ XML hệ thống (`<TASK>`), biến template (`{{...}}`), code block, hoặc nhãn beat (`## Beat 1...`) bên trong văn xuôi. Beats phải chuyển tiếp mượt mà qua nhịp điệu trần thuật thuần túy.

---

## 5. Chuẩn Kết Chương Kim Dung (Narrative Closures)

Mỗi chương kết thúc theo một trong hai cách thức cổ điển:
- **Cảnh ngụ tình / Dư ba (Poetic / Atmospheric Closure)**: Để lại hình ảnh vật lý, âm thanh, hay cảm giác xúc giác cộng hưởng trong thinh lặng (tiếng gió rít qua rặng sậy, giọt mưa nhỏ trên lưỡi kiếm lạnh, tiếng gõ mái chèo trong sương).
- **Thắt nút hành động / Lơ lửng (Cliffhanger / Concrete Interruption)**: Hành động vật lý chưa hoàn tất, một biến cố bất ngờ xuất hiện ngay trước mắt nhân vật mà chưa giải thích ý nghĩa.

---

## 6. Sàn Dung Lượng & Không Gian Sống (Substantiality Floor)

- **Sàn chuẩn**: Tối thiểu 3,500 từ cho mỗi chương đầy đủ.
- 3,500 từ là yêu cầu về độ dung dưỡng đời sống (Living Wulin: cơm áo gạo tiền, lòng kiêu hãnh nghề nghiệp, sự nhàn tản, tình làng nghĩa xóm, hơi ấm nhân gian, dư vị sau xung đột) chứ **KHÔNG PHẢI LÀ LÝ DO ĐỂ BƠM TỪ RỖNG TUẾCH (NO PADDING)**.
