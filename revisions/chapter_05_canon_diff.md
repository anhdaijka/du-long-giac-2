# Đề Xuất Canon Diff: Chương 05 — Tuyệt Vấn Huyết Lộ

> **Cơ quan quản lý**: Novel OS State Ledger  
> **Trạng thái**: Chờ Tác giả xem xét và phê chuẩn trước khi commit vào Sổ cái trạng thái bền vững (Cổng Dừng 3).

---

## 1. Tóm Tắt Biến Chuyển Cốt Truyện & Nhân Vật (Narrative Summary)

- **POV**: Tiêu Phùng (17 tuổi — Hẻm núi Tuyệt Vấn Pha, Ba Lăng Huyện).
- **Thời gian**: 1191-08-18 (Hoàng hôn đến Đêm bão).
- **Biến cố sa trường cốt tử**:
  - Tiêu Phùng cùng Bạch Thu Lâm và nghĩa quân giải cứu Bạch Cương tại hang đá Tuyệt Vấn Pha;
  - Lần đầu tiên nếm trải chiến trường đẫm máu sa trường; thi triển ngón nghề bãi sậy tinh quái tiểu nhân chuẩn Châu Tinh Trì (Quyết định D-021);
  - Trả món nợ Âm kình cho Thẩm Thiết Thạch: Tiêu Phùng dùng mưu bẩn phá kình của Bách hộ Ngột Thất Hãn (Ô Sơ Sa - Kim quốc);
  - Tiêu Phùng gánh chịu **thuế chấn thương sa trường (Damage Tax L3)**: bị rạn xương sườn số 6 mạn sườn trái, nôn máu bầm tím buốt ngực, nẹp tre quấn vải gai cố định;
  - Trùng phùng Bạch Cương sau 17 năm, tiếp nhận bài Sấm Thi 4 câu của Tiêu Lăng Phong: *"Thái bạch dạ quan tinh / Trọc khí quy tam thanh / Thiên mã chấn trường dực / Long Cung trích tử anh"*;
  - Nút thắt thảm họa kép: Nội gián cắt đứt gân chân Cơ quan đại sư Giới Sơn Tông, mở tung chín van xả lũ đê quai; Động Đình bão lụt ngập tràn, còi báo động vỡ đê hú vang.

---

## 2. Đề Xuất Cập Nhật Sổ Cái Thương Tật (`worldbuilding/medical/injuries_ledger.md`)

```diff
Index: worldbuilding/medical/injuries_ledger.md
===================================================================
--- worldbuilding/medical/injuries_ledger.md
+++ worldbuilding/medical/injuries_ledger.md
@@ -48,7 +48,7 @@
 | **INJ-TP-001** | Bả vai phải & ức ngực: bầm tím cơ, trầy da sâu. | **L1** | Va chạm với Hắc Hùng trong hang đá gò Bồ Đề. | Chương 04b | Đang giảm sưng, hơi ê ẩm khi vung gậy. | Còn dấu vết bầm đen tím nhạt dưới da. |
-| **INJ-TP-002** | *(Dự kiến)* Mạn sườn trái: rạn 1 xương sườn, dư chấn Âm kình làm ho ra huyết ứ. | **L3** | Trúng dư kình chưởng phong của Đầu mục sát thủ Kim quốc tại Tuyệt Vấn Pha. | Chương 05 | **Chờ kích hoạt tại Ch.05** | Bó nẹp tre 4 tuần; mỗi nhịp thở sâu đều đau nhói; cấm vận sức mạnh ở tay trái; sợ gió lạnh. |
+| **INJ-TP-002** | Mạn sườn trái: nứt rạn xương sườn số 6, dư chấn Âm kình hàn độc nghẽn tạng phủ, ho ra huyết ứ tím bầm. | **L3** | Trúng cú cùi chỏ sắt và luồng kình phản chấn của Bách hộ Ngột Thất Hãn tại Tuyệt Vấn Pha. | Chương 05 | **ĐANG ĐIỀU TRỊ (Tuần 1/6)**. Đã nẹp tre cố định. | Bó nẹp tre 4–6 tuần; đau buốt óc mỗi nhịp thở sâu hoặc ho; cấm vận sức tay trái; buốt lạnh khi trời mưa gió. |
 
 ### C. Bạch Cương (Trung niên — Binh sĩ Tương Dương)
@@ -62,7 +62,7 @@
 | Vết thương # | Vị trí & Dạng tổn thương | Cấp độ | Tác nhân / Hoàn cảnh | Hồi xuất hiện | Trạng thái hiện tại | Di chứng & Ảnh hưởng hành vi |
 | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
-| **INJ-BC-001** | Bả vai trái đao chém thấu cơ, ngực trúng chưởng phong Âm kình, mất máu nặng. | **L3** | Bị toán thích khách Kim quốc phục kích tại Tuyệt Vấn Pha. | Chương 05 | Nguy kịch, hôn mê, mất máu. | Cần sơ cứu khẩn cấp, bất động dưỡng thương dài ngày tại Ba Lăng Huyện. |
+| **INJ-BC-001** | Bả vai trái đao chém thấu cơ, ngực trúng chưởng phong Âm kình cực hàn, mất máu nặng, suy kiệt. | **L3** | Bị toán thích khách Ô Sơ Sa phục kích tại Tuyệt Vấn Pha. | Chương 05 | **NGUY KỊCH / ỔN ĐỊNH TẠM THỜI**. Đã rịt thuốc rừng và sơ cứu. | Hôn mê từng chặng, thở yếu; cần đưa về y quán Ba Lăng Huyện điều trị dài ngày; không thể tiếp tục chiến đấu. |
```

