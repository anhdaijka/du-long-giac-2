# Đề Xuất Canon Diff: Chương 01 — Rượu Nếp Giang Tân

> **Cơ quan quản lý**: Novel OS State Ledger  
> **Trạng thái**: Chờ Tác giả xem xét và phê chuẩn trước khi commit vào Sổ cái trạng thái bền vững (Cổng Dừng 3).

---

## 1. Tóm Tắt Biến Chuyển Cốt Truyện & Nhân Vật (Narrative Summary)

* **POV**: Tiêu Phùng (17 tuổi — Thiếu niên bãi sậy Giang Tân Thôn / Nghĩa quân Ba Lăng).
* **Mốc thời gian**: 1191-08-12 (Chiều tối đến Đêm).
* **Địa điểm**: Bờ đê Động Đình Hồ, Quán rượu Điềm Tửu Thúc, Doanh trại Nghĩa quân Ba Lăng.
* **Biến chuyển cốt lõi**:
  1. *Lăng kính thiếu niên bãi sậy*: Tiêu Phùng 17 tuổi, lớn lên giữa gió cát Động Đình Hồ; ngoài mặt cợt nhả lười biếng, câu cá bắt ếch, nhưng bên trong nung nấu khao khát tìm lại tung tích người cha mất tích 17 năm trước ở bến Hán Thủy.
  2. *Đổi rượu lấy đinh tán*: Dùng vò rượu nếp 'Thu Phân Điềm Tửu' trộm từ hầm rượu trại nghĩa quân đổi lấy việc Điềm Tửu Thúc gia cố ống sắt bịt 4 đinh tán đồng cho cây đoản côn gỗ nghiến; Điềm Tửu Thúc nhìn thấu bản tính sinh tồn thực dụng của chàng.
  3. *Đối thoại đêm với Thu Di (Bạch Thu Lâm)*: Thu Di phát hiện việc trộm rượu nhưng không phạt nặng; bộc lộ sự xót xa của người tỷ tỷ chăm sóc chàng từ tấm bé; chuẩn hóa xưng hô mẫu mực "Thu Di / Tỷ — Đệ" (Bạch Thu Lâm 24 tuổi, Tiêu Phùng 17 tuổi).
  4. *Nguồn gốc nghĩa quân & Bí mật Hán Thủy*: Tiêu Phùng được lão tướng Bạch Cương liều chết ẵm thoát khỏi trận Hán Thủy Cổ Độ 17 năm trước (1174), cùng thân phụ của Thu Di (Tướng quân Bạch Phụ) đưa về Ba Lăng và cùng toàn trại nuôi nấng.
  5. *Nhiệm vụ đầu đời*: Thu Di giao nhiệm vụ sáng mai mang cá trê sang biếu Long Ngũ Thái Gia và tới tiệm Bất Động Tiên Sinh lấy vải bạt gia cố trại.

---

## 2. Đề Xuất Cập Nhật Sổ Cái Thương Tật (`worldbuilding/medical/injuries_ledger.md`)
*(Chưa phát sinh chấn thương sa trường lớn; Tiêu Phùng chỉ có vết muỗi đốt kết vảy bắp chân)*

---

## 3. Đề Xuất Cập Nhật Hồ Sơ Nhân Vật Chính & Bản Lề (Protagonists & Anchors)

```diff
Index: characters/tieu_phung.md
===================================================================
--- characters/tieu_phung.md
+++ characters/tieu_phung.md
@@ -10,3 +10,8 @@
 - Tuổi: 17 tuổi (sinh năm 1174 - Giáp Ngọ).
 - Xuất thân: Mồ côi sau thảm sát Hán Thủy Cổ Độ 1174; được lão tướng Bạch Cương bế về Ba Lăng, cùng Tướng quân Bạch Phụ và toàn trại nghĩa quân nuôi dưỡng.
 - Vũ khí: Đoản côn gỗ nghiến bãi sậy (dài 2 thước rưỡi, hai đầu bịt ống sắt non đóng 4 đinh tán đồng dẹt).
+
+* Chuyển biến Chương 01:
+  - Gia cố đoản côn tại quán Điềm Tửu Thúc;
+  - Nhận nhiệm vụ xuất hành sang trang viên Long Ngũ Thái Gia;
+  - Kích hoạt tâm nguyện tìm kiếm tung tích thân phụ Tiêu Lăng Phong.
```

---

## 4. Đề Xuất Bổ Sung & Đồng Bộ Danh Bạ Nhân Vật Phụ (`characters/supporting_cast.md`)

