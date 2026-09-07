# Đề Xuất Canon Diff: Chương 08a — Bách Hoa Lang Dạ

> **Cơ quan quản lý**: Novel OS State Ledger  
> **Trạng thái**: Chờ Tác giả xem xét và phê chuẩn trước khi commit vào Sổ cái trạng thái bền vững (Cổng Dừng 3).

---

## 1. Tóm Tắt Biến Chuyển Cốt Truyện & Nhân Vật (Narrative Summary)

- **POV**: Hạ Nương (16 tuổi — Y nữ Thúy Yên Môn / Bách Hoa Cốc — Điền Trì).
- **Thời gian**: Canh hai đêm sương, ngày 1191-08-19.
- **Biến cố môn phái & Pháp y hiện trường cốt tử**:
  - Dược phòng Điền Trì lúc chạng vạng: Doãn Hàm Yên trao áo choàng lông cáo và mật lệnh cho Hạ Nương tháp tùng đoàn người tiến vào cấm địa Bách Hoa Trận; bộc lộ xung đột ý thức hệ ngầm giữa sự thực dụng lo toan kinh tài của Tân Chưởng môn (nợ tiền trang Tạ Hiền 3 vạn lượng bạc, nợ dược liệu Thục Trung) và sự cuồng nộ hoài niệm chấp niệm tình duyên mười bảy năm của Tiền Chưởng môn Lệ Thu Thủy;
  - Canh hai tại Xuân Mai Nhã Trúc: Lệ Thu Thủy đốc thúc 6 đệ tử chấp pháp áo lam mang đuốc dầu trẩu xuất kích; gạt phăng quẻ sấm "Huyết quang tai" của Ma Y Thần Tướng; đoàn người tiến vào lối mòn đỗ quyên cổ thụ ngập sương lam độc;
  - Hẻm núi cửa cấm địa Bách Hoa Trận: Đụng độ bầy sói xám Điểm Thương (Bách Hoa Lang) cuồng loạn với mắt vằn tia đỏ rực máu bất thường;
  - Đan Bích Tú bị sói đầu đàn vồ trúng, rách toạc bả vai trái từ xương quai xanh đến bắp tay (`INJ-DBT-001` L1); Lệ Thu Thủy thi triển Phù Vân Kiếm xé toạc dã thú;
  - Hạ Nương bình tĩnh thi triển Băng Phách Ngân Châm, phóng 2 mũi kim bạc chuẩn xác vào huyệt Phong Trì và chùm dây thần kinh tủy sống sau gáy sói đầu đàn, phong tỏa hoàn toàn chức năng vận động tứ chi của mãnh thú;
  - Hạ Nương thực hiện sơ cứu vết thương cho Đan Bích Tú bằng rượu thuốc hoàng liên bách bộ, rắc Kim Sáng Dược và băng bó chữ nhân, cấm vận lực tay trái trong 3 ngày;
  - Giảo nghiệm pháp y hiện trường: Hạ Nương dùng dao mổ khám nghiệm tử thi sói chết trước cửa cấm địa, phát hiện 3 chứng cứ chấn động:
    1. Hộp sọ sói già bị nghiền nát với 6 lỗ thủng lục giác có cạnh răng cưa — dấu vết đặc trưng của **Bát Giác Lang Nha Chùy** (trọng binh Tây Hạ), hoàn toàn xa lạ với kiếm pháp Thúy Yên;
    2. Máu đông cứng nguội ngắt: Sói đã bị giết từ **hơn hai canh giờ trước** (đầu giờ Tuất);
    3. Kẽ móng vuốt dính **đất sét vàng sa mạc** (hoàng thổ khô) đặc trưng của vùng khô hạn Tây Bắc / sạn đạo Thục Đạo;
  - Kết luận rúng động: **Cấm địa Bách Hoa Trận đã bị toán mật vụ ngoại bang (Tây Hạ Nhất Phẩm Đường) thâm nhập từ trước!**
  - Điểm ngắt kịch tính (Dramatic Hook): Bất chấp cảnh báo, Lệ Thu Thủy tuốt kiếm dẫn đầu bước qua tấm bia đá vỡ "Bách Hoa Bí Cảnh" lao vào mê cung; Hạ Nương xốc hòm thuốc bám theo.

---

## 2. Đề Xuất Cập Nhật Sổ Cái Thương Tật (`worldbuilding/medical/injuries_ledger.md`)

```diff
Index: worldbuilding/medical/injuries_ledger.md
===================================================================
--- worldbuilding/medical/injuries_ledger.md
+++ worldbuilding/medical/injuries_ledger.md
@@ -70,3 +70,18 @@
+
+### I. Đan Bích Tú (Đệ tử chấp pháp Thúy Yên Môn)
+
+| Vết thương # | Vị trí & Dạng tổn thương | Cấp độ | Tác nhân / Hoàn cảnh | Hồi xuất hiện | Trạng thái hiện tại | Di chứng & Ảnh hưởng hành vi |
+| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
+| **INJ-DBT-001** | Bả vai trái & bắp tay: 3 vết móng vuốt sói cào toác da thịt từ xương quai xanh đến bắp tay, rỉ máu liên tục. | **L1** (Nhẹ / Rách phần mềm) | Bị sói xám Điểm Thương (Bách Hoa Lang) đầu đàn vồ trúng trong hẻm đá cửa cấm địa Bách Hoa Trận. | Chương 08a | **ĐÃ SƠ CỨU CẤM VẬN LỰC**. Hạ Nương rửa rượu hoàng liên bách bộ, rắc Kim Sáng Dược, băng bó chữ nhân. | Mất lực tay trái trong 3–5 ngày; cấm vung kiếm hay vận lực mạnh để tránh bục vết thương; ở lại cửa trận hỗ trợ bắn pháo hiệu. |
```

---

## 3. Đề Xuất Cập Nhật Hồ Sơ Nhân Vật Hạ Nương (`characters/ha_nuong.md`)

```diff
Index: characters/ha_nuong.md
===================================================================
--- characters/ha_nuong.md
+++ characters/ha_nuong.md
@@ -73,6 +73,28 @@
+
+---
+
+## 7. SỔ CÁI TRẠNG THÁI HIỆN HÀNH (DURABLE STATE LEDGER)
+* **Mốc thời gian hiện hành:** 1191-08-19 (Đêm sương canh hai — Sau Chương 08a).
+* **Thể trạng thực tế:** Thể lực hao tổn sau một ngày dài sao chế dược liệu và nắn khớp; đầu ngón tay có vết chai mỏng kẹp kim bạc và cầm dao trích nọc; mu bàn chân tê buốt vì giày vải ngấm sương đêm Điền Trì; không mang thương tật ngoại thương.
+* **Binh khí & Trang bị:**
+  - Hòm thuốc da hươu đeo vai (chứa dao róc xương trích nọc, kéo y khoa, bình sứ rượu hoàng liên bách bộ, bột Kim Sáng Dược, băng vải thô).
+  - Hộp trâm Băng Phách Ngân Châm giắt bên đai lưng.
+  - Áo choàng lông cáo trắng muốt viền chỉ bạc do Tân Chưởng môn Doãn Hàm Yên trao tặng.
+* **Vị thế & Quan hệ nội bộ:**
+  - Được Tân Chưởng môn Doãn Hàm Yên tin cẩn tuyệt đối, xem như "con mắt độc lập lý trí" để giám sát Lệ Thu Thủy và bảo toàn tính mạng đệ tử.
+  - Được Đan Bích Tú và các đệ tử chấp pháp kính trọng, tin cậy sau ca cấp cứu sơ cứu vết thương sói cào kịp thời.
+  - Bị Tiền Chưởng môn Lệ Thu Thủy xem là rào cản gàn dở, nhưng sự sắc bén trong khám nghiệm tử thi sói của Hạ Nương đã khiến bà chấn động.
+* **Tri thức & Thông tin nắm giữ:**
+  - Nắm rõ mâu thuẫn tài chính nội bộ: Thúy Yên Môn đang nợ tiền trang Tạ Hiền 3 vạn lượng bạc và nợ tiền dược liệu Thục Trung.
+  - Khám nghiệm tử thi sói: Bóc trần sự thật cấm địa Bách Hoa Trận đã bị thế lực mật vụ ngoại bang dùng chùy gai sắt lục giác thâm nhập từ 2 canh giờ trước; phát hiện vết bùn đất sét vàng sa mạc Tây Bắc.
+* **Ranh giới cấm kỵ (Forbidden Unknowns):**
+  - Chưa trực tiếp giáp mặt Cao Thủ Hồng Y & Tử Y (Tây Hạ Nhất Phẩm Đường) trong tâm trận (sẽ giáp mặt ở Chương 08b).
+  - Chưa biết tình trạng cụ thể của khối hung ngọc Du Long Giác bên trong rương sắt cổ (sẽ mở nắp ở Chương 08b).
+  - Chưa biết biến cố tại Thanh Loa Đảo và việc Bùi Dực Phi dẫn kỵ binh Cáp Xá đang phi ngựa tới Tây Nam.
```

---

## 4. Đề Xuất Cập Nhật Sổ Cái Vật Phẩm & Khí Giới (`worldbuilding/artifacts/artifacts_ledger.md`)

```diff
Index: worldbuilding/artifacts/artifacts_ledger.md
===================================================================
--- worldbuilding/artifacts/artifacts_ledger.md
+++ worldbuilding/artifacts/artifacts_ledger.md
@@ -23,2 +23,3 @@
-| **Hộp ngân châm & Dao mổ bạc** | Dụng cụ y lý phẫu thuật dã chiến của Hạ Nương | **Hạ Nương** | Dược phòng Điền Trì | Tráp gỗ mun chứa bộ ngân châm Thủy kình; dao bạc nhỏ sáng loáng vừa khử trùng sau ca rạch nọc rắn | Chương 03 |
+| **Hộp ngân châm & Dao mổ bạc** | Dụng cụ y lý phẫu thuật dã chiến của Hạ Nương | **Hạ Nương** | Cửa cấm địa Bách Hoa Trận | Đã dùng 2 mũi Băng Phách Ngân Châm hạ gục sói đầu đàn; dao trích nọc dùng mổ hộp sọ sói già dính máu thẫm và đất sét vàng Tây Bắc | Chương 08a |
+| **Áo choàng lông cáo viền chỉ bạc** | Áo choàng giữ ấm môn phái cao cấp của Doãn Hàm Yên trao tặng Hạ Nương | **Hạ Nương** | Khoác trên người Hạ Nương | Vạt áo thấm đẫm sương đêm ẩm lạnh Điền Trì; viền cổ tay áo sờn 2 sợi chỉ tơ minh chứng kinh tài khó khăn | Chương 08a |
```

---

## 5. Đề Xuất Cập Nhật Lần Vết Hứa Hẹn (`plot/promises_tracker.md`)

```diff
Index: plot/promises_tracker.md
===================================================================
--- plot/promises_tracker.md
+++ plot/promises_tracker.md
@@ -16,2 +16,2 @@
-| **TH-005** | **Sấm truyền Huyết Quang Tai tại Thúy Yên Môn** | Chương 03 | Hạ Nương | Ma Y Thần Tướng cảnh báo ngọc báu mang sát khí; bầy sói đào bới cấm địa | **Chương 08a & 08b** | **Chương 13** (*Huyết Quang Tai*) | `ACTIVE / TICKING` (Đếm ngược tai họa) |
+| **TH-005** | **Sấm truyền Huyết Quang Tai tại Thúy Yên Môn** | Chương 03 | Hạ Nương | Bầy sói Điểm Thương cuồng loạn bị tiêu diệt; Hạ Nương giảo nghiệm phát hiện xác sói bị giết bởi trọng binh ngoại bang; cấm địa đã bị thâm nhập (Ch.08a) | **Chương 08a & 08b** | **Chương 13** (*Huyết Quang Tai*) | `ADVANCED / HIGH THREAT` (Sát cơ cận kề) |
@@ -18,2 +18,2 @@
-| **TH-007** | **Ẩn số nam tử trong mối tình dĩ vãng của Lệ Thu Thủy** | Chương 03 | Hạ Nương | Lệ Thu Thủy ôm hận tìm Du Long Giác vì người xưa trong đêm mưa | **Chương 08a & 08b** & **Chương 13** | **Quyển 1 Hồi Ba** | `OPEN MYSTERY` (Bí ẩn chưa giải) |
+| **TH-007** | **Ẩn số nam tử trong mối tình dĩ vãng của Lệ Thu Thủy** | Chương 03 | Hạ Nương | Lệ Thu Thủy bất chấp quẻ sấm và sự xâm nhập của ngoại bang, quyết tâm mở trận cướp ngọc bằng mọi giá vì mối tình 17 năm (Ch.08a) | **Chương 08a & 08b** & **Chương 13** | **Quyển 1 Hồi Ba** | `ADVANCED / OBSESSION PEAK` (Chấp niệm bộc phát) |
@@ -24,2 +24,3 @@
+| **TH-014** | **Dấu vết Chùy gai Lục giác & Mật vụ Tây Hạ tại Điền Trì** | Chương 08a | Hạ Nương | Hạ Nương khám nghiệm sọ sói bị nghiền nát bởi Bát Giác Lang Nha Chùy và đất sét vàng sa mạc; phát hiện cấm địa bị thâm nhập | **Chương 08b & Chương 13** | **Hồi 2** | `PLANTED / CRUCIAL CLUE` (Manh mối trọng binh ngoại bang) |
```

---

## 6. Đề Xuất Cập Nhật Ma Trận Thế Lực (`worldbuilding/factions/relationships_matrix.md`)

```diff
Index: worldbuilding/factions/relationships_matrix.md
===================================================================
--- worldbuilding/factions/relationships_matrix.md
+++ worldbuilding/factions/relationships_matrix.md
@@ -15,1 +15,1 @@
-| **REL-TYM-TH-001** | **Thúy Yên Môn** $\longleftrightarrow$ **Tây Hạ (Nhất Phẩm Đường)** | **Xâm nhập cấm địa & Nguy cơ Huyết tẩy** | `WAR / INFILTRATED` | 1191-08-17 (Chương 08a) | Nhất Phẩm Đường phái Hồng Y và Tử Y Cao Thủ thâm nhập cấm địa Bách Hoa Trận, cưa đứt then chốt tượng Chu Tước và đào trộm hung ngọc Du Long Giác; Thúy Yên chính thức phát hiện nguy cơ diệt môn. |
+| **REL-TYM-TH-001** | **Thúy Yên Môn** $\longleftrightarrow$ **Tây Hạ (Nhất Phẩm Đường)** | **Xâm nhập cấm địa & Nguy cơ Huyết tẩy** | `WAR / INFILTRATED` | 1191-08-19 (Chương 08a) | Hạ Nương khám nghiệm xác sói phát hiện dấu vết Bát Giác Lang Nha Chùy và đất sét vàng sa mạc; Thúy Yên chính thức phát hiện cấm địa Bách Hoa Trận đã bị mật thám Nhất Phẩm Đường thâm nhập trước 2 canh giờ. |
```

---

## 7. Đề Xuất Cập Nhật Dòng Thời Gian (`plot/timeline.md`)

```diff
Index: plot/timeline.md
===================================================================
--- plot/timeline.md
+++ plot/timeline.md
@@ -54,3 +54,3 @@
 * **Ngày 19–20 tháng 8:**
-  * *Bách Hoa Cốc (1191-08-19 Hoàng hôn & Đêm sương):* Lệ Thu Thủy cố chấp dẫn toán người vào Xuân Hoa Viên trong đêm; Doãn Hàm Yên cử Hạ Nương tháp tùng; kịch chiến bầy sói xám Điểm Thương (Bách Hoa Lang) cuồng loạn; Hạ Nương giảo nghiệm tử thi sói, bóc tách dấu tích chùy gai rách thịt và nội kình ngoại bang của toán mật vụ đột nhập trước; dấn thân vào cấm địa (`Task 12: Subtask 86 Step 1–2` — **Chương 08a**).
+  * *Bách Hoa Cốc (1191-08-19 Hoàng hôn & Đêm sương Canh hai):* Lệ Thu Thủy cố chấp dẫn toán người vào Xuân Hoa Viên trong đêm; Doãn Hàm Yên cử Hạ Nương tháp tùng; kịch chiến bầy sói xám Điểm Thương (Bách Hoa Lang) cuồng loạn; Đan Bích Tú bị cào rách vai (INJ-DBT-001 L1); Hạ Nương dùng Băng Phách Ngân Châm hạ gục sói đầu đàn; giảo nghiệm tử thi sói bóc tách dấu tích Bát Giác Lang Nha Chùy và bùn đất sét vàng Tây Bắc của mật thám Nhất Phẩm Đường thâm nhập trước 2 canh giờ; dấn thân vào cấm địa (`Task 12: Subtask 86 Step 1–2` — **Chương 08a đã canon hóa**).
```

---

## Verdict:
**APPROVED FOR AUTHOR REVIEW (TRÌNH TÁC GIẢ DUYỆT ĐỀ XUẤT CANON DIFF Ở CỔNG DỪNG 3)**.  
Chỉ khi Tác giả phê chuẩn bản Diff này, Agent mới tiến hành commit các thay đổi vào các file sổ cái bền vững tương ứng.


---

## Supporting Cast Directory (`characters/supporting_cast.md`)
*(Đã đồng bộ chuẩn hóa kiểm toán vào danh bạ nhân vật phụ)*
