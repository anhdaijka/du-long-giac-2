# Khảo sát ngữ nghĩa nguồn — Arc locator 09–12 và unclassified

Trạng thái: tái dựng phi-canon. Tài liệu này hoàn tất lượt đọc semantic cấp locator cho Arc 09–12 và 19 task không được Narrative Book gán Arc. Cùng với hai báo cáo 00–03 và 04–08, cả 13 locator đã được khảo sát trước khi phân quyển.

## Phương pháp và độ phủ

| Tập | Packet có query + kết quả | Tasks | Subtasks | Steps | Dialogues | Repeatable tasks |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| Arc 09 | `evidence/source-packets/arc_09.json` | 50 | 49 | 251 | 56 | 22 |
| Arc 10 | `evidence/source-packets/arc_10.json` | 40 | 49 | 256 | 51 | 13 |
| Arc 11 | `evidence/source-packets/arc_11.json` | 50 | 59 | 247 | 61 | 11 |
| Arc 12 | `evidence/source-packets/arc_12.json` | 44 | 44 | 237 | 46 | 1 |
| Unclassified | `evidence/source-packets/unclassified.json` | 19 | 19 | 62 | 19 | 17 |

Task 288 là hàng task duy nhất không có subtask. Các packet tự lưu SHA-256 SQLite, query template, bind `task_ids` và kết quả đầy đủ. Bảng trên là kết quả `Q-0912-COUNT` trong phụ lục.

## Arc locator 09 — gameplay Phục Ngưu trộn với Chu Hy, Bắc tiến và Đại Lý

Hai mươi hai trong 50 task có `repeat=1`; Task 288 không có subtask. Task 271–290 chủ yếu là công việc lặp/phó bản quanh Phục Ngưu, Man Chướng Sơn và Ngưu Lan Trại. Task 291–300 tạo thành cụm Chu Hy–Trường Ca–Hàn Thác Trụ có quan hệ tiếp nối rõ hơn. Task 303–320 lại mở rộng sang Mông Cổ, Phục Ngưu, địa danh cổ và chuỗi Đại Lý/La Tuyết.

Không có literal hit `Du Long` trong các trường narrative của packet 09 (`Q-0912-DL`). Nhãn “Đại Lý Kỳ Án” chỉ khớp một phần cuối tập, không mô tả được các task lặp Phục Ngưu hoặc cụm Chu Hy.

### Kết luận locator 09

Không dùng toàn bộ Arc 09 như một tuyến liền. Tối thiểu phải tách: gameplay loop Phục Ngưu; cụm chính trị Chu Hy; cụm mở rộng chiến lược; cụm Đại Lý/La Tuyết.

## Arc locator 10 — bí mật thứ hai, Du Long Kinh Phượng và nhiều lớp live/gameplay

Task 321–332 nối tiếp Đại Lý và các thế lực ngoại biên. Task 332 / subtask 507 nói trong cẩm nang của Ngô thái hậu có “bí mật thứ hai” của Du Long Giác và kho báu từng phát hiện chỉ là một phần. Đây là lời kể/đầu mối của nhân vật, không tự chứng minh mọi nội dung của bí mật.

Task 352 (*Du Long Kinh Phượng*) là mega-task 10 subtask (`527–536`) về chuyến do thám phương Bắc của player-avatar cùng Doãn Tiêu Vũ và Đan Bích Tú, rồi tam giác căng thẳng Doãn Tiêu Vũ–Gia Luật Sở Tài–Hoàn Nhan Tương. Tên task có `Du Long`, nhưng nội dung 10 subtask được đọc trong packet chủ yếu là tình báo, tình cảm, giam lỏng và giải cứu; không được suy ra một cơ chế Du Long Giác chỉ từ nhan đề.

Các phần còn lại trộn:

- Task 335–348 và 369–370: task lặp, cấp độ, sự kiện trở lại/chúc tết hoặc biến thể đồng đội.
- Task 349–351: hướng dẫn người chơi/hệ thống.
- Task 353–362: truyện ngắn và nhiệm vụ địa phương, trong đó có cứu Đan Bích Tú.
- Các Task 333–334 và 337–338 bị locator bỏ ngoài, dù là các phiên bản Cổ Họa liên quan đến cụm Đại Lý; chúng được giữ ở unclassified, không tự chèn vào Arc 10.

### Kết luận locator 10

Task 332 và 352 là hai nút lớn khác loại: một đầu mối Du Long Giác và một tuyến nhân vật/phương Bắc. Chúng cần các cạnh source graph riêng; không gộp thành một arc chỉ vì cùng locator.

## Arc locator 11 — Bắc phạt, route môn phái và lớp cấp độ

Task 371–381 là 11 task lặp/phó bản. Task 382 (*Giang Sơn Bắc Vọng*) là mega-task 10 subtask (`566–575`) bao quát việc giải cấm, đấu tranh cung đình, Hàn Thác Trụ và chuẩn bị Bắc phạt. Task 395–404 tiếp tục huy động Tào Bang, Diêm Bang, Mã Bang, Mông Cổ, nhân lực và quân nhu.

Xen giữa các nút macro là hai family môn phái:

- Task 383–394: mười hai nhiệm vụ môn phái cấp 20.
- Task 405–416: mười hai nhiệm vụ môn phái cấp 30.
- Task 417–420: bốn nhiệm vụ đầu của family cấp 40; tám nhiệm vụ còn lại nằm đầu locator 12.

Không có literal hit `Du Long` trong packet 11 (`Q-0912-DL`).

### Kết luận locator 11

Nguồn chứng minh một trục chuẩn bị Bắc phạt nhưng locator còn chứa nhiều route/cấp độ song song. Source graph phải giữ Task 382 và 395–404 như macro candidates, đồng thời chuyển các family cấp độ vào branch/gameplay matrix.

## Arc locator 12 — endpoint gameplay, chiến dịch Linh Bích và Du Long tái hiện

Đầu locator vẫn tiếp tục lớp gameplay:

- Task 421–428 hoàn tất family môn phái cấp 40.
- Task 429 là task lặp.
- Task 430–441 là mười hai nhiệm vụ kỹ năng cấp 110.

Từ Task 442, nguồn ghi trực tiếp “Năm 1205” và mở chuỗi Bắc phạt/Linh Bích. Đây là **fact game có mốc năm**; việc nó có khớp sử thật hay không phải được kiểm tra bằng nguồn lịch sử riêng trước khi gắn nhãn fact lịch sử.

Các nút Du Long đáng chú ý (`Q-0912-DL`):

- Task 450 / subtask 643: player-avatar trải nghiệm một **Thân Thế Mộng Cảnh**. Trong cảnh này, cha được gọi là Minh Dương, mẹ là Tố Trinh, nhân vật được nói có huyết mạch Nhạc gia quân; một gấm cũ kể Du Long Giác chia Thư–Hùng và mở kho báu.
- Task 451 / subtask 644: nguồn giải thích player-avatar đã trọng thương, được Dục Tâm Liên cứu và gặp người mình muốn gặp trong Huyễn Cảnh; NPC nói không thể giải thích cảnh đó là thật hay giả. Vì vậy Task 450 là **diegetic vision / reliability unresolved**, không phải tiểu sử khách quan đã xác nhận.
- Task 452 / subtask 645: player-avatar kể lại nội dung Huyễn Cảnh cho Bạch Thu Lâm; Bạch Thu Lâm cảnh báo Du Long Giác không đủ tự nó xoay chuyển cục diện và việc lộ tin sẽ gây tranh đoạt.
- Task 456 / subtask 648: nguồn gọi Từ Hương Hương là Du Long Sứ đời này và nói Từ gia quân nhiều đời bảo vệ Du Long Bảo Khố.
- Task 457 / subtask 649: nguồn đặt *Thái Tổ Bí Sử* trong Du Long Bảo Khố và mô tả nguy cơ khi quân lực bảo vệ bị chuyển ra tiền tuyến.
- Task 462 / subtask 655: nguồn nói sóng gió Du Long Giác đã lắng một thời gian và báu vật trong bảo khố được dùng cho quân bị.

Task 464–465 quay về hướng dẫn hệ thống đồng hành. Task ID 463 không tồn tại trong bảng `tasks`, nên khoảng số không được diễn giải thành sự kiện bị thất lạc.

### Kết luận locator 12

Locator 12 chứa một endpoint chiến dịch có nhiều thông tin Du Long, nhưng nguồn tự đánh dấu một phần thân thế là giấc/huyễn cảnh không rõ thật giả. Đây là vùng bắt buộc giữ speaker, medium và reliability; không được dùng Task 450 để tự retcon Task 157 hoặc ba profile chính.

## Mười chín task unclassified

Các task không được ép vào Arc bằng số ID:

- 219, 220, 224: ba task lặp/phó bản.
- 226–227: hai phiên bản chuẩn bị chiến sự, có quan hệ nội dung với quân doanh Phục Ngưu nhưng locator không gán.
- 333–334, 337–338: bốn phiên bản Cổ Họa (daily/main, sơ/trung), thuộc cùng một family nội dung.
- 363–368: sáu biến thể Hải Lăng Vương Mộ theo cấp độ/main–daily, lặp lại cùng premise về bản đồ phong thủy long mạch Kim.
- 466: sự kiện chúc tết; 467: hướng dẫn hôn nhân; 468: Vô Tự Thiên Thư/kỹ năng; 469: nội dung cứu trợ/live-event pha văn bản Trung–Việt.

Mười bảy trong 19 task có `repeat=1`; chỉ 467 và 468 có `repeat=0`. Không mục nào được tự động đưa vào chronology chính. Các premise có ích chỉ được trích như lore candidate với đúng reliability và provenance.

## Branch, reliability và normalization candidates mới

- `BR-007`: Task 352 là một tuyến nhân vật dài, không phải bằng chứng rằng toàn bộ locator 10 là một route.
- `BR-008`: family môn phái cấp 20/30/40/110 là các lựa chọn song song/gameplay scaffolding.
- `BR-009`: các phiên bản main/daily/cấp độ ở unclassified là variant family, không phải nhiều lần biến cố.
- `BR-010`: Task 450–451 tạo một thân thế trong Huyễn Cảnh mà nguồn tự để ngỏ thật/giả; không được hợp nhất lặng lẽ với Task 157.
- `BR-011`: Task 463 là ID không tồn tại, không phải missing-event evidence.

## Phụ lục provenance/query

### Q-0912-PACKETS

`arc_09.json` đến `arc_12.json` và `unclassified.json` chứa trực tiếp query template, bind task IDs và toàn bộ kết quả. SQLite SHA-256: `b5c30040c9449f2223cf40bfec9866216423a60a82e2333b5cedb4fb5261bdb0`.

### Q-0912-COUNT

Sử dụng cùng query aggregate như `Q-0408-COUNT`, bind lần lượt mảng `task_ids` của từng packet. Kết quả là bảng độ phủ ở đầu tài liệu; Task 288 có `subtask_count=0`.

### Q-0912-DL

```sql
SELECT DISTINCT t.task_id, t.name AS task_name,
       s.sub_id, s.name AS subtask_name, d.phase
FROM tasks AS t
JOIN subtasks AS s ON s.task_id = t.task_id
LEFT JOIN dialogues AS d ON d.sub_id = s.sub_id
LEFT JOIN steps AS st ON st.sub_id = s.sub_id
WHERE t.task_id IN (:arc_09_through_12_task_ids)
  AND (COALESCE(t.name, '') || char(10) ||
       COALESCE(t.describe_cleaned, '') || char(10) ||
       COALESCE(s.name, '') || char(10) ||
       COALESCE(s.describe_cleaned, '') || char(10) ||
       COALESCE(d.cleaned_text, '') || char(10) ||
       COALESCE(st.instruction, '') || char(10) ||
       COALESCE(st.target_params, '')) LIKE '%Du Long%'
ORDER BY t.task_id, s.sub_id, d.id, st.id;
```

Bind values là phép nối bốn mảng `task_ids` trong packet 09–12. Sau khi khử trùng theo task/subtask/dialogue phase, kết quả gồm Task 332/sub 507; Task 352/sub 527–536; Task 450/sub 643; 451/sub 644; 452/sub 645; 456/sub 648; 457/sub 649; 462/sub 655. Chi tiết đầy đủ nằm trong packet tương ứng.

### Q-450-451-RELIABILITY

```sql
SELECT t.task_id, t.name, s.sub_id, s.name AS subtask_name,
       s.describe_cleaned, st.step_index, st.target_params,
       d.phase, d.cleaned_text
FROM tasks AS t
JOIN subtasks AS s ON s.task_id = t.task_id
LEFT JOIN steps AS st ON st.sub_id = s.sub_id
LEFT JOIN dialogues AS d ON d.sub_id = s.sub_id
WHERE t.task_id IN (450, 451)
ORDER BY t.task_id, s.sub_id, st.step_index, d.id;
```

Kết quả đầy đủ được giữ trong `arc_12.json`. Các hàng của Task 451 nói rõ trải nghiệm phát sinh khi nhân vật trọng thương, được Dục Tâm Liên cứu, và tính thật/giả của Huyễn Cảnh không được NPC giải thích.

