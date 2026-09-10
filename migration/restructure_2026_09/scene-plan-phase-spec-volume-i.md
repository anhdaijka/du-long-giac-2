# Spec đã duyệt — Phase Scene Plan Quyển I

Trạng thái: `AUTHOR-APPROVED PHASE SPEC / SPQ-01–06 / NOT A SCENE PLAN / NOT CANON / NOT PROSE`.

Lifecycle hiện hành: `APPROVED REFERENCE / SCENE_PLAN_IMPLEMENTATION_FROZEN_POST_MACRO_CONSOLIDATION / D-034-R-65-R-68`.

Tài liệu này chỉ định nghĩa cách dựng và kiểm tra **candidate scene plan** từ 25 chapter brief đã được duyệt. Tác giả đã phê duyệt toàn bộ SPQ-01–06 ngày 2026-09-09, mở quyền triển khai đúng package ở mục 7. D-034/R-65 sau đó đóng băng việc thực thi quyền này để ưu tiên macro 13 Arc → 5 quyển; R-66–R-68 đã hoàn tất macro design nhưng không gỡ đóng băng. Bản spec không phân scene, không đặt scene ID thật, không viết beat, thoại, choreography, ending image hoặc văn xuôi; candidate package tương lai vẫn phải quay lại cổng V1SPAQ trước bất kỳ prose phase nào.

## 1. Restate Brief

V1CBQ-01–06 đã biến baseline 25 chương, 25 tên làm việc, reading order bất quy tắc và 25 bounded brief thành planning authority. Phase kế tiếp cần hạ độ phân giải từ **chapter function** xuống **scene function** nhưng phải giữ nguyên:

- một POV duy nhất trong từng chương và deep third-person limited;
- thứ tự tương đối, state transition và knowledge boundary đã duyệt;
- living wulin: NPC/tổ chức hành động vì mục tiêu riêng, không biến thành đạo cụ cho trio;
- game fact, historical fact và Novelization Bridge là ba lớp khác nhau;
- mọi exact date, travel duration, custody Du Long, cơ chế Huyền Nguyệt và hung khí Ân Đồng vẫn để mở;
- canon Tĩnh Xuyên–Ân Đồng tuyệt đối bất khả thay thế, nhưng Task 4/S28–S37 không được diễn trước trong Quyển I.

## 2. Kết quả SPQ-01–06 — APPROVED 2026-09-09

| ID | Đề xuất khuyến nghị | Hệ quả nếu duyệt |
| --- | --- | --- |
| SPQ-01 | Duyệt bảy nhóm artifact ở mục 7 và schema scene-row ở mục 8. | Có package reviewable/machine-checkable mà chưa viết prose. |
| SPQ-02 | Dùng **2–4 scene/chương như heuristic**, cho phép 1 hoặc 5 khi chức năng chứng minh được; không quota. Tổng estimate trên 5.500 từ hoặc hai irreversible turn độc lập bắt buộc trình split proposal, không tự tách. | Giữ low-burn nhưng không nghiền mọi chương thành cùng một nhịp máy móc. |
| SPQ-03 | Scene chỉ được dùng địa điểm/thời gian có nguồn hoặc nhãn `PROPOSED LOCATION/TIME BRIDGE`; exact calendar date, travel duration và route vẫn deferred. | Cho phép hình dung không gian để review mà không giả chronology. |
| SPQ-04 | Giữ POV của 25 chương đúng V1CBQ; không chèn satellite POV/interlude. Nếu một event-family thật sự cần camera ngoài trio, phải trình amendment ở cấp chapter architecture trước. | Bảo toàn one-POV chapter và ngăn mở tràn POV trong detail pass. |
| SPQ-05 | Bridge bền vững phải có decision ID đã duyệt; Bridge mới chỉ được ghi `BRIDGE-CANDIDATE / AUTHOR APPROVAL REQUIRED` và không được dùng làm exit-state bắt buộc. Wording, gesture và vi động tác không tạo durable fact để dành cho prose discretion sau này. | Phân biệt rõ thiết kế nhân quả với quyền thi hành văn chương. |
| SPQ-06 | Sau khi spec được duyệt, chỉ mở việc dựng **candidate scene plan**. Candidate plan phải qua cổng `V1SPAQ` riêng; nếu được duyệt, bước sau chỉ được đề xuất prose-phase spec, chưa tự viết chương. | Giữ hai cổng độc lập giữa spec → scene plan → prose. |

## 3. Assumptions an toàn

1. [Chapter Plan Quyển I](chapter-plan-volume-i/README.md), sequence, provenance ledger và 25 brief là planning authority theo R-53–R-58 / D-032.
2. `chapter_key`, `source_function_id`, working title, primary POV và reading order không đổi trong phase scene-plan. Mọi đổi các trường này là amendment V1CBQ, không phải chỉnh scene cục bộ.
3. Creative Constitution áp dụng deep third-person limited, word band 3.500–5.200 và split review trên 5.500 từ; 3-1-1 chỉ là heuristic cấp series.
4. Scene plan được phép mô tả **chức năng**, xung đột, state turn, tri thức và causal return; không được viết câu thoại mẫu, đoạn văn mẫu hoặc choreography chi tiết.
5. Không có `story.md` hiện hành trong checkout này; phase không canonize hoặc sửa Story Skills state. Canon promotion vẫn là lifecycle riêng sau prose/review và approval.
6. Archive/rejected chỉ phục vụ audit lịch sử, không là nguồn cảm hứng hoặc bằng chứng cho scene.

## 4. Approval boundary đã duyệt

Checkpoint D25 đã dừng tại SPQ-01–06 và không tạo output. SPQ mở `CANDIDATE SCENE PLAN IMPLEMENTATION AUTHORIZED`, nhưng quyền này hiện **suspended** bởi `SCENE_PLAN_IMPLEMENTATION_FROZEN_POST_MACRO_CONSOLIDATION / D-034-R-65-R-68`, với các giới hạn:

- không tạo package `scene-plan-volume-i/` trước macro review;
- khi suspension được Tác giả gỡ, scene row và scene map chỉ là candidate planning; không tạo dialogue sketch hoặc prose sample;
- không đổi số/tên/POV/thứ tự của 25 chương;
- không giải bất kỳ protected unknown nào;
- không coi việc duyệt spec là duyệt toàn bộ candidate package tương lai.

Phê duyệt spec chỉ mở candidate scene-plan implementation. Nó không tự phê duyệt bất kỳ scene nào, không mở prose-phase spec và không mở prose.

## 5. Goal

Tạo một candidate scene plan đủ chi tiết để Tác giả đánh giá causal execution, POV integrity, knowledge flow, living-wulin agency và dung lượng từng chương trước prose, trong khi mọi claim bền vững vẫn truy được về source hoặc quyết định Bridge.

Candidate plan phải trả lời được cho từng scene tương lai:

1. Scene này thay đổi state hay áp lực gì?
2. POV nhìn, biết và hiểu sai điều gì trước/sau scene?
3. Ai ngoài POV hành động, muốn gì và trả giá gì?
4. Proposition nào là game fact, historical fact hoặc Bridge?
5. Scene trả causal consequence về đâu; nếu bỏ scene thì mất gì?
6. Dung lượng dự kiến có làm chương vượt load gate hoặc chứa hai irreversible turn không?

## 6. Scope

### In scope sau khi SPQ được duyệt

- Phân candidate scene theo 25 chương đã duyệt, không đổi chapter routing.
- Ghi scene function, state in/out, knowledge in/out, conflict/pressure turn và causal return.
- Gắn source nodes, packet/query/full-result locator và decision IDs ở cấp scene.
- Ghi onstage cast, offstage agency và medium truyền tin.
- Đề xuất location/time bridge có nhãn rõ, không biến thành fact.
- Ước lượng dung lượng scene/chapter và trình split/merge proposal khi chạm gate.
- Lập register cho protected unknown, departure request và Bridge candidate mới.
- Chạy adversarial review và trình Tác giả duyệt candidate scene plan.

### Out of scope

- Viết prose, thoại mẫu, độc thoại nội tâm mẫu, mô tả võ công/y thuật hoặc action blocking chi tiết.
- Chọn exact date, giờ, travel duration, tuyến đường hoặc đồng bộ tuyệt đối các lane.
- Thêm satellite POV, interlude toàn tri hoặc đổi primary POV đã duyệt.
- Chốt custody thật của Du Long Giác, cơ chế Huyền Nguyệt hoặc kết quả open slot.
- Thiết kế người/cách cứu Lục trong Quyển I.
- Đưa Task 4/S28–S37, Ân Đồng hoặc rehearsal thay thế vào content Quyển I.
- Tạo Legendary Shadow profile, route Quyển II–V hoặc canon promotion.
- Sửa manuscript, `chapters/`, canonical plot/character/world state.

