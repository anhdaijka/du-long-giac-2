# Validation report — Chapter Architecture Quyển I

Trạng thái: `V1CAQ-01–06 APPROVED / STRUCTURAL VALIDATION / NOT SEMANTIC CERTIFICATION / NOT CANON`.

## 1. Phạm vi kiểm

- Sáu artifact đúng danh sách CAPQ-01.
- Header/schema, ID, POV, movement, load, channel và status của matrix.
- Ownership của mọi locator task/subtask/step/dialogue đối với packet SQLite đã lưu.
- Event-family tồn tại trong World Coverage ledger.
- Dependency ID, projection và braid không bỏ candidate.
- Hàng rào không gặp trio, custody mở, Huyền Nguyệt deferred, Task 4/Ân Đồng ngoài content Quyển I.
- Negative tests cho source sai và các phép lấp khoảng mở bị cấm.

Kiểm tra không chứng minh chất lượng văn học, logic lịch sử/địa lý, tính tối ưu của nhịp, độ đúng của Bridge mới hoặc quyền phê duyệt Tác giả.

## 2. Kết quả tự động

`python scripts/check_chapter_architecture.py --self-test`: **PASS**.

- 26 retained rows: 25 approved default functions + 1 deferred satellite record.
- POV inventory: Tĩnh Xuyên 8, Tiêu Phùng 11, Hạ Nương 6, satellite deferred 1.
- Movement inventory: M1 4, M2 12, M3 4, M4 4, M5 2.
- 105 source locators được kiểm task/subtask/step/dialogue ownership qua full-result packets.
- 17 local file links hợp lệ sau khi nối sang Chapter Plan Quyển I.
- 12 negative tests bị từ chối đúng: task không tồn tại, step sai owner, Task 4 contamination, cuộc gặp sớm, fixed count, named Lục rescuer, custody holder, satellite thiếu LWCQ-02, projection thiếu row, tái đưa satellite vào mặc định, bỏ CDK-02 predecessor và bỏ approval Cầu relay.
- Assurance: `STRUCTURE_LOCATORS_DEPENDENCIES_AND_BOUNDARIES_ONLY_NOT_SEMANTIC`.

## 3. Adversarial review theo CAI-01–12

| Invariant | Kết quả | Bằng chứng/giới hạn |
| --- | --- | --- |
| CAI-01 — không hội tụ thể chất | PASS cấu trúc | Mỗi row có một primary POV; `018 → 021` bắt buộc Tĩnh Xuyên rời trước Tiêu. Không có scene/prose để kiểm blocking. |
| CAI-02 — một POV hạn tri | PASS cấu trúc | `primary_pov` là enum đơn; knowledge in/out bắt buộc. V1-CAND-020 đã được defer khỏi architecture mặc định theo V1CAQ-02. |
| CAI-03 — provenance | PASS locator | Mọi row có source locator và decision anchor; query/full result nằm trong packet. Semantic paraphrase vẫn cần human review. |
| CAI-04 — partial order | PASS cấu trúc | Braid ghi cạnh bắt buộc và cạnh candidate; không có ngày, độ trễ hoặc travel duration. |
| CAI-05 — Lục | PASS boundary | CDK-02 giữ cứu ngoài màn/không tên; Lục tự đấu Thôi; Tiêu không nhận chiến công. Satellite option không được kể người/cách cứu. |
| CAI-06 — relay | PASS approved planning | V1CAQ-03 chọn Cầu Chỉ Thủy cho function chính trị của V1-CAND-026; nếu đổi thành field task phải áp lại CDQ-02 với La Phong. |
| CAI-07 — custody | PASS boundary | `DU_LONG_OBJECTIVE_CUSTODY = UNRESOLVED` trong README/rows/World Spine; không holder/location cụ thể. |
| CAI-08 — Huyền Nguyệt | PASS boundary | V1-CAND-011 giữ tên/biến cố phòng thủ; `HUYEN_NGUYET_MECHANISM = DEFERRED`. |
| CAI-09 — Tĩnh Xuyên–Ân Đồng | PASS exclusion | T4/S28–S37 chỉ ở World Spine như future-invariant audit input; không có T4 locator trong matrix. Chủ thể/kết cục/trách nhiệm canon không đổi; hung khí vẫn mở. |
| CAI-10 — NPC/tổ chức agency | PASS structure | Mọi row có `npc_agency`; World Spine giữ lãnh đạo, kỹ nghệ, cứu hộ, chiến đấu, relay và tái thiết ngoài trio. |
| CAI-11 — emergent count | PASS method | Dải 23–24 minimum và 25–28 recommended phát sinh từ 25 function mặc định + split/merge review; không có fixed target hoặc quota 3-1-1. |
| CAI-12 — planning only | PASS boundary | 25 row là `AUTHOR-APPROVED PLANNING / NOT CANON`, row 020 là deferred; chưa tạo file trong `chapters/`, `briefs/` hoặc canonical plot/story paths. |

## 4. Density review

