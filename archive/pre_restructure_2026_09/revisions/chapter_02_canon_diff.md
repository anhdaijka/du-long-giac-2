# Đề Xuất Canon Diff: Chương 02 — Chiến Thuyền Tỷ Võ (02a & 02b)

> **Cơ quan quản lý**: Novel OS State Ledger  
> **Trạng thái**: Chờ Tác giả xem xét và phê chuẩn trước khi commit vào Sổ cái trạng thái bền vững (Cổng Dừng 3).

---

## 1. Tóm Tắt Biến Chuyển Cốt Truyện & Nhân Vật (Narrative Summary)

* **POV**: Tĩnh Xuyên (20 tuổi — Tiểu tướng kỵ binh thiết giáp Thanh Loa Đảo / Thiên Vương Bang).
* **Mốc thời gian**: 1191-08-16 (Sáng sớm đến Giữa trưa).
* **Địa điểm**: Soái hạm ba tầng khoang Thiên Vương Bang, Đảo Thanh Loa, Động Đình Hồ.
* **Biến chuyển cốt lõi**:
  1. *Lăng kính tiểu tướng sa trường & Đạo hiếu*: Tĩnh Xuyên 20 tuổi (sinh 1171 - Tân Mão, tuổi nhược quán); mồ côi cha Tĩnh Hùng năm 10 tuổi (1181) sau trận Trường Giang; có 10 năm đan cói, sắc thuốc phụng dưỡng mẹ mù Diệp Mẫu trên đảo Thanh Loa; tôn sùng kỷ luật sắt sa trường.
  2. *Chuyển giao quyền lực lịch sử*: Lão Bang chủ Anh Cô (Dương Anh, ~63 tuổi) thoái ẩn sau hơn mười năm bặt vô âm tín, trao lại đồng bài Bang chủ cho nghĩa tử Dương Thiết Tâm (42 tuổi, sinh ~1149, đệ tử Côn Lôn Kiếm Hoàng Sở Khi Thiên).
  3. *Đại hội tỷ võ trên 3 tầng khoang*: Phe cựu trào Lâu Nhất Quan phản đối; Anh Cô hạ lệnh tỷ võ thử thách; Dương Thiết Tâm dùng thương pháp biến ảo đả bại liên tiếp Tam đại dũng tướng (Tần Công Xích, Lê Việt, Lưu Mặc).
  4. *Khảo nghiệm thế thương Tĩnh Xuyên*: Thiết Tâm nhận ra Bát Hàn Thiết Thương nẹp da đầu hổ của cố danh tướng Tĩnh Hùng; mời Tĩnh Xuyên xuất thế thương 'Thiết Bích Khóa Giang'; nương đà điểm trúng khâu sắt chỉ điểm và ngợi khen phong thái con nhà tông, kỷ luật mẫu mực; thiết lập niềm tin cậy sâu sắc.
  5. *Đăng quang & Sóng ngầm chia rẽ*: Dương Thiết Tâm chính thức đăng quang Tân Bang chủ; Anh Cô chèo thuyền nan về Hồ Tâm Cô Đảo; Lâu Nhất Quan bằng mặt không bằng lòng, nuôi mối thù hận chia rẽ môn phái.

---

## 2. Đề Xuất Cập Nhật Sổ Cái Thương Tật (`worldbuilding/medical/injuries_ledger.md`)
*(Tam đại dũng tướng chỉ trúng đòn khảo nghiệm kình lực, tụ máu phần mềm L1, không gây tàn tật; Tĩnh Xuyên nguyên vẹn thể trạng)*

---

## 3. Đề Xuất Cập Nhật Hồ Sơ Nhân Vật Chính & Bản Lề (Protagonists & Anchors)

```diff
Index: characters/tinh_xuyen.md
===================================================================
--- characters/tinh_xuyen.md
+++ characters/tinh_xuyen.md
@@ -10,4 +10,10 @@
 - Tuổi: 20 tuổi (sinh năm 1171 - Tân Mão, tuổi nhược quán).
 - Thân phận: Tiểu tướng thị vệ thuộc trướng Quý tổng quản, kỵ binh thiết giáp Thanh Loa Đảo.
 - Vũ khí: Bát Hàn Thiết Thương (nặng 23 cân, thân sắt nguội dài 1 trượng 2 thước, khâu nối bọc da đầu hổ mòn lông tơ).
 - Điểm tựa tinh thần: Mẹ mù Diệp Mẫu; lời răn sa trường 'kẻ nào coi mạng mình nhẹ như lông hồng, kẻ đó chôn xác trước tiên'.
+
+* Chuyển biến Chương 02 (02a & 02b):
+  - Xuất thế thương 'Thiết Bích Khóa Giang' khảo nghiệm cùng Tân Bang chủ;
+  - Được Dương Thiết Tâm ngợi khen kỷ luật và điểm trúng khâu sắt chỉ điểm kiếm ý dung hợp thương pháp;
+  - Sẵn sàng đón nhận quân lệnh cơ mật từ tân chủ.
```

---

## 4. Đề Xuất Bổ Sung & Đồng Bộ Danh Bạ Nhân Vật Phụ (`characters/supporting_cast.md`)

```diff
Index: characters/supporting_cast.md
===================================================================
--- characters/supporting_cast.md
+++ characters/supporting_cast.md
@@ -25,4 +25,18 @@
+| **Dương Thiết Tâm** | **A** | Tân Bang chủ đời thứ hai Thiên Vương Bang | 42 tuổi (sinh ~1149). Nghĩa tử Anh Cô, đệ tử Côn Lôn Kiếm Hoàng Sở Khi Thiên. | Thương pháp Côn Lôn / Thiết Giáp Bát Quái Thương | Thu phục nhân tâm bằng võ đức và thương pháp cái thế; đăng quang Bang chủ | Xuất hiện Ch.02a, Ch.02b, Ch.07a, Ch.07b, Ch.10 |
+| **Dương Anh (Anh Cô)** | **A** | Lão Bang chủ sáng lập Thiên Vương Bang | ~63 tuổi (sinh ~1128). | Khinh công lướt sóng / Áo tơi nón lá | Thoái ẩn về Hồ Tâm Cô Đảo sau khi chuyển giao quyền lực thành công | Xuất hiện Ch.02a, Ch.02b |
+| **Lâu Nhất Quan** | **B** | Trưởng lão phe bảo thủ Thiên Vương Bang | ~63 tuổi (bậc nguyên lão khai quốc cùng thời Anh Cô). | Đoản đao / Phủ việt | Ganh ghét Tân Bang chủ, bằng mặt không bằng lòng; nuôi dã tâm chia rẽ nội bộ | Xuất hiện Ch.02a, Ch.02b |
+| **Diệp Mẫu** | **B** | Thân mẫu của Tĩnh Xuyên | ~49 tuổi. Mù lòa sau trận Trường Giang 1181 khi phu quân Tĩnh Hùng tử trận. | Chõng tre / Giỏ cói | Điểm tựa đạo đức và lương tri sa trường cho Tĩnh Xuyên | Xuất hiện Ch.02a |
```

---

## 5. Đề Xuất Cập Nhật Sổ Cái Bảo Vật & Cơ Quan (`worldbuilding/artifacts/artifacts_ledger.md`)

```diff
Index: worldbuilding/artifacts/artifacts_ledger.md
===================================================================
--- worldbuilding/artifacts/artifacts_ledger.md
+++ worldbuilding/artifacts/artifacts_ledger.md
@@ -15,4 +15,9 @@
+
+### Bát Hàn Thiết Thương (Tĩnh Xuyên)
+- Rèn từ thép nguội đáy sông Trường Giang; dài 1 trượng 2 thước, nặng 23 cân.
+- Cán thương nẹp da đầu hổ do cố danh tướng Tĩnh Hùng để lại; có thêm vết chạm điểm thương của Dương Thiết Tâm trên khâu sắt.
+
+### Đồng Bài Bang Chủ Thiên Vương Bang
+- Đúc bằng đồng đen, thêu hình hai ngọn giáo bắt chéo; đã chuyển giao từ Dương Anh sang Dương Thiết Tâm.
```

---

## 6. Đề Xuất Cập Nhật Ma Trận Quan Hệ Phe Phái (`worldbuilding/factions/relationships_matrix.md`)

```diff
Index: worldbuilding/factions/relationships_matrix.md
===================================================================
--- worldbuilding/factions/relationships_matrix.md
+++ worldbuilding/factions/relationships_matrix.md
@@ -25,4 +25,9 @@
+
+### Nội bộ Thiên Vương Bang (1191-08-16)
+- **Dương Thiết Tâm <-> Tĩnh Xuyên**: Mối quan hệ chủ tướng - tiểu tướng tin cậy; Thiết Tâm nhận ra phẩm chất kỷ luật sa trường của Tĩnh Xuyên và có ý cất nhắc vào trọng trách cơ mật.
+- **Dương Thiết Tâm <-> Lâu Nhất Quan**: Bằng mặt không bằng lòng; phe bảo thủ nghi kỵ người ngoài, mầm mống cho biến cố phản nghịch.
```

---

## 7. Đề Xuất Cập Nhật Bảng Theo Dõi Lời Hứa Cốt Truyện (`plot/promises_tracker.md`)

```diff
Index: plot/promises_tracker.md
===================================================================
--- plot/promises_tracker.md
+++ plot/promises_tracker.md
@@ -20,4 +20,8 @@
+| **TH-003** | **Chuyển giao quyền lực Thiên Vương Bang** | Chương 02a | Tĩnh Xuyên / Thiết Tâm | Anh Cô nhường ngôi; Thiết Tâm tỷ võ thu phục nhân tâm | **Chương 02b** | **Hồi 1** | `RESOLVED / PAID OFF` |
+| **TH-004** | **Sóng ngầm chia rẽ của Lâu Nhất Quan** | Chương 02b | Tĩnh Xuyên / Lâu Nhất Quan | Lâu Nhất Quan ôm hận thất bại, mưu toan vu oan gián điệp | **Chương 07a & 07b** | **Hồi 2** | `OPENED / FACTION CONFLICT` |
```

---

## 8. Đề Xuất Cập Nhật Biên Niên Sử & Outline Deck (`plot/timeline.md` & `plot/volume_01_deck.md`)

```diff
Index: plot/timeline.md
===================================================================
--- plot/timeline.md
+++ plot/timeline.md
@@ -24,4 +24,4 @@
+  * *Chiến thuyền Thanh Loa Đảo - Động Đình Hồ (1191-08-16 Sáng sớm đến Trưa):* Tĩnh Xuyên (20 tuổi) theo Quý Thúc Ban lên soái hạm; Dương Anh nhường ngôi cho Dương Thiết Tâm; đại hội tỷ võ 3 tầng khoang; Thiết Tâm khảo nghiệm thương pháp Tĩnh Xuyên và đăng quang Tân Bang chủ (`Task 01: Subtask 01 & 02` — **Chương 02a & 02b đã canon hóa**).
```

---

## 9. Phê Duyệt Của Tác Giả (Author Sign-Off)

- [x] **Phê chuẩn toàn bộ (Accept all)**: Toàn bộ 4 trụ cột đã đồng bộ tuyệt đối với phả hệ, niên biểu 17 năm và tuổi debut 20 của Tĩnh Xuyên.
- [ ] **Yêu cầu chỉnh sửa thêm (Request changes)**:
