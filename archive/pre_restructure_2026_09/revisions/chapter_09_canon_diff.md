# Đề Xuất Canon Diff: Chương 09 — Huyết Chiến Miếu Cổ

> **Cơ quan quản lý**: Novel OS State Ledger  
> **Trạng thái**: Chờ Tác giả xem xét và phê chuẩn trước khi commit vào Sổ cái trạng thái bền vững (Cổng Dừng 3).

---

## 1. Tóm Tắt Biến Chuyển Cốt Truyện & Nhân Vật (Narrative Summary)

- **POV**: Tiêu Phùng (17 tuổi — Ngôi thứ ba hạn tri hiệp sĩ áo vải / Ba Lăng Huyện).
- **Thời gian**: Chiều muộn ngày 1191-08-20 đến Canh ba rạng sáng ngày 1191-08-21.
- **Bối cảnh & Dòng thời gian mượt mà**:
  - Khoảng đệm tự nhiên 2 ngày sau cơn giông bão ngập lụt rạng sáng 19/8; nước sông Động Đình rút bớt, phù sa se mặt; làng chài Giang Tân Thôn gượng dậy phơi lưới dựng lại lều bạt;
  - Tiêu Phùng bị "giam lỏng" hai ngày trên gác xép tiệm thuốc Thẩm Hà Diệp uống thuốc hoàng liên đắng ngắt, nẹp tre mạn sườn trái; tính khí hiếu động bãi sậy khiến chàng cuồng chân nhấp nhổm than vãn "lưng mọc nấm rơm nấu canh gà";
  - Thấy chàng quá ngột ngạt và vết nẹp tạm ổn, chiều muộn 20/8 Thu Di cho chàng đi theo xe bò chở đồ cứu tế ra Miếu Thần Ba Lăng ven đê để hóng gió sông cho thoáng phổi và giúp lão Trương kiểm kê sổ sách nhẹ nhàng, nghiêm cấm chạy nhảy mang vác.
- **Huyết chiến Miếu Cổ & Phân vai rõ rệt**:
  - Đêm Canh hai tại Miếu Thần Ba Lăng: Toán 4 thích khách sa trường mặc giáp da đen phá tung cửa gỗ lim xông vào miếu hòng cướp đoạt chiếc tráp sắt chứa cuốn da dê *Vô Danh Mật Tịch*;
  - Tổ tuần trinh nghĩa quân (Ngũ trưởng Trương Đỉnh cùng hai tráng đinh Đại Cường, Tiểu Lục) vung giáo tre và trường đao tử chiến chặn cửa miếu; hai tráng đinh ngã gục trong vũng máu, Trương Đỉnh bị chém rách bắp đùi;
  - Tiêu Phùng mang thương tật `INJ-TP-002` (L3) lực bất tòng tâm, chỉ dùng phản xạ sinh tồn thọc rơi giàn đèn dầu lạc tạo dải lửa cản bước giặc, lết thân mình kéo giấu chiếc tráp sắt vào hốc đá tượng Thần Nông;
  - Tên thủ lĩnh đoản trùy sấn tới đá bạt góc bàn thờ đập trúng mạn sườn trái làm gãy toác nẹp tre, Tiêu Phùng hộc máu bầm ngất lịm; Trương Đỉnh dồn tàn lực ôm chặt cổ chân tên giặc câu giờ;
  - Bạch Thu Lâm cùng mười kỵ mã nghĩa quân phá cửa ùa vào, một mũi tên sắt bắn xuyên thái dương tên thủ lĩnh, kiếm quang danh tướng chém chết toàn bộ toán giặc, cứu Tiêu Phùng và Trương Đỉnh thoát chết trong gang tấc;
  - Khám nghiệm tử thi: Xác nhận là mật thám của **Tây Hạ Nhất Phẩm Đường** (`ORG-TH-NHATPHAM`), đồng quy rùng rợn với thảm biến Thúy Yên Môn (Ch.08b).
- **Khớp nối Hai Mảnh Mật Mã & Quyết định Xuất Sơn**:
  - Thu Di mở tráp sắt đối soát cuốn da dê *Vô Danh Mật Tịch* với 4 câu sấm thi của Tiêu Lăng Phong (*"Thái bạch dạ quan tinh / Trọc khí quy tam thanh / Thiên mã chấn trường dực / Long Cung trích tử anh"*);
  - Khẳng định *Vô Danh Mật Tịch* ghi chép cách giải cơ quan Trụ Thần Thạch Động Đình, nhưng cần hung ngọc *Du Long Giác* dẫn đường kinh vĩ độ. Hai mảnh bảo vật chính là hai nửa âm - dương không thể tách rời;
  - Nhận thấy thân thế Tiêu Phùng đã bị gián điệp ngoại bang phát giác, Thu Di trao phong thư niêm sáp đỏ cử chàng sang **Cái Bang Yến Tử Ổ** bái kiến Bang chủ **Thạch Hiên Viên** tị nạn và rèn giũa bản lĩnh, chính thức mở màn lộ trình xuất sơn.

---

## 2. Đề Xuất Cập Nhật Sổ Cái Thương Tật (`worldbuilding/medical/injuries_ledger.md`)

```diff
Index: worldbuilding/medical/injuries_ledger.md
===================================================================
--- worldbuilding/medical/injuries_ledger.md
+++ worldbuilding/medical/injuries_ledger.md
@@ -40,3 +40,3 @@
 | **INJ-TP-002** | Mạn sườn trái: nứt rạn xương sườn@@ -85,3 +85,11 @@
+### L. Ngũ trưởng Trương Đỉnh (Nghĩa Quân Ba Lăng — 42 tuổi)
+
+| Vết thương # | Vị trí & Dạng tổn thương | Cấp độ | Tác nhân / Hoàn cảnh | Hồi xuất hiện | Trạng thái hiện tại | Di chứng & Ảnh hưởng hành vi |
+| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
+| **INJ-TRD-001** | Bắp đùi ngoài chân phải: Đao mỏng Tây Vực chém rách cơ sâu 1 tấc rưỡi, đứt mạch máu nhánh, mất máu nhiều. | **L2** (Trung bình / Tổn thương cơ & mạch) | Tử chiến bảo vệ Miếu Thần Ba Lăng và ôm chân tên thủ lĩnh đoản trùy cứu Tiêu Phùng (Ch.09). | Chương 09 | **ĐÃ KHÂU DÃ CHIẾN**. Kỵ binh nghĩa quân băng bó garô và chuyển về y quán Ba Lăng. | Đi khập khiễng trong 3 tuần; cần dưỡng thương và bồi bổ khí huyết; không nguy hiểm tính mạng. |
```

---

## 3. Đề Xuất Cập Nhật Hồ Sơ Nhân Vật Tiêu Phùng (`characters/tieu_phung.md`)

```diff
Index: characters/tieu_phung.md
===================================================================
--- characters/tieu_phung.md
+++ characters/tieu_phung.md
@@ -77,7 +77,7 @@
 ## 6. SỔ CÁI TRẠNG THÁI HIỆN HÀNH (DURABLE STATE LEDGER)
-* **Mốc thời gian hiện hành:** 1191-08-19 (Rạng sáng & Bình minh — Sau Chương 06).
-* **Thể trạng thực tế:** Đang mang chấn thương L3 (INJ-TP-002: rạn xương sườn số 6 mạn sườn trái, nẹp tre cố định) kèm chấn thương L1 (INJ-TP-003: chuột rút cơ hoành và cơ bụng); miệng còn vị tanh máu bầm cũ; hơi thở nông khò khè khi vận động.
+* **Mốc thời gian hiện hành:** 1191-08-20 (Canh ba rạng sáng — Sau Chương 09).
+* **Thể trạng thực tế:** Vừa trải qua tái chấn động mạn sườn trái do va đập bàn thờ tại Miếu Thần Ba Lăng; gãy rời một thanh nẹp tre, nôn máu bầm ngất lịm; đã được Bạch Thu Lâm truyền chân khí hộ tâm khai thông phế khí và nẹp lại hai thanh tre mới tẩm rượu thuốc; thể lực kiệt quệ nhưng tâm thần tỉnh táo, hơi thở khò khè đau buốt khi vặn mình.
 * **Binh khí & Trang bị:** 
   - Đoản côn gỗ nghiến bãi sậy (đầu bịt sắt non mẻ thêm khía rãnh sau khi dùng thọc giàn đèn dầu lạc; thân gỗ bám bụi than và tàn tro Miếu Thần).
   - Đôi Lữ Hành Ngoa bằng da dê núi của Thẩm Hà Diệp (đã khô bùn đỏ Động Đình).
   - Quần áo vải thô màu xám tro rộng thùng thình dính máu giặc và máu bầm của chính mình.
 * **Vật phẩm mang theo:**
   - Chiếc khánh bạc sơ sinh khắc chìm "Tiêu Phùng (簫逢) — Thuần Hi nguyên niên", mặt sau chạm Bát Quái ôm ngọn lửa (giắt sát tim).
   - Chìa khóa bạch đồng hoa văn mây xoắn mắt quạ (dắt bên đai lưng).
+  - **01 Phong thư tiến cử** niêm sáp đỏ thẫm hình hoa sen ôm đoản kiếm của Nghĩa Quân Ba Lăng do Bạch Thu Lâm trao, gửi Bang chủ Cái Bang Thạch Hiên Viên tại Yến Tử Ổ.
 * **Tri thức đã biết (Known Facts):**
   - Đã trực tiếp chứng kiến cuốn da dê *Vô Danh Mật Tịch*; nắm rõ mối liên hệ giữa bản đồ Trụ Thần Thạch và bài sấm thi của cha Tiêu Lăng Phong.
   - Biết chữ "Long Cung trích tử anh" trong sấm thi chính là khối hung ngọc *Du Long Giác* — chìa khóa định vị và kích hoạt mạng lưới Trụ Thần Thạch.
   - Nhận diện trực tiếp toán sát thủ sa trường thuộc **Tây Hạ Nhất Phẩm Đường** qua hình xăm chim ưng quắp chùy gai, đao mỏng Tây Vực và đất sét vàng sa mạc.
   - Nhận thức rõ thân thế của mình đã bị lộ, Ba Lăng Huyện không còn an toàn; chuẩn bị rời quê hương vượt hồ sang Cái Bang Yến Tử Ổ.
```

---

## 3b. Đề Xuất Cập Nhật Danh Bạ Nhân Vật Phụ Trợ (`characters/supporting_cast.md`)