---

## 3. Đề Xuất Cập Nhật Sổ Động Thái Võ Học (`worldbuilding/martial/martial_dynamics.md`)

```diff
Index: worldbuilding/martial/martial_dynamics.md
===================================================================
--- worldbuilding/martial/martial_dynamics.md
+++ worldbuilding/martial/martial_dynamics.md
@@ -62,8 +62,10 @@
 - **Chiêu thức & Ngón nghề hiện có**:
   - *Đoản côn gỗ nghiến*: Đòn gánh bến sông, chọc chấn thủy, thụt hạ bộ (*"Gió xuân thổi vỡ ấm trà"*), giẫm mu bàn chân.
   - *Đòn bẩn bãi sậy (Châu Tinh Trì Style - Quyết định D-021)*: Ném vôi bột, hất cát sỏi, giả vờ quỳ lạy van xin khóc lóc rồi bất ngờ cắn xé/móc mắt.
+  - *Kinh nghiệm sa trường mới (Ch.05)*: Sử dụng túi vôi sống trộn ớt khô cay xè; thụt gậy phá huyệt Khí Xung đan điền; nhận thức sâu sắc khoảng cách sinh tử giữa Tier 0 và Tier 2.
   - *Kinh nghiệm sinh tồn*: Bơi lặn nước sâu Động Đình, nín thở dưới đầm sậy, bò trườn bùn lầy.
 - **Hạn chế thể xác chí mạng**:
+  - **Đang mang chấn thương L3 (INJ-TP-002)**: Rạn nứt xương sườn số 6 bên trái, phải nẹp tre quấn vải gai, hơi thở nông, miệng rỉ máu bầm khi ho; cấm vận sức mạnh tay trái.
   - Không có hộ thể chân khí. Gặp đòn chưởng lực có nội kình (như Âm Kình giặc Kim) dù chỉ trúng gió chưởng cũng đủ rạn xương, chấn động tạng phủ, ho ra máu cục tím bầm.
   - Thể lực cạn kiệt rất nhanh sau 10–15 hiệp ẩu đả kịch liệt.
 - **Lịch sử kỳ ngộ đã được Tác giả phê duyệt**:
+  - **Chương 05**: Thể nghiệm thực tế sa trường (First Contact with Internal Force). Giữ nguyên Tier 0 thô mộc, trả giá đắt bằng chấn thương L3 để hiểu được sự khốc liệt của võ học chân chính.
```

---

## 4. Đề Xuất Cập Nhật Hồ Sơ Nhân Vật Tiêu Phùng (`characters/tieu_phung.md`)

```diff
Index: characters/tieu_phung.md
===================================================================
--- characters/tieu_phung.md
+++ characters/tieu_phung.md
@@ -48,6 +48,7 @@
 * **Quyển 1: Dã Hồ Côn Pháp & Túy Bộ Bãi Sậy — Phong cách "Tiểu nhân Châu Tinh Trì" (17 tuổi — Sinh tồn thảo dã, Decision D-021)**
   * *Binh khí:* Đoản côn gỗ nghiến bọc sắt của Điềm Tửu Thúc (`Task 157: Subtask 133`). (Khâu sắt non bị mẻ dăm sau trận Tuyệt Vấn Pha Ch.05).
+  * *Thương tật thực thể hiện tại:* Rạn xương sườn số 6 mạn sườn trái (INJ-TP-002, L3) do trúng cùi chỏ sắt của bách hộ Kim quốc Ngột Thất Hãn; nẹp tre cố định 4–6 tuần.
   * *Phong cách chiến đấu:* Hoàn toàn chưa có nội lực chính thống; áp dụng triệt để lối đánh tinh quái, mưu mẹo, thực dụng đến mức "tiểu nhân" theo chuẩn phim Châu Tinh Trì (Stephen Chow / Mo Lei Tau). Không câu nệ phong phạm đại hiệp: ném cát sỏi mù mắt, rắc vôi bột, thụt đoản côn vào chấn thủy, đạp hạ bộ, đập mắt cá chân, giả vờ chịu thua lạy lục rồi phản đòn bất ngờ, vừa đánh vừa nói xàm gây phân tâm; vỏ bọc tiểu nhân bến sông nhưng bên trong là trái tim trượng nghĩa liều chết bảo vệ đồng đội.
@@ -70,6 +71,7 @@
 * **Thạch Hiên Viên:** Vị sư phụ truyền thừa đại nghĩa Cái Bang, người uốn nắn cái tâm bắng nhắng của thiếu niên thành rường cột võ lâm.
+* **Bạch Cương:** Ân nhân cận vệ mười bảy năm trước. Trùng phùng tại Tuyệt Vấn Pha (Ch.05), trao chiếc khánh bạc và cùng giải mã trục cuốn sấm thi.
```

---

## 5. Đề Xuất Cập Nhật Sổ Bảo Vật (`worldbuilding/artifacts/artifacts_ledger.md`)

```diff
Index: worldbuilding/artifacts/artifacts_ledger.md
===================================================================
--- worldbuilding/artifacts/artifacts_ledger.md
+++ worldbuilding/artifacts/artifacts_ledger.md
@@ -34,6 +34,7 @@
 - **Chất liệu**: Gỗ nghiến bãi sậy ngâm bùn Động Đình mười năm, hai đầu bịt khâu sắt non do Điềm Tửu Thúc rèn thủ công.
 - **Người sở hữu hiện tại**: Tiêu Phùng.
 - **Tình trạng biến dạng**: Đầu khâu sắt non bị mẻ khía sâu sau cú thụt xuyên giáp vào đan điền của Ngột Thất Hãn (Chương 05); thân gỗ dính máu đông đặc tanh nồng.
 
+### Mảnh Trục Cuốn Sấm Thi Cổ (Ma Y Cốc Di Cảo)
+- **Mã định danh**: `ART-SAM-THI-001`
+- **Chất liệu**: Lụa tơ tằm cổ viền chỉ bạc, thêu chìm bốn câu sấm thi chỉ vàng: *"Thái bạch dạ quan tinh / Trọc khí quy tam thanh / Thiên mã chấn trường dực / Long Cung trích tử anh"*.
+- **Xuất xứ**: Di vật của Tiêu Lăng Phong để lại trước đại biến Ma Y Cốc 1174. Thu hồi sau trận Tuyệt Vấn Pha (Chương 05).
+- **Người nắm giữ**: Bạch Thu Lâm & Bạch Cương (bảo quản trong tráp da hươu).
```

---

## 6. Đề Xuất Cập Nhật Sổ Theo Dõi Lời Hứa & Hạt Giống (`plot/promises_tracker.md`)

```diff
Index: plot/promises_tracker.md
===================================================================
--- plot/promises_tracker.md
+++ plot/promises_tracker.md
@@ -18,6 +18,10 @@
 - **TH-001 (Thân thế Tiêu Phùng & Bức thư máu Ma Y Cốc)**: `ADVANCED`. Đã trùng phùng Bạch Cương tại Tuyệt Vấn Pha (Chương 05), nhận diện khánh bạc và tiếp nhận trục cuốn sấm thi của Tiêu Lăng Phong.
+- **TH-008 (Toán sát thủ Âm kình giặc Kim)**: `PARTIALLY RESOLVED`. Tiêu diệt tên đầu mục Bách hộ Ô Sơ Sa Ngột Thất Hãn tại Tuyệt Vấn Pha, trả món nợ máu cho Thẩm Thiết Thạch; phát hiện đây là kế dương đông kích tây của thế lực Kim quốc.
+- **TH-009 (Bài Sấm Thi 4 câu & Long Cung Khởi Họa)**: `OPENED`. Bốn câu sấm thi Ma Y Cốc khai mở đầu mối truy tìm tung tích hung ngọc Du Long Giác.
+- **Tình huống khẩn cấp bùng nổ (Thảm họa vỡ đê Ba Lăng)**: Phản đồ cắt gân chân Cơ quan đại sư Giới Sơn Tông, mở tung chín van xả lũ thạch thất; giông bão Động Đình ập xuống đê quai (Bridge sang Chương 06).
```

---

## 7. Đề Xuất Cập Nhật Dòng Thời Gian (`plot/timeline.md`)

```diff
Index: plot/timeline.md
===================================================================
--- plot/timeline.md
+++ plot/timeline.md
@@ -28,3 +28,4 @@
 - **1191-08-18 (Sáng & Trưa)**: Chương 04a — Hàn Độc Thiết Thạch.
 - **1191-08-18 (Chiều muộn)**: Chương 04b — Kỳ Trân Mê. Thu di trao khánh bạc; còi báo động Tuyệt Vấn Pha hú vang.
+- **1191-08-18 (Hoàng hôn đến Đêm)**: Chương 05 — Tuyệt Vấn Huyết Lộ. Huyết chiến Tuyệt Vấn Pha; Bạch Thu Lâm chém Ngột Thất Hãn; Tiêu Phùng rạn xương sườn L3; trùng phùng Bạch Cương; sấm thi Ma Y Cốc; giặc Kim mở van xả lũ đê Ba Lăng.
```
