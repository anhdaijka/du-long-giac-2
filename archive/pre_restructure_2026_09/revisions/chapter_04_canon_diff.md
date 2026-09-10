# ĐỀ XUẤT CANON DIFF: CHƯƠNG 04a & 04b

> **Căn cứ thực thi:** Quyết định D-020 (Giao thức State Commitment 4 bước) và Quy tắc Kỷ Luật 3 Cổng Dừng Cứng (`docs/WORKFLOW.md` — Cổng Dừng 3: State Commit Hard Stop).
> **Trạng thái:** Chờ Tác giả phê duyệt. Tuyệt đối KHÔNG tự ý chỉnh sửa sổ cái bền vững khi chưa có lệnh `"Duyệt diff"`!

---

## 1. BƯỚC 1: CẬP NHẬT DANH BẠ NHÂN VẬT PHỤ (`characters/supporting_cast.md`)

Bổ sung và cập nhật trạng thái các nhân vật phụ tại **Khu vực Ba Lăng Huyện & Giang Tân Thôn**:

```markdown
| Nhân Vật | Tier | Môn Phái / Thân Phận | Ngoại Hình & Nhận Diện | Binh Khí / Nghề Nghiệp | Trạng Thái Hiện Tại | Lần Xuất Hiện Gần Nhất |
| :--- | :---: | :--- | :--- | :--- | :--- | :---: |
| **Thẩm Thiết Thạch** | **B** | Nghĩa quân cựu trào / Thợ săn độc hành | Thân hình hộ pháp vai rộng như phản gỗ lim, râu ria xồm xoàm bết dính tro than; ngực in hằn 3 vết chưởng ấn màu đen tím lạnh ngắt | Đoản đao săn thú / Cung săn thú | Bị hàn độc Âm Kình giặc Kim nhập não từ trận Tương Dương 1187, nửa điên nửa tỉnh, hễ gặp lạnh là phát cuồng đau đớn; vừa nhận lại chuỗi Hắc Trân Châu từ Tiêu Phùng, đang tịnh dưỡng trong lều cỏ bãi sậy phía tây Ba Lăng | Chương 04a |
| **Hứa Sĩ Vĩ** | **B** | Học trò thầy thuốc Trương Trảm Kinh | Thư sinh nho nhã ngoài đôi mươi, mặc áo dài vải xanh vá chằng vá đụp; tính tình nhân hậu, hết lòng vì huynh đệ | Gùi thuốc rừng, dao hái thuốc, y thuật sơ cấp | Tình nguyện ở lại lều cỏ 4 năm chăm sóc Thẩm Thiết Thạch để đền ơn cứu mạng; vừa bái tạ cảm kích Tiêu Phùng | Chương 04a |
| **Thẩm Hà Diệp** | **B** | Chủ tiệm phòng cụ Ba Lăng Huyện | Nữ tử thanh tú, đoan trang hiền thục; khóe mắt đượm buồn lo âu; tỷ tỷ của Thẩm Thiết Thạch, con gái Binh bộ Thị lang tiền triều | Khung cửi, kim chỉ, may đo phòng cụ da thú | Quản lý tiệm may và phòng cụ da dê; vừa nhận lại di vật chuỗi Hắc Trân Châu của cố mẫu thân trong nước mắt nghẹn ngào; coi Tiêu Phùng như đệ đệ trong nhà | Chương 04a |
| **Bất Động Tiên Sinh** | **B** | Chủ tiệm tạp hóa Ba Lăng Huyện | Thân hình hộ pháp núc ních hai trăm cân mỡ, mặc áo lụa rộng thùng thình; nằm ườn trên ghế mây phe phẩy quạt mo cau, mồm nhóp nhép cắn hạt dưa tanh tách | Quạt mo cau, tài buôn bán biết tuốt | Trông coi tiệm tạp hóa mặt phố kiêm kho quân nhu ngầm của Nghĩa quân; vừa sai Tiêu Phùng sang tiền trang Tạ Hiền đòi nợ và kiểm kê hàng tồn | Chương 04a, 04b |
| **Tạ Hiền** | **B** | Chủ tiền trang Tạ Hiền | Lão già gầy gò như bộ xương bọc da, chòm râu dê hoa râm dài chấm ngực; mười ngón tay khẳng khiu như móng chim ưng; kiệt sỉ, tính toán chi li từng hạt bụi vàng | Bàn tính gỗ mun, cân tiểu ly | Quản lý tiền trang đổi tiền và kho hầm đồ cầm cố; vừa nhờ Tiêu Phùng dọn ba rương gỗ mục nát dưới hầm sau lũ | Chương 04b |
| **Trâu Đức Khoái** | **B** | Thủ khố Nghĩa quân Ba Lăng | Trung niên béo lùn, mặc áo dài vải thô màu chàm, đeo kính tròn pha lê; cẩn thận, biết rõ gốc tích nghĩa quân | Bàn tính gỗ mun, sổ kho Nghĩa quân | Đánh rơi bàn tính vỡ kính khi thấy thư Ma Y Cốc; thừa nhận làm thất lạc tráp di vật trong trận lụt 1175; vừa dẫn Tiêu Phùng về trướng sảnh trần tình trước Thu Di | Chương 04b |
| **Bạch Cương** | **B** | Nghĩa quân tiền bối / Cố nhân Ma Y Cốc | Lão nghĩa quân sa trường; người đã liều chết bế Tiêu Phùng thoát khỏi vũng máu bến Hán Thủy năm 1174 | Đao sa trường / Tín hàm mật | Sau 17 năm mai danh ẩn tích ở phương Bắc vừa về đến chân đèo Tuyệt Vấn Pha thì bị toán sát thủ Âm kình giặc Kim vây hãm trọng thương; đang cùng Cao Thăng cố thủ chờ viện binh | Gieo mầm Ch.04b (Xuất hiện Ch.06) |
```