```diff
Index: characters/supporting_cast.md
===================================================================
--- characters/supporting_cast.md
+++ characters/supporting_cast.md
@@ -15,3 +15,15 @@
+| **Bạch Thu Lâm (Thu Di)** | **A** | Thủ lĩnh Nghĩa quân Ba Lăng | 24 tuổi (sinh 1167). Ái nữ của cố Tướng quân Bạch Phụ tại Biện Kinh. Nghĩa tỷ kiêm người bảo hộ của Tiêu Phùng. Xưng hô: Thu Di / Tỷ — Đệ. | Thương pháp Bạch gia / Du Long Kiếm | Quản lý quân doanh, nghiêm khắc rèn giũa Tiêu Phùng nhưng hết lòng yêu thương bảo bọc | Xuất hiện Ch.01, Ch.04b, Ch.05, Ch.06, Ch.09 |
+| **Điềm Tửu Thúc** | **B** | Thợ rèn kiêm chủ quán rượu Giang Tân Thôn | ~48–50 tuổi. Cựu binh nghĩa quân mai danh ẩn tích. | Búa rèn / Lò than | Rèn ống sắt bịt đoản côn cho Tiêu Phùng; răn dạy đạo lý sinh tồn nơi đầu sóng | Xuất hiện Ch.01 |
+| **Bạch Cương** | **B** | Nghĩa quân tiền bối / Cố nhân Ma Y Cốc | ~45 tuổi. Cựu thuộc hạ của Tiêu Lăng Phong. | Đao sa trường | Người đã liều chết bế bọc tã Tiêu Phùng sơ sinh thoát khỏi vũng máu Hán Thủy Cổ Độ năm 1174 đưa về Ba Lăng | Gieo mầm Ch.01, Xuất hiện Ch.05 |
```

---

## 5. Đề Xuất Cập Nhật Sổ Cái Bảo Vật & Cơ Quan (`worldbuilding/artifacts/artifacts_ledger.md`)

```diff
Index: worldbuilding/artifacts/artifacts_ledger.md
===================================================================
--- worldbuilding/artifacts/artifacts_ledger.md
+++ worldbuilding/artifacts/artifacts_ledger.md
@@ -10,3 +10,7 @@
+
+### Đoản Côn Gỗ Nghiến (Tiêu Phùng)
+- Dài 2 thước rưỡi, đẽo từ rễ cây gỗ nghiến bãi sậy Động Đình.
+- Hai đầu bịt ống sắt non đóng 4 đinh tán đồng dẹt do Điềm Tửu Thúc tôi luyện nước sông.
```

---

## 6. Đề Xuất Cập Nhật Ma Trận Quan Hệ Phe Phái (`worldbuilding/factions/relationships_matrix.md`)

```diff
Index: worldbuilding/factions/relationships_matrix.md
===================================================================
--- worldbuilding/factions/relationships_matrix.md
+++ worldbuilding/factions/relationships_matrix.md
@@ -20,3 +20,7 @@
+
+### Tiêu Phùng <-> Bạch Thu Lâm (Thu Di)
+- **Mối quan hệ**: Nghĩa tỷ đệ gắn bó máu thịt, người giám hộ và dẫn dắt.
+- **Xưng hô chuẩn mực**: Thu Di / Tỷ — Đệ. Thu Di vừa nghiêm khắc rèn nết vừa che chở Tiêu Phùng trước giông bão giang hồ.
```

---

## 7. Đề Xuất Cập Nhật Bảng Theo Dõi Lời Hứa Cốt Truyện (`plot/promises_tracker.md`)

```diff
Index: plot/promises_tracker.md
===================================================================
--- plot/promises_tracker.md
+++ plot/promises_tracker.md
@@ -15,3 +15,7 @@
+| **TH-001** | **Thân thế cha Tiêu Phùng & Huyết kiếp Hán Thủy Cổ Độ** | Chương 01 | Tiêu Phùng / Thu Di | Tiêu Phùng nung nấu tìm cha; Thu Di hứa khi đủ lông đủ cánh sẽ nói rõ chân tướng | **Chương 04b & Chương 05** | **Quyển 2** | `OPENED / CORE MYSTERY` |
+| **TH-002** | **Nhiệm vụ Long Ngũ Thái Gia & Tiệm Bất Động** | Chương 01 | Tiêu Phùng | Thu Di giao nhiệm vụ sang trang viên Long Ngũ biếu cá và lấy vải bạt | **Chương 04b** | **Hồi 1** | `OPENED / QUEST STEP` |
```

---

## 8. Đề Xuất Cập Nhật Biên Niên Sử & Outline Deck (`plot/timeline.md` & `plot/volume_01_deck.md`)

```diff
Index: plot/timeline.md
===================================================================
--- plot/timeline.md
+++ plot/timeline.md
@@ -20,3 +20,4 @@
+  * *Giang Tân Thôn & Trại Nghĩa Quân Ba Lăng (1191-08-12 Chiều tối đến Đêm):* Tiêu Phùng câu cá bên đê Động Đình Hồ; đổi rượu nếp lấy ống sắt bịt đoản côn tại quán Điềm Tửu Thúc; đối thoại đêm với Thu Di (Bạch Thu Lâm); nhận nhiệm vụ tiếp cận Long Ngũ Thái Gia (`Task 00: Subtask 01` — **Chương 01 đã canon hóa**).
```

---

## 9. Phê Duyệt Của Tác Giả (Author Sign-Off)

- [x] **Phê chuẩn toàn bộ (Accept all)**: Toàn bộ 4 trụ cột đã đồng bộ tuyệt đối với phả hệ, bối phận và niên biểu mới.
- [ ] **Yêu cầu chỉnh sửa thêm (Request changes)**:
