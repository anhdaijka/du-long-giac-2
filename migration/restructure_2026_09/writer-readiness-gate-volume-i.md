# Đề xuất Writer-Readiness Gate — Quyển I

Trạng thái: `AUTHOR-APPROVED GEMINI-PRIMARY PREFLIGHT / WRGQ-01–04 / R-70 / NOT A SCENE PLAN / NOT PROSE / NOT CANON`.

## Mục tiêu

Gemini là agent vận hành chính: tự đọc nguồn, tự dựng candidate preflight packet, tự viết non-canon draft khi gateway đã mở. Gate này **không** gỡ freeze scene-plan, không tạo packet cụ thể và không cấp quyền viết prose. Nó chỉ định nghĩa điều kiện tối thiểu để Gemini được phép làm từng bước dưới author gate.

## Writer contract bắt buộc

Mọi batch tương lai phải kèm đúng năm khối, lấy từ chapter brief/provenance đã duyệt chứ không tự suy:

1. `ALLOWED`: fact game có locator/query-result, Bridge có decision ID, và wording/vi động tác không tạo durable fact.
2. `MUST PRESERVE`: primary POV, entry/exit state, knowledge boundary, agency NPC/tổ chức và các protected canon.
3. `OPEN — DO NOT FILL`: exact date/travel/venue, objective custody, cơ chế Huyền Nguyệt, kết quả y khoa/chi tiết giao đấu, hung khí Ân Đồng và mọi Bridge chưa duyệt.
4. `KNOWLEDGE IN/OUT`: chỉ những gì POV thực sự nhận qua scene/relay đã được phép; `READER_KNOWLEDGE != CHARACTER_KNOWLEDGE`.
5. `ESCALATE`: khi writer cần một durable fact, actor, chronology, mechanism hoặc causal exit-state chưa có trong packet, dừng và hỏi; không đoán hoặc “làm cho tròn cảnh”.

## Gemini-first source protocol

1. Gemini tự truy nguồn trước khi đưa một proposition vào `ALLOWED`: SQLite query/result hoặc source packet phải khớp **đúng chủ thể, predicate và scope**. Narrative Book chỉ là locator.
2. Một clue, tên task, tiêu đề, lời đồn, một dòng dialogue, numeric adjacency, hoặc glue giữa hai nguồn **không đủ** để nâng thành fact game, historical fact hay durable state.
3. Khi source chỉ hỗ trợ khả năng/diễn giải, Gemini phải ghi `SOURCE-SUPPORTED INFERENCE` hoặc `BRIDGE-CANDIDATE`, không được viết thành fact. Bridge bền vững chỉ được dùng sau decision ID của Tác giả.
4. Gemini không tự gỡ một `OPEN — DO NOT FILL`, không tự chọn fact nào thắng khi Foundation–SQLite mâu thuẫn, và không sửa source/canon để hợp với draft của mình.
5. Gemini có thể tự review candidate packet bằng contract này, nhưng self-review không thay tác giả: gate canon, amendment, V1SPAQ và mọi decision ID vẫn chỉ do Tác giả mở/duyệt.

Từ D-062/R-88, [Gemini Chapter Workflow Router](gemini-chapter-workflow-router.md) áp dụng contract này cho từng chapter Quyển I–V. Nó chỉ tạo preflight cục bộ theo yêu cầu, vẫn giữ V1SPAQ và các cổng prose hiện hành.

## Luồng làm việc tối giản

```text
approved brief + provenance → preflight packet → candidate scene plan → V1SPAQ author approval → non-canon prose batch → review → separate canon decision
```

- Preflight packet không thay candidate scene plan; nó chỉ là lớp bảo vệ để writer không đọc cả repository hay tự nối source gap.

## Default-progress policy — D52/R-78

Source reconstruction, source map, non-canon architecture, provenance/coverage ledger, deterministic check và các proposal planning có thể đi thẳng theo workflow khi chúng chỉ giữ hoặc thu hẹp ranh giới evidence. Không tạo hard stop chỉ để hỏi lại một lựa chọn mặc định đã có đề xuất an toàn; agent ghi rõ trạng thái `AUTHOR-DEFAULTED PLANNING`, giữ artifact có thể sửa và tiếp tục bước kế tiếp cần thiết.