```diff
Index: characters/supporting_cast.md
===================================================================
--- characters/supporting_cast.md
+++ characters/supporting_cast.md
@@ -12,4 +12,4 @@
-| **Lão Trương (Trương bá)** | **C** | Dân chài bến đò Giang Tân | Tuổi ngoài ngũ tuần, da đen nhẻm, tay đầy nốt chai sần, khoác áo tơi lá tơi tả; tính tình cộc cằn nhưng khẩu xà tâm phật | Xuồng ba lá, lưới đánh cá; chuyên câu cá mè hoa và mè gai | Đang lái đò bến đò đầm lau, hay quát mắng và quăng cá mè gai cho Tiêu Phùng; tiếp nhận lương thực cứu trợ tại Miếu Thần | Chương 01 |
+| **Lão Trương (Trương bá)** | **C** | Dân chài bến đò Giang Tân | Tuổi ngoài ngũ tuần, da đen nhẻm, tay đầy nốt chai sần, khoác áo tơi lá tơi tả; tính tình cộc cằn nhưng khẩu xà tâm phật | Xuồng ba lá, lưới đánh cá; chuyên câu cá mè hoa và mè gai | Đang lái đò bến đò đầm lau, hay quát mắng và quăng cá mè gai cho Tiêu Phùng; tiếp nhận lương thực cứu trợ tại Miếu Thần | Chương 01, 09 |
@@ -15,1 +15,1 @@
-| **Thẩm Hà Diệp** | **B** | Chủ tiệm phòng cụ Ba Lăng Huyện | Nữ tử thanh tú, đoan trang hiền thục; khóe mắt đượm buồn lo âu; tỷ tỷ của Thẩm Thiết Thạch, con gái Binh bộ Thị lang tiền triều | Khung cửi, kim chỉ, may đo phòng cụ da thú, sơ cứu thương tật | Quản lý tiệm may và bốc thuốc đắp trật đả; dầm mưa cứu hàng và ôm chầm Tiêu Phùng mừng rỡ sau đêm hộ đê; chăm sóc nẹp xương sườn cho Tiêu Phùng; coi Tiêu Phùng như đệ đệ trong nhà | Chương 04a, 06, 07a |
+| **Thẩm Hà Diệp** | **B** | Chủ tiệm phòng cụ Ba Lăng Huyện | Nữ tử thanh tú, đoan trang hiền thục; khóe mắt đượm buồn lo âu; tỷ tỷ của Thẩm Thiết Thạch, con gái Binh bộ Thị lang tiền triều | Khung cửi, kim chỉ, may đo phòng cụ da thú, sơ cứu thương tật | Quản lý tiệm may và bốc thuốc đắp trật đả; dầm mưa cứu hàng và ôm chầm Tiêu Phùng mừng rỡ sau đêm hộ đê; chăm sóc nẹp xương sườn cho Tiêu Phùng; coi Tiêu Phùng như đệ đệ trong nhà | Chương 04a, 06, 07a, 09 |
@@ -24,0 +25,3 @@
+| **Trương Đỉnh** | **B** | Ngũ trưởng tuần trinh Nghĩa quân | Lão binh ngoài tứ tuần (42 tuổi), da ngăm gió sương, tính tình cương liệt mộc mạc | Côn sắt bọc đồng / Trường đao sa trường | Bị thích khách Tây Hạ chém rách đùi (`INJ-TRD-001` Level 2) khi liều chết ôm chân địch giải cứu Tiêu Phùng tại Miếu Thần Ba Lăng; đã được kỵ binh cứu chữa, hiện tịnh dưỡng | Chương 09 |
+| **Đại Cường** | **C** | Tráng đinh tuần đê Nghĩa quân | Thanh niên khỏe mạnh thuộc ngũ tuần trinh Trương Đỉnh | Giáo tre vạt nhọn, dao găm | Bị thích khách Tây Hạ phóng phi tiêu trúng vai và chém trọng thương tại Miếu Thần; đã được cứu chữa qua cơn nguy kịch | Chương 09 |
+| **Tiểu Lục** | **C** | Tráng đinh tuần đê Nghĩa quân | Thiếu niên mới gia nhập tuần trinh đê điều | Gậy gỗ bịt sắt | Bị chém rách mạn sườn trong lúc tử thủ bảo vệ xe lương cứu tế tại Miếu Thần; đã được đưa về huyện đường tịnh dưỡng | Chương 09 |
```

---

## 4. Đề Xuất Cập Nhật Sổ Cái Bảo Vật (`worldbuilding/artifacts/artifacts_ledger.md`)

```diff
Index: worldbuilding/artifacts/artifacts_ledger.md
===================================================================
--- worldbuilding/artifacts/artifacts_ledger.md
+++ worldbuilding/artifacts/artifacts_ledger.md
@@ -25,5 +25,8 @@
 ### B. Vô Danh Mật Tịch (Cuốn da dê quân cơ cổ)
-* **Vị trí hiện tại:** Chuyển từ thạch thất cơ quan lên cất giữ tạm thời tại Miếu Thần Ba Lăng sau trận lũ.
+* **Vị trí hiện tại:** Được bảo vệ toàn vẹn sau trận huyết chiến Miếu Thần Ba Lăng (Chương 09); Bạch Thu Lâm đã thu hồi về đại doanh Nghĩa quân bảo mật tối thượng.
 * **Bản chất xác thực:** Bản đồ phối trí trận đồ cơ quan ngoại vi của toàn bộ hệ thống Trụ Thần Thạch xung quanh Động Đình Hồ do Tiêu Lăng Phong khảo sát mười năm; các tọa độ kinh vĩ đều bị mã hóa, bắt buộc phải có từ trường địa cực của khối hung ngọc Du Long Giác dẫn đường mới giải mã được.
```

---

## 5. Đề Xuất Cập Nhật Ma Trận Quan Hệ (`worldbuilding/factions/relationships_matrix.md`)

```diff
Index: worldbuilding/factions/relationships_matrix.md
===================================================================
--- worldbuilding/factions/relationships_matrix.md
+++ worldbuilding/factions/relationships_matrix.md
@@ -60,3 +60,7 @@
+| **REL-NQ-TH-001** | **Nghĩa Quân Ba Lăng** $\leftrightarrow$ **Tây Hạ Nhất Phẩm Đường** |
+  - *Trạng thái:* `HOSTILE / CLANDESTINE ASSAULT` (Thích sát & Tập kích bất thành).
+  - *Mô tả:* Mật thám Nhất Phẩm Đường mang đoản trùy và đao mỏng tập kích Miếu Thần Ba Lăng hòng cướp đoạt Vô Danh Mật Tịch; toán giặc bị Bạch Thu Lâm và nghĩa quân tiêu diệt toàn bộ; danh tính Tây Hạ bị bóc trần (Chương 09).
```

---

## 6. Đề Xuất Cập Nhật Bảng Theo Dõi Lời Hứa Cốt Truyện (`plot/promises_tracker.md`)

```diff
Index: plot/promises_tracker.md
===================================================================
--- plot/promises_tracker.md
+++ plot/promises_tracker.md
@@ -12,4 +12,4 @@
 | **TH-001** | **Thân thế cha Tiêu Phùng & Dấu tích Ma Y Cốc** | Chương 01 | Tiêu Phùng | Chương 04b nhận khánh bạc; Chương 05 trùng phùng Bạch Cương; Chương 09 đối soát sấm thi với Vô Danh Mật Tịch | **Quyển 2** | `ADVANCED / HIGH ENGAGEMENT` |
@@ -20,3 +20,3 @@
-| **TH-009** | **Bài Sấm Thi 4 câu & Bí mật Long Cung** | Chương 05 | Tiêu Phùng / Bạch Cương | Bạch Cương giải mã 4 câu sấm thi Tiêu Lăng Phong để lại; mở ra đầu mối Du Long Giác | **Hồi 2 & Hồi 3** | `OPENED / CORE MYSTERY` |
+| **TH-009** | **Bài Sấm Thi 4 câu & Bí mật Long Cung** | Chương 05 | Tiêu Phùng / Bạch Cương / Thu Di | Thu Di mở Vô Danh Mật Tịch giải mã chữ "Long Cung" chỉ hung ngọc Du Long Giác, chìa khóa Trụ Thần Thạch (Ch.09) | **Hồi 2 & Hồi 3** | `ADVANCED / CORE MYSTERY` |
@@ -22,3 +22,3 @@
-| **TH-011** | **Hành trình Cái Bang Yến Tử Ổ & Mối liên hệ Thạch Hiên Viên** | Chương 06 | Tiêu Phùng / Tĩnh Xuyên / Cầu Chỉ Thủy | Thiết Tâm bí mật gửi mật thư cho Thạch Hiên Viên đón Cầu Chỉ Thủy sang Yến Tử Ổ tị nạn (Ch.07b); chuẩn bị tao ngộ với Tiêu Phùng | **Chương 14 & 15** | `ADVANCED / STRATEGIC BRIDGE` |
+| **TH-011** | **Hành trình Cái Bang Yến Tử Ổ & Mối liên hệ Thạch Hiên Viên** | Chương 06 | Tiêu Phùng / Tĩnh Xuyên / Cầu Chỉ Thủy | Thu Di chính thức trao phong thư tiến cử gửi Thạch Hiên Viên cử Tiêu Phùng sang Yến Tử Ổ (Ch.09); kích hoạt hành trình xuất sơn | **Chương 12 & 15** | `ADVANCED / EXPEDITION ACTIVATED` |
@@ -25,3 +25,3 @@
-| **TH-014** | **Dấu vết Chùy gai Lục giác & Mật vụ Tây Hạ tại Điền Trì** | Chương 08a | Hạ Nương | Trực tiếp giáp mặt và tiêu diệt toán Hồng Y & Tử Y Đầu Mục Nhất Phẩm Đường tại tâm trận Bát Quái (Ch.08b) | **Chương 13** | `PAID OFF IN SKIRMISH / WAR ESCALATION` |
+| **TH-014** | **Mạng lưới mật vụ Tây Hạ Nhất Phẩm Đường (Điền Trì & Động Đình)** | Chương 08a | Hạ Nương / Tiêu Phùng | Tiêu diệt toán Hồng Y & Tử Y tại Thúy Yên (Ch.08b); tiêu diệt toán thích khách đoản trùy sa mạc tại Miếu Thần Ba Lăng (Ch.09) | **Hồi 2 & Hồi 3** | `CONFIRMED MULTI-FRONT THREAT` |
```

