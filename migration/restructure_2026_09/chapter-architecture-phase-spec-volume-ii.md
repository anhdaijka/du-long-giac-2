# Đề xuất Chapter Architecture Quyển II — source-first

Trạng thái: `AUTHOR-APPROVED FUNCTIONAL ARCHITECTURE / V2CAQ-01–05 / NOT A CHAPTER PLAN / NOT A SCENE PLAN / NOT PROSE / NOT CANON`.

## Restate brief

Quyển II phải biến áp lực công cộng quanh Du Long thành hợp tác hữu hạn đầu tiên của trio, rồi đi tới transition Phục Ngưu; nhưng Gemini không được tự biến task title, avatar gameplay, report NPC hay macro wording thành fact/cảnh/chronology.

Đầu vào đủ điều kiện là [source-window map](writer-preflight-volume-ii/volume-ii-source-window-map.md) và [coverage ledger](writer-preflight-volume-ii/volume-ii-source-window-coverage-ledger.md). SQLite result containers của `arc_04.json`, `arc_05.json`, `arc_07.json` tiếp tục là authority; Narrative Book không thay thế chúng.

## Kết luận density trung thực

Khảo sát hiện chỉ có ba source window `CHAPTER-READY`: `V2-SW-04`, `V2-SW-05`, `V2-SW-09`. Vì vậy proposal này **không** đặt số chapter, không giả định 25 chương, không cân quota ba POV, và không tạo `V2-CH-*`.

Một architecture đầy đủ chỉ được sinh khi Tác giả chọn Bridge/khảo sát bổ sung cho ba gap đã thấy: mapping POV trong task avatar, lane y-chứng Hạ Nương, và điều kiện first physical convergence. Đây là fail-closed có chủ ý, không phải thiếu sót để Gemini bù bằng văn phong.

## Candidate functional spine

| Candidate | Function, không phải chapter | Evidence envelope | POV / channel | State được phép | Hard stop |
| --- | --- | --- | --- | --- | --- |
| `V2-CAND-001` | Đặt tin Du Long thành áp lực lên một cộng đồng và mở hai report có thể liên quan nhưng chưa được nhập làm một. | `V2-SW-04`: T146/S295; `V2-SW-05`: T150/S299. | `POV UNASSIGNED`; organization report/aftermath. | Có hai report + task-local action scope; không có combined-network truth. | Không gán avatar cho Tiêu; không xác nhận Diêm Bang/Từ Bân Kiếm motive, phe thống nhất, venue/date hay combat outcome. |
| `V2-CAND-002` | Cho độc giả thấy giá xã hội của information/quyền lực mà không biến World Spine thành side-quest checklist. | `V2-SW-02` T93/S242; `V2-SW-03` T96/100/103/106/110. | `WORLD SPINE`; document/witness/aftermath, không satellite mặc định. | Các report/vignette độc lập giữ scope riêng. | Không ghép thành chính biến, historical fact hoặc chronology; không gán Hạ làm người biết/giải tất cả. |
| `V2-CAND-003` | Gieo một layer living lore về ký ức võ lâm để đối trọng tin đồn đương thời, nhưng không dựng “Legendary Shadow”. | `V2-SW-06`: T197/S360, T202/S365. | `LIVING LORE`; người kể/tư liệu. | Người kể có thể kể/nhớ/“nghe nói”. | Không xác nhận Độc Cô Kiếm, trận Thái Thạch, cái chết, di vật, võ công hay genealogy như objective/historical truth. |
| `V2-CAND-004` | **First physical convergence gate**: xác định pressure tối thiểu khiến ba POV gặp/hợp tác hữu hạn mà không thành party cố định. | Không có direct source window nào chỉ ra ai gặp ai, ở đâu, khi nào hay làm gì. Chỉ có macro planning R-67/CMQ-01. | Ba POV chỉ ở cấp macro; `BRIDGE REQUIRED`. | Cần một decision ID của Tác giả mới có entry/exit/knowledge boundary. | Gemini không được tạo meeting scene, sender, venue, dialogue, custody reveal hay kết quả hợp tác. |
| `V2-CAND-005` | Đóng Quyển II bằng việc thế giới/tổ chức chuyển từ tranh bảo sang chuẩn bị Phục Ngưu, không biến resource loop thành “hero quest”. | `V2-SW-09`: T225/S400. | `POV UNASSIGNED`; organization action/document/aftermath. | Source game narrative đặt hậu Thái Tổ Bảo Khố → preparation transition. | Không nâng lời Bạch Thu Lâm thành lịch sử khách quan; không gán command/authority/secret truth, exact path, teleport, resource count, dungeon/combat hoặc trio participation. |

