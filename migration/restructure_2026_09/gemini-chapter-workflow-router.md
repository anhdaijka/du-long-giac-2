> Current temporal/creative authority: migration/restructure_2026_09/temporal-continuity-contract.md and temporal-character-framework.md (D-064/R-90 and D-065/R-91). Read both before chapter operations. Framework direction is not source receipt or prose authorization.

# Gemini Chapter Workflow Router — Quyển I–V

Trạng thái: `AUTHOR-DEFAULTED OPERATIONAL ROUTER / D62-R88 / GEMINI-PRIMARY / NOT A SCENE PLAN / NOT PROSE AUTHORITY / NOT CANON`.

## Mục đích

Router này là contract vận hành chung để Gemini làm **một chương đang được yêu cầu** mà không đọc tản mạn cả repository, không tự nối clue/glue thành fact, và không dựng sẵn 140 packet. Nó áp dụng cho tất cả 140 chapter-function trong [Series Chapter Allocation Index](series-chapter-allocation-index.md).

Mặc định mỗi yêu cầu chỉ tạo `CHAPTER-LOCAL PREFLIGHT`. Scene plan hoặc `NON-CANON DRAFT` chỉ được tạo khi Tác giả đã mở đúng cổng prose/scene còn hiệu lực cho chương đó. Router không tự mở cổng này.

## Cách gọi Gemini

Người dùng chỉ cần nêu một câu theo mẫu:

```text
Làm PREFLIGHT cho Quyển <I–V>, chương <số>.
Mục tiêu cục bộ: <nếu có>.
```

Hoặc, chỉ khi cổng viết đã được Tác giả mở rõ ràng:

```text
Làm NON-CANON DRAFT cho Quyển <I–V>, chương <số>, theo preflight đã duyệt: <receipt/gate>.
```

Gemini không hỏi lại count, POV aperture, working title hay function đã được allocation khóa. Nếu mục tiêu cục bộ vắng mặt, Gemini dùng function của chapter row và tiếp tục preflight.

## Router bắt buộc

### 1. Xác định authority chain

1. Mở [Series Chapter Allocation Index](series-chapter-allocation-index.md) để lấy source scope, reuse guard, volume handoff và `WG-*` liên quan.
2. Đọc `canon-registry/README.md` và query `registry-index.tsv` hẹp nếu registry có row liên quan. Registry rỗng là bình thường; không có row không chứng minh fact không tồn tại. Mọi row chỉ là locator, vẫn phải mở raw receipt/decision.
3. Mở đúng `chapter-sequence.md` của quyển để lấy chapter key, POV, function và writer boundary.
4. Mở đúng row trong `provenance-ledger.tsv` để lấy packet, `result_refs` (hoặc `query_result_container` ở Quyển II), evidence class và escalation.
5. Mở đúng JSON source packet, query templates/binds và result container. SQLite packet là authority game fact; Narrative Book chỉ là locator.
6. Chỉ với Quyển I, mở thêm bounded brief và [coverage ledger](writer-preflight-volume-i/volume-i-coverage-ledger.md). Với Quyển II–V, chapter sequence + ledger + source window là ceiling hiện hành, không được bù bằng một brief tự viết như source.

Không dùng archive/rejected, task title, Task ID adjacency, latent memory, Foundation chưa đối soát hoặc source locator làm evidence thay receipt.

### 2. Lập claim receipt trước khi dùng claim

Mỗi proposition bền vững Gemini định dùng phải có đúng schema dưới đây. Một chapter có thể có ít claim; không có quota claim.

```text
chapter_key:
proposition:
classification: DIRECT SOURCE | SOURCE REPORT | SOURCE-SUPPORTED INFERENCE |
                AUTHOR-APPROVED NOVELIZATION BRIDGE | OPEN
sqlite_source: task_id/sub_id + source node, hoặc N/A cho Bridge
query_and_result: packet path + exact result container
receiver_scope: POV | organization | reader | unknown
chapter_boundary: sequence/brief constraint được áp dụng
decision_id: bắt buộc nếu là durable Bridge; nếu không thì N/A
verdict: ALLOWED | HOLD AS REPORT | ESCALATE QUESTION
```

`SOURCE REPORT`, document claim, rumor, game-alt-history, gameplay instruction hoặc một clue chỉ được dùng đúng nhãn. Chúng không tự trở thành objective fact, historical fact hay causal exit-state.

### 3. Xuất đúng một trong ba kết quả

| Kết quả | Khi dùng | Nội dung được xuất |
| --- | --- | --- |
| `PREFLIGHT READY` | Mọi durable proposition cần dùng đã có receipt/decision và không chạm gate. | Route card, receipts, allowed/preserve/open/knowledge và self-check. Không scene/beat/prose. |
| `QUESTION ONLY` | Cần chi tiết thuộc `WG-*` hoặc `PF-*` để thực hiện. | Một author question tối thiểu; không lấp gap bằng draft thử nghiệm. |
| `DRAFT READY` | Tác giả đã mở cổng scene/prose liên quan **và** preflight được duyệt. | Chỉ `NON-CANON DRAFT`, theo packet đã duyệt; không canonization hoặc state update. |

Nếu một phần chương không cần gap, Gemini được phép trả `PREFLIGHT READY` cho phần đó và liệt kê gap ở `OPEN — DO NOT FILL`; không tự chặn cả workflow chỉ vì một khả năng chưa dùng.

## Mẫu output `CHAPTER-LOCAL PREFLIGHT`

```markdown
# Preflight — V<volume>-CH-<number>

Status: PREFLIGHT READY | QUESTION ONLY
Authority read: <index + sequence + ledger + packet + brief/coverage nếu có>
POV / function: <đúng nguyên văn allocation>

## Route card
- Source receipt: <T/S + exact packet container>
- Evidence class: <đúng ledger>
- Cross-volume handoff: <nếu có, chỉ relative order>
- Reuse guard: <nếu locator bị tái dùng>

## Claim receipts
| Proposition | Classification | Receipt | Receiver scope | Verdict |
| --- | --- | --- | --- | --- |

## MUST PRESERVE
- <POV, agency, protected canon, function boundary>

## OPEN — DO NOT FILL
- <chỉ các gap liên quan chapter>

## KNOWLEDGE IN / OUT
- In: <được biết>
- Out: <không tự biết>

## Self-check
- proposition receipt: PASS/FAIL
- report/alt-history labeling: PASS/FAIL
- open-slot preservation: PASS/FAIL
- POV knowledge: PASS/FAIL
- form boundary: PASS/FAIL
```

Với Quyển I, `MUST PRESERVE`, `OPEN` và knowledge phải đối chiếu thêm bounded brief. Với II–V, không được tự mở rộng các trường này vượt sequence row, ledger và packet.

## Điều kiện hard-stop thực sự

Gemini chỉ xuất `QUESTION ONLY` khi detail là cần thiết và chạm một trong các nhóm sau:

| Trigger | Hành động |
| --- | --- |
| `WG-01` / `PF-FACT-01`, `PF-REPORT-02`, `PF-BRANCH-07` | Không nâng report/clue/branch chưa replay thành fact; hỏi nếu claim cần thiết. |
| `WG-02` / `PF-OPEN-04` | Không chọn date, duration, route, venue, chronology hay causal order còn mở. |
| `WG-03` | Không chọn Du Long mechanism, custody, function hay final truth. |
| `WG-04` | V2-CH-21: không tự đặt actor, venue, dialogue, combat, outcome hoặc durable relation của first convergence. |
| `WG-05` | Không hòa giải T330/T352 hoặc giải “bí mật thứ hai”. |
| `WG-06` | V5-CH-20: không tự chốt placement, hung khí, ngày hay logistics Ân Đồng; killer/outcome/responsibility của Tĩnh phải giữ nguyên. |
| `WG-07` | V5-CH-27–28: không gọi Huyễn Cảnh là corroboration thân thế và không tự tạo chứng cứ độc lập. |
| `WG-08` | V5-CH-32–35: không khép Du Long, quân bị, chữa trị hay hậu truyện. |
| `PF-KNOW-05` | Hạ receiver scope hoặc hỏi nếu scene cần chuyển knowledge bền vững. |
| `PF-FORM-06` | Quay lại preflight nếu request chưa được mở scene/prose. |

Một author question luôn dùng mẫu ngắn này:

```text
AUTHOR QUESTION — <chapter key / gate>
Need: <một proposition hoặc lựa chọn không thể tránh>.
Evidence: <packet + exact locator, hoặc decision ID hiện có>.
Open reason: <vì sao evidence không đủ / branch xung đột>.
Optional proposal: <tối đa một Bridge candidate, hoặc “không đề xuất”>.
```

Không hỏi Tác giả về gesture, sensory realization, wording hoặc micro-action không làm đổi durable fact/knowledge/outcome.

## Quy tắc riêng cho `NON-CANON DRAFT`

Chỉ sau `DRAFT READY`, Gemini mới được viết. Khi viết:

- Giữ POV, knowledge scope, protected canon, agency NPC/tổ chức và mọi `OPEN — DO NOT FILL` của preflight.
- Có thể tạo wording, nhịp câu, gesture, texture và micro-action không làm đổi durable state.
- Không tự thêm event, route completion, chiến công avatar, medical/combat outcome, relationship shift hoặc authority change.
- Gắn nhãn `NON-CANON DRAFT`; không sửa Story Skills, canon, Foundation, ledger hoặc source để hợp draft.

## Tự kiểm trước khi giao

Trước mỗi output, Gemini trả `PASS` cho cả năm câu:

1. Mỗi durable proposition có exact receipt hoặc decision ID chưa?
2. Có claim nào đang nâng report, clue, title, gameplay, Huyễn Cảnh hay alt-history thành fact khách quan không?
3. Có open slot nào bị lấp bằng chi tiết “hợp lý” nhưng chưa được source/author quyết không?
4. POV có biết vượt receiver scope hoặc biến agency NPC/tổ chức thành công lao trio không?
5. Output có vượt mode đang được mở (preflight / scene / prose) không?

Một `FAIL` khiến output là `QUESTION ONLY` hoặc rút claim. Gemini không dùng bản draft để thử nghiệm một fact còn thiếu.

## Antigravity execution — D63/R89

Các lệnh `/dlg-preflight`, `/dlg-write`, `/dlg-review`, `/dlg-revise` dùng skills tương ứng trong `.agents/skills/`. Đọc [hướng dẫn sử dụng](../../docs/antigravity-novel-workflows.md).
Review/sửa theo review dùng [contract đối chiếu nguồn](../../docs/playbooks/gemini-evidence-review.md): đọc toàn manuscript hiện tại, tự tìm cả claim ngoài ledger, đối chiếu raw source/author decisions và kiểm knowledge/continuity. Review có thể thực hiện khi draft chưa được duyệt. Review PASS không thay author acceptance.

## Ranh giới

Router không phải source, canon, scene plan, prompt thay cho packet, hay một timeline tuyệt đối. Nó không thay đổi 140 allocation, không mở prose và không khép Foundation claim audit.
