# Khảo sát ngữ nghĩa nguồn — Arc locator 04–08

Trạng thái: tái dựng một phần, phi-canon. Tài liệu này hoàn tất lượt đọc Arc locator 04–08; nó chưa hoàn tất khảo sát đủ 13 Arc, chưa chọn tuyến tiểu thuyết và chưa phân quyển/chương.

## Phương pháp và độ phủ

Mỗi source packet chứa danh sách tham số, câu query SQLite đã dùng và toàn bộ kết quả task/subtask/step/dialogue. Narrative Book chỉ cung cấp membership locator; nhãn Arc không được coi là niên biểu hay tóm tắt canon.

| Locator | Packet có query + kết quả | Tasks | Subtasks | Steps | Dialogues | Repeatable tasks |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| 04 | `evidence/source-packets/arc_04.json` | 34 | 34 | 105 | 70 | 0 |
| 05 | `evidence/source-packets/arc_05.json` | 40 | 40 | 122 | 42 | 0 |
| 06 | `evidence/source-packets/arc_06.json` | 40 | 54 | 173 | 75 | 17 |
| 07 | `evidence/source-packets/arc_07.json` | 30 | 42 | 168 | 46 | 4 |
| 08 | `evidence/source-packets/arc_08.json` | 43 | 43 | 217 | 47 | 5 |

Kết quả tổng hợp ở bảng trên được ghi lại dưới mã truy xuất `Q-0408-COUNT` trong phụ lục provenance của tài liệu này.

## Arc locator 04 — cụm địa phương, môn phái và ký ức Thúy Yên

Ba mươi bốn task đều là task không lặp và chỉ có một subtask. Nội dung trải rộng qua nhiều cụm địa phương/môn phái: Nga My, Đường Môn, Thúy Yên, Tống–Kim, đời sống dân sự và triều chính. Vì vậy nhãn locator “Du Long Giác Hiện Thế” không đủ để mô tả tập nguồn này.

Không có chuỗi nguyên văn `Du Long Giác` trong các trường narrative của 34 task thuộc locator 04 (`Q-0408-DLG`). Điều này chỉ chứng minh không có literal hit trong tập trường đã truy vấn; nó không chứng minh mọi task đều vô can với tuyến Du Long Giác.

Task 92 / subtask 241 là một mốc nguồn đáng giữ riêng: phần `describe_cleaned` kể vụ thảm sát Bách Hoa Trận mười năm trước, nêu thứ tự môn chủ đời 6–8 và dùng tên **Lệ Thu Thủy**; dialogue start của chính subtask lại dùng **Lịch Thu Thủy**. Đây là bất nhất nội tại của SQLite, chưa được tự động chuẩn hóa (`SQ-001`).

### Kết luận locator 04

Locator 04 hiện là một kho cụm truyện địa phương và hồi cố, không phải một chuỗi Du Long Giác đã được chứng minh. Khi dựng source graph phải tách các mẩu có quan hệ nhân quả khỏi các vignette chỉ chia sẻ vùng/NPC.

## Arc locator 05 — nền địa phương và hai móc Du Long Giác trực tiếp

Bốn mươi task đều không lặp và chỉ có một subtask. Phần lớn là các vụ việc độc lập hoặc bán độc lập ở Cư Diên Trạch, Điểm Thương, Phục Ngưu, Đại Lý, Tây Hạ, triều Tống và các môn phái.

Hai task có literal hit Du Long Giác trong tập 04–08 (`Q-0408-DLG`):

- Task 146 / subtask 295: Bạch Thu Lâm nói Diêm Bang và Từ Bân Kiếm nhiều lần nhắm tới Du Long Giác, rồi phái player-avatar đi dằn mặt bang chúng.
- Task 150 / subtask 299: Bạch Thu Lâm cho biết nhóm do Từ Bân Kiếm tập hợp từng tham gia tranh đoạt Du Long Giác và phái player-avatar đến điều tra/đối phó.