---

## 7. Đề Xuất Cập Nhật Biên Niên Sử (`plot/timeline.md`)

```diff
Index: plot/timeline.md
===================================================================
--- plot/timeline.md
+++ plot/timeline.md
@@ -57,2 +57,2 @@
-  * *Ba Lăng Huyện (1191-08-20):* Thích khách đột nhập miếu cổ ven sông cướp Vô Danh Mật Tịch (`Task Arc 00: Subtask 5–8`). Tiêu Phùng cùng nghĩa quân tử chiến bảo vệ bí tịch.
+  * *Ba Lăng Huyện (1191-08-20 Chiều muộn đến 1191-08-21 Canh ba):* Mật thám Tây Hạ Nhất Phẩm Đường tập kích Miếu Thần Ba Lăng cướp *Vô Danh Mật Tịch*. Tổ tuần trinh nghĩa quân Trương Đỉnh tử thủ; Tiêu Phùng liều mình giấu tráp bị đá gãy nẹp tre hộc máu bầm; Bạch Thu Lâm dẫn kỵ binh phá cửa bắn tên tiêu diệt toàn bộ quân thù; khám nghiệm tử thi nhận diện Tây Hạ Nhất Phẩm Đường; mở tráp đối soát Vô Danh Mật Tịch với 4 câu sấm thi của Tiêu Lăng Phong về Trụ Thần Thạch và hung ngọc Du Long Giác; Thu Di trao phong thư tiến cử cử Tiêu Phùng sang Cái Bang Yến Tử Ổ (`Task Arc 00: Subtask 5–8` & `Task 157: Subtask 320–323` — **Chương 09 đã canon hóa**).
```

---

## 8. Đề Xuất Cập Nhật Outline Deck (`plot/volume_01_deck.md`)

```diff
Index: plot/volume_01_deck.md
===================================================================
--- plot/volume_01_deck.md
+++ plot/volume_01_deck.md
@@ -45,1 +45,1 @@
-| **09** | *Huyết Chiến Miếu Cổ* | **Tiêu Phùng** | Core Plot | Miếu Thần Ba Lăng | Hắc y nhân tập kích miếu cổ Ba Lăng hòng cướp Vô Danh Mật Tịch; Tiêu Phùng vung đoản côn gỗ nghiến cùng nghĩa quân tử chiến giữ bí tịch; nhận ra võ công đối phương mang hơi hướng Tây Hạ. | `Task Arc 00: Subtask 5–8`<br>(*Bảo Vệ Mật Tịch*) |
+| **09** | *Huyết Chiến Miếu Cổ* | **Tiêu Phùng** | Core Plot | Miếu Thần Ba Lăng | Thích khách Tây Hạ Nhất Phẩm Đường tập kích Miếu Thần cướp Vô Danh Mật Tịch; tổ tuần trinh Trương Đỉnh tử thủ; Tiêu Phùng giấu tráp bị đá gãy nẹp tre hộc máu; Thu Di dẫn kỵ binh tiếp viện bắn tên diệt giặc; giải mã Vô Danh Mật Tịch khớp với sấm thi Tiêu Lăng Phong về Trụ Thần Thạch; Thu Di trao thư tiến cử Tiêu Phùng sang Cái Bang Yến Tử Ổ. *(ĐÃ CANON HÓA)* | `Task Arc 00: Subtask 5–8`<br>(*Bảo Vệ Mật Tịch*) |
```

---

## 9. Quyết Định & Chỉ Thị Của Tác Giả (Cổng Dừng Cứng 3)

- [x] Phê chuẩn toàn văn Đề xuất Canon Diff Chương 09 (Tác giả đã duyệt lúc 19:12 ngày 07/09/2026).
- *(Đã hoàn tất commit toàn diện vào 4 Trụ Cột Sổ cái bền vững theo đúng SOLID Workflow Protocol).*