---

## 2. BƯỚC 2: CẬP NHẬT SỔ CÁI BẢO VẬT & KHÍ TÀI (`worldbuilding/artifacts/artifacts_ledger.md`)

Bổ sung 4 khí tài và cập nhật tình trạng đồ vật:

```markdown
| Vật Phẩm / Khí Tài | Xuất Xứ / Bản Chất | Người Giữ Hiện Tại | Vị Trí Vật Lý | Tình Trạng Hiện Tại (Vết Tích / Biến Dạng) | Lần Cập Nhật Gần Nhất |
| :--- | :--- | :--- | :--- | :--- | :---: |
| **Chiếc khánh bạc trẻ con** | Di vật định danh sơ sinh của Tiêu Phùng; đúc bằng bạc ròng xỉn màu; mặt trước khắc chìm chữ: "Tiêu Phùng (簫逢) — Thuần Hi nguyên niên", mặt sau chạm Bát Quái ôm ngọn lửa | **Tiêu Phùng** | Trong ngực áo Tiêu Phùng | Mặt bạc xỉn đen vì 17 năm ẩm ướt; mép kim loại sắc nhọn vừa đâm rướm máu lòng bàn tay Tiêu Phùng khi chàng xúc động siết chặt | Chương 04b |
| **Bức thư máu Ma Y Cốc** | Mật thư bọc vải dầu xám của Bạch Cương gửi Trâu Đức Khoái năm Giáp Ngọ (1174); niêm phong sáp chu sa mang con dấu đầu quạ ngậm quẻ Càn; ghi rõ thân thế Tiêu Lăng Phong | **Bạch Thu Lâm & Tiêu Phùng** | Quân trướng Ba Lăng Huyện | Giấy dó vàng khè ố bùn; sáp chu sa bị cạy mép; mực pha máu khô giòn nghiêng ngả | Chương 04b |
| **Chìa khóa bạch đồng** | Đúc bằng đồng trắng ánh xám bạc dài nửa gang tay, tay cầm chạm hoa văn mây xoắn khoét mắt quạ; chìa khóa mở tráp da trâu cổ | **Tiêu Phùng** | Dắt bên đai lưng vải gai | Sáng loáng không bị rỉ sét dù ngâm bùn lụt 17 năm | Chương 04b |
| **Chuỗi Hắc Trân Châu** | Chuỗi ba mươi sáu viên ngọc trân châu đen ánh xà cừ ngũ sắc; di vật gia truyền duy nhất của cố mẫu thân Thẩm gia | **Thẩm Hà Diệp** | Tiệm phòng cụ Ba Lăng Huyện | Nguyên vẹn lóng lánh; vừa được Tiêu Phùng đoạt lại từ hang Gấu Đen trên hài cốt tên sơn tặc | Chương 04a |
| **Đoản côn bịt sắt** | Gậy gỗ nghiến bãi sậy hai đầu bọc sắt non đóng bốn đinh tán đồng dẹt của Tiêu Phùng | **Tiêu Phùng** | Trên tay Tiêu Phùng | Khâu sắt non dính bùn hang gấu và trầy xước nhẹ sau cú đâm chệch khớp gân kheo gấu; thân gậy dính vệt máu khô từ vết rách da tay của Tiêu Phùng | Chương 04a, 04b |
```

---

## 3. BƯỚC 3: CẬP NHẬT BẢNG THEO DÕI HẠT GIỐNG CỐT TRUYỆN (`plot/promises_tracker.md`)

Cập nhật tiến triển và bổ sung hạt giống mới:

* **Mã TH-001 (Thân thế cha Tiêu Phùng & Ma Y Cốc):**
  - *Tiến triển:* **Chương 04b** thu hoạch bước 1 (`PARTIALLY RESOLVED / ACTIVE`). Tiêu Phùng tận tay cầm chiếc khánh bạc mang tên mình và phong thư máu của Bạch Cương; Thu Di xác nhận cha chàng là **Tiêu Lăng Phong** (đại đệ tử Ma Y Cốc hy sinh tại Hán Thủy Cổ Độ 17 năm trước).
  - *Kỳ hạn tiếp theo:* **Chương 06** (*Người Mất Tích*) và Quyển 2.
* **Mã TH-006 (Mối liên hệ giữa Ma Y Thần Tướng và Ma Y Cốc):**
  - *Tiến triển:* **Chương 04b** củng cố mối liên hệ (`ACTIVE / CONNECTED`). Đồ hình Bát Quái và con dấu đầu quạ Ma Y Cốc ở Ba Lăng khớp với pháp cụ Kham Dư la bàn đồng cổ mà Ma Y Thần Tướng cầm ở Bách Hoa Cốc (Chương 03).
* **Bổ sung MÃ HẠT GIỐNG MỚI — TH-008:**
  - *Nội dung:* **Toán sát thủ giặc Kim mang Âm Kình cực hàn**.
  - *Nơi gieo (Planted):* **Chương 04a** (3 vết chưởng ấn đen tím trên ngực Thẩm Thiết Thạch từ trận Tương Dương 1187) và **Chương 04b** (toán thích khách khăn đen thêu chim ưng dùng chưởng hàn băng tập kích đội tiếp ứng Tuyệt Vấn Pha).
  - *Tuyến nhân vật:* Tiêu Phùng / Thẩm Thiết Thạch / Bạch Cương.
  - *Kỳ hạn thu hoạch dự kiến (Target Payoff):* **Chương 06** (*Người Mất Tích*) & Hồi 2.
  - *Trạng thái:* `ACTIVE / TICKING THREAT`.

---

## 4. BƯỚC 4: CẬP NHẬT HỒ SƠ NHÂN VẬT & DÒNG THỜI GIAN

### 4.1. Hồ sơ Tiêu Phùng (`characters/tieu_phung.md`)
* **Mốc thời gian hiện hành:** 1191-08-18 (Đầu giờ chiều).
* **Binh khí & Vật phẩm mang theo:**
  - Đoản côn gỗ nghiến hai đầu bịt sắt non đóng 4 đinh tán đồng;
  - Chiếc khánh bạc trẻ con khắc chữ *"Tiêu Phùng — Thuần Hi nguyên niên"*;
  - Chìa khóa bạch đồng hoa văn mắt quạ;
  - Đôi Lữ Hành Ngoa mới bằng da dê do Thẩm Hà Diệp tặng;
  - Chiến mã Nghĩa quân cấp tốc phi về Tuyệt Vấn Pha.
* **Tri thức mới tiếp nhận (Known Facts):**
  - Biết rõ cha ruột là **Tiêu Lăng Phong** (đại đệ tử chân truyền Ma Y Cốc), đã hy sinh lẫm liệt cản hậu cứu chàng tại Hán Thủy Cổ Độ năm Giáp Ngọ (1174);
  - Biết lão nghĩa quân Bạch Cương là ân nhân bế chàng chạy trốn ngàn dặm về phương Nam và hiện đang lâm nguy ở Tuyệt Vấn Pha;
  - Biết giặc Kim có một nhánh sát thủ tà môn dùng Âm Kình cực hàn (kẻ thù chung đã phế bỏ Thẩm Thiết Thạch và đang truy sát Bạch Cương).

### 4.2. Dòng thời gian song hành (`plot/timeline.md`)
* **Ngày 18 tháng 8 năm 1191:**
  - *Ba Lăng Huyện (Sáng):* Tiêu Phùng thử đoản côn ở lò rèn Điềm Tửu Thúc; mang rượu nóng ra lều thợ săn độc hành Thẩm Thiết Thạch; nghe Hứa Sĩ Vĩ kể bi kịch 3 chưởng Âm kình Tương Dương; Tiêu Phùng vào hang Hắc Hùng Quật dùng rượu cay bột ớt hạ gục gấu đen, đoạt chuỗi Hắc Trân Châu di vật mẫu thân Thẩm gia trao lại cho Thẩm Hà Diệp (`Task 157: Subtask 309, 317–319` — **Chương 04a**).
  - *Ba Lăng Huyện (Trưa - Chiều):* Thu Di giao việc sang tiệm Bất Động Tiên Sinh; Tiêu Phùng sang tiền trang Tạ Hiền dọn kho đá vôi; phát hiện chìa khóa bạch đồng, tráp da trâu, chiếc khánh bạc khắc tên mình và bức thư máu Ma Y Cốc gửi Trâu Đức Khoái. Tiêu Phùng thất thần qua chợ huyện, đối chất kho bạc Trâu Đức Khoái; Trâu thủ khố dẫn chàng về trướng sảnh trần tình trước Bạch Thu Lâm; Thu Di giải mã thân thế Tiêu Lăng Phong; tiếng tù và hiệu giác rú vang cấp báo biến cố Tuyệt Vấn Pha; Bạch Thu Lâm cùng Tiêu Phùng phát binh xuất trận (`Task 157: Subtask 313` — **Chương 04b**).

## 5. PHÊ DUYỆT TỪ TÁC GIẢ (AUTHOR APPROVAL)

- [x] **accept all** (Tác giả đã phê duyệt chính thức ngày 2026-09-07)
- [ ] accept selected only
- [ ] reject

> **Trạng thái thực thi:** ĐÃ COMMIT THÀNH CÔNG toàn bộ 4 bước vào hệ thống sổ cái bền vững:
> 1. `characters/supporting_cast.md` (7 nhân vật Ba Lăng Huyện)
> 2. `worldbuilding/artifacts/artifacts_ledger.md` (4 khí tài mới & tình trạng đoản côn)
> 3. `plot/promises_tracker.md` (TH-001, TH-006, TH-008)
> 4. `characters/tieu_phung.md` & `plot/timeline.md` (Mốc 1191-08-18)
