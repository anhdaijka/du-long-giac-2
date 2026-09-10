# Writer preflight coverage ledger — Quyển I

Trạng thái: `AUTHOR-APPROVED COVERAGE SCOPE / R-71 / PREFLIGHT ONLY / NOT A SCENE PLAN / NOT PROSE / NOT CANON`.

## Mục đích

Đây là chỉ mục thi hành đầy đủ cho 25 chapter baseline đã duyệt. Nó **không** sao chép hoặc diễn giải lại source thành lore mới: bản sao thứ hai của 25 brief sẽ tạo thêm nơi Gemini có thể đọc nhầm một suy diễn thành fact.

Thay vào đó, mỗi lượt Gemini bắt buộc mở đúng ba lớp đã có: chapter brief, shared provenance ledger và JSON extraction result được chỉ rõ dưới đây. Chỉ sau khi replay/đọc được result tương ứng, Gemini mới được đưa một proposition vào `ALLOWED` của candidate packet; không có “knowledge mặc định” từ tên chương, function, sequence, task number hay một brief đơn lẻ.

## Quy tắc thực thi zero-trust

1. **Mở đúng input.** Mỗi chương phải đọc brief được dẫn, dòng `provenance-ledger.tsv`, và container JSON được dẫn trong bảng. JSON chứa query templates, query binds và extraction result replay từ `story_database.sqlite3`.
2. **Tạo receipt trước claim.** Mỗi durable proposition trong output phải có `claim → source node → query/result container → evidence class`. Nếu nguồn chỉ là lời nhân vật, receipt phải ghi `SOURCE REPORT`, không phải fact khách quan.
3. **Phân lớp không được trộn.** `DIRECT SOURCE`, `SOURCE-SUPPORTED INFERENCE`, `AUTHOR-APPROVED NOVELIZATION BRIDGE` và `OPEN — DO NOT FILL` là bốn lớp khác nhau. Một brief/function là planning authority, không tự biến thành Direct Source.
4. **Chỉ thi hành ranh giới, không hoàn thành hộ nguồn.** Starting/ending state, knowledge boundary, NPC agency, protected unknown và forbidden changes trong brief là hard bounds. Chúng không cấp quyền bịa cause, route, venue, mechanism, medical/combat detail, dialogue hay chronology.
5. **Fail closed.** Một receipt thiếu bất kỳ trường nào dưới đây chỉ có kết quả `ESCALATE QUESTION`; Gemini không được viết candidate scene plan hay prose để “thử xem có hợp lý không”.

### Receipt bắt buộc cho từng proposition

```text
chapter_key:
proposition:
classification: DIRECT SOURCE | SOURCE REPORT | SOURCE-SUPPORTED INFERENCE |
                AUTHOR-APPROVED NOVELIZATION BRIDGE | OPEN
sqlite_source: task_id/sub_id + source node
query_and_result: packet path + exact result container
receiver_scope: POV / organization / reader / unknown
brief_boundary: section + quoted constraint
decision_id: required for every durable Bridge; otherwise N/A
verdict: ALLOWED | ESCALATE QUESTION
```

### Lỗi dừng bắt buộc

| Code | Khi nào dùng | Gemini phải làm gì |
| --- | --- | --- |
| `PF-FACT-01` | Result không nói đúng subject + predicate + scope của claim. | Xóa claim, hỏi Tác giả nếu claim cần thiết. |
| `PF-REPORT-02` | Claim được suy từ lời kể, lời đồn, notice hay thông cáo. | Ghi `SOURCE REPORT` / `DOCUMENT CLAIM`; không xác nhận khách quan. |
| `PF-BRIDGE-03` | Cần connective material tạo durable fact nhưng không có decision ID. | Ghi `BRIDGE-CANDIDATE`, dừng chờ amendment. |
| `PF-OPEN-04` | Cần ngày, đường đi, venue, custody, mechanism, combat/medical detail hoặc open slot khác. | `ESCALATE QUESTION`; không chọn phương án “hợp lý nhất”. |
| `PF-KNOW-05` | POV biết điều chỉ reader/nhân vật/tổ chức khác biết. | Hạ scope hoặc dừng. |
| `PF-FORM-06` | Output đã thành scene, beat, dialogue, action blocking hay prose. | Loại output; preflight không được mở cổng này. |
| `PF-BRANCH-07` | Claim dựa route/flag/đối thoại condition chưa kiểm tra. | Ghi condition và hỏi Tác giả trước khi linearize. |

## Coverage 01–25

`Query/result` dùng packet provenance `query_templates` + `query_binds` và JSON result container ghi ở cột tương ứng. Gemini không được thay packet bằng Narrative Book, archive hay latent memory.

| Chương | Brief bất biến | SQLite query/result bắt buộc | Proof obligation bổ sung |
| --- | --- | --- | --- |
| 01 | `briefs/chapter_01.md` | `arc_00.json` → `tasks[task_id=1].subtasks[sub_id=1]` | Đã có packet mẫu `chapters_01_03.md`; tỷ võ/thiết lập kế vị không tự cho phép chọn avatar thắng hay Tĩnh trực tiếp giao đấu. |
| 02 | `briefs/chapter_02.md` | `arc_06.json` → `tasks[task_id=157].subtasks[sub_id=306..309]` | Đã có packet mẫu; tên bảo hộ không suy ra họ thật/cha mẹ/võ học. |
| 03 | `briefs/chapter_03.md` | `arc_06.json` → `tasks[task_id=157].subtasks[sub_id=317..319]` | Đã có packet mẫu; lời Hứa về bệnh sử là `SOURCE REPORT`, không khách quan hóa. |
| 04 | `briefs/chapter_04.md` | `arc_01.json` → `tasks[task_id=12].subtasks[sub_id=85,86]` | Mọi lời về ngọc/đồ vật/ai giữ nó phải qua `PF-FACT-01`; không suy artifact truth từ nhiệm vụ xâm nhập. |
| 05 | `briefs/chapter_05.md` | `arc_00.json` → `tasks[task_id=1].subtasks[sub_id=2]` | Cáo buộc và thư tin là report/document claim; không giải custody hay biến cáo buộc thành historical truth. |
| 06 | `briefs/chapter_06.md` | `arc_00.json` → `tasks[task_id=1].subtasks[sub_id=3]` | Lý Tuyền tự nhận/lãnh đạo bàn việc là scope nguồn; không suy nội gián, nội dung thư hay kế hoạch cứu. HEAVY cần split review nếu vượt guard. |
| 07 | `briefs/chapter_07.md` | `arc_06.json` → `tasks[task_id=157].subtasks[sub_id=310]` | Lời giới thiệu môn phái không cấp nội tình Cái Bang, năng lực hay lộ trình gia nhập. |
| 08 | `briefs/chapter_08.md` | `arc_01.json` → `tasks[task_id=12].subtasks[sub_id=87,88]` | Cháy/thương tích chỉ ở mức result xác nhận; không nhận diện phe địch, lý do xâm nhập hay artifact truth. HEAVY guard. |
| 09 | `briefs/chapter_09.md` | `arc_06.json` → `tasks[task_id=157].subtasks[sub_id=311,320]` | “Hai mươi mốt chìa khóa” và cảnh báo thủy lưu không tự xác nhận nước đã ngập hoặc phe phối hợp. |
| 10 | `briefs/chapter_10.md` | `arc_06.json` → `tasks[task_id=157].subtasks[sub_id=312,320]` | Tổ chức đã hành động không đồng nghĩa Tiêu biết kết quả cứu hay có quyền gán actor/cách cứu. |
| 11 | `briefs/chapter_11.md` | `arc_00.json` → `tasks[task_id=1].subtasks[sub_id=4]` | Thủy đạo/tin mật và mọi causal explanation phải tách source report khỏi objective truth. HEAVY guard. |
| 12 | `briefs/chapter_12.md` | `arc_00.json` → `tasks[task_id=1].subtasks[sub_id=5]` | Độc, cờ quan và dấu hiệu không đủ để chỉ thủ phạm, cơ chế hay allegiance. |
| 13 | `briefs/chapter_13.md` | `arc_01.json` → `tasks[task_id=12].subtasks[sub_id=89,90]` | Quyền Bách Hoa chỉ dùng đúng predicate trong result; không invent lịch sử môn phái, y thuật hay bản chất vật chứng. HEAVY guard. |
| 14 | `briefs/chapter_14.md` | `arc_06.json` → `tasks[task_id=157].subtasks[sub_id=313,321,322]` | Trục cuốn/ghi chép là document scope; không đọc thành complete history, cơ chế hoặc parentage. HEAVY guard. |
| 15 | `briefs/chapter_15.md` | `arc_00.json` → `tasks[task_id=1].subtasks[sub_id=6]` | Bãi/địa bàn được giữ không xác nhận thương vong, chiến thuật, chủ quyền hay thời lượng ngoài result. HEAVY guard. |
| 16 | `briefs/chapter_16.md` | `arc_00.json` → `tasks[task_id=1].subtasks[sub_id=7]` | Tiễn xa/quân lệnh không cấp exact chronology, đường hành quân, mục tiêu kín hoặc knowledge cross-POV. |
| 17 | `briefs/chapter_17.md` | `arc_06.json` → `tasks[task_id=157].subtasks[sub_id=323]` | Giấy rách/lời ghi chỉ là document claim trừ khi result xác nhận độc lập; không suy parental/custody truth. HEAVY guard. |
| 18 | `briefs/chapter_18.md` | `arc_00.json` → `tasks[task_id=1].subtasks[sub_id=8]`; `tasks[task_id=2].subtasks[sub_id=9]` | Hai thư tạo handoff giới hạn, không chứng minh người nhận, thời điểm nhận hoặc nội dung ngoài source. HEAVY guard. |
| 19 | `briefs/chapter_19.md` | `arc_01.json` → `tasks[task_id=12].subtasks[sub_id=91]` | Bệnh/độc/tù binh là đặc biệt dễ overclaim: không suy thủ phạm, prognosis, thuốc hay kết quả Tam Muội. HEAVY guard. |
| 20 | `briefs/chapter_20.md` | `arc_00.json` → `tasks[task_id=2].subtasks[sub_id=9]`; `arc_06.json` → `tasks[task_id=157].subtasks[sub_id=310,323]` | Handoff giữa packet chỉ là planning bridge đã duyệt; Tiêu không biết thư Thiên Vương hay identity người relay nếu result/brief không cho. |
| 21 | `briefs/chapter_21.md` | `arc_00.json` → `tasks[task_id=2].subtasks[sub_id=10,12,13]` | Lục–Thôi là organizational agency: không chuyển chiến công cho Tiêu, không nêu người/cách cứu Lục. HEAVY guard. |
| 22 | `briefs/chapter_22.md` | `arc_00.json` → `tasks[task_id=2].subtasks[sub_id=14]` | Phân công áp giải không suy toàn bộ nội bộ Thạch Trường, hành trình hay mức tin cậy Tiêu. |
| 23 | `briefs/chapter_23.md` | `arc_01.json` → `tasks[task_id=12].subtasks[sub_id=91,92]` | Hậu quả tổ chức không tự xác nhận con số thương vong, custody, Tam Muội outcome hay phản ứng dài hạn. |
| 24 | `briefs/chapter_24.md` | `arc_01.json` → `tasks[task_id=12].subtasks[sub_id=92]` | Thông cáo chỉ là lời công khai/document claim; không xác nhận custody, relay actor, phản ứng bốn phái hay artifact function. HEAVY guard. |
| 25 | `briefs/chapter_25.md` | `arc_00.json` → `tasks[task_id=2].subtasks[sub_id=13,14]`; `arc_01.json` → `tasks[task_id=12].subtasks[sub_id=92]` | Public relay không nối trio trực tiếp, không tiết lộ custody và không tạo chronology kín. |

## Handoff cho Gemini theo lô

Không có chapter nào tự writer-ready chỉ vì đã nằm trong bảng. Khi Tác giả mở một lô, Gemini phải:

1. Sao chép receipt trống ở trên cho **mọi proposition** định dùng, không chỉ claim “quan trọng”.
2. Đối chiếu mỗi receipt với brief theo chapter, nhất là `Knowledge boundary`, `NPC and world agency`, `Protected unknowns`, `Forbidden changes`.
3. Chạy self-check năm câu trong [packet 01–03](chapters_01_03.md); thêm mọi `PF-*` phát hiện được.
4. Chỉ trình **candidate preflight packet**, không scene/beat/prose. Tác giả duyệt packet và cổng kế tiếp riêng rẽ.

## Rào toàn Quyển I

- Không có cuộc gặp trực tiếp của trio; custody khách quan Du Long Giác, cơ chế Huyền Nguyệt, ngày/thời lượng/đường đi, chi tiết y khoa/giao đấu và mọi open slot không được tự lấp.
- Canon Tĩnh Xuyên/Mộc Nhất Lâu tự tay hạ sát Ân Đồng trong tương lai và gánh hậu quả không được đổi/giảm nhẹ; không chọn hung khí hay implementation ở Quyển I.
- Không đọc archive/rejected, Narrative Book hay Foundation claim chưa đối soát như evidence thay SQLite.
- Mọi `BRIDGE-CANDIDATE`, contradiction Foundation–SQLite, branch/flag chưa replay hoặc cần thiết kế scene là câu hỏi dành cho Tác giả.