## 7. Hình dạng artifact được đề xuất

Theo SPQ-01–06 đã duyệt, phase implementation chỉ được tạo các nhóm artifact sau dưới `migration/restructure_2026_09/scene-plan-volume-i/`:

1. `README.md`
   - authority order, trạng thái, cách review, gate và giới hạn.
2. `scene-ledger.tsv`
   - nguồn máy đọc; một row cho mỗi candidate scene.
3. `scene-ledger.md`
   - projection đọc nhanh; không thêm fact ngoài TSV.
4. `provenance-ledger.tsv`
   - proposition-level source/query/result và decision/bridge mapping.
5. `chapter-maps/chapter_01.md` tới `chapter_25.md`
   - projection scene-function theo từng chapter; không có prose hoặc dialogue wording.
6. `open-slots-and-departures.md`
   - protected unknown, Bridge candidate, amendment request và split proposal.
7. `validation-report.md`
   - kiểm cấu trúc, density, provenance, knowledge, continuity và cổng `V1SPAQ`.

Không tạo file trong `chapters/`, `briefs/`, `plot/` hoặc story-state canonical paths. `chapter-maps/` là planning artifact trong migration, không phải manuscript.

## 8. Schema candidate scene-row

| Field | Bắt buộc | Contract |
| --- | --- | --- |
| `scene_candidate_id` | Có | Pattern `V1-CH-NNN-SNN`; ID chỉ sinh sau SPQ approval, không phải canon. |
| `chapter_key` | Có | Một trong 25 key V1CBQ; không đổi chapter number/title/function. |
| `scene_ordinal` | Có | Thứ tự đọc trong chapter; không phải timestamp. |
| `primary_pov` | Có | Phải bằng primary POV của chapter; không có secondary/interior POV. |
| `scene_function` | Có | Một câu nêu pressure/state change, không phải synopsis văn xuôi. |
| `entry_state` / `exit_state` | Có | State trước/sau; exit không được dựa vào Bridge chưa duyệt. |
| `knowledge_in` / `knowledge_out` | Có | Chỉ điều POV có kênh biết hợp lệ; ghi cả hiểu sai nếu có. |
| `reader_delta` | Có | Điều độc giả biết thêm; không tự chuyển thành character knowledge. |
| `source_nodes` | Có | Task/subtask/step/dialogue locator; `NONE` chỉ khi scene thuần Bridge đã duyệt. |
| `packet_refs` / `result_refs` | Có khi có game fact | Trỏ packet, query/bind và full result đã lưu. |
| `evidence_classes` | Có | Tách `GAME FACT`, `HISTORICAL FACT`, `AUTHOR-APPROVED NOVELIZATION BRIDGE`, `BRIDGE-CANDIDATE` và `PROTECTED UNKNOWN`. |
| `decision_refs` | Có khi dùng Bridge | R/PB/BFCQ/CDQ/CAPQ/V1CAQ/V1CBQ; không dùng tên file thay decision ID. |
| `onstage_cast` | Có | Nhân vật hiện diện; không mặc định toàn bộ NPC biết cùng thông tin. |
| `offstage_agency` | Có | Actor/tổ chức ngoài POV đang hành động và cái giá của họ; `NONE` phải có lý do. |
| `location_basis` | Có | `SOURCE-VERIFIED`, `APPROVED BRIDGE` hoặc `PROPOSED LOCATION BRIDGE`. |
| `relative_time_anchor` | Có | Quan hệ trước/sau với scene/chapter khác; không exact date/duration. |
| `conflict_turn` | Có | Thay đổi pressure, lựa chọn hoặc nhận thức; không viết choreography. |
| `irreversible_turn` | Có | `YES/NO`; nếu `YES`, chỉ rõ state nào không thể hoàn tác. |
| `causal_predecessors` / `causal_returns` | Có | Cạnh vào/payoff; không tạo orphan scene. |
| `coverage_channel` | Có | Kế thừa/thu hẹp từ chapter: direct trio, document, witness, aftermath hoặc living lore. |
| `estimated_words` | Có | Estimate planning để cộng load; không phải quota prose. |
| `protected_unknowns` | Có | Các điều scene tuyệt đối không được quyết định. |
| `status` | Có | `CANDIDATE / V1SPAQ AUTHOR REVIEW REQUIRED`, `BRIDGE-CANDIDATE`, `SPLIT-PROPOSAL` hoặc `DEFERRED_WITH_REASON`. |