## Gaps bắt buộc phải chọn trước chapter map

| ID | Gap | Vì sao chưa tự giải | Đề xuất an toàn |
| --- | --- | --- | --- |
| `V2CAQ-01` | Cách ánh xạ `V2-SW-04/05/09` từ avatar source sang POV/organization novel. | R-70 cấm suy avatar = Tiêu ở task mới; macro role không là proposition-level Bridge. | Tác giả chọn: (a) chỉ dùng organization/doc/aftermath, hoặc (b) cho phép Bridge mapping theo từng window, có decision ID. |
| `V2CAQ-02` | Lane Hạ Nương/y-chứng của Quyển II. | `V2-SW-02/03` là report/world material, chưa phải y-chứng của Hạ hay direct POV route. | Giữ Hạ ở `UNASSIGNED` cho tới deep survey mới, hoặc Tác giả chỉ định một source family để khảo sát; không bịa ca bệnh/chứng cứ. |
| `V2CAQ-03` | First physical convergence. | Không source row nào cho cụ thể encounter; macro chỉ duyệt chức năng. | Tác giả chỉ duyệt **level of bridge** (không scene): pressure chung, knowledge ceiling, non-party exit. Details tiếp tục để candidate scene-plan gate. |
| `V2CAQ-04` | Density. | Ba window chapter-ready không chứng minh count hay interleave đủ một quyển. | Giữ `COUNT = UNRESOLVED`; chỉ 5 functional candidates, trong đó 001–003/005 là source-constrained và 004 đang bridge-gated. |
| `V2CAQ-05` | Expansion source. | `V2-SW-10/11` chưa deep-read, `V2-SW-01/03/06/08` không mặc định thành plot. | Mở đúng một deep survey khi architecture chứng minh causal need; không “đào cho đủ chương”. |

## Invariants

- `DU_LONG_OBJECTIVE_CUSTODY = UNRESOLVED`; `HUYEN_NGUYET_MECHANISM = DEFERRED`.
- `READER_KNOWLEDGE != CHARACTER_KNOWLEDGE`; report/document/rumor không tự thành truth hoặc handoff cho trio.
- Gặp vật lý đầu tiên, nếu được duyệt, chỉ là hợp tác hữu hạn: không tiểu đội cố định, không shared omniscience, không một POV chiếm tuyến của người khác.
- Game alt-history, NPC testimony và memory/legendary lore không tự thành `HISTORICAL FACT`.
- Không sử dụng `V2-SW-07`, `V2-SW-10`, `V2-SW-11` cho architecture hiện hành.
- Future canon Tĩnh Xuyên/Mộc Nhất Lâu–Ân Đồng không được diễn, làm nhẹ hay chọn implementation tại đây.

## Approval gate

Phê duyệt `V2CAQ-01`–`05` chỉ có thể nâng functional spine thành `AUTHOR-APPROVED PLANNING` và cho phép **đề xuất** chapter numbering/title/briefs. Nó không tạo chapter, không mở scene/prose/canon, và không phê duyệt bất kỳ Bridge cụ thể nào ngoài phạm vi Tác giả đã chọn.

## Quyết định Tác giả — V2CAQ-01–05

Ngày 2026-09-10, Tác giả duyệt toàn bộ proposal. Áp dụng cách đọc fail-closed sau:

1. `V2CAQ-01`: chọn organization/document/aftermath cho `V2-SW-04/05/09`; chưa Bridge-map avatar sang Tiêu Phùng hay POV khác.
2. `V2CAQ-02`: Hạ Nương tiếp tục `UNASSIGNED` cho tới khi một deep survey tìm được evidence phù hợp; không bịa ca bệnh/y-chứng để cân POV.
3. `V2CAQ-03`: duyệt first physical convergence ở **cấp chức năng Bridge**: pressure chung, knowledge ceiling, non-party exit. Venue, actor trigger, dialogue, duration, action và outcome cụ thể vẫn đóng.
4. `V2CAQ-04`: `COUNT = UNRESOLVED`; năm function candidate không phải năm chương và không phải density target.
5. `V2CAQ-05`: chỉ mở deep survey khi có causal need. Gap lane Hạ Nương và density hiện là nhu cầu hợp lệ; source family cụ thể phải được khảo sát/provenance trước khi vào chapter proposal.

Bước kế tiếp được phép là một deep survey hữu hạn nhằm tìm evidence cho lane Hạ/density, sau đó mới đề xuất chapter numbering/title/brief. Không được nhảy thẳng từ năm function sang `V2-CH-*`.
