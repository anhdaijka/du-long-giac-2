# Đề Xuất Canon Diff: Chương 07a — Ám Toán Trong Đêm

> **Cơ quan quản lý**: Novel OS State Ledger  
> **Trạng thái**: Chờ Tác giả xem xét và phê chuẩn trước khi commit vào Sổ cái trạng thái bền vững (Cổng Dừng 3).

---

## 1. Tóm Tắt Biến Chuyển Cốt Truyện & Nhân Vật (Narrative Summary)

- **POV**: Tĩnh Xuyên (18 tuổi — Dũng sĩ thiết giáp, Thanh Loa Đảo).
- **Thời gian**: Đêm giông bão 1191-08-18 đến Canh tư rạng sáng 1191-08-19.
- **Biến cố sa trường & Trinh thám pháp y cốt tử**:
  - Tĩnh Xuyên dầm mưa tuần tra bờ tây trở về lều nứa, sắc thuốc ngải cứu đắp ngực cho mẹ già mù lòa Diệp Mẫu; chuông đồng báo biến ba hồi chín tiếng rền vang xé toạc màn mưa đêm; Diệp Mẫu dặn dò giữ vững tâm mắt sa trường;
  - Tĩnh Xuyên mang Bát Hàn Thiết Thương lao lên sườn đồi, tiếp cận hiện trường vụ thích sát hụt Tổng quản Lâu Nhất Quan;
  - Phối hợp cùng Thống lĩnh Cáp Xá Bùi Dực Phi thực hiện khám nghiệm pháp y sa trường tỉ mỉ (Rule 11.7):
    + Đo đạc vết chém trên cột gỗ trắc ở độ cao ba thước sáu tấc, góc chém xốc từ dưới nách lên, thớ gỗ xơ nhẹ xác định hung khí là Xước Đao mạ bạc dài tám tấc chuyên dùng ám toán cận thân;
    + Bùi Dực Phi nhỏ giấm thanh thử độc: sủi bọt trắng xám mùi củ ấu thối rữa, xác định độc thảo ô kết hợp hàn băng thạch làm đông máu từ từ;
    + Khám nghiệm vết thương bắp tay trái Lâu Nhất Quan dài ba tấc, sưng phù tím tái (`INJ-LNQ-001`);
    + Phát hiện vết bùn đen tanh rêu thối của đáy cọc ngầm bờ kè phía đông, vạch trần đường đột nhập lặn nước qua các chốt canh do phân đà Ích Dương quản lý;
  - Thẩm vấn thích khách Tôn Báo (22 tuổi, phân đà Ích Dương) tại hầm đá nghị sự đường: Tôn Báo bị bắt, gãy ngón trỏ phải (`INJ-TB-001`), khai nhận Cầu Chỉ Thủy là chủ mưu và là Thống lĩnh ngầm mười năm của Thiên Nhẫn Giáo;
  - Tĩnh Xuyên và Tân Bang chủ Dương Thiết Tâm vạch trần ba lỗ hổng chết người trong lời khai mớm cung: Tôn Báo khai quá trơn tru sau vài roi; Cầu lão không đời nào dùng chính đệ tử mình bảo lãnh để tự trói cổ nộp mình; ngọn Xước Đao rèn bằng thép dẻo của phường rèn Ngũ Lăng (Thục Trung) chứ không phải thép Nữ Chân Kim quốc;
  - Xung đột chính trị gay gắt bùng nổ tại Tiền sảnh Hành dinh: Lâu Nhất Quan quấn khăn tay thấm máu, đập vỡ bàn trà gỗ sồi, gầm thét đòi lôi Cầu Chỉ Thủy ra bến chém đầu răn chúng; Quý Thúc Ban can ngăn; đệ tử hai phe tuốt kiếm sắp sửa nội chiến;
  - Dương Thiết Tâm cắm ngập mũi thương sắt ba tấc xuống sàn đá hoa cương nứt toác, dùng uy nghi tướng lĩnh sa trường trấn áp phe phái; ban lệnh tạm giam Cầu Chỉ Thủy xuống Thạch ngục bờ đông, niêm phong doanh trại Ích Dương ba ngày để rà soát nội ứng;
  - Trong mật thất lúc canh tư, Thiết Tâm trao giỏ mây đựng hoa quả khô giấu ngọn Xước Đao vật chứng và bản tự khai mật của Tôn Báo cho Tĩnh Xuyên, lệnh cho chàng một mình thâm nhập Thạch ngục bờ đông đối chất với Cầu Chỉ Thủy để tìm ra chân tướng.

---

## 2. Đề Xuất Cập Nhật Sổ Cái Thương Tật (`worldbuilding/medical/injuries_ledger.md`)

```diff
Index: worldbuilding/medical/injuries_ledger.md
===================================================================
--- worldbuilding/medical/injuries_ledger.md
+++ worldbuilding/medical/injuries_ledger.md
@@ -58,3 +58,18 @@
 | **INJ-GST-001** | Hai gót chân: Đứt lìa gân gót (Achilles), dập nát mắt cá chân, bỏng lạnh do ngâm bùn thạch thất. | **L3** (Nặng) | Bị mật thám công binh giặc Kim tra tấn cắt gân nhằm bức cung chìa khóa cơ quan thạch thất. | Chương 06 | **ĐANG ĐIỀU TRỊ KHẨN CẤP**. Đã được nẹp gỗ sơ cứu và chuyển về y quán Ba Lăng. | Mất vĩnh viễn khả năng đi lại nhanh nhẹn; sau này chỉ có thể chống nạng hoặc ngồi xe đẩy; bàn tay và trí tuệ cơ quan nguyên vẹn. |
+
+### E. Lâu Nhất Quan (Tổng quản cựu thần Thiên Vương Bang)
+
+| Vết thương # | Vị trí & Dạng tổn thương | Cấp độ | Tác nhân / Hoàn cảnh | Hồi xuất hiện | Trạng thái hiện tại | Di chứng & Ảnh hưởng hành vi |
+| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
+| **INJ-LNQ-001** | Bắp tay trái: Vết chém sượt dài ba tấc, rách toạc da thịt, nhiễm độc thảo ô pha hàn băng thạch; mép thịt sưng phù tím tái, rỉ huyết tương lẫn máu đen. | **L1** (Nhẹ / Độc nhẹ) | Bị thích khách Tôn Báo ám toán bằng Xước Đao mạ bạc trong trướng thất đêm giông bão. | Chương 07a | **ĐANG SƠ CỨU**. Đã rịt tro than lá ngải cứu hút độc và quấn băng trắng cố định. | Nhức buốt và giật cơ bắp tay khi cử động mạnh hoặc kích động giận dữ; độc tính làm tê dại nhẹ kinh lạc cánh tay trái trong 3–5 ngày; không nguy hiểm đến tính mạng nhưng kích động tâm lý thù hận cực đoan. |
+
+### F. Tôn Báo (Thích khách / Đệ tử phân đà Ích Dương)
+
+| Vết thương # | Vị trí & Dạng tổn thương | Cấp độ | Tác nhân / Hoàn cảnh | Hồi xuất hiện | Trạng thái hiện tại | Di chứng & Ảnh hưởng hành vi |
+| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
+| **INJ-TB-001** | Bàn tay phải: Gãy trẹo ngón tay trỏ; khắp ngực và lưng chằng chịt lằn roi gân bò rách da ứa máu; trán dập bầm dập do dập đầu xuống sàn đá. | **L1** (Nhẹ) | Bị thị vệ tước đao bẻ gãy ngón tay khi bắt sống; bị thẩm vấn tra khảo dưới hầm đá nghị sự đường. | Chương 07a | **BỊ GIAM GIỮ**. Đang bị trói nghiến vào cột lim hầm ngục. | Mất khả năng cầm nắm vũ khí tay phải; đau đớn thể xác khiến tinh thần hoảng loạn nhưng lời khai vẫn rập khuôn theo bài mớm cung. |
```

---

## 3. Đề Xuất Cập Nhật Sổ Động Thái Võ Học (`worldbuilding/martial/martial_dynamics.md`)