Không có field cho prose text, sample dialogue, exact date, true custody, hidden narrator truth, stunt choreography hoặc final wording.

## 9. Invariant của phase

| ID | Ràng buộc | Điều validator/reviewer phải bắt |
| --- | --- | --- |
| SPI-01 | `PHYSICAL_CONVERGENCE_VOLUME_I = NONE`. | Không scene nào chứa trực tiếp hơn một protagonist hoặc cho trio nhận ra nhau. |
| SPI-02 | Một POV/chương và một interior POV/scene. | Mọi scene POV phải bằng chapter POV; không head-hopping, omniscient interlude hoặc satellite insertion. |
| SPI-03 | `READER_KNOWLEDGE != CHARACTER_KNOWLEDGE`. | Mọi knowledge delta phải có witness/document/relay/observation hợp lệ. |
| SPI-04 | Game fact, historical fact và Bridge không được trộn nhãn. | Mỗi proposition bền vững có evidence class cùng provenance/decision tương ứng. |
| SPI-05 | Bridge mới là default-deny. | `BRIDGE-CANDIDATE` không được dùng làm required exit state, predecessor hoặc narrator truth trước author approval. |
| SPI-06 | Partial order là chronology duy nhất. | Không exact date, giờ, duration hoặc travel route chưa audit. |
| SPI-07 | `DU_LONG_OBJECTIVE_CUSTODY = UNRESOLVED`. | Không scene note, offstage truth hoặc dramatic irony ngầm chọn holder/location. |
| SPI-08 | `HUYEN_NGUYET_MECHANISM = DEFERRED`. | Chỉ được dựng tác động quan sát/niềm tin nhân vật có nguồn; không giải cơ chế. |
| SPI-09 | Lục được cứu bởi hành động tổ chức ngoài màn, không nêu rescuer; Lục đấu Thôi. | Không scene cứu Lục, không hero mới, không trao công/truyền võ cho Tiêu Phùng. |
| SPI-10 | Hạ Nương cứu/chuyển chữa, không giữ/giao/xác nhận ngọc. | Không dùng y thuật làm quyền kể toàn tri; không miracle cure. |
| SPI-11 | Cầu Chỉ Thủy giữ relay chính trị V1-CAND-026. | Không lặp tin qua La Phong, tạo sứ giả mới hoặc biến thông cáo thành custody fact. |
| SPI-12 | Tĩnh Xuyên–Ân Đồng là protected future canon bất khả thay thế. | Không Task 4/S28–S37, Ân Đồng, nạn nhân rehearsal, hung khí hoặc giảm trách nhiệm trong Quyển I. |
| SPI-13 | NPC/tổ chức giữ agency và causal return. | Không scene chỉ để NPC khen, giải thích, cứu hoặc trao vật cho protagonist. |
| SPI-14 | Scene density phát sinh từ function, không quota. | 2–4 chỉ là heuristic; estimate chapter vượt 5.500 từ hoặc hai irreversible turn phải thành split proposal. |
| SPI-15 | Candidate scene plan không phải prose authority. | Không thoại mẫu, paragraph sample, choreography, ending image hoặc file manuscript; sau implementation vẫn dừng tại V1SPAQ. |

## 10. Quy trình implementation đề xuất

### Pass A — freeze inputs

- Đọc sequence TSV và đủ 25 brief; xác nhận status V1CBQ approved.
- Chạy lại các validator route/bridge/continuity/architecture/chapter brief.
- Ghi SHA SQLite và dùng packet/query/result hiện hành; không đọc archive/rejected như authority.

### Pass B — proposition slicing

- Tách chapter function thành các proposition/state obligations, chưa thành scene.
- Với từng obligation, ghi evidence class, source locator hoặc decision ID.
- Nếu cần fact mới để nối, đưa vào departure register; không dựng scene quanh giả định ấy.

### Pass C — candidate scene functions

- Nhóm obligations theo một pressure turn và một interior POV liên tục.
- Scene có thể chứa nhiều source row nếu cùng causal function; không một source row = một scene máy móc.
- Chỉ mô tả scene function/state/knowledge/conflict, không mô tả lời văn hoặc từng động tác.

### Pass D — living-wulin and knowledge pass

- Với mỗi scene, xác định actor ngoài POV, mục tiêu, nguồn lực và cái giá.
- Sự kiện ngoài trio đi qua document, witness, aftermath hoặc living lore đã được chapter routing cho phép.
- Không dựng satellite camera để “kể cho đủ”; nếu reader cần trực tiếp thấy event mà current POV không thể tiếp cận, ghi amendment request.

### Pass E — time/location pass

- Chỉ dùng partial order và location basis có nhãn.
- `PROPOSED LOCATION/TIME BRIDGE` phải nằm trong departure register; không được biến thành historical/game fact.
- Không suy thời gian di chuyển từ nhịp chapter hoặc khoảng cách tưởng tượng.

### Pass F — density and split review

- Cộng `estimated_words` theo chapter và đối chiếu word band đã duyệt.
- 2–4 scene/chương là heuristic review, không phải quota; 1 hoặc 5 phải có lý do function/continuity.
- Trên 5.200 từ là caution; trên 5.500 từ hoặc hai irreversible turn độc lập là mandatory split proposal.
- Split proposal không tự đổi chapter key/number/title. Nó ghi phương án và chờ amendment approval.

### Pass G — adversarial review

- Kiểm head-hopping, knowledge leak, protagonist gravity, unsupported Bridge, orphan scene, repeated briefing, gameplay literalism, chronology invention và future-canon contamination.
- Kiểm tổng scene estimate không được dùng để lấp dung lượng bằng filler.
- Kiểm mỗi document/witness/aftermath có sender, recipient, medium và giới hạn tri thức.

### Pass H — V1SPAQ author gate

- Trình scene ledger, 25 chapter map, provenance ledger, departure/split register và validation report.
- Cho phép Tác giả duyệt/sửa/reject theo chapter hoặc scene candidate.
- Không tạo prose-phase spec hay prose trong cùng lượt implementation.

## 11. Density và chapter-integrity contract

| Tín hiệu | Xử lý |
| --- | --- |
| 2–4 scene, một irreversible turn, tổng estimate trong working band | Bình thường; vẫn review chất lượng nhịp. |
| 1 scene | Chỉ hợp lệ nếu là một continuous pressure/action unit và đủ entry/turn/exit; không kéo dài để đủ từ. |
| 5 scene | Chỉ hợp lệ khi các scene ngắn có medium/location/knowledge function khác nhau và không thể merge an toàn. |
| Tổng estimate 5.201–5.500 | `CAUTION`; giảm lặp, kiểm merge hoặc chuyển aftermath trước khi xin split. |
| Tổng estimate trên 5.500 | `SPLIT-PROPOSAL REQUIRED`; không tự sửa baseline 25 chương. |
| Hai irreversible turn độc lập | `SPLIT-PROPOSAL REQUIRED` dù tổng từ chưa vượt 5.500. |
| Scene không đổi state/knowledge/pressure và không có causal return | Loại hoặc gộp; không giữ làm phong cảnh/filler. |

Scene plan không đặt hard minimum cho từng scene. Dung lượng chỉ là capacity forecast, không phải chỉ tiêu để người viết nhồi chữ.

## 12. Provenance và departure contract

### Durable claim

Mỗi durable claim trong candidate scene plan phải ghi một trong ba đường:

1. `GAME FACT` → source node + packet + query/bind + full-result locator.
2. `HISTORICAL FACT` → nguồn lịch sử được lưu/cited trong evidence ledger; chưa có nguồn thì ghi research departure.
3. `AUTHOR-APPROVED NOVELIZATION BRIDGE` → decision ID và phạm vi quyết định.

Không được dùng planning artifact làm bằng chứng gốc cho game fact; brief chỉ định tuyến, packet mới lưu evidence.

### Non-durable prose discretion

Wording, gesture, cảm giác tức thời, micro-action và nhịp câu có thể để nhãn `PROSE DISCRETION — NOT YET EXERCISED` nếu chúng không tạo:

- quan hệ hoặc lời hứa bền vững;
- kiến thức mới;
- thương tích/vật sở hữu/vị trí bền vững;
- luật thế giới, kỹ thuật võ/y hoặc historical assertion;
- causal outcome làm chapter sau phụ thuộc.

Spec và candidate scene plan không viết những vi chi tiết này trước.

### Departure register

Mọi đề xuất vượt authority phải ghi: `departure_id`, scene/chapter bị ảnh hưởng, proposition cần thêm, evidence thiếu, loại quyết định cần Tác giả chốt, downstream impact và phương án giữ mở. Không được “tạm chọn” rồi viết quanh lựa chọn.

## 13. Fresh-review checklist

- Đủ đúng 25 chapter map; không tự thêm chapter 26–28.
- Mọi scene POV khớp chapter POV đã duyệt.
- Không có satellite/interlude/toàn tri.
- Mỗi durable game fact có packet/query/result; mỗi Bridge có decision ID hoặc candidate gate.
- Không exact date/travel duration/route chưa audit.
- Không hidden custody hoặc giải Huyền Nguyệt.
- Không scene cứu Lục; Lục giữ trận Thôi; Tiêu không nhận công/truyền võ.
- Cầu Chỉ Thủy giữ relay chính trị cuối Quyển I; knowledge boundary không bị xuyên.
- Hạ Nương không xác nhận artifact truth hoặc chữa lành kỳ tích.
- Không Task 4/S28–S37, Ân Đồng/rehearsal/hung khí trong Quyển I.
- Mỗi world-facing scene có agency và causal return.
- Không dialogue wording, prose paragraph, choreography hoặc ending image.
- Mọi chapter vượt density gate chỉ có split proposal, chưa đổi baseline.
- Package dừng tại `V1SPAQ AUTHOR REVIEW REQUIRED`.

## 14. Expected output và acceptance criteria

### Expected output sau khi spec được duyệt

- Bảy nhóm artifact ở mục 7.
- Một machine-readable scene ledger có scene count phát sinh từ function.
- 25 chapter maps giữ nguyên sequence/POV/function đã duyệt.
- Một provenance ledger cấp proposition.
- Một register minh bạch cho Bridge mới, location/time proposal, split và departure.
- Một validation report cùng cổng V1SPAQ trước prose.

### Acceptance criteria

1. Đúng 25 chapter key và không có chapter mới nếu chưa có amendment approval.
2. Mọi scene row đầy đủ schema, một POV, state/knowledge delta và causal return.
3. Mọi durable claim truy được source/query/result hoặc decision ID; lớp fact không bị trộn.
4. `PHYSICAL_CONVERGENCE_VOLUME_I = NONE`, custody unresolved, Huyền Nguyệt deferred và protected Tĩnh Xuyên–Ân Đồng còn nguyên.
5. Không scene cứu Lục, không satellite insertion, không protagonist chiếm agency của tổ chức.
6. Không exact chronology, prose, dialogue wording, choreography hoặc canon promotion.
7. Density report dùng 2–4 như heuristic và phát hiện đúng split gate trên 5.500 từ/hai irreversible turn.
8. Validator có negative tests cho POV drift, knowledge leak, early meeting, custody, Task 4 contamination, unsupported Bridge, prose injection và split-gate bypass.
9. Tác giả có thể duyệt/reject từng scene hoặc chapter map mà không sửa source ledger.
10. Candidate package vẫn mang trạng thái `AUTHOR REVIEW REQUIRED`; không tự mở prose.

## 15. Implementation plan đã được mở

1. Freeze 25 chapter brief và toàn bộ authority/provenance.
2. Tách proposition/state obligations từng chapter.
3. Dựng candidate scene functions và machine ledger.
4. Chiếu ledger thành 25 chapter map, không thêm prose.
5. Chạy knowledge/living-wulin/time-location pass.
6. Chạy density, split và departure review.
7. Chạy validator cùng adversarial review.
8. Trình `V1SPAQ` cho Tác giả; dừng trước prose-phase spec và prose.

## 16. Author decision record — SPQ-01–06

Tác giả đã phê duyệt toàn bộ SPQ-01–06 bằng chỉ thị “Duyệt toàn bộ SPQ-01–06 theo đề xuất.” Quyết định được lưu tại R-59–R-64 / D-033. Các policy có thể được sửa sau bằng quyết định mới mà không làm thay đổi các phê duyệt V1CBQ trước đó.

Quyền implementation chỉ là tạo candidate scene-plan package theo schema này. Không scene nào trở thành canon hoặc prose authority; mọi departure, split, Bridge mới và toàn bộ candidate plan vẫn phải qua V1SPAQ.