Hai hàng nguồn trên chứng minh lời kể và hành động điều động của nhân vật trong game. Chúng chưa chứng minh toàn bộ cơ chế, quyền sở hữu hay công năng khách quan của Du Long Giác.

### Kết luận locator 05

Locator 05 có hai móc Du Long Giác trực tiếp nằm giữa một tập lớn các nhiệm vụ địa phương. Source graph sau này cần kiểm tra quan hệ ngược của Task 146/150 với chuỗi Bách Hoa Trận và quan hệ xuôi với Thái Tổ Bảo Khố, thay vì mặc định mọi Task 111–150 là một tuyến liền nhau.

## Arc locator 06 — lõi thân thế bị trộn với tuyến vùng và gameplay

Locator 06 là tập hỗn hợp rõ nhất trong batch:

- Task 151–156 tiếp tục nhiều tuyến Đại Lý, Tiêu Dao Tử, Cổ Yên Nhiên, Bạch Thu Lâm và triều đình.
- Task 157 (*Thân Thế Chi Mê*) là một mega-task 15 subtask, khác hẳn các task một subtask xung quanh (`Q-157-STRUCTURE`).
- Task 158–160 là ba cổng xuất hành khác nhau: Thiên Vương/Giang Nam, Côn Lôn/Trung Nguyên và Nga My/Tây Nam.
- Task 161–190 chứa 17 task `repeat=1`, xen cùng nhiệm vụ môn phái, sinh hoạt và phó bản.

Task 157 cung cấp một lõi game-source rất mạnh cho **player-avatar**:

1. Bạch Thu Lâm gọi nhân vật là “thiếu chủ”, nói sắp đến sinh nhật và đã đủ lớn để hành tẩu (`subtask 306`).
2. Nhân vật được cho biết cha là đệ tử được yêu quý của một thầy tướng số Ma Y Cốc; cha mẹ mất tích sau biến cố Hán Thủy, và Bạch Thu Lâm đã nhận đứa trẻ từ người mẹ (`subtask 313`, step 4).
3. Bạch Cương nói đã mười tám năm từ lần gặp thiếu chủ và mang theo bài thơ dự báo của người cha (`subtasks 321–322`).
4. Bài sấm trong SQLite, tại `subtask 323`, step 5, là:

   > Thái bạch dạ quan tinh  
   > Trọc khí quy tam thanh  
   > Thiên mã chấn trường dực  
   > Long Cung trích tử anh

5. Sau khi ghép trục cuốn, player-avatar được đưa rời nơi đã lớn lên; các subtask kế tiếp 158–160 mở ra những hướng xuất hành khác nhau.

Các hàng này là **fact game về player-avatar**. Tác giả đã duyệt đồng nhất player-avatar với Tiêu Phùng và chốt tuổi mở truyện 18; đó vẫn là `NOVELIZATION BRIDGE`, không biến thành fact game. Năm mở truyện và năm sinh sẽ được khóa ở chronology mới, không suy ra chỉ từ số Task.

### Kết luận locator 06

Task 157 phải trở thành một nút lõi trong source graph, nhưng phần tutorial và gameplay của nó cần được tách khỏi các sự kiện bền vững. Task 158–160 và nhóm task lặp phải đi vào branch/gameplay matrix, không được ép thành ba biến cố liên tiếp của cùng một nhân vật.

## Arc locator 07 — lore hồi cố, tuyến nhập môn song song và mốc chuyển giai đoạn

Tập này có bốn nhóm khác nhau:

- Task 191–194: bốn task lặp.
- Task 197–202: các truyện hồi cố/giang hồ về Tàng Kiếm, nhân vật và thần binh.
- Task 203–214: mười hai nhiệm vụ tiếp dẫn tương ứng mười hai môn phái; đây là route-family rõ ràng cần branch matrix.
- Task 215–223: nghĩa quân, Bạch Hổ Đường và các truyện địa phương; Task 225 mở “Hành Trình Mới”.

Task 225 / subtask 400 là mốc thứ tự được phát biểu ngay trong nội dung (`Q-225-STRUCTURE`): sau trận Thái Tổ Bảo Khố, Hoàn Nhan Tương bộc lộ ý đồ xâm lược; Bạch Thu Lâm báo Hàn Thác Trụ, nhận mật chỉ và cho dựng quân doanh Phục Ngưu để chuẩn bị chiến tranh. Đây là quan hệ trước–sau do chính nguồn kể, mạnh hơn phép suy đoán từ số task hoặc tên locator.

### Kết luận locator 07

Nhãn “Khánh Nguyên Chi Biến” không thể biến toàn bộ Task 191–225 thành một tuyến chính biến. Locator 07 chủ yếu là gói hỗn hợp; Task 225 mới là cầu nối trực tiếp sang giai đoạn quân doanh, còn Task 203–214 là các lựa chọn môn phái song song.

## Arc locator 08 — hậu Du Long Giác và trục chính trị/quân sự rõ hơn

Task 231 / subtask 406 mở bằng câu “Chuyện Du Long Giác đã đến hồi kết” rồi chuyển trọng tâm sang tân hoàng đế, nội trị và phòng bị ngoại bang (`Q-0408-DLG`). Cách nói này là mốc chuyển giai đoạn của source; nó không tự giải thích kết cục cụ thể của Du Long Giác.

Sau mốc đó, tập nguồn có một trục tương đối rõ nhưng vẫn gồm nhiều cụm:

- Task 228–230: thao luyện tân quân và hai task luyện sách/cơ quan có `repeat=1`.
- Task 231–242: hợp luyện nghĩa quân–triều đình, Gia Vương đăng cơ, Chu Hy, Triệu Nhữ Nhu, Hàn Thác Trụ và Khánh Nguyên đảng cấm.
- Task 243–256: do thám Thát Đát, Kim và Tây Hạ.
- Task 257–267: hậu quả chính biến, Chu Hy/Thái Nguyên Định và chuỗi quân doanh Phục Ngưu; Task 267 đưa tin Triệu Nhữ Nhu qua đời.
- Task 268–270: ba task lặp của quân doanh.

Những tên người/sự kiện trùng lịch sử trong các hàng này trước mắt vẫn là **fact game**. Khi dùng làm mốc lịch sử thật phải có truy xuất nguồn lịch sử độc lập và ghi nhãn **fact lịch sử**; mọi cách nối khoảng trống nhân quả cho tiểu thuyết phải ghi **Novelization Bridge**.

### Kết luận locator 08

Locator 08 có trục chính trị–quân sự mạnh hơn các locator 04–07 và có một mốc hậu Du Long Giác trực tiếp. Tuy nhiên các nhóm do thám, quân doanh và task lặp vẫn cần tách lớp trước khi xây timeline tiểu thuyết.

## Branch và normalization candidates phát hiện trong batch

Các mục chi tiết được ghi vào `branch-candidates.md`:

- `BR-003`: ba cổng xuất hành Task 158–160.
- `BR-004`: mười hai tuyến tiếp dẫn môn phái Task 203–214.
- `BR-005`: task lặp/gameplay trong Arc 06–08 không được tự động đưa vào chronology.
- `BR-006`: Task 157 là player-avatar origin; phép ánh xạ sang Tiêu Phùng là adaptation decision.
- `SQ-001`: cùng một subtask 241 dùng cả “Lệ Thu Thủy” và “Lịch Thu Thủy”.

## Phụ lục provenance/query

### Q-0408-PACKETS — kết quả chi tiết đầy đủ

Mỗi file `evidence/source-packets/arc_04.json` đến `arc_08.json` tự lưu:

- đường dẫn và SHA-256 của SQLite;
- đúng danh sách `task_ids` lấy từ locator;
- bốn query template dùng cho `tasks`, `subtasks`, `steps`, `dialogues`;
- toàn bộ kết quả trích xuất trong khóa `tasks`.

