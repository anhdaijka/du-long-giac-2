# Đề Xuất Canon Diff: Chương 03 — Hương Dược Bách Hoa

> **Cơ quan quản lý**: Novel OS State Ledger  
> **Trạng thái**: Chờ Tác giả xem xét và phê chuẩn trước khi commit vào Sổ cái trạng thái bền vững (Cổng Dừng 3).

---

## 1. Tóm Tắt Biến Chuyển Cốt Truyện & Nhân Vật (Narrative Summary)

* **POV**: Hạ Nương (16 tuổi — Y nữ Điền Trì Dược Phòng / Thúy Yên Môn — Bách Hoa Cốc, Điểm Thương Sơn).
* **Mốc thời gian**: 1191-08-17 (Sáng sớm đến Hoàng hôn).
* **Địa điểm**: Dược phòng Điền Trì, Hậu đình Xuân Mai Nhã Trúc, Tứ Đại Hoa Viên (Xuân - Hạ - Thu - Đông), cấm địa Bách Hoa Trận.
* **Biến chuyển cốt lõi**:
  1. *Y đạo thực chứng & Sinh kế Thúy Yên*: Hạ Nương thức sớm sao chế thảo dược, xử lý cấp cứu ca rắn lục cắn kèm trật khớp cho tiểu đệ tử tuần sơn Tiểu Đào; bộc lộ đời sống thực tế không tiên hiệp của nữ phái Thúy Yên.
  2. *Gánh nặng kinh tài & Sự trở về của Tiền Chưởng môn*: Doãn Hàm Yên (40 tuổi, Lục Đại Môn Chủ tái nhậm chấn hưng) lo toan sổ sách kinh tài và kho dược hao hụt; Tiền Chưởng môn Lệ Thu Thủy (43 tuổi) đột ngột trở về cùng quái nhân phong thủy Ma Y Thần Tướng mang la bàn tầm long.
  3. *Nâng tầm báu vật Du Long Giác*: Lệ Thu Thủy tiết lộ Du Long Giác là báu vật trấn quốc thời Tống Thái Tổ Triệu Khuông Dẫn do Khai sơn tổ sư Doãn Tuyết Dao bí mật phong ấn tại Bách Hoa Cốc làm trận nhãn Trụ Thần Thạch. Năm xưa (1174, 19 năm trước) tại bến đò Giang Nam, Tiêu Lăng Phong từng cảnh báo bà về hiểm họa thiên thạch bộc phát. Mười ngày trước tại chân núi Nga My, giang hồ phương Bắc bỗng râm ran tin đồn hung ngọc xuất thế ở Thúy Yên.
  4. *Khảo nghiệm la bàn & Phát hiện bầy sói*: Hạ Nương cầm la bàn đo đạc 4 hoa viên, phát hiện bầy sói xám Điểm Thương cào bới cuồng loạn; ráp đồ hình chữ thập xác định tâm trận rơi trúng Bách Hoa Trận.
  5. *Vạch trần âm mưu "Mượn đao đào ngọc" & Quyết định cảm tử*: Doãn Hàm Yên chất vấn vì sao mật báo Thành Đô khẳng định giang hồ đã râm ran tin tức từ 3 ngày trước khi sơn môn chưa hay biết; Ma Y Thần Tướng thừa nhận ngoại bang tung tin để ép Thúy Yên tự phá cấm địa dẹp bầy sói đào ngọc lên hòng cướp trắng.
  6. *Thế cờ ngồi trên miệng núi lửa*: Từ trường thiên thạch thức giấc kích thích bầy thú phát cuồng cắn xé đệ tử (ca bệnh Tiểu Đào), đe dọa nổ vỡ then chốt cơ quan sắt thép khiến trận pháp tự sụp đổ trong 3 ngày tới. Lệ Thu Thủy dũng cảm nhận lãnh trách nhiệm cảm tử xông vào Xuân Hoa Viên dọn sói đào ngọc, dùng hộp đồng bọc chì ngâm dầu trẩu phong tỏa từ trường; Doãn Hàm Yên quyết đoán hạ lệnh Chấp pháp đường và Hạ Nương xuất kích phối hợp.

---

## 2. Đề Xuất Cập Nhật Sổ Cái Thương Tật (`worldbuilding/medical/injuries_ledger.md`)

```diff
Index: worldbuilding/medical/injuries_ledger.md
===================================================================
--- worldbuilding/medical/injuries_ledger.md
+++ worldbuilding/medical/injuries_ledger.md
@@ -85,3 +85,13 @@
+
+### J. Tiểu Đào (Đệ tử tuần sơn Dược phòng Thúy Yên Môn)
+
+| Vết thương # | Vị trí & Dạng tổn thương | Cấp độ | Tác nhân / Hoàn cảnh | Hồi xuất hiện | Trạng thái hiện tại | Di chứng & Ảnh hưởng hành vi |
+| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
+| `INJ-TD-001` | Cổ chân phải (răng nanh rắn lục Điểm Thương cắn) & Trật khớp mắt cá ngoài | Level 1 (Nhẹ) | Rắn lục tấn công khi tuần tra ven hồ Điền Trì; ngã trật khớp mắt cá | Chương 03 | Đã được Hạ Nương trích nọc, áp cao độc thảo dĩ độc trị độc, nắn khớp cố định nẹp tre | Kiêng chạy nhảy mạnh trong 5 ngày; bình phục hoàn toàn |
```

---

## 3. Đề Xuất Cập Nhật Hồ Sơ Nhân Vật Chính & Bản Lề (Protagonists & Anchors)

```diff
Index: characters/ha_nuong.md
===================================================================
--- characters/ha_nuong.md
+++ characters/ha_nuong.md
@@ -25,3 +25,8 @@
 - Tuổi: 16 tuổi (sinh năm 1175 - Ất Mùi).
 - Thân phận: Đệ tử Điền Trì Dược Phòng, Thúy Yên Môn (Bách Hoa Cốc, Điểm Thương Sơn).
 - Lăng kính cốt lõi: Y đạo Thực chứng (The Empirical Healer); duy vật thực nghiệm, không tin dị đoan.
+
+* Chuyển biến Chương 03:
+  - Cấp cứu thành công ca rắn độc kèm trật khớp cho Tiểu Đào;
+  - Cầm la bàn tầm long đo đạc 4 hoa viên, phát hiện dấu vết đào bới bất thường của bầy sói xám;
+  - Nhận lệnh từ Doãn Hàm Yên mang hòm thuốc dã chiến và kim sang dược theo sau tiếp ứng cứu thương cho đoàn cảm tử tiến vào Bách Hoa Trận.
```

---

## 4. Đề Xuất Bổ Sung & Đồng Bộ Danh Bạ Nhân Vật Phụ (`characters/supporting_cast.md`)

```diff
Index: characters/supporting_cast.md
===================================================================
--- characters/supporting_cast.md
+++ characters/supporting_cast.md
@@ -40,3 +40,21 @@
+| **Doãn Hàm Yên** | **A** | Lục Đại Môn Chủ Thúy Yên Môn | 40 tuổi (sinh 1151). Phu nhân Đường Nhất Trần, mẹ Doãn Tiêu Vũ (17t) và Đường Hiểu (17t). Sư muội Lệ Thu Thủy. | Thúy Yên Kiếm Pháp / Chưởng môn ngọc bài | Đang chấn hưng môn phái, giải quyết bài toán kinh tài khó khăn; vạch trần âm mưu 'mượn đao đào ngọc' của ngoại bang và quyết đoán hạ lệnh phòng thủ cấm địa | Xuất hiện Ch.03, Ch.08a, Ch.08b, Ch.11 |
+| **Lệ Thu Thủy** | **A** | Tiền Chưởng môn Thúy Yên Môn | 43 tuổi (sinh 1148). Sư tỷ Doãn Hàm Yên. Người từng nhận lời cảnh báo của Tiêu Lăng Phong 19 năm trước tại bến đò Giang Nam. | Băng Tâm Song Kiếm / Phù Vân Kiếm | Trở về cốc sau nhiều năm biệt tích; dũng cảm nhận lãnh trách nhiệm cảm tử xông vào Xuân Hoa Viên dọn sói đào ngọc để ngăn ngừa nguy cơ nổ vỡ cấm địa từ bên trong | Xuất hiện Ch.03, Ch.08a, Ch.08b |
+| **Ma Y Thần Tướng** | **B** | Thuật sĩ Kham Dư giang hồ / Ma Y phái | Trạc 45–50 tuổi. Áo vải thô chắp vá xám tro, râu tóc rối bù. | Thuật Kham Dư Bát Quái / La bàn tầm long cổ | Mang la bàn cổ 24 phương vị vào cốc đo đạc ngọc khí; thừa nhận cạm bẫy 'mượn đao đào ngọc' của giặc ngoại bang | Xuất hiện Ch.03 |
+| **Đan Bích Tú** | **B** | Đệ tử Chấp pháp đường Thúy Yên Môn | 23 tuổi (sinh 1168). Sư tỷ gác cổng Bách Hoa Cốc. | Song đoản kiếm / Giáp gai | Chấp hành mệnh lệnh Chưởng môn; điều động 10 đệ tử mang giáp gai và đuốc lửa xông vào Bách Hoa Trận bảo vệ Lệ Thu Thủy | Xuất hiện Ch.03, Ch.08a, Ch.08b, Ch.11 |
+| **Tiểu Đào** | **C** | Đệ tử sơ cấp Điền Trì Dược Phòng | 14 tuổi (sinh 1177). Đệ tử tuần sơn. | Nẹp tre / Thuốc hoàng liên | Bị rắn độc Điểm Thương cắn kèm trật khớp mắt cá ngoài (`INJ-TD-001` L1); được Hạ Nương cứu chữa kịp thời | Xuất hiện Ch.03 |
```

---

## 5. Đề Xuất Cập Nhật Sổ Cái Bảo Vật & Cơ Quan (`worldbuilding/artifacts/artifacts_ledger.md`)

```diff
Index: worldbuilding/artifacts/artifacts_ledger.md
===================================================================
--- worldbuilding/artifacts/artifacts_ledger.md
+++ worldbuilding/artifacts/artifacts_ledger.md
@@ -25,3 +25,12 @@
+
+### B. Du Long Giác (Mảnh Thần Khí Tọa Độ Non Sông)
+
+- **Nguồn gốc lịch sử**: Báu vật trấn quốc từ thời Tống Thái Tổ Triệu Khuông Dẫn; chứa mạng lưới tọa độ Trụ Thần Thạch ngàn năm.
+- **Vị trí trấn yểm**: Khai sơn tổ sư Thúy Yên Môn — Doãn Tuyết Dao — bí mật phong ấn tại tâm cấm địa Bách Hoa Trận (Điền Trì, Tây Nam) từ thời Tống sơ làm trận nhãn hộ sơn.
+- **Cơ chế vật lý**: Khối thiên thạch cổ có từ trường cực mạnh, tác động lên kim sắt la bàn và kích thích hệ thần kinh dã thú phát cuồng.
+- **Phương pháp cách ly**: Phải dùng hộp đồng bọc chì ngâm dầu trẩu để phong tỏa hoàn toàn từ trường bức xạ.
+- **Hiện trạng Chương 03**: Từ trường thức giấc sau trăm năm; tâm điểm rơi đúng giao điểm 4 hoa viên tại Bách Hoa Trận; đang bị đoàn cảm tử mở đường khai quật.
```

---

## 6. Đề Xuất Cập Nhật Ma Trận Quan Hệ Phe Phái (`worldbuilding/factions/relationships_matrix.md`)