```diff
Index: worldbuilding/martial/martial_dynamics.md
===================================================================
--- worldbuilding/martial/martial_dynamics.md
+++ worldbuilding/martial/martial_dynamics.md
@@ -70,3 +70,12 @@
   - **Chương 06**: Thể nghiệm cơ quan học và dưỡng thể dã chiến thợ thuyền. Giữ nguyên Tier 0, áp dụng trí tuệ đòn bẩy và then khóa cơ hoành vượt qua hiểm cảnh.
+
+### C. Tĩnh Xuyên (Thiên Vương Thiết Kỵ — Bậc Tier 1)
+- **Tiến trình võ học tại Chương 07a (Không đột phá cảnh giới — Nâng tầm Nhãn quan Chiến thuật & Cận chiến Không gian Hẹp)**:
+  - **Nhận diện giới hạn ngọn trường thương**: Qua việc khám nghiệm vết đao chém trên cột trướng thất và cấu tạo Xước Đao dài 8 tấc, Tĩnh Xuyên nhận ra ngọn trường thương dài 1 trượng của mình tuy uy mãnh trên bãi trống trận địa nhưng cực kỳ bất lợi trong không gian chật hẹp (trướng thất, buồng thuyền, ngục ngầm) trước các đòn xốc nách, cắt gân hạ bàn của đoản nhận cận chiến.
+  - **Pháp y khí giới & độc chất sa trường**: Học được từ Bùi Dực Phi phương pháp thử độc dã chiến bằng giấm thanh (nhận diện độc thảo ô hàn băng thạch qua phản ứng sủi bọt xám mùi củ ấu thối); nhận diện dấu vết lò rèn Ngũ Lăng (Thục Trung) qua ký hiệu ba vạch sóng nước trên sống đao.
+  - **Kế thừa thể trạng**: Khớp bả vai phải vẫn còn dư chấn ê ẩm từ cuộc tỷ võ khảo nghiệm với Dương Thiết Tâm (Chương 02b); thể lực tiêu hao sau ca tuần tra dầm mưa bão.
```

---

## 4. Đề Xuất Cập Nhật Hồ Sơ Nhân Vật Tĩnh Xuyên (`characters/tinh_xuyen.md`)

```diff
Index: characters/tinh_xuyen.md
===================================================================
--- characters/tinh_xuyen.md
+++ characters/tinh_xuyen.md
@@ -78,0 +79,20 @@
+
+---
+
+## 7. SỔ CÁI TRẠNG THÁI HIỆN HÀNH (DURABLE STATE LEDGER)
+* **Mốc thời gian hiện hành:** 1191-08-19 (Canh tư rạng sáng — Sau Chương 07a).
+* **Thể trạng thực tế:** Thể lực mỏi mệt sau ca tuần tra đêm dầm mưa bão; khớp bả vai phải còn dư chấn ê ẩm nhẹ từ trận tỷ võ Chương 02b; không mang thương tật nặng.
+* **Binh khí & Trang bị:**
+  - Ngọn Bát Hàn Thiết Thương (khâu sắt cán thương có vết mẻ nhỏ; vừa được Tân Bang chủ mượn cắm ngập ba tấc xuống sàn đá hoa cương sảnh chính chấn áp phe phái).
+  - Áo giáp thiết giáp ướt sũng nước mưa, khoác áo tơi lá cọ rách tơi tả.
+  - Giỏ mây tre đựng hoa quả khô (bên dưới giấu ngọn Xước Đao mạ bạc vật chứng và bản tự khai của thích khách Tôn Báo).
+* **Vị thế & Quan hệ nội bộ:**
+  - Được Dương Thiết Tâm tin cẩn tuyệt đối, xem như "tai mắt độc lập" ngoài vòng kiềm tỏa của hai phe Lâu Nhất Quan và Quý Thúc Ban; nhận mật lệnh một mình xuống Thạch ngục bờ đông điều tra.
+  - Phối hợp ăn ý với Thống lĩnh Cáp Xá Bùi Dực Phi trong nghiệp vụ khám nghiệm pháp y sa trường.
+  - Nhận thức sâu sắc nỗi đau xé lòng và sự bế tắc chính trị của thế hệ cựu thần khởi nghĩa nông dân.
+* **Tri thức & Thông tin nắm giữ:**
+  - Nắm toàn bộ hiện trường vật chứng vụ ám sát: góc chém xốc nách, độc thảo ô hàn tính, dấu vết cọc ngầm bờ đông, đao của thợ rèn Ngũ Lăng (Thục Trung).
+  - Nhận diện bẫy mớm cung của Tôn Báo hòng mượn tay Lâu Nhất Quan tiêu diệt Cầu Chỉ Thủy.
+* **Ranh giới cấm kỵ (Forbidden Unknowns):**
+  - Hoàn toàn CHƯA BIẾT bí mật về chuyến thuyền đêm chở 6 hòm lương của Cầu Chỉ Thủy (sẽ giải mã ở Chương 07b).
+  - CHƯA BIẾT tin tức về hung ngọc Du Long Giác xuất hiện tại Thúy Yên Môn (sẽ cập bến ở cuối Chương 07b).
```