### Q-0408-COUNT — thống kê cấu trúc

Query logic (chạy trên từng danh sách `task_ids` được bind trong packet):

```sql
SELECT t.task_id, t.repeat,
       COUNT(DISTINCT s.sub_id) AS subtask_count,
       COUNT(DISTINCT st.id) AS step_count,
       COUNT(DISTINCT d.id) AS dialogue_count
FROM tasks AS t
LEFT JOIN subtasks AS s ON s.task_id = t.task_id
LEFT JOIN steps AS st ON st.sub_id = s.sub_id
LEFT JOIN dialogues AS d ON d.sub_id = s.sub_id
WHERE t.task_id IN (:packet_task_ids)
GROUP BY t.task_id
ORDER BY t.task_id;
```

Kết quả gộp: bảng “Phương pháp và độ phủ” ở đầu tài liệu. Bind values đầy đủ nằm tại `provenance.query_parameters.task_ids` của từng packet.

### Q-0408-DLG — literal scan trong batch

```sql
SELECT DISTINCT t.task_id, t.name AS task_name,
       s.sub_id, s.name AS subtask_name, d.phase
FROM tasks AS t
JOIN subtasks AS s ON s.task_id = t.task_id
LEFT JOIN dialogues AS d ON d.sub_id = s.sub_id
WHERE t.task_id IN (:arc_04_through_08_task_ids)
  AND (COALESCE(t.name, '') || char(10) ||
       COALESCE(t.describe_cleaned, '') || char(10) ||
       COALESCE(s.name, '') || char(10) ||
       COALESCE(s.describe_cleaned, '') || char(10) ||
       COALESCE(d.cleaned_text, '')) LIKE '%Du Long Giác%'
ORDER BY t.task_id, s.sub_id, d.id;
```

Bind values là phép nối năm mảng `task_ids` trong packet 04–08. Kết quả: 3 hàng — `(146, Khiêu Sơn Chấn Hổ, 295, Thuật Giam Cầm, start)`, `(150, Thân Bạn Nguy Cơ, 299, Kế Hoạch Tuyệt Mật, start)`, `(231, Vì Nước Vì Dân, 406, Vì Nước Vì Dân, start)`.

### Q-157-STRUCTURE — lõi thân thế

```sql
SELECT t.task_id, t.name, s.sub_id, s.name AS subtask_name,
       s.dialog_npc_name,
       COUNT(DISTINCT st.id) AS steps,
       COUNT(DISTINCT d.id) AS dialogues
FROM tasks AS t
JOIN subtasks AS s ON s.task_id = t.task_id
LEFT JOIN steps AS st ON st.sub_id = s.sub_id
LEFT JOIN dialogues AS d ON d.sub_id = s.sub_id
WHERE t.task_id = 157
GROUP BY t.task_id, s.sub_id
ORDER BY s.sub_id;
```

Kết quả: 15 hàng, `sub_id` 306–313 và 317–323; tổng 15 subtask. Nội dung đầy đủ của từng hàng, step và dialogue nằm trong `evidence/source-packets/arc_06.json`.

### Q-225-STRUCTURE — cầu nối Phục Ngưu

```sql
SELECT t.task_id, t.name, s.sub_id, s.name AS subtask_name,
       t.repeat, t.order_type, s.dialog_npc_name,
       COUNT(DISTINCT st.id) AS steps,
       COUNT(DISTINCT d.id) AS dialogues
FROM tasks AS t
JOIN subtasks AS s ON s.task_id = t.task_id
LEFT JOIN steps AS st ON st.sub_id = s.sub_id
LEFT JOIN dialogues AS d ON d.sub_id = s.sub_id
WHERE t.task_id = 225
GROUP BY t.task_id, s.sub_id
ORDER BY s.sub_id;
```

Kết quả: một hàng — task 225, subtask 400, `repeat=0`, `order_type=linear`, 6 steps, 1 dialogue. Nội dung đầy đủ nằm trong `evidence/source-packets/arc_07.json`.
