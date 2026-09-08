# Đề Xuất Canon Diff: Chương 07b — Thạch Ngục Đối Bí

> **Cơ quan quản lý**: Novel OS State Ledger  
> **Trạng thái**: Chờ Tác giả xem xét và phê chuẩn trước khi commit vào Sổ cái trạng thái bền vững (Cổng Dừng 3).

---

## 1. Tóm Tắt Biến Chuyển Cốt Truyện & Nhân Vật (Narrative Summary)

- **POV**: Tĩnh Xuyên (20 tuổi — Dũng sĩ thiết giáp, Thanh Loa Đảo).
- **Thời gian**: Canh tư rạng sáng đến buổi sáng ngày 1191-08-19.
- **Biến cố sa trường & Đối chất chính trị cốt tử**:
  - Tĩnh Xuyên vượt qua hàng rào lính canh thiết vệ của phái Lâu Nhất Quan bằng lệnh bài Bang chủ, thâm nhập Thạch ngục bờ đông ngập mùi tử khí và tiếng sóng ngầm rền rĩ;
  - Đối diện Trưởng lão Cầu Chỉ Thủy bị cùm chân sắt năm mươi cân (`INJ-CCT-001`) nhưng vẫn ngồi thẳng như bàn thạch nhai trầu muối;
  - Tĩnh Xuyên đặt ngọn Xước Đao mạ bạc và bản tự khai của Tôn Báo lên bàn đá, chất vấn thẳng thắn bằng chứng cứ vật lý: chuyến thuyền nan 6 hòm kín rời bến đông và con dấu phân đà Ích Dương;
  - Cầu Chỉ Thủy bật cười rung chuyển thạch thất, bóc trần sự thật cay đắng:
    + Sáu chiếc hòm bí mật chứa 60 bao muối hột và 20 bao gạo khô do lão trích bổng lộc đi cứu đói gia quyến nghĩa sĩ Động Đình tử trận ở cù lao bãi sậy phía đông — việc Lâu Nhất Quan từng nhiều lần bác bỏ;
    + Thích khách Tôn Báo là con côi của Tôn Đại Lực — người lính thiết giáp từng lấy thân mình đỡ ba ngọn giáo cứu mạng lão tại bến Ba Lăng năm xưa;
    + Kẻ thù giấu mặt đã tính toán tinh vi, dùng chính lòng trắc ẩn của lão để biến thành chiếc thòng lọng siết cổ nhằm kích động nội chiến làm tê liệt Thiên Vương Bang;
  - Cầu lão truyền dạy cho Tĩnh Xuyên bài học chính trị đỉnh cao, chủ động yêu cầu Tân Bang chủ: *"Hãy công khai TRỤC XUẤT ta khỏi đảo!"* để dẹp yên phe Lâu Nhất Quan, giữ vững ghế bang chủ và nhử địch lộ diện;
  - Canh năm tại Mật thất Hành dinh: Dương Thiết Tâm và Bùi Dực Phi nghẹn ngào trước tấm lòng trung liệt của Cầu lão; Thiết Tâm quyết định tương kế tựu kế: ra lệnh trục xuất công khai, nhưng bí mật viết thư gửi Bang chủ Cái Bang Thạch Hiên Viên đón Cầu lão sang Yến Tử Ổ lánh nạn (khớp nối hoàn hảo với `Task 2`);
  - Tiền sảnh rạng sáng: Thiết Tâm tuyên bố phán quyết tước chức, trục xuất Cầu Chỉ Thủy khỏi đảo; Lâu Nhất Quan thu đao chấp thuận; nguy cơ nội chiến được dập tắt;
  - Bến nam đón đệ tử Phân đà Thành Đô vượt 800 dặm bằng thuyền nan rách nát, kiệt sức thổ huyết (`INJ-TD-001`), trao ống đồng niêm phong sáp đỏ hình chim ưng;
  - Mật thư hé lộ tin tức sét đánh ngang tai: **"Thúy Yên Môn tại Điền Trì đã khai quật được hung ngọc Du Long Giác! Thiên hạ đại loạn!"**;
  - Thiết Tâm giác ngộ đòn nghi binh của kẻ thù: Vụ án ám sát Lâu Nhất Quan nhằm kìm chân Thiên Vương Bang để rảnh tay tranh đoạt Du Long Giác ở Tây Nam;
  - Thiết Tâm hạ lệnh cho Thống lĩnh Cáp Xá Bùi Dực Phi dẫn đầu 30 kỵ mã tinh anh xuất chinh rời đảo hỏa tốc đi Tây Nam; giao quyền chỉ huy phòng tuyến bờ kè và bến đảo cho Tĩnh Xuyên;
  - Dư ba Kim Dung: Ngọn Bát Hàn Thiết Thương cắm trên cát ướt, cánh buồm đen khuất trong sương sớm, mặt trời đỏ như máu nhô lên từ sóng nước Động Đình bao la.

---

## 2. Đề Xuất Cập Nhật Sổ Cái Thương Tật (`worldbuilding/medical/injuries_ledger.md`)

```diff
Index: worldbuilding/medical/injuries_ledger.md
===================================================================
--- worldbuilding/medical/injuries_ledger.md
+++ worldbuilding/medical/injuries_ledger.md
@@ -70,3 +70,18 @@
 | **INJ-TB-001** | Bàn tay phải: Gãy trẹo ngón tay trỏ; khắp ngực và lưng chằng chịt lằn roi gân bò rách da ứa máu; trán bầm dập do dập đầu xuống sàn đá. | **L1** (Nhẹ) | Bị thị vệ tước đao bẻ gãy ngón tay khi bắt sống; bị thẩm vấn tra khảo dưới hầm đá nghị sự đường. | Chương 07a | **BỊ GIAM GIỮ**. Đang bị trói nghiến vào cột lim hầm ngục. | Mất khả năng cầm nắm vũ khí tay phải; đau đớn thể xác khiến tinh thần hoảng loạn nhưng lời khai vẫn rập khuôn theo bài mớm cung. |
+
+### G. Cầu Chỉ Thủy (Trưởng lão cựu thần Thiên Vương Bang)
+
+| Vết thương # | Vị trí & Dạng tổn thương | Cấp độ | Tác nhân / Hoàn cảnh | Hồi xuất hiện | Trạng thái hiện tại | Di chứng & Ảnh hưởng hành vi |
+| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
+| **INJ-CCT-001** | Cổ chân trái & Khớp gối hai chân: Cổ chân bị cùm sắt 50 cân cọ xát rách da tụ máu bầm tím; khớp gối viêm thoái hóa tái phát do ẩm lạnh ngục ngầm. | **L1** (Nhẹ / Viêm khớp) | Bị biệt giam bằng xích sắt nặng trong Thạch ngục bờ đông ngập nước mặn Động Đình. | Chương 07b | **ĐÃ GIẢI CÙM & DI CHUYỂN**. Được Cáp Xá tháo cùm sắt để áp giải rời đảo. | Bước chân tập tễnh, đau buốt khớp gối khi trời mưa lạnh; cần dầu xoa bóp thảo dược khi chuyển sang Cái Bang Yến Tử Ổ; thể lực lão tướng vẫn dồi dào. |
+
+### H. Đệ tử Phân đà Thành Đô (Liên lạc viên Cáp Xá Tây Nam)
+
+| Vết thương # | Vị trí & Dạng tổn thương | Cấp độ | Tác nhân / Hoàn cảnh | Hồi xuất hiện | Trạng thái hiện tại | Di chứng & Ảnh hưởng hành vi |
+| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
+| **INJ-TD-001** | Toàn thân: Kiệt sức hoàn toàn, suy kiệt tạng phủ, thổ huyết đen ứ đọng; da thịt tím tái do ngấm mưa lạnh nhiều ngày; lưng dính vết chém khô máu. | **L2** (Trung bình / Suy kiệt) | Vượt 800 dặm đường trường, cưỡi chết 3 tuấn mã, chèo thuyền nan vượt bão Động Đình dưới sự truy sát của mật thám giặc. | Chương 07b | **ĐANG CẤP CỨU**. Đã chuyển về dược phòng thủy trại hồi sức. | Hôn mê bất tỉnh sau khi trao mật thư; mất 7–10 ngày dùng sâm nhung bổ khí huyết mới có thể bình phục; không nguy hiểm đến tính mạng nếu được chăm sóc kịp thời. |
```

---

## 3. Đề Xuất Cập Nhật Sổ Động Thái Võ Học (`worldbuilding/martial/martial_dynamics.md`)

```diff
Index: worldbuilding/martial/martial_dynamics.md
===================================================================
--- worldbuilding/martial/martial_dynamics.md
+++ worldbuilding/martial/martial_dynamics.md
@@ -79,2 +79,8 @@
   - **Kế thừa thể trạng**: Khớp bả vai phải vẫn còn dư chấn ê ẩm từ cuộc tỷ võ khảo nghiệm với Dương Thiết Tâm (Chương 02b); thể lực tiêu hao sau ca tuần tra dầm mưa bão.
+  - **Tiến trình võ học tại Chương 07b (Đốn ngộ Tâm thuật Giang hồ & Khí phách Sa trường)**:
+    - **Tâm thuật sa trường**: Tiếp nhận khẩu quyết và bản lĩnh điềm tĩnh trước cái chết từ Trưởng lão Cầu Chỉ Thủy; nhận thức được ranh giới giữa "Võ dũng đâm chém" và "Mưu lược chính trị".
+    - **Nhãn quan toàn cục**: Thấu hiểu đòn nghi binh chiến lược của kẻ thù giấu mặt (dùng nội biến Thanh Loa để kìm chân Thiên Vương Bang); nâng tầm tư duy từ một dũng sĩ tiền phong thành người chỉ huy phòng tuyến hậu phương.
```

---

## 4. Đề Xuất Cập Nhật Hồ Sơ Nhân Vật Tĩnh Xuyên (`characters/tinh_xuyen.md`)

```diff
Index: characters/tinh_xuyen.md
===================================================================
--- characters/tinh_xuyen.md
+++ characters/tinh_xuyen.md
@@ -80,4 +80,4 @@
 ## 7. SỔ CÁI TRẠNG THÁI HIỆN HÀNH (DURABLE STATE LEDGER)
-* **Mốc thời gian hiện hành:** 1191-08-19 (Canh tư rạng sáng — Sau Chương 07a).
+* **Mốc thời gian hiện hành:** 1191-08-19 (Buổi sáng rạng đông — Sau Chương 07b).
 * **Thể trạng thực tế:** Thể lực mỏi mệt sau ca tuần tra đêm dầm mưa bão; khớp bả vai phải còn dư chấn ê ẩm nhẹ từ trận tỷ võ Chương 02b; không mang thương tật nặng.
 * **Binh khí & Trang bị:**
@@ -87,4 +87,5 @@
 * **Vị thế & Quan hệ nội bộ:**
-  - Được Dương Thiết Tâm tin cẩn tuyệt đối, xem như "tai mắt độc lập" ngoài vòng kiềm tỏa của hai phe Lâu Nhất Quan và Quý Thúc Ban; nhận mật lệnh một mình xuống Thạch ngục bờ đông điều tra.
-  - Phối hợp ăn ý với Thống lĩnh Cáp Xá Bùi Dực Phi trong nghiệp vụ khám nghiệm pháp y sa trường.
-  - Nhận thức sâu sắc nỗi đau xé lòng và sự bế tắc chính trị của thế hệ cựu thần khởi nghĩa nông dân.
+  - Trở thành chỉ huy trưởng hệ thống tuần phòng bờ kè và chốt trinh sát bến cảng Thanh Loa Đảo khi Bùi Dực Phi xuất chinh Tây Nam.
+  - Hoàn thành xuất sắc nhiệm vụ đối chất thạch ngục; chiếm trọn niềm tin cẩn của Tân Bang chủ Dương Thiết Tâm.
+  - Nhận được sự kính trọng và lời chúc phúc chân thành từ Trưởng lão Cầu Chỉ Thủy.
 * **Tri thức & Thông tin nắm giữ:**
@@ -93,4 +94,5 @@
+  - Biết rõ toàn bộ chân tướng án oan của Cầu Chỉ Thủy (chuyến thuyền 6 hòm muối gạo cứu tế tử sĩ và ân tình với Tôn Đại Lực).
+  - Biết cơ mật phán quyết "trục xuất": Cầu lão được bí mật hộ tống sang Cái Bang Yến Tử Ổ tị nạn an toàn.
+  - Biết tin tức chấn động toàn cõi giang hồ: **Ngọc Du Long Giác phát lộ tại Thúy Yên Môn (Đại Lý)**; Bùi Dực Phi dẫn 30 kỵ mã Cáp Xá xuất chinh thám thính.
 * **Ranh giới cấm kỵ (Forbidden Unknowns):**
-  - Hoàn toàn CHƯA BIẾT bí mật về chuyến thuyền đêm chở 6 hòm lương của Cầu Chỉ Thủy (sẽ giải mã ở Chương 07b).
-  - CHƯA BIẾT tin tức về hung ngọc Du Long Giác xuất hiện tại Thúy Yên Môn (sẽ cập bến ở cuối Chương 07b).
+  - Chưa biết kẻ giấu mặt mua chuộc Tôn Báo là toán mật thám Kim quốc (mạng lưới Ô Sơ Sa / Thiên Nhẫn Giáo) cấu kết gian tế địa phương.
+  - Chưa biết hiểm họa đẫm máu mà Thúy Yên Môn và Hạ Nương sắp sửa gánh chịu tại Bách Hoa Cốc.
+  - Chưa biết sự hiện diện của Tiêu Phùng tại Ba Lăng Huyện và mối dây liên kết chung về ngọc Du Long Giác.
```

---

## 5. Đề Xuất Cập Nhật Sổ Cái Vật Phẩm & Khí Giới (`worldbuilding/artifacts/artifacts_ledger.md`)

```diff
Index: worldbuilding/artifacts/artifacts_ledger.md
===================================================================
--- worldbuilding/artifacts/artifacts_ledger.md
+++ worldbuilding/artifacts/artifacts_ledger.md
@@ -25,2 +25,3 @@
 | **Xước Đao mạ bạc Ngũ Lăng** | Đoản đao dài 8 tấc, sống đao khắc 3 vạch sóng nước (lò rèn Ngũ Lăng, Thục Trung); tẩm độc thảo ô pha hàn băng thạch màu xanh đen | **Tĩnh Xuyên** (giữ vật chứng) | Đáy giỏ mây tre của Tĩnh Xuyên | Bùi Dực Phi nhỏ giấm thanh thử độc để lại vệt xám; đang mang xuống Thạch ngục bờ đông để đối chất | Chương 07a |
 | **Giỏ quả mây tre Hành Dinh** | Giỏ mây tre đựng hoa quả khô (hồng sấy, vải khô), đáy lót vải thô giấu Xước Đao và mật thư | **Tĩnh Xuyên** | Trên tay Tĩnh Xuyên | Đẫm nước mưa đêm bão; đạo cụ ngụy trang chuyển giao vật chứng điều tra nội bộ | Chương 07a |
+| **Ống đồng niêm phong sáp ưng Phân đà Thành Đô** | Ống đồng dài 1 thước, nắp đúc ren vặn, niêm phong sáp đỏ in hình chim ưng tung cánh; bên trong chứa cuộn giấy dầu mật thư viết bằng mực pha máu báo tin Du Long Giác phát lộ tại Thúy Yên Môn | **Dương Thiết Tâm** | Nội sảnh Hành dinh Thanh Loa | Đã bẻ gãy niêm phong sáp đỏ lấy thư mật; đệ tử Thành Đô bàn giao cho Bang chủ | Chương 07b |
```

---

## 6. Đề Xuất Cập Nhật Lần Vết Hứa Hẹn (`plot/promises_tracker.md`)

```diff
Index: plot/promises_tracker.md
===================================================================
--- plot/promises_tracker.md
+++ plot/promises_tracker.md
@@ -14,2 +14,2 @@
-| **TH-003** | **Mối nghi kỵ chia rẽ ngầm của Lâu Nhất Quan** | Chương 02b | Tĩnh Xuyên | Lâu Nhất Quan bị thích khách ám sát hụt trong đêm bão; đòi chém đầu Cầu Chỉ Thủy; ra tối hậu thư 3 ngày cho Thiết Tâm (Ch.07a) | **Chương 07a & 07b** | `ADVANCED / HIGH CRISIS` (Khủng hoảng chính trị bùng nổ) |
+| **TH-003** | **Mối nghi kỵ chia rẽ ngầm của Lâu Nhất Quan** | Chương 02b | Tĩnh Xuyên | Thiết Tâm ban lệnh trục xuất Cầu Chỉ Thủy; Lâu Nhất Quan thu đao chấp nhận bang quy; nguy cơ nội chiến tạm thời được dập tắt (Ch.07b) | **Chương 07b** | `RESOLVED / TEMPORARILY MANAGED` (Kiểm soát thành công) |
@@ -15,2 +15,2 @@
-| **TH-004** | **Sự tin cậy của Dương Thiết Tâm với Tĩnh Xuyên** | Chương 02b | Tĩnh Xuyên | Điểm thương chỉ điểm kiếm ý Côn Lôn; giao trọng trách điều tra độc lập, trao giỏ quả giấu vật chứng xuống Thạch ngục bờ đông (Ch.07a) | **Chương 07b & Chương 10** | `ADVANCED / INNER CIRCLE` (Thân tín cơ mật) |
+| **TH-004** | **Sự tin cậy của Dương Thiết Tâm với Tĩnh Xuyên** | Chương 02b | Tĩnh Xuyên | Tĩnh Xuyên hoàn thành xuất sắc nhiệm vụ đối chất; Thiết Tâm giao toàn bộ tuyến phòng thủ bờ kè và trinh sát bến cảng đảo cho chàng khi Cáp Xá xuất chinh (Ch.07b) | **Chương 10** (*Hình Thiên Lĩnh*) & **Chương 14** | `ADVANCED / PILLAR OF DEFENSE` (Trụ cột phòng thủ) |
@@ -22,2 +22,3 @@
-| **TH-011** | **Hành trình Cái Bang Yến Tử Ổ & Mối liên hệ Thạch Hiên Viên** | Chương 06 | Tiêu Phùng / Bạch Thu Lâm | Bạch Thu Lâm viết thư tiến cử Tiêu Phùng lên đường tới Yến Tử Ổ bái sư nhập môn Cái Bang (Task 2) | **Chương 07 – 10** | `PLANTED / TRANSITION TO ARC 02` |
+| **TH-011** | **Hành trình Cái Bang Yến Tử Ổ & Mối liên hệ Thạch Hiên Viên** | Chương 06 | Tiêu Phùng / Tĩnh Xuyên / Cầu Chỉ Thủy | Thiết Tâm bí mật gửi mật thư cho Thạch Hiên Viên đón Cầu Chỉ Thủy sang Yến Tử Ổ tị nạn (Ch.07b); chuẩn bị tao ngộ với Tiêu Phùng | **Chương 14 & 15** | `ADVANCED / STRATEGIC BRIDGE` (Cầu nối liên bang phái) |
+| **TH-013** | **Chiến dịch thám thính Du Long Giác tại Tây Nam của Bùi Dực Phi** | Chương 07b | Bùi Dực Phi / Tĩnh Xuyên | Nhận mật thư từ đệ tử Thành Đô, Bùi Dực Phi dẫn 30 kỵ mã Cáp Xá xuất chinh đi Điểm Thương Sơn / Thúy Yên Môn thám thính hung ngọc | **Hồi 2 (Chương 08–13)** | `PLANTED / CORE EXPEDITION` (Xuất chinh Tây Nam) |
```

---

## 7. Đề Xuất Cập Nhật Dòng Thời Gian (`plot/timeline.md`)