Hard stop chỉ còn bắt buộc **trong writer workflow Gemini** khi packet/draft thực sự cần một trong các điều sau:

1. một game/historical fact bền vững mà SQLite/source packet không chứng minh đúng proposition;
2. chọn giữa source/Foundation mâu thuẫn, branch loại trừ nhau, hoặc chronology làm đổi trách nhiệm;
3. canonize/retcon durable state, identity, relationship, outcome, custody hay world rule;
4. một Novelization Bridge sáng tạo bền vững (đặc biệt actor, motive, venue, dialogue, combat outcome hoặc causal exit) không đã có decision ID;
5. Gemini cần lấp `OPEN — DO NOT FILL`, hard stop hoặc vượt knowledge boundary để hoàn thành scene/draft.

Khi đó Gemini không tự đoán: nó xuất đúng author question có source receipt, phần còn thiếu và tối đa một đề xuất. Ngoài năm trường hợp này, Gemini tiếp tục làm preflight/self-check/draft non-canon theo packet đã có.
- Prose luôn là `NON-CANON DRAFT`; không bản nào tự cập nhật Story Skills/canon.
- Khi một agent không tuân contract, output bị loại khỏi continuity thay vì sửa ngược nguồn/canon cho khớp output.

## Phạm vi batch đầu được khuyến nghị

| Hạng mục | Đề xuất |
| --- | --- |
| Quyển | Chỉ Quyển I. Quyển II–V chưa writer-ready. |
| Kích thước | 3 chương/batch: 01–03 trước. Đây là pilot độ an toàn, không phải cadence bắt buộc. |
| Writer và preflight | Gemini tự đọc các source artifact được phép, dựng candidate packet và làm self-check theo contract. |
| Reviewer | Tác giả là authority duy nhất cho gate/canon/amendment. Deterministic checks chỉ kiểm cấu trúc, không thay author approval. |
| Cổng prose | Giữ SPQ → candidate scene plan → V1SPAQ. Không có shortcut từ chapter brief sang prose. |

## Không thay thế được bằng prompt

- Prompt “đừng bịa” một mình không đủ: writer phải có `OPEN — DO NOT FILL` và `ESCALATE` rõ ràng theo batch.
- Không cho writer chọn/chuyển task, nhân vật giao tin, lịch, scene location hoặc cách giải protected unknown.
- Không giao tiếp trực tiếp bằng “timeline đầy đủ” vì chronology tuyệt đối chưa tồn tại và không được tự suy từ task number.

## Quyết định tác giả — WRGQ-01–04

| ID | Điểm cần chốt | Đề xuất |
| --- | --- | --- |
| WRGQ-01 | Có duyệt Writer contract năm khối làm bắt buộc cho mọi writer model? | Duyệt; bất cứ agent nào vi phạm thì output chỉ là discarded draft. |
| WRGQ-02 | Có pilot 3 chương 01–03 trước thay vì đưa 25 chương cho Gemini? | Duyệt; kiểm độ tuân thủ trước khi tăng batch. |
| WRGQ-03 | Có giữ gateway SPQ → V1SPAQ trước khi prose, không mở shortcut? | Duyệt; đây là một cổng hiện có, không tạo thủ tục mới. |
| WRGQ-04 | Có chỉ định Terra medium là reviewer contract/provenance, còn Gemini chỉ là writer non-canon? | Thay thế bởi R-70: Gemini vận hành toàn thời gian; chỉ Tác giả duyệt gate/canon/amendment. |

Ngày 2026-09-09, Tác giả duyệt toàn bộ đề xuất. R-70 sau đó thay vai Terra bằng Gemini-first source protocol, giữ nguyên author gate. WRGQ-01–04 trở thành planning authority. Bước tiếp theo được mở là Gemini tạo **một candidate preflight packet mẫu cho chương 01–03**, không prose, để Tác giả xem trước khi quyết định có gỡ freeze candidate scene-plan hay không.