---

## 5. Đề Xuất Cập Nhật Sổ Cái Vật Phẩm & Khí Giới (`worldbuilding/artifacts/artifacts_ledger.md`)

```diff
Index: worldbuilding/artifacts/artifacts_ledger.md
===================================================================
--- worldbuilding/artifacts/artifacts_ledger.md
+++ worldbuilding/artifacts/artifacts_ledger.md
@@ -45,3 +45,13 @@
 | **Chìa Khóa Cửu Môn Thạch Thất** | Xâu 9 chìa khóa bằng đồng thau đúc đặc, cán khắc chữ triện số từ Nhất đến Cửu, gắn vòng sắt non. | Mở 9 cửa đá cự thạch cơ quan điều tiết nước lũ Động Đình. | Cơ quan đại sư Giới Sơn Tông cất giấu trong cối đá buồng rèn. | Tiêu Phùng đoạt lại từ tay tử sĩ Kim, sau trận bàn giao cho nghĩa quân Ba Lăng quản lý. | Chương 06 | **ĐÃ BÀN GIAO NGHĨA QUÂN**. |
+
+### C. Binh Khí & Vật Chứng Sa Trường Thanh Loa Đảo (Chương 07a)
+
+| Tên Khí Giới / Vật Chứng | Đặc Điểm Cấu Tạo & Xuất Xứ | Công Năng / Tính Chất | Người Sở Hữu Ban Đầu | Người Giữ Hiện Tại / Vị Trí | Hồi Xuất Hiện | Trạng Thái Lưu Trữ |
+| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
+| **Xước Đao Mạ Bạc Ngũ Lăng** | Đoản đao dài 8 tấc, lưỡi mạ bạc mỏng nhẹ, sống đao khắc 3 vạch sóng nước (ký hiệu phường rèn Ngũ Lăng, Thục Trung); lưỡi đao tẩm độc thảo ô pha hàn băng thạch màu xanh đen. | Đoản nhận chuyên dụng ám toán cận thân; độc làm đông máu kinh lạc sau 3 canh giờ. | Thích khách Tôn Báo (phân đà Ích Dương). | Giấu dưới đáy giỏ quả mây tre do Tĩnh Xuyên mang theo xuống Thạch ngục bờ đông. | Chương 07a | **VẬT CHỨNG ÁN MẬT**. Đang dùng để đối chất Cầu Chỉ Thủy. |
+| **Giỏ Quả Mây Tre Hành Dinh** | Giỏ đan bằng mây tre rừng Động Đình; bên trên đựng quả hồng khô và vải sấy, bên dưới lót vải thô giấu Xước Đao và mật thư. | Ngụy trang vật chứng điều tra nội bộ tránh tai mắt của phái Lâu Nhất Quan. | Tân Bang chủ Dương Thiết Tâm. | Tĩnh Xuyên cầm trên tay trên đường xuống ngục đá bờ đông. | Chương 07a | **ĐANG SỬ DỤNG**. |
```

---

## 6. Đề Xuất Cập Nhật Lần Vết Hứa Hẹn (`plot/promises_tracker.md`)

```diff
Index: plot/promises_tracker.md
===================================================================
--- plot/promises_tracker.md
+++ plot/promises_tracker.md
@@ -35,7 +35,9 @@
-| `TH-003` | Mối nghi kỵ nội bộ Thiên Vương Bang | Lâu Nhất Quan phản đối Dương Thiết Tâm trên soái hạm (Ch.02a). | **PLANTED** | Khủng hoảng chuyển giao quyền lực giữa cựu thần khởi nghĩa nông dân và tân minh chủ. |
+| `TH-003` | Mối nghi kỵ nội bộ Thiên Vương Bang | Lâu Nhất Quan bị thích khách ám sát hụt trong đêm bão; đòi chém đầu Cầu Chỉ Thủy; ra tối hậu thư 3 ngày cho Thiết Tâm (Ch.07a). | **ADVANCED** | Nguy cơ nội chiến bùng nổ giữa hai phe cựu trào và cấp tiến; thử thách sinh tử cho uy tín của Tân Bang chủ. |
-| `TH-004` | Lòng trung kiên & Trưởng thành của Tĩnh Xuyên | Tĩnh Xuyên được Thiết Tâm chỉ điểm kiếm ý Côn Lôn (Ch.02b). | **ADVANCED** | Chuyển hóa từ người lính chỉ biết vung thương sang người điều tra độc lập có nhãn quan sa trường. |
+| `TH-004` | Lòng trung kiên & Trưởng thành của Tĩnh Xuyên | Tĩnh Xuyên vạch trần 3 mâu thuẫn trong lời khai mớm cung của Tôn Báo; nhận giỏ quả giấu vật chứng một mình xuống Thạch ngục bờ đông (Ch.07a). | **ADVANCED** | Trở thành cánh tay phải tin cẩn độc lập của Dương Thiết Tâm; trực tiếp đối diện với bi kịch chính trị cựu tướng. |
+| `TH-012` | Kẻ giấu mặt giật dây thích khách Tôn Báo | Tôn Báo dùng Xước Đao của thợ rèn Ngũ Lăng (Thục Trung) nhưng khai là người của Thiên Nhẫn Giáo (Ch.07a). | **PLANTED / OPENED** | Kẻ thù nào đang giăng bẫy ly gián hòng làm tê liệt Thiên Vương Bang từ bên trong? |
```

---

## 7. Đề Xuất Cập Nhật Dòng Thời Gian (`plot/timeline.md`)

```diff
Index: plot/timeline.md
===================================================================
--- plot/timeline.md
+++ plot/timeline.md
@@ -48,3 +48,4 @@
 | **1191-08-18 (Đêm)** | Ba Lăng Huyện | Đê quai Ba Lăng & Thạch thất cửu môn | Bão lớn làm nước lũ dâng vỡ đê quai; Tiêu Phùng cùng nghĩa quân giải cứu Giới Sơn Tông, hạ 3 Cơ Quan Nhân Thô, đóng sập 9 cửa cự thạch cứu nguy cho toàn huyện Ba Lăng. (Chương 06) |
+| **1191-08-18 (Đêm) đến 1191-08-19 (Canh tư)** | Thanh Loa Đảo | Trướng thất Lâu Nhất Quan & Tiền sảnh Hành dinh | Thích khách Tôn Báo ám toán hụt Lâu Nhất Quan; Tĩnh Xuyên cùng Bùi Dực Phi khám nghiệm hiện trường; tra vấn bóc trần bẫy mớm cung vu cáo Cầu Chỉ Thủy; khẩu chiến suýt nổ ra nội chiến; Dương Thiết Tâm cắm thương trấn áp, tạm giam Cầu lão xuống Thạch ngục bờ đông; phái Tĩnh Xuyên cầm vật chứng xuống ngục điều tra. (Chương 07a) |
```

---

## Verdict:
**APPROVED FOR AUTHOR REVIEW (TRÌNH TÁC GIẢ DUYỆT ĐỀ XUẤT CANON DIFF Ở CỔNG DỪNG 3)**.
Chỉ khi Tác giả phê chuẩn bản Diff này, Agent mới tiến hành commit các thay đổi vào các file sổ cái bền vững tương ứng.


---

## Supporting Cast Directory (`characters/supporting_cast.md`)
*(Đã đồng bộ chuẩn hóa kiểm toán vào danh bạ nhân vật phụ)*