| Nhóm | Số row | Nhận định |
| --- | ---: | --- |
| `LIGHT` | 3 | Không tự động gộp: V1-CAND-006, 021 và 026 có ba handoff khác nhau. |
| `MEDIUM` | 11 | Có thể gộp chọn lọc khi cùng POV/cùng function; không gộp chỉ để đạt con số. |
| `HEAVY` | 12 | Ưu tiên review V1-CAND-008, 010, 011, 017, 018, 019, 022 và 025; chỉ tách nếu lộ hai irreversible turn hoặc hai climax độc lập. |
| Satellite deferred | 1 trong 26 row | V1-CAND-020 không nằm trong count mặc định; chỉ giữ audit trail và không được dùng nếu chưa có cổng Tác giả mới. |

Kết luận density: **23–24 minimum viable / 25–28 recommended / trên 28 là overflow risk**. Đây không phải chapter count đã khóa.

## 5. Unresolved register

- Phân vai từng đòn/chiến thắng player-avatar ở T1, T12 và T157.
- Tĩnh Xuyên trực tiếp đấu Dương Thiết Tâm hay chỉ chứng kiến; cấp bậc, gia thế và người chàng muốn ở lại bảo vệ.
- Người/cách cứu Giới; tình trạng thủy lưu, chìa thứ 21, thiệt hại và quan hệ thật giữa phá hoại–vụ Bạch Cương.
- Diễn giải sấm thi, tri thức hiện thời của Tiêu về cha mẹ, thư/đường/bến/lễ nhập Cái Bang.
- Người/cách cứu Lục, chi tiết trận Thôi, thương tích và mức Tiêu tận mắt thấy.
- Kết quả chữa Tam Muội, người đồng hành, hành trình Đại Lý và phản ứng nội bộ dài hạn.
- Custody Du Long, công năng artifact, cơ chế Huyền Nguyệt, câu chữ/độ trễ thông cáo.
- Thứ tự tuyệt đối giữa `CB-E` và `HN-E`; quan hệ thời gian giữa tin T1/S2 và T12/S92.
- Đích đi của Tĩnh Xuyên sau handoff; không đưa thông cáo T12/S92 tới chàng chỉ để đối xứng.
- V1-CAND-020 đã deferred; Cầu Chỉ Thủy đã được duyệt cho relay chính trị V1-CAND-026. Câu chữ, độ trễ và phản ứng kín vẫn mở.
- Tĩnh Xuyên–Ân Đồng: future canon giữ nguyên; Quyển I không mở route, hung khí hoặc chronology.

## 6. Kết quả Author gate — V1CAQ-01–06 APPROVED 2026-09-09

| ID | Đề xuất khuyến nghị | Hệ quả nếu duyệt |
| --- | --- | --- |
| V1CAQ-01 | Duyệt 25 function mặc định cùng causal braid và state/knowledge boundary trong matrix. | Architecture trở thành planning authority; row vẫn chưa phải prose/canon. |
| V1CAQ-02 | **Không dùng V1-CAND-020 làm satellite chapter mặc định**; giữ CDK-02 ngoài màn rồi cho agency của Lục hiện qua trạng thái/lời công khai và trận do chính ông đấu. | Đạt living wulin mà không mở POV khi tiêu chí “không thể kể bằng kênh khác” chưa chắc. |
| V1CAQ-03 | Duyệt **Cầu Chỉ Thủy** là relay candidate của V1-CAND-026 vì function là phán đoán bang vụ/chính trị; nếu sau này đổi function sang field task thì chuyển La Phong. | Khóa actor theo CDQ-02 nhưng không khóa câu chữ, độ trễ hoặc custody. |
| V1CAQ-04 | Duyệt density inference `23–24 minimum / 25–28 recommended / >28 overflow risk`, không coi bất kỳ số nào là target. | Có capacity envelope để bước sau đặt candidate sequence mà không trở lại quota. |
| V1CAQ-05 | Duyệt World Spine footprint hiện tại; giữ EF-DEPARTURE, T2/S15–S24, T12/S93–S95 và reservoir chưa deep-read ở trạng thái deferred. | Không nhồi nguồn ngoài pilot; không loại chúng khỏi series. |
| V1CAQ-06 | Sau khi V1CAQ-01–05 được duyệt, cho phép bước kế tiếp gán **số/tên chương ở mức proposal** và tạo chapter briefs theo architecture đã duyệt; prose và canon promotion vẫn cần cổng riêng. | Thực hiện cổng thứ hai CAPQ-06 mà không mở viết văn xuôi. |

Phê duyệt V1CAQ-01–06 không tự duyệt scene wording, beat, dialogue, prose, chronology tuyệt đối, kết quả các open slot, route Quyển II–V hoặc canon promotion.

Quyết định đã được lưu tại R-47–R-52 / D-031. Hai mươi lăm function mặc định là planning authority; V1-CAND-020 deferred; Cầu Chỉ Thủy là relay V1-CAND-026; density và World Spine footprint được giữ theo đề xuất. [Chapter Plan Quyển I](../chapter-plan-volume-i/README.md) đã được duyệt qua V1CBQ-01–06 (R-53–R-58 / D-032). [Scene-plan phase spec](../scene-plan-phase-spec-volume-i.md) đã được duyệt qua SPQ-01–06 (R-59–R-64 / D-033); candidate scene plan được mở nhưng mọi scene vẫn chờ V1SPAQ và văn xuôi còn đóng.