```diff
Index: plot/timeline.md
===================================================================
--- plot/timeline.md
+++ plot/timeline.md
@@ -52,3 +52,3 @@
-* **Ngày 19–20 tháng 8:**
-  * *Thanh Loa Đảo (1191-08-19 Rạng sáng):* Tĩnh Xuyên đối chất Cầu Chỉ Thủy trong thạch ngục bờ đông, bóc trần bi kịch lòng trắc ẩn; Thiết Tâm hạ lệnh trục xuất Cầu lão sang Cái Bang nương náu; đệ tử Phân đà Thành Đô vượt 800 dặm mang mật thư báo tin **Du Long Giác** tái xuất tại Thúy Yên Môn; Bùi Dực Phi xuất chinh Tây Nam (`Task 1: Subtask 2 Step 3–7` — **Chương 07b sắp tới**).
+* **Ngày 19 tháng 8:**
+  * *Thanh Loa Đảo (1191-08-19 Rạng sáng & Sáng sớm):* Tĩnh Xuyên thâm nhập Thạch ngục bờ đông đối chất Cầu Chỉ Thủy bằng Xước Đao và bản tự khai; Cầu lão bóc trần sự thật về chuyến thuyền 6 hòm lương cứu tế tử sĩ và ân tình cha con Tôn Báo; Cầu lão hiến kế trục xuất; Thiết Tâm tuyên bố tước chức trục xuất Cầu lão trước toàn bang để dẹp yên phe Lâu Nhất Quan, bí mật gửi thư cho Thạch Hiên Viên đón Cầu lão sang Cái Bang Yến Tử Ổ tá túc an toàn; bến nam đón đệ tử Phân đà Thành Đô kiệt sức trao mật thư báo tin hung ngọc **Du Long Giác** tái xuất tại Thúy Yên Môn; Thiết Tâm giác ngộ kế nghi binh, lệnh Bùi Dực Phi dẫn 30 kỵ mã Cáp Xá xuất chinh Tây Nam; giao quyền chỉ huy phòng thủ đảo cho Tĩnh Xuyên (`Task 1: Subtask 2 Step 3–7` — **Chương 07b đã canon hóa**).
```

---

## 8. Đề Xuất Cập Nhật Danh Bạ Nhân Vật Phụ (`characters/supporting_cast.md`)

```diff
Index: characters/supporting_cast.md
===================================================================
--- characters/supporting_cast.md
+++ characters/supporting_cast.md
@@ -38,2 +38,4 @@
+| **Cầu Chỉ Thủy** | **A/B** | Cựu Trưởng lão khai quốc công thần | Lão nhân 60 tuổi, râu tóc muối tiêu, ngực vạm vỡ chằng chịt sẹo đao kiếm sa trường; tính tình bộc trực, nóng nảy nhưng trọng đại nghĩa và giàu lòng trắc ẩn; hay nhai trầu muối đỏ tươi | Đao thuật sa trường / Khẩu quyết điều tức Động Đình Quy Tức Công | Mang thương tích `INJ-CCT-001` Level 1 (cổ chân trái rách da tụ máu do cùm sắt 50 cân, đau nhức khớp gối ngục tối); được Dương Thiết Tâm dùng kế trục xuất để bảo toàn tính mạng và sang Cái Bang Yến Tử Ổ tị nạn | Chương 07a, 07b |
+| **Đệ tử Phân đà Thành Đô** | **C** | Kỵ trinh Phân đà Thành Đô | Thanh niên ngoài đôi mươi (~25 tuổi), da thịt tím tái dầm mưa gió nhiều ngày; kiên cường trung nghĩa | Kỵ mã đường trường / Ống đồng niêm sáp ưng mật thư | Mang chấn thương `INJ-TD-001` Level 2 (kiệt sức, sốt lạnh và thổ huyết); đã chuyển giao mật thư Du Long Giác cho Dương Thiết Tâm; đang tịnh dưỡng tại quân doanh bến nam | Chương 07b |
 | **Bùi Dực Phi** | **A/Anchor** | Thống lĩnh Cáp Xá / Kỵ tướng Thiên Vương | Giáp trụ xám tro, cưỡi chiến mã đen tuyền; phong thái cương nghị sa trường (đã lập hồ sơ riêng `anchors/bui_duc_phi.md`) | Đại kích sa trường, tài cưỡi ngựa bắn cung | Nhận mệnh Dương Anh dẫn 30 thiết kỵ xuất phát sang Tây Nam (Thúy Yên Môn) hộ tống quân lương cứu tế và điều tra cổ án Ma Y Cốc | Chương 07b |
```

---

## 9. PHÊ DUYỆT TỪ TÁC GIẢ (AUTHOR APPROVAL)

- [x] **accept all** (Đã đồng bộ kiểm toán theo Ground Truth bản thảo Chương 07b)
- [ ] accept selected only
- [ ] reject
