# Đề Xuất Canon Diff: Chương 10 — Hình Thiên Lĩnh Huyết Lộ

> **Cơ quan quản lý**: Novel OS State Ledger  
> **Trạng thái**: Chờ Tác giả xem xét và phê chuẩn trước khi commit vào Sổ cái trạng thái bền vững (Cổng Dừng 3).

---

## 1. Tóm Tắt Biến Chuyển Cốt Truyện & Nhân Vật (Narrative Summary)

* **POV**: Tĩnh Xuyên (18 tuổi — Tiền phong Cáp Xá / Chỉ huy trưởng tuần phòng bờ kè Thanh Loa Đảo).
* **Mốc thời gian**: 1191-08-25 (Trưa oi nồng đến Đêm trăng rằm tháng Tám — Cách 6 ngày sau Chương 07b).
* **Địa điểm**: Thanh Loa Đảo (Bến Nam, Tiền sảnh Hành Dinh, Sườn núi & Cửa hang Hình Thiên Lĩnh, Bến đò Thủy Lục).
* **Biến chuyển cốt lõi**:
  1. *Khám nghiệm bến nam*: Tĩnh Xuyên bóc trần dấu vết ngụy trang của thị vệ ngự tiền Lý Tuyền (vết chai kéo cung đại nội, đai lụa cấm quân thêu kim tuyến, vết thương nhiễm trùng mạn sườn `INJ-LT-001` L2), tiếp nhận ống đồng niêm sáp đỏ mang mật chiếu Tống Hiếu Tông từ phủ Tông thất Triệu Nhữ Ngu.
  2. *Quyết sách chính trị trướng sảnh*: Bùng nổ khẩu chiến nảy lửa: Lâu Nhất Quan căm thù triều đình vì mối thù diệt môn Dương Ma, đập bàn làm nứt vảy vết chém bắp tay (`INJ-LNQ-001` L1); Quý Thúc Ban e ngại họa diệt môn; Dương Thiết Tâm phân tích đại cục kháng Kim sống còn, ban bố kế *Điệu Hổ Ly Sơn* (cho kỵ binh cựu trào nghi binh ở bến Thanh Tiễn) và bí mật trao mặt nạ sắt cho Tĩnh Xuyên độc hành phá vây.
  3. *Gặp gỡ Lư Tiếu Bần & Hàn Thác Trụ*: Tĩnh Xuyên thâm nhập bãi chiến trường đẫm máu Hình Thiên Lĩnh, tìm thấy Tuyên phủ sứ Hàn Thác Trụ (39 tuổi) bị phồng rộp bàn chân (`INJ-HTT-001` L1). Đụng độ Bạch Kỳ Chủ Ngũ Độc Giáo Lư Tiếu Bần (Diệu Thủ Không Không); đọc mật chiếu Hiếu Tông, Lư Tiếu Bần ngửa mặt cười vang, bộc lộ khí phách trượng phu không nỡ hại trung thần, ném trả chiếu thư và bảo hộ Hàn đại nhân để Tĩnh Xuyên xông lên phá chốt chặn.
  4. *Huyết chiến cửa hang*: Tĩnh Xuyên vận dụng "Động Đình Quy Tức Công" nín thở ép đan điền, múa Bát Hàn Thiết Thương thành bão lốc gạt sạch châm độc; mượn phản lực vách đá hoa cương đâm gãy khớp vai Viêm Dương Sứ khiến bom lân tinh tự thiêu rụi gã bạo đồ; quét cán sắt chấn nát xương quai xanh hạ gục Lãnh Nguyệt Sứ, giải tỏa huyết lộ.
  5. *Mật ước Lâm An & Dư ba*: Đưa Hàn Thác Trụ xuống bến đò bí mật Thủy Lục bàn giao cho Bang Chúng Kính Trang; Hàn Thác Trụ nắm chặt tay Tĩnh Xuyên lập lời thề đền đáp tại kinh thành Lâm An (`TH-016`); xuồng nan rẽ sương đêm rời đảo; Tĩnh Xuyên tháo mặt nạ sắt đón trăng rằm Động Đình.

---

## 2. Đề Xuất Cập Nhật Sổ Cái Thương Tật (`worldbuilding/medical/injuries_ledger.md`)

```diff
Index: worldbuilding/medical/injuries_ledger.md
===================================================================
--- worldbuilding/medical/injuries_ledger.md
+++ worldbuilding/medical/injuries_ledger.md
@@ -102,6 +102,28 @@
 | **INJ-LNQ-001** | Lâu Nhất Quan | L1 (Nhẹ) | Vết chém sượt bắp tay trái (ba tấc) do đoản đao Tôn Báo; mép thịt phù nề rỉ dịch huyết tương độc thảo ô | Khâu dã chiến, rắc thuốc bột giải độc, băng gạc gai | Tuần 2/3 (Đang lên da non; mép vảy nứt rỉ máu lấm tấm khi lão tức giận đập bàn gỗ lim trướng sảnh ngày 1191-08-25) | Chương 07a, 10 |
 
+<!-- ================================================================================= -->
+<!-- 4. THƯƠNG TẬT KHU VỰC HÌNH THIÊN LĨNH & BẾN THỦY LỤC (CHƯƠNG 10)                  -->
+<!-- ================================================================================= -->
+
+| Mã Thương Tật | Nhân Vật | Cấp Độ (Level) | Bản Chất Giải Phẫu & Cơ Chế Thương Tổn | Phương Pháp Điều Trị / Dược Liệu | Tiến Trình Hồi Phục & Giới Hạn Thực Tế | Chương Xuất Hiện |
+| :--- | :--- | :---: | :--- | :--- | :--- | :---: |
+| **INJ-LT-001** | Lý Tuyền (Thị vệ ngự tiền) | **L2 (Trung bình)** | Vết đâm rách mạn sườn phải dài bốn tấc do đoản đao tẩm độc; nhiễm trùng mô mềm do ngâm nước bùn đầm lầy; bàn chân toác máu kiệt sức | Băng bó dã chiến, rửa nước muối, uống nước đường hồi sức tại trạm tuần tra bến nam | Cần nghỉ ngơi tĩnh dưỡng 3–4 tuần; mất sức chiến đấu tạm thời | Chương 10 |
+| **INJ-HTT-001** | Hàn Thác Trụ (Tuyên phủ sứ) | **L1 (Nhẹ)** | Lòng bàn chân phồng rộp rách da do giày lụa cứa nát trên dốc đá tai mèo; say nắng nhiệt độ cao, môi nứt nẻ | Xé vạt áo tơi băng bó lòng bàn chân, uống nước ngọt làm mát lồng ngực | Hồi phục sau 5–7 ngày nghỉ ngơi trên thuyền nan xuôi dòng | Chương 10 |
```

---

## 3. Đề Xuất Cập Nhật Hồ Sơ Nhân Vật Chính & Bản Lề (Protagonists & Anchors)

```diff
Index: characters/tinh_xuyen.md
===================================================================
--- characters/tinh_xuyen.md
+++ characters/tinh_xuyen.md
@@ -81,17 +81,20 @@
 ## 7. SỔ CÁI TRẠNG THÁI HIỆN HÀNH (DURABLE STATE LEDGER)
-* **Mốc thời gian hiện hành:** 1191-08-19 (Buổi sáng rạng đông — Sau Chương 07b).
-* **Thể trạng thực tế:** Thể lực mỏi mệt sau ca tuần tra đêm dầm mưa bão và chuyến thâm nhập Thạch ngục bờ đông; khớp bả vai phải còn dư chấn ê ẩm nhẹ từ trận tỷ võ Chương 02b; không mang thương tật nặng.
+* **Mốc thời gian hiện hành:** 1191-08-25 (Đêm trăng rằm tháng Tám — Sau Chương 10).
+* **Thể trạng thực tế:** Thể lực sung mãn sau 6 ngày rèn luyện và điều tức "Động Đình Quy Tức Công"; bả vai hết hẳn dư chấn ê ẩm; áo giáp sắt bị lửa liếm sém nhẹ ở góc áo, dính tro than hỏa dược và máu độc (đã lau sạch); không mang thương tật mới.
 * **Binh khí & Trang bị:**
   - Ngọn Bát Hàn Thiết Thương (khâu sắt cán thương có vết mẻ nhỏ; vừa cắm trên bãi cát ướt bến nam khi tiễn đoàn kỵ mã Cáp Xá).
-  - Áo giáp thiết giáp ướt sũng nước mưa, thắt lưng da bò nạm đồng, khoác áo tơi lá cọ.
+  - Chiếc mặt nạ da trâu bọc sắt xám lạnh do Dương Thiết Tâm trao tặng.
+  - Áo giáp thiết giáp nhẹ, thắt lưng da bò nạm đồng, túi lương khô, bầu nước, khăn vải thô.
 * **Vị thế & Quan hệ nội bộ:**
-  - Trở thành chỉ huy trưởng hệ thống tuần phòng bờ kè và chốt trinh sát bến cảng Thanh Loa Đảo khi Bùi Dực Phi xuất chinh Tây Nam.
-  - Hoàn thành xuất sắc nhiệm vụ đối chất thạch ngục; chiếm trọn niềm tin cẩn của Tân Bang chủ Dương Thiết Tâm.
-  - Nhận được sự kính trọng và lời chúc phúc chân thành từ Trưởng lão Cầu Chỉ Thủy.
+  - Hoàn thành xuất sắc nhiệm vụ cơ mật phá vây cứu người; giữ vững vị thế trụ cột sa trường thân tín bậc nhất của Tân Bang chủ Dương Thiết Tâm (TH-004).
+  - Kết giao ân tình sinh tử với Tuyên phủ sứ Nam Tống Hàn Thác Trụ; nhận lời ước hẹn tri ân tại kinh thành Lâm An (TH-016).
+  - Thiết lập mối quan hệ kỳ dị nửa bạn nửa thù với Bạch Kỳ Chủ Ngũ Độc Giáo Lư Tiếu Bần (TH-017).
 * **Tri thức & Thông tin nắm giữ:**
   - Nắm toàn bộ hiện trường vật chứng vụ ám sát: góc chém xốc nách, độc thảo ô hàn tính, dấu vết cọc ngầm bờ đông, đao của thợ rèn Ngũ Lăng (Thục Trung).
   - Biết rõ toàn bộ chân tướng án oan của Cầu Chỉ Thủy (chuyến thuyền 6 hòm muối gạo cứu tế tử sĩ và ân tình với Tôn Đại Lực).
   - Biết cơ mật phán quyết "trục xuất": Cầu lão được bí mật hộ tống sang Cái Bang Yến Tử Ổ tị nạn an toàn.
   - Biết tin tức chấn động toàn cõi giang hồ: **Ngọc Du Long Giác phát lộ tại Thúy Yên Môn (Đại Lý)**; Bùi Dực Phi dẫn 30 kỵ mã Cáp Xá xuất chinh thám thính.
+  - Nắm bắt trực tiếp cuộc khủng hoảng quyền lực tại cung đình Lâm An: mâu thuẫn giữa phái chủ chiến (Hiếu Tông, Triệu Nhữ Ngu, Hàn Thác Trụ) và bè lũ ngoại thích Lý Hoàng hậu; biết rõ bức mật chiếu của Thái Thượng Hoàng.
+  - Biết sự phân hóa tư tưởng bên trong Ngũ Độc Giáo qua hành vi của Lư Tiếu Bần.
 * **Ranh giới cấm kỵ (Forbidden Unknowns):**
   - Chưa biết kẻ giấu mặt mua chuộc Tôn Báo là toán mật thám Kim quốc (mạng lưới Ô Sơ Sa / Thiên Nhẫn Giáo) cấu kết gian tế địa phương.
-  - Chưa biết hiểm họa đẫm máu mà Thúy Yên Môn và Hạ Nương sắp sửa gánh chịu tại Bách Hoa Cốc.
+  - Chưa biết hiểm họa đẫm máu mà Thúy Yên Môn và Hạ Nương đang và sắp sửa gánh chịu tại Bách Hoa Cốc.
   - Chưa biết sự hiện diện của Tiêu Phùng tại Ba Lăng Huyện và mối dây liên kết chung về ngọc Du Long Giác.
+  - Chưa biết tương lai bản thân sẽ phải mang thân phận gián điệp Mộc Nhất Lâu thâm nhập Ngũ Độc Giáo (Task 5).
```

---

## 4. Đề Xuất Bổ Sung & Đồng Bộ Danh Bạ Nhân Vật Phụ (`characters/supporting_cast.md`)

```diff
Index: characters/supporting_cast.md
===================================================================
--- characters/supporting_cast.md
+++ characters/supporting_cast.md
@@ -40,6 +40,12 @@
 | **Lưu Mặc** | **B** | Dũng tướng cựu trào | Vóc dáng tầm thước nhưng hai cánh tay dài quá đầu gối, cơ bắp cuồn cuộn như dây chão thừng; ánh mắt lì lợm sa trường | Ô Thiết Côn dài một trượng bọc vòng thép; sở trường đòn quét chân càn quét tầm thấp | Bị ngọn thương của Thiết Tâm dùng nhu kình cuốn bay binh khí chém vào cột khoang; kính nể tân chủ | Chương 02b |
 | **Bùi Dực Phi** | **A/Anchor** | Thống lĩnh Cáp Xá / Kỵ tướng Thiên Vương | Giáp trụ xám tro, cưỡi chiến mã đen tuyền; phong thái cương nghị sa trường (đã lập hồ sơ riêng `anchors/bui_duc_phi.md`) | Đại kích sa trường, tài cưỡi ngựa bắn cung | Nhận mệnh Dương Anh dẫn 30 thiết kỵ xuất phát sang Tây Nam (Thúy Yên Môn) hộ tống quân lương cứu tế và điều tra cổ án Ma Y Cốc | Chương 07b |
+| **Lý Tuyền** | **B** | Thị vệ ngự tiền triều Tống cải trang ăn mày | Dáng người gầy gộc, ngón tay có vết chai kéo cung cứng và ghìm cương ngựa; giấu đai lụa kim tuyến đại nội dưới áo tơi | Cung tiễn sa trường / Đoản kiếm | Bị đâm rách mạn sườn nhiễm trùng máu (`INJ-LT-001` L2); mang ống sáp mật Triệu Nhữ Ngu lên đảo cầu cứu; đang tịnh dưỡng tại bến nam | Chương 10 |
+| **Hàn Thác Trụ** | **A/Anchor** | Tuyên phủ sứ Nam Tống / Cháu họ Ngô Thái Hậu | Quan văn 39 tuổi, dáng nho nhã thanh tú; áo gấm rách tả tơi, chân đi giày lụa phồng rộp; kiên định, mang khí phách sĩ phu | Nho sinh mang mật chiếu Tống Hiếu Tông | Bị phồng rộp chân (`INJ-HTT-001` L1) và say nắng; được Tĩnh Xuyên giải cứu an toàn xuống xuồng nan bến Thủy Lục rời đảo; hẹn ngày đền đáp tại Lâm An | Chương 10 |
+| **Lư Tiếu Bần** | **B** | Bạch Kỳ Chủ Ngũ Độc Giáo | Trạc 33 tuổi, dáng gầy gò phong trần, áo xám tơi tả, khóe miệng nhếch cười bỡn cợt; tính tình phóng khoáng, trọng đại nghĩa | Tuyệt kỹ trộm đồ "Diệu Thủ Không Không" | Nhận lệnh ám sát Hàn Thác Trụ nhưng không nỡ hại trung thần; ném trả mật chiếu, bảo hộ Hàn Thác Trụ để Tĩnh Xuyên diệt Nhị Sứ; phiêu bạt giang hồ | Chương 10 |
+| **Bang Chúng Kính Trang** | **C** | Đệ tử tinh nhuệ Thiên Vương Bang | Tráng đinh mặc áo giáp nhẹ màu lam, tác phong nhanh nhẹn cẩn mật | Xuồng nan ngụy trang lưới rách bến Thủy Lục | Phụng mệnh Dương Thiết Tâm cắm chốt tại vụng nước bến Thủy Lục; chèo xuồng nan đưa Hàn Thác Trụ rời đảo an toàn | Chương 10 |
+| **Viêm Dương Sứ** | **C (Tử trận)** | Cao thủ hỏa trận Ngũ Độc Giáo | Hộ pháp cởi trần da đỏ gay như đồng hun, xăm rắn lửa đầy mình; tính tình hung bạo cuồng sát | Hỏa lân đao đỏ rực, bom lân tinh hỏa dược | Bị Tĩnh Xuyên đâm gãy khớp vai phải, bom lân tinh vỡ bén lửa tự thiêu rụi rồi rơi xuống vực Hình Thiên Lĩnh đền mạng | Chương 10 |
+| **Lãnh Nguyệt Sứ** | **C (Tử trận)** | Nữ sát thủ Ngũ Độc Giáo | Thân hình mảnh khảnh khoác áo choàng lông quạ lam thẫm, mạng che mặt thêu trăng khuyết; âm hiểm xảo quyệt | Song đoản nhận hàn khí, Băng Phách Đoản Châm tẩm độc rết | Bị Tĩnh Xuyên quét cán sắt Bát Hàn chấn gãy xương quai xanh đập vào vách đá chết tại chỗ | Chương 10 |
```

---

## 5. Đề Xuất Cập Nhật Sổ Cái Bảo Vật & Cơ Quan (`worldbuilding/artifacts/artifacts_ledger.md`)

```diff
Index: worldbuilding/artifacts/artifacts_ledger.md
===================================================================
--- worldbuilding/artifacts/artifacts_ledger.md
+++ worldbuilding/artifacts/artifacts_ledger.md
@@ -74,6 +74,20 @@
 | **ART-THU-TIEN-CU-001** | **Phong thư tiến cử Cái Bang** | Tín hàm giấy tuyên chỉ niêm sáp đỏ triện ấn Nghĩa Quân Ba Lăng; chữ viết tay của Bạch Thu Lâm gửi Bang chủ Cái Bang Thạch Hiên Viên | Tiêu Phùng | Ba Lăng Huyện $\rightarrow$ Yến Tử Ổ | Chứng thực tư cách gia nhập Cái Bang và bảo lãnh Tiêu Phùng | Toàn vẹn, giắt trong bọc áo Tiêu Phùng chuẩn bị xuất sơn | Chương 09, 12 |
 
+<!-- ================================================================================= -->
+<!-- 5. BẢO VẬT & TÍN VẬT KHU VỰC THANH LOA ĐẢO — HÌNH THIÊN LĨNH (CHƯƠNG 10)         -->
+<!-- ================================================================================= -->
+
+| Mã Bảo Vật | Tên Bảo Vật / Tín Vật | Nguồn Gốc & Đặc Điểm Vật Lý | Người Nắm Giữ | Vị Trí Hiện Tại | Công Năng / Ý Nghĩa Chiến Lược | Trạng Thái Bền Vững | Chương Xuất Hiện |
+| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :---: |
+| **ART-ONG-SAP-001** | **Ống sáp mật thư Triệu Nhữ Ngu** | Ống đồng nhỏ cỡ ngón tay cái, niêm sáp đỏ triện ấn đóa sen ngậm ngọc của phủ Tông thất Triệu thị tại Lâm An; bên trong chứa mật chiếu viết mực son của Tống Hiếu Tông | Hàn Thác Trụ | Rời Thanh Loa Đảo sang đất liền | Mật chiếu hiệu triệu cần vương chống lại bè lũ phản trắc Lý Hoàng hậu | Đã mở sáp kiểm tra; cuộn lụa mật chiếu nguyên vẹn trong tay Hàn Thác Trụ | Chương 10 |
+| **ART-MAT-NA-001** | **Mặt nạ da trâu bọc sắt** | Mặt nạ chế tác từ da trâu thuộc dày, bên ngoài bọc các phiến sắt xám lạnh, che kín diện mạo chỉ chừa hai hốc mắt | Tĩnh Xuyên | Bến Thủy Lục / Doanh trại bờ kè | Ngụy trang diện mạo sa trường, ngăn triều đình và tà giáo truy vết Thiên Vương Bang | Nguyên vẹn, Tĩnh Xuyên cất giữ làm trang bị ngụy trang cá nhân | Chương 10 |
```

---

## 6. Đề Xuất Cập Nhật Ma Trận Quan Hệ Phe Phái (`worldbuilding/factions/relationships_matrix.md`)

```diff
Index: worldbuilding/factions/relationships_matrix.md
===================================================================
--- worldbuilding/factions/relationships_matrix.md
+++ worldbuilding/factions/relationships_matrix.md
@@ -48,6 +48,8 @@
 | **REL-CB-TVB-001** | Cái Bang (Yến Tử Ổ) $\longleftrightarrow$ Thiên Vương Bang (Thanh Loa) | **ALLIED / MUTUAL RESPECT** | Quan hệ đồng minh truyền thống giữa hai thế lực giang hồ lớn nhất Động Đình; Thiết Tâm gửi thư bí mật gởi gắm Cầu Chỉ Thủy; Thạch Hiên Viên đón nhận nồng nhiệt | Chương 07b |
 | **REL-TY-NPD-001** | Thúy Yên Môn $\longleftrightarrow$ Tây Hạ Nhất Phẩm Đường | **BLOODY ENMITY / AT WAR** | Mối thù diệt môn truyền kiếp; Nhất Phẩm Đường phái thích khách đồ sát bầy sói Điểm Thương và thâm nhập Bách Hoa Trận cướp Du Long Giác | Chương 08a, 08b |
 | **REL-NQ-TH-001** | Nghĩa Quân Ba Lăng $\longleftrightarrow$ Tây Hạ Nhất Phẩm Đường | **DEADLY ENMITY** | Thích khách Tây Hạ đột nhập Miếu Thần cướp Vô Danh Mật Tịch; Trương Đỉnh trọng thương, Thu Di bắn chết Bách hộ giặc; đối đầu trực diện | Chương 09 |
+| **REL-TVB-HTT-001** | Thiên Vương Bang (Tĩnh Xuyên) $\longleftrightarrow$ Phái Chủ Chiến Triều Tống (Hàn Thác Trụ) | **ALLIED UNDER THE TABLE / DEBT OF LIFE** | Mật ước đồng minh ngầm và ơn cứu mạng; Thiết Tâm ra lệnh cứu viện; Hàn Thác Trụ hẹn ngày đền đáp tại kinh thành Lâm An | Chương 10 |
+| **REL-TVB-NGUDOC-001** | Thiên Vương Bang $\longleftrightarrow$ Ngũ Độc Giáo | **HOSTILE / COMPLEX SPLIT** | Xung đột vũ trang đẫm máu: Tĩnh Xuyên tiêu diệt Ngũ Độc Nhị Sứ; song Bạch Kỳ Chủ Lư Tiếu Bần bộc lộ sự phản kháng ngầm với giáo lệnh, mở ra mắt xích trung lập | Chương 10 |
```

---

## 7. Đề Xuất Cập Nhật Bảng Theo Dõi Lời Hứa Cốt Truyện (`plot/promises_tracker.md`)

```diff
Index: plot/promises_tracker.md
===================================================================
--- plot/promises_tracker.md
+++ plot/promises_tracker.md
@@ -15,8 +15,10 @@
 | **TH-003** | **Mối nghi kỵ chia rẽ ngầm của Lâu Nhất Quan** | Chương 02b | Tĩnh Xuyên | Thiết Tâm ban lệnh trục xuất Cầu Chỉ Thủy; Lâu Nhất Quan thu đao chấp nhận bang quy; nguy cơ nội chiến tạm thời được dập tắt (Ch.07b) | **Chương 07b** | `RESOLVED / TEMPORARILY MANAGED` (Kiểm soát thành công) |
-| **TH-004** | **Sự tin cậy của Dương Thiết Tâm với Tĩnh Xuyên** | Chương 02b | Tĩnh Xuyên | Tĩnh Xuyên hoàn thành xuất sắc nhiệm vụ đối chất; Thiết Tâm giao toàn bộ tuyến phòng thủ bờ kè và trinh sát bến cảng đảo cho chàng khi Cáp Xá xuất chinh (Ch.07b) | **Chương 10** (*Hình Thiên Lĩnh*) & **Chương 14** | `ADVANCED / PILLAR OF DEFENSE` (Trụ cột phòng thủ) |
+| **TH-004** | **Sự tin cậy của Dương Thiết Tâm với Tĩnh Xuyên** | Chương 02b | Tĩnh Xuyên | Thiết Tâm trao mặt nạ sắt và mật lệnh độc hành cứu Hàn Thác Trụ cho Tĩnh Xuyên; Tĩnh Xuyên hoàn thành trọn vẹn nhiệm vụ, trở thành tướng tiên phong tin cậy nhất của Bang chủ (Ch.10) | **Chương 14** (*Tứ Diện Sở Ca*) | `PAID OFF (STAGE 1) / CORE ANCHOR` (Hoàn tất giai đoạn 1) |
+| **TH-016** | **Ân tình Lâm An & Lời hứa của Hàn Thác Trụ** | Chương 10 | Tĩnh Xuyên / Hàn Thác Trụ | Tĩnh Xuyên xả thân phá vây cứu mạng; Hàn Thác Trụ hứa đền đáp công ơn tại kinh đô Lâm An khi Tĩnh Xuyên đặt chân đến kinh kỳ | **Quyển 2 / Quyển 3** (Biến cố chính trị Lâm An) | `PLANTED / ACTIVE PROMISE` (Gieo mầm lời hứa chính trị) |
+| **TH-017** | **Mầm mống phân hóa Ngũ Độc Giáo & Cơ duyên Lư Tiếu Bần** | Chương 10 | Tĩnh Xuyên / Lư Tiếu Bần | Lư Tiếu Bần tha mạng Hàn Thác Trụ, ném trả mật chiếu và chỉ điểm phục binh; gieo mầm cho thân phận gián điệp Mộc Nhất Lâu thâm nhập Ngũ Độc | **Quyển 1 Hồi 3 & Quyển 2** (Task 5: Mộc Nhất Lâu) | `PLANTED / STRUCTURAL SEED` (Gieo mầm phân nhánh Ngũ Độc) |
```

---

## 8. Đề Xuất Cập Nhật Biên Niên Sử & Outline Deck (`plot/timeline.md` & `plot/volume_01_deck.md`)

```diff
Index: plot/timeline.md
===================================================================
--- plot/timeline.md
+++ plot/timeline.md
@@ -56,5 +56,5 @@
 * **Ngày 25–26 tháng 8 (1191-08-25 – 26):**
-  * *Thanh Loa Đảo (1191-08-25 Trưa oi nồng đến Đêm trăng rằm):* Đúng 6 ngày sau khi Cầu Chỉ Thủy rời đảo và Bùi Dực Phi dẫn 30 kỵ mã xuất chinh Tây Nam (1191-08-19). Thị vệ ngự tiền cải trang Lý Tuyền mang mật thư phủ Tông thất Triệu Nhữ Ngu dạt vào bờ kè bến nam. Tuyên phủ sứ Hàn Thác Trụ (39 tuổi) mang mật chiếu Tống Hiếu Tông chạy trốn bị sát thủ Ngũ Độc Giáo bao vây tại Hình Thiên Lĩnh (`Task 1: Subtask 3–4`). Dương Thiết Tâm dùng kế điệu hổ ly sơn cho kỵ binh Cáp Xá tại đảo làm mồi nhử ở bến Thanh Tiễn; Tĩnh Xuyên (18 tuổi) mang mặt nạ sắt bí mật phá vây Hình Thiên Lĩnh, đối mặt Bạch Kỳ Chủ Lư Tiếu Bần, huyết chiến tiêu diệt Ngũ Độc Nhị Sứ (Lãnh Nguyệt Sứ & Viêm Dương Sứ), giải cứu Hàn Thác Trụ an toàn xuống bến đò Thủy Lục.
+  * *Thanh Loa Đảo (1191-08-25 Trưa oi nồng đến Đêm trăng rằm):* Đúng 6 ngày sau khi Cầu Chỉ Thủy rời đảo và Bùi Dực Phi dẫn 30 kỵ mã xuất chinh Tây Nam (1191-08-19). Thị vệ ngự tiền cải trang Lý Tuyền mang mật thư phủ Tông thất Triệu Nhữ Ngu dạt vào bờ kè bến nam. Tuyên phủ sứ Hàn Thác Trụ (39 tuổi) mang mật chiếu Tống Hiếu Tông chạy trốn bị sát thủ Ngũ Độc Giáo bao vây tại Hình Thiên Lĩnh (`Task 1: Subtask 3–4`). Dương Thiết Tâm dùng kế điệu hổ ly sơn cho kỵ binh Cáp Xá tại đảo làm mồi nhử ở bến Thanh Tiễn; Tĩnh Xuyên (18 tuổi) mang mặt nạ sắt bí mật phá vây Hình Thiên Lĩnh, đối mặt Bạch Kỳ Chủ Lư Tiếu Bần, huyết chiến tiêu diệt Ngũ Độc Nhị Sứ (Lãnh Nguyệt Sứ & Viêm Dương Sứ), giải cứu Hàn Thác Trụ an toàn xuống bến đò Thủy Lục. *(ĐÃ CANON HÓA — 5.835 từ)*
```

```diff
Index: plot/volume_01_deck.md
===================================================================
--- plot/volume_01_deck.md
+++ plot/volume_01_deck.md
@@ -46,3 +46,3 @@
-| **10** | *Hình Thiên Lĩnh Huyết Lộ*| **Tĩnh Xuyên** | Core Plot | Hình Thiên Lĩnh | Tĩnh Xuyên cùng kỵ binh thiết giáp phá vây giải cứu Tuyên phủ sứ Hàn Thác Trụ đang bị sát thủ Ngũ Độc bao vây; đối mặt với sự tàn khốc của độc trùng và thuật dịch dung. | `Task 1: Subtask 3–4`<br>(*Sát Cơ Trùng Trùng*) |
+| **10** | *Hình Thiên Lĩnh Huyết Lộ*| **Tĩnh Xuyên** | Core Plot | Hình Thiên Lĩnh | Khám xét thị vệ Lý Tuyền; khẩu chiến trướng sảnh & kế Điệu Hổ Ly Sơn; Tĩnh Xuyên mang mặt nạ sắt lên núi đụng độ Lư Tiếu Bần (Diệu Thủ Không Không); huyết chiến hạ sát Ngũ Độc Nhị Sứ (Lãnh Nguyệt Sứ & Viêm Dương Sứ); giải cứu Tuyên phủ sứ Hàn Thác Trụ xuống bến đò Thủy Lục; lời ước hẹn tại Lâm An. *(ĐÃ CANON HÓA — 5.835 từ)* | `Task 1: Subtask 3–4`<br>(*Sát Cơ Trùng Trùng*) |
```

---

## 9. Quyết Định & Chỉ Thị Của Tác Giả (Cổng Dừng Cứng 3)

- [x] Phê chuẩn toàn văn Đề xuất Canon Diff Chương 10 (Đã được Tác giả chính thức phê chuẩn).
- *(Agent đã hoàn tất commit state vào đủ 4 Trụ Cột bền vững: characters/tinh_xuyen.md, characters/supporting_cast.md, worldbuilding/medical/injuries_ledger.md, worldbuilding/artifacts/artifacts_ledger.md, worldbuilding/factions/relationships_matrix.md, plot/promises_tracker.md, plot/timeline.md, plot/volume_01_deck.md).*