```diff
Index: worldbuilding/factions/relationships_matrix.md
===================================================================
--- worldbuilding/factions/relationships_matrix.md
+++ worldbuilding/factions/relationships_matrix.md
@@ -45,3 +45,9 @@
+
+### Thúy Yên Môn <-> Thế Lực Ngoại Bang & Giang Hồ Tà Phái (1191-08-17)
+
+- **Quan hệ**: Đối đầu trinh thám ngấm ngầm (Sát cơ cận kề).
+- **Bản chất xung đột**: Kẻ địch (Tây Hạ Nhất Phẩm Đường, mật thám Kim quốc) biết Du Long Giác nằm ở Thúy Yên nhưng sợ cạm bẫy cơ quan và đàn sói Điểm Thương nên tung tin đồn ra khắp giang hồ nhằm 'mượn đao đào ngọc', ép Thúy Yên tự phá trận để chúng ập vào cướp.
+- **Thái độ Thúy Yên**: Doãn Hàm Yên và Lệ Thu Thủy đồng thuận sách lược đi trước kẻ thù một bước, chấp nhận cảm tử dọn sói đào ngọc để phong tỏa kiểm soát bảo vật trước khi giặc kéo đến.
```

---

## 7. Đề Xuất Cập Nhật Bảng Theo Dõi Lời Hứa Cốt Truyện (`plot/promises_tracker.md`)

```diff
Index: plot/promises_tracker.md
===================================================================
--- plot/promises_tracker.md
+++ plot/promises_tracker.md
@@ -35,3 +35,11 @@
+| **TH-005** | **Sấm truyền Huyết Quang Tai tại Thúy Yên Môn** | Chương 03 | Hạ Nương / Doãn Hàm Yên | Ma Y Thần Tướng sấm truyền huyết quang tai; Doãn Hàm Yên vạch trần âm mưu mượn đao đào ngọc của giặc; đoàn người tiến vào Bách Hoa Trận | **Chương 08a & 08b** | **Chương 13** (*Huyết Quang Tai*) | `OPENED / HIGH THREAT` (Kích hoạt ngòi nổ tai kiếp) |
+| **TH-007** | **Lời cảnh báo 19 năm trước & Bí mật Trụ Thần Thạch** | Chương 03 | Hạ Nương / Lệ Thu Thủy | Tiêu Lăng Phong 19 năm trước (1174) ở bến đò Giang Nam từng cảnh báo Lệ Thu Thủy về bí mật Du Long Giác thời Tống Thái Tổ; món nợ sa trường Lệ Thu Thủy phải gánh | **Chương 08b & Chương 13** | **Quyển 2** | `PLANTED / CORE MYSTERY` (Khởi động tuyến thân thế) |
```

---

## 8. Đề Xuất Cập Nhật Biên Niên Sử & Outline Deck (`plot/timeline.md` & `plot/volume_01_deck.md`)

```diff
Index: plot/timeline.md
===================================================================
--- plot/timeline.md
+++ plot/timeline.md
@@ -28,3 +28,4 @@
+  * *Bách Hoa Cốc - Điền Trì (1191-08-17 Sáng sớm đến Hoàng hôn):* Hạ Nương cấp cứu Tiểu Đào bị rắn cắn; Doãn Hàm Yên lo toan kinh tài; Lệ Thu Thủy dẫn Ma Y Thần Tướng mang la bàn về cốc; đo đạc 4 hoa viên phát hiện Du Long Giác thời Tống Thái Tổ chôn dưới Bách Hoa Trận; Doãn Hàm Yên vạch trần âm mưu 'mượn đao đào ngọc' của ngoại bang; Lệ Thu Thủy nhận lãnh sứ mệnh cảm tử dẫn Chấp pháp đường và Hạ Nương tiến vào cấm địa dọn sói đào ngọc (`Task 12: Subtask 85` — **Chương 03 đã canon hóa**).
```

---

## 9. Phê Duyệt Của Tác Giả (Author Sign-Off)

- [x] **Phê chuẩn toàn bộ (Accept all)**: Toàn bộ 4 trụ cột đã đồng bộ tuyệt đối với phả hệ, niên biểu và quyết định trinh thám của Tác giả.
- [ ] **Yêu cầu chỉnh sửa thêm (Request changes)**:
