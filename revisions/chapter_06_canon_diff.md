# Đề Xuất Canon Diff: Chương 06 — Hộ Đê Cứu Nạn

> **Cơ quan quản lý**: Novel OS State Ledger  
> **Trạng thái**: Chờ Tác giả xem xét và phê chuẩn trước khi commit vào Sổ cái trạng thái bền vững (Cổng Dừng 3).

---

## 1. Tóm Tắt Biến Chuyển Cốt Truyện & Nhân Vật (Narrative Summary)

- **POV**: Tiêu Phùng (17 tuổi — Đê quai Ba Lăng & Thạch thất ngầm sông Động Đình).
- **Thời gian**: 1191-08-18 đêm muộn chuyển sang 1191-08-19 rạng sáng và bình minh.
- **Biến cố sa trường cốt tử**:
  - Tiêu Phùng nén đau do chấn thương rạn xương sườn L3 (`INJ-TP-002`), cùng Bạch Thu Lâm và nghĩa quân Ba Lăng phi kỵ trong giông bão về cứu đê;
  - Cảnh tượng vỡ đê nghìn cân treo sợi tóc: hàng ngàn dân phu áo vải và dân chài thôn Giang Tân dầm bùn lầy, dùng thân mình chặn bao tải đất giữ chân đê;
  - Tiêu Phùng cùng Bạch Thu Lâm lặn ngụp dòng nước lũ thâm nhập vào khu thạch thất ngầm cơ quan thủy lưu;
  - Phát hiện và giải cứu Cơ quan đại sư Giới Sơn Tông bị mật thám giặc Kim cắt đứt gân hai gót chân, kiên trung giấu chìa khóa trong cối đá buồng rèn;
  - Giới Sơn Tông chỉ điểm cho Tiêu Phùng: "Nguyên Lý Then Khóa Cơ Hoành" để ghì chặt lồng ngực giảm đau dã chiến và cách dùng đòn bẩy bẩy bung chốt then chữ *Đinh* ở khớp gối Cơ Quan Nhân Thô;
  - Tiêu Phùng cùng nghĩa quân hạ ba cỗ Cơ Quan Nhân Thô bằng gỗ lim bọc đồng thau; đoạt lại xâu chìa khóa cửu môn;
  - Hợp lực cùng Bạch Thu Lâm và nghĩa quân ghì đòn bẩy đồng đen ngầm, đóng sập chín khối cự thạch vòm xả lũ, chặn đứng dòng nước lũ hung hãn;
  - Bão tan, rạng đông bừng sáng trên hồ Động Đình; Tiêu Phùng hội ngộ trong nước mắt mừng vui của Thẩm Hà Diệp, uống rượu nếp mừng công của Điềm Tửu Thúc;
  - Mở ra bước ngoặt rời bỏ thôn làng dấn thân vào đại giang hồ phương Nam — hướng về Cái Bang Yến Tử Ổ.

---

## 2. Đề Xuất Cập Nhật Sổ Cái Thương Tật (`worldbuilding/medical/injuries_ledger.md`)

```diff
Index: worldbuilding/medical/injuries_ledger.md
===================================================================
--- worldbuilding/medical/injuries_ledger.md
+++ worldbuilding/medical/injuries_ledger.md
@@ -40,7 +40,8 @@
-| **INJ-TP-002** | Mạn sườn trái: nứt rạn xương sườn số 6, dư chấn Âm kình hàn độc nghẽn tạng phủ, ho ra huyết ứ tím bầm. | **L3** | Trúng cú cùi chỏ sắt và luồng kình phản chấn của Bách hộ Ngột Thất Hãn tại Tuyệt Vấn Pha. | Chương 05 | **ĐANG ĐIỀU TRỊ (Tuần 1/6)**. Đã nẹp tre cố định. | Bó nẹp tre 4–6 tuần; đau buốt óc mỗi nhịp thở sâu hoặc ho; cấm vận sức tay trái; buốt lạnh khi trời mưa gió. |
+| **INJ-TP-002** | Mạn sườn trái: nứt rạn xương sườn số 6, dư chấn Âm kình hàn độc nghẽn tạng phủ, tấy buốt sau dầm mưa lạnh & ngâm nước lụt thạch thất. | **L3** | Trúng cú cùi chỏ sắt Ngột Thất Hãn (Ch.05); tiếp tục chịu xung lực khi lội bùn & gián tiếp vận lực cơ hoành (Ch.06). | Chương 05 | **ĐANG ĐIỀU TRỊ (Tuần 2/6)**. Giữ nguyên nẹp tre cố định. | Bó nẹp tre 4–6 tuần; đau nhức dữ dội khi hít sâu; tuyệt đối cấm mang vác nặng hay vận kình thượng thừa; cần cao dán giữ ấm. |
+| **INJ-TP-003** | Cơ hoành & cơ bụng: co thắt dữ dội (chuột rút cơ hoành dã chiến), cơ ngực căng cứng, rỉ dịch máu bầm cũ đọng phế quản. | **L1** | Hậu quả lạm dụng "Mẹo Then Khóa Cơ Hoành" của Giới Sơn Tông để nén đau vận lực trong thạch thất ngập nước. | Chương 06 | **MỚI PHÁT SINH**. Đang nghỉ ngơi dã chiến. | Đau tức bụng dưới mỗi khi cười hoặc ho; tự hồi phục sau 3–5 ngày tĩnh dưỡng, không để lại di chứng vĩnh viễn. |
 
 ### B. Thẩm Thiết Thạch (Đồ tể Ba Lăng)
 
@@ -52,3 +53,9 @@
 | **INJ-BC-001** | Bả vai trái đao chém thấu cơ, ngực trúng chưởng phong Âm kình cực hàn, mất máu nặng, suy kiệt. | **L3** | Bị toán thích khách Ô Sơ Sa phục kích tại Tuyệt Vấn Pha. | Chương 05 | **NGUY KỊCH / ỔN ĐỊNH TẠM THỜI**. Đã rịt thuốc rừng và sơ cứu. | Hôn mê từng chặng, thở yếu; cần đưa về y quán Ba Lăng Huyện điều trị dài ngày; không thể tiếp tục chiến đấu. |
+
+### D. Giới Sơn Tông (Cơ quan đại sư Giới Sơn Tông)
+
+| Vết thương # | Vị trí & Dạng tổn thương | Cấp độ | Tác nhân / Hoàn cảnh | Hồi xuất hiện | Trạng thái hiện tại | Di chứng & Ảnh hưởng hành vi |
+| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
+| **INJ-GST-001** | Hai gót chân: Đứt lìa gân gót (Achilles), dập nát mắt cá chân, bỏng lạnh do ngâm bùn thạch thất. | **L3** (Nặng) | Bị mật thám công binh giặc Kim tra tấn cắt gân nhằm bức cung chìa khóa cơ quan thạch thất. | Chương 06 | **ĐANG ĐIỀU TRỊ KHẨN CẤP**. Đã được nẹp gỗ sơ cứu và chuyển về y quán Ba Lăng. | Mất vĩnh viễn khả năng đi lại nhanh nhẹn; sau này chỉ có thể chống nạng hoặc ngồi xe đẩy; bàn tay và trí tuệ cơ quan nguyên vẹn. |
```

---

## 3. Đề Xuất Cập Nhật Sổ Động Thái Võ Học (`worldbuilding/martial/martial_dynamics.md`)

```diff
Index: worldbuilding/martial/martial_dynamics.md
===================================================================
--- worldbuilding/martial/martial_dynamics.md
+++ worldbuilding/martial/martial_dynamics.md
@@ -56,7 +56,9 @@
    - *Kinh nghiệm sa trường mới (Ch.05)*: Sử dụng túi vôi sống trộn ớt khô cay xè phòng thân; đòn đoản côn thụt huyệt Khí Xung đan điền; nhận thức sâu sắc khoảng cách sinh tử giữa Tier 0 và Tier 2.
+  - *Mẹo dã chiến thợ thuyền mới (Ch.06)*:
+    - **Nguyên Lý Then Khóa Cơ Hoành** (Giới Sơn Tông truyền): Hóp sâu bụng ép cơ hoành cố định lồng ngực dã chiến, giảm 4 phần đau đớn của vết rạn sườn L3 khi phải vận lực tức thời. Trả giá: chuột rút cơ bụng L1 sau trận.
+    - **Mẹo bẩy then khớp máy**: Dùng đoản côn làm đòn bẩy cạy bật chốt then chữ Đinh ở khớp gối Cơ Quan Nhân Thô thay vì đập vào sắt thép.
    - *Kinh nghiệm sinh tồn*: Bơi lặn nước sâu Động Đình, nín thở dưới đầm sậy, bò trườn bùn lầy.
  - **Hạn chế thể xác chí mạng**:
-  - **Đang mang chấn thương L3 (INJ-TP-002)**: Rạn nứt xương sườn số 6 bên trái, phải nẹp tre quấn vải gai, hơi thở nông, miệng rỉ máu bầm khi ho; cấm vận sức mạnh tay trái trong 4–6 tuần.
+  - **Đang mang chấn thương L3 (INJ-TP-002)** và **chấn thương L1 (INJ-TP-003)**: Rạn xương sườn số 6, nẹp tre quấn vải gai; cơ hoành co rút từng cơn; cấm vận sức mạnh lồng ngực và tay trái.
@@ -64,3 +66,4 @@
    - **Chương 05**: Thể nghiệm thực tế sa trường (First Contact with Internal Force). Giữ nguyên Tier 0 thô mộc, trả giá đắt bằng chấn thương L3 để hiểu được sự khốc liệt của võ học chân chính.
+  - **Chương 06**: Thể nghiệm cơ quan học và dưỡng thể dã chiến thợ thuyền. Giữ nguyên Tier 0, áp dụng trí tuệ đòn bẩy và then khóa cơ hoành vượt qua hiểm cảnh.
```

---

## 4. Đề Xuất Cập Nhật Hồ Sơ Nhân Vật Tiêu Phùng (`characters/tieu_phung.md`)

```diff
Index: characters/tieu_phung.md
===================================================================
--- characters/tieu_phung.md
+++ characters/tieu_phung.md
@@ -77,7 +77,7 @@
-## 6. SỔ CÁI TRẠNG THÁI HIỆN HÀNH (DURABLE STATE LEDGER)
-* **Mốc thời gian hiện hành:** 1191-08-18 (Đêm bão — Sau Chương 05).
-* **Thể trạng thực tế:** Đang mang chấn thương L3 (rạn xương sườn số 6 mạn sườn trái, nẹp tre quấn vải gai), ngực buốt nhói, miệng rỉ máu bầm khi ho; cấm vận sức mạnh tay trái trong 4–6 tuần.
+## 6. SỔ CÁI TRẠNG THÁI HIỆN HÀNH (DURABLE STATE LEDGER)
+* **Mốc thời gian hiện hành:** 1191-08-19 (Rạng sáng & Bình minh — Sau Chương 06).
+* **Thể trạng thực tế:** Đang mang chấn thương L3 (INJ-TP-002: rạn xương sườn số 6 mạn sườn trái, nẹp tre cố định) kèm chấn thương L1 (INJ-TP-003: chuột rút cơ hoành và cơ bụng); miệng còn vị tanh máu bầm cũ; hơi thở nông khò khè khi vận động.
 * **Binh khí & Trang bị:** 
-  - Đoản côn gỗ nghiến bãi sậy (dài 2 thước rưỡi, hai đầu bịt ống sắt non đóng 4 đinh tán đồng dẹt; khâu sắt non mẻ khía sâu sau cú thụt xuyên giáp vào đan điền Ngột Thất Hãn, thân gỗ dính máu khô đặc).
-  - Đôi Lữ Hành Ngoa mới bằng da dê núi do Thẩm Hà Diệp may tặng (dính đầy bùn đất Tuyệt Vấn Pha).
-  - Quần áo vải thô xé rách tả tơi, đẫm nước mưa và máu bầm sa trường.
+  - Đoản côn gỗ nghiến bãi sậy (đầu bịt sắt non mẻ thêm một rãnh sâu do dùng bẩy bật then chốt sắt khớp gối Cơ Quan Nhân Thô; thân gỗ bám phù sa bùn đỏ Động Đình khô cứng).
+  - Đôi Lữ Hành Ngoa bằng da dê núi của Thẩm Hà Diệp (ngấm bùn lụt đỏ quạch, trầy da mép ngoài nhưng đường chỉ may thủ công vẫn chắc nịch).
+  - Quần áo vải thô ướt sũng bùn lầy, dải vải gai nẹp ngực ngấm nước lạnh và vệt máu loãng.
@@ -93,4 +93,5 @@
    - Biết tin tình báo khẩn cấp: Giặc Kim dùng trận Tuyệt Vấn Pha làm mồi nhử để nội gián ám hại Cơ quan đại sư Giới Sơn Tông, cắt đứt gân chân và mở toang chín van xả lũ gây vỡ đê Ba Lăng trong đêm giông bão.
+  - **Tri thức mới (Ch.06):** Nắm vững "Nguyên Lý Then Khóa Cơ Hoành" và điểm yếu then chốt chữ Đinh ở khớp máy cơ quan; trực tiếp giải cứu Giới Sơn Tông; cùng nghĩa quân đóng chín cửa cự thạch thạch thất cứu toàn bộ huyện Ba Lăng; thấu hiểu chiều sâu của hai chữ "Quốc nạn".
 * **Ranh giới cấm kỵ (Forbidden Unknowns):**
   - Tuyệt đối CHƯA BIẾT chi tiết thảm án Ma Y Cốc tại sao xảy ra và ai chủ mưu diệt môn.
   - CHƯA BIẾT mối liên hệ giữa ngọc Du Long Giác và Ma Y Cốc.
```

---

## 5. Đề Xuất Cập Nhật Sổ Bảo Vật (`worldbuilding/artifacts/artifacts_ledger.md`)

```diff
Index: worldbuilding/artifacts/artifacts_ledger.md
===================================================================
--- worldbuilding/artifacts/artifacts_ledger.md
+++ worldbuilding/artifacts/artifacts_ledger.md
@@ -13,3 +13,4 @@
 | **Đoản côn bịt sắt** | Cây gậy gỗ nghiến bãi sậy của Tiêu Phùng | **Tiêu Phùng** | Trên tay / bên hông Tiêu Phùng | Khâu sắt non bị mẻ khía sâu sau cú thụt xuyên giáp vào đan điền của Bách hộ Ngột Thất Hãn; thân gậy dính máu đen đông đặc sa trường | Chương 05 |
+| **Đoản côn bịt sắt** | Cây gậy gỗ nghiến bãi sậy của Tiêu Phùng | **Tiêu Phùng** | Trên tay / bên hông Tiêu Phùng | Khâu sắt non mẻ thêm một rãnh sâu do cạy then chốt sắt Cơ Quan Nhân Thô; thân gỗ bám bùn đỏ Động Đình khô cứng | Chương 06 |
 | **Chiếc khánh bạc trẻ con** | Di vật định danh sơ sinh của Tiêu Phùng; đúc bằng bạc ròng xỉn màu; mặt trước khắc chìm chữ: "Tiêu Phùng (簫逢) — Thuần Hi nguyên niên", mặt sau chạm Bát Quái ôm ngọn lửa | **Tiêu Phùng** | Trong ngực áo Tiêu Phùng | Đã đưa cho Bạch Cương nhận diện tại Tuyệt Vấn Pha rồi đeo lại vào cổ; dính vệt máu bầm tím sau khi Tiêu Phùng trúng đòn rạn xương sườn | Chương 05 |
@@ -25,3 +26,4 @@
 | **Hung ngọc Du Long Giác** | Khối ngọc hình rồng ngậm máu đúc từ thiên thạch ngàn năm; ẩn chứa cơ quan quân sự đoạt thiên hoán nhật | *Đang bị phong ấn* | Trung tâm Bách Hoa Trận (Cấm địa Thúy Yên) | Nằm trong rương sắt vùi sâu dưới đất đá cấm địa; đang tỏa ngọc khí kích thích từ trường và bầy sói | Chương 03 (Tiền triệu) |
+| **Xâu chìa khóa đồng thau thạch thất cửu môn** | Bộ chín chiếc chìa bằng đồng thau chạm khắc rãnh răng cưa cơ quan thủy lưu Động Đình | **Bạch Thu Lâm & Nghĩa quân** | Khố phòng nghĩa quân Ba Lăng | Giới Sơn Tông giao cho Tiêu Phùng dùng đóng 9 cửa vòm xả lũ; sau đó Tiêu Phùng đã trao trả lại cho Bạch Thu Lâm niêm phong | Chương 06 |
```

---

## 6. Đề Xuất Cập Nhật Bảng Theo Dõi Lời Hứa (`plot/promises_tracker.md`)

```diff
Index: plot/promises_tracker.md
===================================================================
--- plot/promises_tracker.md
+++ plot/promises_tracker.md
@@ -21,3 +21,4 @@
-| **TH-010** | **Nội gian phá đê Ba Lăng & Đại hồng thủy Động Đình** | Chương 05 | Tiêu Phùng / Bạch Thu Lâm | Giặc cắt gân chân Cơ quan đại sư Giới Sơn Tông, mở tung 9 van xả lũ; tiếng còi báo động vỡ đê trong đêm mưa bão | **Chương 06** (*Hộ Đê Cứu Nạn*) | `URGENT CRISIS / TICKING CLOCK` |
+| **TH-010** | **Nội gian phá đê Ba Lăng & Đại hồng thủy Động Đình** | Chương 05 | Tiêu Phùng / Bạch Thu Lâm | Chương 06 giải cứu Giới Sơn Tông, hạ 3 Cơ Quan Nhân Thô, đóng sập chín cửa cự thạch ngăn lũ; bão tan rạng đông | **Chương 06** (*Hộ Đê Cứu Nạn*) | `PAID OFF / RESOLVED` (Cứu nguy thành công) |
+| **TH-011** | **Hành trình Cái Bang Yến Tử Ổ & Mối liên hệ Thạch Hiên Viên** | Chương 06 | Tiêu Phùng / Bạch Thu Lâm | Bạch Thu Lâm viết thư tiến cử Tiêu Phùng lên đường tới Yến Tử Ổ bái sư nhập môn Cái Bang (Task 2) | **Chương 07 – 10** | `PLANTED / TRANSITION TO ARC 02` |
```

---

## 7. Đề Xuất Cập Nhật Dòng Thời Gian (`plot/timeline.md`)

```diff
Index: plot/timeline.md
===================================================================
--- plot/timeline.md
+++ plot/timeline.md
@@ -48,3 +48,6 @@
+* **Ngày 19 tháng 8:**
+  * *Ba Lăng Huyện (1191-08-19 — Rạng sáng & Bình minh):* Tiêu Phùng dầm mưa bão, vượt bùn lầy hộ đê; cùng nghĩa quân thâm nhập thạch thất ngầm, giải cứu Cơ quan đại sư Giới Sơn Tông bị cắt đứt gân hai gót chân; áp dụng "Nguyên Lý Then Khóa Cơ Hoành" và đòn bẩy bẻ khớp then chữ Đinh hạ ba cỗ Cơ Quan Nhân Thô; cùng Bạch Thu Lâm gạt đòn bẩy đồng đen đóng chín khối cự thạch van xả lũ, cứu toàn huyện Ba Lăng khỏi cảnh đại hồng thủy; bình minh rạng rỡ, nhân dân mừng vui thoát nạn (`Task 157: Subtask 320, 312` & `Task Arc 00` — **Chương 06 đã canon hóa**).
```

---

## 8. Trình Duyệt Tác Giả (Verdict Request)

Đề xuất Canon Diff Chương 06 đã được kiểm tra tính nhất quán toàn diện với:
- `worldbuilding/medical/injuries_ledger.md` (Quản lý thương tật L3 và L1)
- `worldbuilding/martial/martial_dynamics.md` (Duy trì Tier 0 thô mộc, bổ sung cơ chế dưỡng thể dã chiến)
- `characters/tieu_phung.md` (Cập nhật thể trạng, đồ đạc và nhận thức)
- `worldbuilding/artifacts/artifacts_ledger.md` (Ghi nhận biến dạng đoản côn và chuyển giao chìa khóa)
- `plot/promises_tracker.md` (Chốt Payoff TH-010, mở hạt giống TH-011)
- `plot/timeline.md` (Khớp mốc ngày 19-08-1191)

> [!IMPORTANT]
> **CỔNG DỪNG 3 (State Commit Hard Stop):**
> Em **DỪNG LẠI TẠI ĐÂY** để chờ Tác giả xem xét và phê chuẩn bản Diff.
> Khi Tác giả đồng thuận, xin mời ban hành lệnh:
> **`"Duyệt diff"`**
> *(Sau khi nhận lệnh duyệt diff, em sẽ thực thi commit toàn bộ các thay đổi trên vào các sổ cái trạng thái bền vững).*


---

## Supporting Cast Directory (`characters/supporting_cast.md`)
*(Đã đồng bộ chuẩn hóa kiểm toán vào danh bạ nhân vật phụ)*
