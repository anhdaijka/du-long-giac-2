# Spec đã duyệt — Phase Chapter Architecture Quyển I

Trạng thái: `AUTHOR-APPROVED PHASE SPEC / CAPQ-01–06 / NOT A CHAPTER ARCHITECTURE / NOT CANON`.

Tài liệu này chỉ định nghĩa cách tạo và kiểm tra chapter architecture Quyển I sau khi continuity-detail đã được duyệt. Tác giả đã phê duyệt CAPQ-01–06 ngày 2026-09-09, mở quyền tạo sáu artifact dạng candidate ở mục 6. Phê duyệt này **không** đặt số chương, số thứ tự chương, tên chương, scene, beat, lời thoại hoặc prose, và không tự phê duyệt bất kỳ chapter-function row nào sẽ được đề xuất.

## 1. Restate Brief

Phase kế tiếp phải chuyển ba Route Bible, World Spine và continuity-detail contract thành một kiến trúc chương có thể review mà không quay lại mô hình player-avatar làm mọi việc. Kiến trúc tương lai phải:

- cho Tiêu Phùng, Tĩnh Xuyên và Hạ Nương mỗi người có nhịp phát triển độc lập;
- cho thế giới/môn phái/NPC tự vận động và để độc giả thấy sự kiện ngoài trio;
- giữ hội tụ Quyển I ở mức thư, tin và hậu quả, không gặp trực tiếp;
- không khóa ngày, custody Du Long, cơ chế Huyền Nguyệt hoặc hung khí Ân Đồng;
- tuyệt đối bảo toàn future canon Tĩnh Xuyên–Ân Đồng nhưng không diễn trước route ấy trong Quyển I.

## 2. Authority và đầu vào bắt buộc

### Planning authority

1. [Author decisions](author-decisions.md), R-11–R-40.
2. [Volume architecture](volume-architecture-proposal.md), Quyển I “Ba ngả xuất hành”.
3. [Route Bible pilot](route-bibles/README.md) và ba bible/convergence matrix.
4. [Bridge feasibility](bridge-feasibility-volume-i.md), BFCQ-01–04.
5. [Continuity-detail contract](continuity-detail-spec-volume-i.md), CDQ-01–05.
6. [World coverage](world-coverage/README.md) và ledger 465 task/390 family ở mức preliminary disposition.

### Source authority

SQLite `story_database.sqlite3`, SHA-256 `b5c30040c9449f2223cf40bfec9866216423a60a82e2333b5cedb4fb5261bdb0`, vẫn là nguồn tối thượng cho game fact. Phase không được dùng chính các planning artifact làm bằng chứng thay cho source proposition.

| Cụm lõi | Query/bind phải tái dùng | Full result đã lưu |
| --- | --- | --- |
| Task 1, 2, 4 | `SELECT task_id, task_id_hex, name, describe_cleaned, category, category_desc, order_type, repeat, task_type_code, file_path FROM tasks WHERE task_id = ?` bind `(1)`, `(2)`, `(4)`; các query subtask/step/dialogue theo packet | [arc_00.json](evidence/source-packets/arc_00.json) |
| Task 12 | Cùng query task bind `(12)` và query con theo packet | [arc_01.json](evidence/source-packets/arc_01.json) |
| Task 157 | Cùng query task bind `(157)` và query con theo packet | [arc_06.json](evidence/source-packets/arc_06.json) |

Task 4 chỉ là **future-invariant audit input** cho Tĩnh Xuyên–Ân Đồng, không phải content pool được phân vào Quyển I.

## 3. Mục tiêu của phase

Tạo một **chapter-function architecture draft** đủ để Tác giả đánh giá nhịp, tỷ trọng POV, causal coverage và living-wulin coverage trước khi có chapter brief. Mỗi đơn vị tương lai được định nghĩa bằng chức năng và state transition, không bằng prose premise hấp dẫn nhưng thiếu provenance.

Phase phải trả lời được năm câu hỏi:

1. Mỗi chương ứng viên tồn tại để thay đổi điều gì?
2. Ai có quyền POV và người ấy thật sự biết gì?
3. Source node/event-family nào cung cấp chất liệu và phần nào là Bridge?
4. State nào đi vào, state nào đi ra, hậu quả chuyển sang đâu?
5. Nếu bỏ chương ứng viên, causal chain hoặc character arc mất điều gì?

## 4. Phạm vi

### In scope

- Đề xuất movement structure của Quyển I.
- Dựng các **chapter-function row ứng viên**, chưa đánh số và chưa viết brief.
- Interleave ba POV bằng dependency/pressure, không theo vòng chia đều máy móc.
- Chọn World Spine footprint ở mức `candidate`, gồm document, relay, aftermath, living lore và satellite candidate.
- Ước lượng narrative load để suy ra một **dải số chương**, chỉ sau khi mapping hoàn tất.
- Chạy continuity/provenance/density checks và trình Tác giả duyệt architecture draft.

### Out of scope

- Tên/số chương chính thức, scene list, beat sheet, cliffhanger chi tiết, thoại và prose.
- Chốt ngày tháng, quãng đường, thời lượng di chuyển hoặc lịch sử tuyệt đối.
- Lời giải custody Du Long, Huyền Nguyệt hoặc hung khí Ân Đồng.
- Phân Task 4/S28–S37 vào Quyển I.
- Nội dung Route Bible Quyển II–V, Legendary Shadow profile hoặc canon promotion.
- Khôi phục chapter/deck/timeline trong archive làm authority.

## 5. Invariant của phase

| ID | Ràng buộc | Điều validator/reviewer phải bắt |
| --- | --- | --- |
| CAI-01 | `PHYSICAL_CONVERGENCE_VOLUME_I = NONE`. | Không chapter row nào chứa hai protagonist hiện diện trực tiếp. |
| CAI-02 | Mỗi chapter row chỉ có một primary POV; ngôi ba hạn tri sâu. | Không head-hopping hoặc “POV toàn tri tạm thời”. |
| CAI-03 | Chapter function không được thay thế source proposition. | Mỗi game claim có query/result locator; mỗi phép phân vai có decision ID. |
| CAI-04 | Partial order CDQ-03 là chronology duy nhất. | Không ngày, giờ, độ trễ hay đường đi chưa audit. |
| CAI-05 | Lục được cứu ngoài màn, không nêu rescuer; Lục đấu Thôi. | Không tạo chương cứu Lục hoặc trao trận cho Tiêu Phùng. |
| CAI-06 | Relay chọn theo chức năng đã duyệt. | La Phong chỉ khi row cần nhiệm vụ hiện trường; Cầu Chỉ Thủy chỉ khi row cần phán đoán bang vụ/chính trị; không dùng cả hai lặp tin. |
| CAI-07 | `DU_LONG_OBJECTIVE_CUSTODY = UNRESOLVED`; Hạ Nương không xác nhận artifact truth. | Không hidden-holder note, narrator truth hoặc custody side effect. |
| CAI-08 | Huyền Nguyệt chỉ giữ tên/biến cố phòng thủ; mechanism deferred. | Không giải quang học, cơ khí, “năng lượng” hay huyền thuật. |
| CAI-09 | Tĩnh Xuyên–Ân Đồng là future canon bất khả thay thế. | Không đưa Ân Đồng/T4-S28–S37 vào Quyển I; không substitute victim/rehearsal; không làm mềm trách nhiệm tương lai. |
| CAI-10 | NPC/tổ chức giữ agency và causal return. | Không chương nào tồn tại chỉ để NPC khen, cứu hoặc trao vật cho protagonist. |
| CAI-11 | Số chương phát sinh từ density, không từ quota cũ. | Không ép 18, 20, 24, 30 hay công thức vòng lặp trước mapping. |
| CAI-12 | Architecture draft vẫn là proposal. | Không sinh chapter briefs/prose hoặc cập nhật canon trước cổng duyệt riêng. |

## 6. Hình dạng artifact được phép triển khai

CAPQ-01 đã mở quyền tạo đúng các artifact dưới đây:

1. `chapter-architecture/README.md`
   - authority order, trạng thái, cách đọc, cổng duyệt và giới hạn.
2. `chapter-architecture/chapter-function-matrix.tsv`
   - bảng máy đọc được; một row cho mỗi chapter candidate.
3. `chapter-architecture/chapter-function-matrix.md`
   - projection cho Tác giả review, không thêm fact ngoài TSV.
4. `chapter-architecture/interleave-and-dependency-map.md`
   - movement, POV braid, causal edge và handoff giữa các row.
5. `chapter-architecture/world-spine-selection.md`
   - event-family footprint, kênh kể và lý do include/defer/exclude.
6. `chapter-architecture/validation-report.md`
   - kết quả validator, density review, unresolved slots và giới hạn chưa kiểm.

Không tạo file trong `chapters/`, `briefs/`, `plot/` hoặc story-state canonical paths ở phase này.

## 7. Schema chapter-function row

| Field | Bắt buộc | Ý nghĩa |
| --- | --- | --- |
| `candidate_id` | Có | ID ổn định kiểu `V1-CAND-001`; không phải số chương. |
| `movement_id` | Có | Nhóm chức năng macro, chưa phải act/chương chính thức. |
| `primary_pov` | Có | Một trong Tiêu Phùng, Tĩnh Xuyên, Hạ Nương hoặc `SATELLITE_CANDIDATE`. |
| `chapter_function` | Có | Một câu chỉ rõ state/pressure thay đổi. |
| `entry_state` / `exit_state` | Có | Durable state trước/sau; không chứa prose. |
| `source_nodes` | Có | Task/subtask/step locator và packet result. |
| `event_family_ids` | Có | Liên kết World Spine; có thể nhiều family nếu quan hệ đã chứng minh. |
| `bridge_decisions` | Có nếu dùng | R/PB/BFCQ/CDQ ID; bridge mới giữ author gate. |
| `knowledge_in` / `knowledge_out` | Có | Điều POV biết trước/sau và medium truyền tin. |
| `npc_agency` | Có | Ai ngoài POV hành động, muốn gì, trả giá gì. |
| `irreversible_change` | Có | Lựa chọn hoặc hậu quả không thể hoàn tác; `NONE` phải có lý do. |
| `causal_predecessors` / `causal_returns` | Có | Cạnh vào và nơi payoff/aftershock quay lại. |
| `narrative_load` | Có | `LIGHT`, `MEDIUM`, `HEAVY`; dùng để tách/gộp sau review. |
| `coverage_channel` | Có | `DIRECT_TRIO`, `DOCUMENT_TRACE`, `WITNESS_RELAY`, `AFTERMATH`, `LIVING_LORE` hoặc `SATELLITE_CANDIDATE`. |
| `protected_unknowns` | Có | Những điều row tuyệt đối không được quyết định. |
| `status` | Có | `CANDIDATE / AUTHOR REVIEW REQUIRED`, `DEFERRED` hoặc `REJECTED_WITH_REASON`. |

Không có field `scene`, `dialogue`, `chapter_title`, `exact_date`, `travel_duration` hay `true_custody`.

## 8. Quy trình triển khai đề xuất

### Pass A — freeze inputs

- Ghi SHA SQLite và revision của các planning authority.
- Chạy lại validator Route Bible, Bridge, continuity-detail và World Coverage.
- Không dùng archive/rejected làm nguồn cảm hứng mặc định.

### Pass B — movement baskets

Sắp source/route obligations vào năm nhóm chức năng tạm, chưa phải chapter:

1. `M1 — ROOTED WORLDS`: ba môi trường sống và hệ giá trị trước khủng hoảng.
2. `M2 — PRESSURE NETWORKS`: tin đồn, chính danh, thương tích, tổ chức và nhu cầu cộng đồng siết lại.
3. `M3 — IRREVERSIBLE DEPARTURES`: Tiêu Phùng xuất hành, Tĩnh Xuyên nhận giao thư/rời phòng tuyến, Hạ Nương chọn cứu/chuyển chữa.
4. `M4 — INSTITUTIONS ACT`: Cái Bang xử bang quy, Lục đấu Thôi, Thúy Yên tự phòng thủ–tái thiết; trio không ôm mọi chiến công.
5. `M5 — INDIRECT CONVERGENCE`: thư, thông cáo và hậu quả khiến độc giả thấy cùng một trường lực; trio chưa gặp.

Movement chỉ là taxonomy để kiểm nhịp. Một lane có thể tiến qua movement ở tốc độ khác lane khác; không ép round-robin.

### Pass C — chapter-function candidates

- Tạo row từ một state change hoặc một pressure turn, không từ mỗi subtask.
- Gộp source rows khi chúng cùng một causal function và không vượt narrative load.
- Tách khi một row có hơn một irreversible choice, hơn một primary POV, hai cao trào độc lập hoặc cần giải thích nguồn quá dày.
- Không đặt chapter number/title ở pass này.

### Pass D — braid và dependency

- Dùng causal predecessor/return để xếp tương đối.
- Chỉ đổi POV khi lane trước đã tạo một câu hỏi, áp lực hoặc hậu quả mà lane sau làm sâu thêm; không đổi chỉ để “đến lượt”.
- Kiểm `TX handoff → TX exits window → TP Cái Bang window` và `HN notice → Thạch receives → functional relay candidate`.
- Giữ `CB-E` (Lục đấu Thôi) và `HN-E` (thông cáo tới Thạch) chưa có thứ tự tuyệt đối nếu source/contract chưa cấp.

### Pass E — World Spine integration

- Mỗi candidate row phải nêu world footprint hoặc lý do `NONE`.
- Ưu tiên document, relay, aftermath và living lore trước satellite POV.
- Satellite chỉ được ghi `SATELLITE_CANDIDATE`; phải qua sáu tiêu chí LWCQ-02 và author review trước khi thành chapter row thật.
- Không dùng living lore như filler; nó phải đổi lựa chọn, quan hệ, rủi ro hoặc cách hiểu.

### Pass F — density và count inference

- Chấm `LIGHT/MEDIUM/HEAVY` theo số state change, source clusters, cast pressure và combat/medical complexity.
- Đề xuất gộp/tách bằng chức năng, không theo con số chương mong muốn.
- Chỉ sau khi matrix ổn định mới báo: minimum viable count, recommended count band và overflow risks.
- Dải từ/chương trong creative constitution dùng làm capacity check ở phase brief/draft, không dùng để nhồi trước nội dung vào quota chương.

### Pass G — adversarial review và author gate

- Review route overlap, head-hopping, knowledge leak, protagonist gravity, unsupported bridge, world-event orphan và future-canon contamination.
- Trình architecture draft cùng unresolved register.
- Chỉ sau phê duyệt riêng mới được đánh số/tên chương hoặc tạo chapter brief.

## 9. Movement obligations — chưa phải phân chương

| Movement | Tiêu Phùng | Tĩnh Xuyên | Hạ Nương | World Spine | Exit condition |
| --- | --- | --- | --- | --- | --- |
| M1 | Quan hệ lao động/chăm sóc tại quê; trách nhiệm không đồng nghĩa toàn năng. | Chính danh, quân kỷ, vu cáo và mạng phòng tuyến. | Y lý thực chứng, môn phái, giới hạn điều quan sát. | Giá hàng, lời đồn, người bị thương, lệnh điều động có chủ thể. | Mỗi POV có một pressure question riêng. |
| M2 | Chìa khóa, người bị nạn, Bạch Cương/sấm thi tạo nhu cầu rời quê. | Hộ tống/phòng thủ cho thấy quân lệnh cần mạng người và hậu cần. | Tập kích cho thấy y thuật không thay thế chiến đấu/tổ chức. | NPC và thiết chế hành động ngoài trio. | Mỗi route có một lựa chọn sắp không thể rút lại. |
| M3 | Mang trách nhiệm cộng đồng đi theo khi xuất hành. | Mang thư và rời người mình muốn ở lại bảo vệ. | Theo người bị thương/chuyển chữa thay vì truy ngọc. | Handoff phải có người nhận và hậu quả. | Ba irreversible choices hoàn tất, không gặp nhau. |
| M4 | Bước vào Cái Bang như người mới, không nhận công avatar. | Đã rời cửa sổ; hậu quả tồn tại dù POV vắng mặt. | Môn phái/cao thủ giữ chiến công; nàng giữ chăm sóc. | Lục, Thạch, Cầu, La, Doãn, Lệ, Chung và Đường có agency. | Bang quy/phòng thủ/tái thiết đã tạo aftershock. |
| M5 | Có thể nhận phần công khai qua relay đúng chức năng. | Không cần nhận thông cáo T12/S92. | Biết việc tổ chức công bố, không biết phản ứng Cái Bang. | Reader thấy nhiều bản tin và custody bất định. | Hội tụ gián tiếp đạt; `PHYSICAL_CONVERGENCE = NONE`. |

## 10. Nhịp, số chương và xung đột 3-1-1

`author/creative-constitution.md` hiện còn công thức 3-1-1 và mô tả “chương khoảng lặng lữ hành/tương tác bộ ba”. R-17/CDI-02 lại cấm trio gặp trong Quyển I; R-03/R-16/CAI-11 giữ số chương linh hoạt. Đây là xung đột áp dụng, không được giải bằng cách cho trio gặp sớm.

Phương án khuyến nghị cho Quyển I:

- dùng 3-1-1 như **heuristic kiểm độ nghẹt**, không phải chu kỳ năm chương hoặc quota;
- “khoảng lặng” là road/local chapter của **một** POV hoặc world aftermath, không phải tương tác bộ ba;
- không cố tạo đúng một lore chapter sau mỗi ba core chapter;
- matrix phải chứng minh mỗi lore/quiet candidate có causal return;
- số chương chỉ được đề xuất sau Pass F.

Xử lý này đã được duyệt tại CAPQ-05; creative constitution phải diễn đạt 3-1-1 như heuristic cấp series, không phải quota hoặc lý do cho trio gặp sớm.

## 11. Fresh-review checklist

Mỗi architecture draft phải kiểm:

- source locator owner và query/result path;
- route ownership không chồng player-avatar;
- one-POV-per-row và knowledge in/out;
- three irreversible choices không bị hoán đổi;
- không có physical convergence Quyển I;
- Lục rescue không tên, Lục giữ trận Thôi;
- relay La/Cầu khớp chapter function;
- custody/Huyền Nguyệt vẫn mở;
- T4/S28–S37 và Ân Đồng không bị phân vào Quyển I;
- không resurrect archive/rejected;
- mọi satellite/living-lore candidate có causal return;
- candidate count là kết quả của density, không là đầu vào.

## 12. Expected output và acceptance criteria

### Expected output của phase triển khai

- Sáu artifact ở mục 6.
- Một chapter-function matrix chưa đánh số/tên chương.
- Một dải số chương đề xuất có giải trình density, không phải số khóa.
- Một unresolved register giữ mọi open slot.
- Một author gate mới trước việc đánh số chương/chapter brief.

### Acceptance criteria

1. Mỗi candidate row đầy đủ schema và truy được provenance.
2. Mỗi POV có opening pressure, irreversible choice và carried consequence nhưng không quota số chương.
3. Mọi World Spine inclusion có channel, subject agency và causal return.
4. Dependency graph thỏa toàn bộ CAI-01–12 và continuity-detail state ledger.
5. Không có exact date, travel duration, true custody, Huyền Nguyệt mechanism hoặc Ân Đồng weapon.
6. Không có Task 4/S28–S37 trong Volume I content rows.
7. Không file nào được tạo trong canonical story/chapter/brief paths.
8. Validator có negative tests cho meeting sớm, knowledge leak, hidden custody, named Lục rescuer, T4 contamination và fixed-count injection.
9. Tác giả có thể duyệt/reject từng candidate row hoặc movement mà không phải viết lại source ledger.

## 13. Kế hoạch triển khai đã được mở

1. Freeze và validate toàn bộ input authority.
2. Sinh movement-obligation ledger từ ba bible và continuity-detail contract.
3. Tạo chapter-function candidates chưa đánh số.
4. Braid theo dependency, không round-robin.
5. Gắn World Spine footprint và satellite candidates.
6. Chạy density pass để đề xuất dải số chương.
7. Chạy validator cùng adversarial review.
8. Trình Tác giả architecture draft; dừng trước chapter numbering/brief/prose.

## 14. Kết quả CAPQ-01–06 — APPROVED 2026-09-09

| ID | Quyết định đã duyệt | Hệ quả ràng buộc |
| --- | --- | --- |
| CAPQ-01 | Phê duyệt bộ sáu artifact và schema chapter-function row ở mục 6–7. | Phase có output reviewable, machine-checkable nhưng chưa phân chương chính thức. |
| CAPQ-02 | Phê duyệt **emergent count**: không đặt target chapter count trước; sau density pass mới báo minimum/recommended band/overflow. | Giữ low-burn và tính linh hoạt mà không biến “linh hoạt” thành kéo dài vô hạn. |
| CAPQ-03 | Phê duyệt năm movement basket M1–M5 và kiểu **irregular causal braid**, không round-robin ba POV. | Có macro rhythm để tổ chức candidate nhưng không khóa chapter sequence. |
| CAPQ-04 | Phê duyệt World Spine policy: ưu tiên document/relay/aftermath/living lore; satellite chỉ là candidate và phải qua sáu tiêu chí trước khi thành row. | Tận dụng source ngoài trio mà không mở tràn POV hoặc tạo filler. |
| CAPQ-05 | Phê duyệt cách áp dụng 3-1-1 như heuristic; “khoảng lặng” Quyển I là đơn tuyến/world aftermath, tuyệt đối không cho trio gặp sớm. | Giải quyết FC-010: giữ nhịp tham chiếu cấp series nhưng bỏ cách đọc như quota năm chương. |
| CAPQ-06 | Phê duyệt hai cổng: architecture draft được review trước; chỉ sau một phê duyệt riêng mới đánh số/tên chương và tạo chapter brief. | Phê duyệt phase này không bị hiểu nhầm là phê duyệt chapter plan hay prose. |

Phê duyệt CAPQ-01–06 chỉ mở quyền triển khai sáu artifact chapter-architecture **dạng candidate**. Tại thời điểm ghi quyết định này chưa có chapter row hoặc dải số chương nào được tạo. Nó không tự duyệt một chapter row tương lai, số chương, tên/số thứ tự chương, chapter brief, scene, prose, chronology tuyệt đối, route Quyển II–V hoặc canon promotion.
