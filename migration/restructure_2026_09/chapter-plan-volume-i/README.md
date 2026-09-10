# Chapter Plan Quyển I — sequence và bounded briefs

Trạng thái: `AUTHOR-APPROVED PLANNING / V1CBQ-01–06 / NOT CANON / NOT A SCENE PLAN / NOT PROSE`.

## Restate brief

V1CAQ-01–06 đã duyệt 25 function mặc định; V1CBQ-01–06 ngày 2026-09-09 tiếp tục duyệt baseline 25 chương, 25 tên làm việc, reading order/POV và 25 bounded briefs. Package này là planning authority nhưng không biến partial order thành lịch tuyệt đối.

## Assumptions đã dùng

- Baseline 25 chương, một function đã duyệt mỗi chương; đây là planning baseline trong dải recommended 25–28, không phải fixed count canon.
- V1-CAND-020 tiếp tục deferred và không có brief.
- Row HEAVY chưa tự split; chỉ mang cờ review nếu detail pass dự kiến vượt 5.500 từ.
- Số/tên chương là working planning authority. Exact date, travel, venue chưa có source và scene structure tiếp tục deferred.

## Output

- [chapter-sequence.tsv](chapter-sequence.tsv): nguồn máy đọc cho 25 số/tên/route.
- [chapter-sequence.md](chapter-sequence.md): projection đọc nhanh và nhịp POV.
- [provenance-ledger.tsv](provenance-ledger.tsv): source nodes, packet, query record và full-result references.
- `briefs/chapter_01.md` tới `briefs/chapter_25.md`: brief hữu hạn, không có scene list hoặc prose.
- [validation-report.md](validation-report.md): kết quả kiểm và biên bản phê duyệt V1CBQ-01–06.

## Scope và constraints

- In scope: approved planning number/title, one-POV routing, function, entry/exit state, knowledge, agency, causal edge, load guard và protected unknowns.
- Out of scope: exact chronology, exact travel, new venue, scene/beat/dialogue, prose, detailed combat, medical outcome, objective custody, Huyền Nguyệt mechanism, Tĩnh Xuyên–Ân Đồng route detail, Volume II–V và canon promotion.
- SQLite packet tiếp tục là authority cho game fact. Assignment, order và title là planning/Bridge, không phải game fact.

## Acceptance criteria

- Đúng 25 brief cho 25 function approved; không có V1-CAND-020.
- Mỗi brief chỉ có một POV và trỏ source packet/query/full-result reference.
- Sequence giữ mọi lane edge cùng các handoff bắt buộc.
- Không khóa ngày, hành trình, custody, mechanism hoặc scene wording.
- Tất cả artifact dừng ở planning authority sau V1CBQ. [Scene-plan phase spec](../scene-plan-phase-spec-volume-i.md) đã được duyệt qua SPQ-01–06 và mở candidate implementation; chưa scene nào được phê duyệt và prose vẫn đóng.
