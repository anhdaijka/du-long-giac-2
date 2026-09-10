# Tái cấu trúc Du Long Giác — working area

Current update D-065/R-91: [Temporal/creative contract](temporal-continuity-contract.md) and [temporal-character framework](temporal-character-framework.md) are approved. Operational temporal references use the contract; legacy matrices are archived. The framework gives author direction for timeline, trio, relationships, martial growth, living Wulin, history and secrets without becoming a game-fact ledger or complete chronology. Earlier phase statuses below are historical; the current chapter baseline is the 140-function index and Gemini router.

Current proposal D-066: [Canon Registry proposal](canon-registry-proposal.md) defines a minimal, source-safe registry schema and lifecycle. It creates no registry or fact rows; CRQ-01–03 apply only when implementation starts.

Current implementation D-067/R-93: `canon-registry/` is initialized empty/on-demand under the approved proposal. It has schema/open-slot pointers only; no fact/state row has been seeded.

Trạng thái: `WORLD COVERAGE PRELIMINARY COMPLETE / SERIES ARC-VOLUME MAP AUTHOR-APPROVED / VOLUME II–V ROLE-MAP PROPOSAL AUTHORIZED / SCENE-PLAN IMPLEMENTATION FROZEN`.

Đây là khu làm việc không-canon cho đợt tái cấu trúc bắt đầu ngày 2026-09-08. Không artifact nào trong thư mục này tự thay đổi canon, phân quyển, timeline, nhân vật, hay văn xuôi.

Thứ tự làm việc:

1. kiểm kê và tái dựng nguồn;
2. lập adaptation contract mới và trình Tác giả;
3. chỉ sau đó mới đề xuất cấu trúc quyển/chương;
4. chỉ sau các cổng duyệt mới tạo hoặc cập nhật trạng thái canon.

`evidence/arc-membership.tsv` và `evidence/arc-membership-report.md` được sinh lặp lại bằng `python scripts/restructure_source_survey.py`. Chúng dùng Narrative Book như locator của tập task; dữ liệu SQLite mới là bằng chứng cho task, subtask, step và dialogue.

Khảo sát theo locator đủ 13 Arc và 19 task unclassified đã được lưu; không đồng nghĩa mọi proposition đã qua deep audit. AQ-01–05, VAQ-01–04, RABQ-01–03 và LWCQ-01–04 đã được Tác giả duyệt. `volume-architecture-proposal.md` là planning authority năm quyển.

[World coverage](world-coverage/README.md) đã có disposition sơ bộ cho 465 task, 390 nhóm lưu trữ; 27 nhóm nhiều task không tự được gộp thành một sự kiện. Phạm vi là tasks và subtasks/steps/dialogues, chưa phải mọi bảng SQLite hoặc XML.

[Pilot Quyển I](route-bibles/README.md) gồm ba bible và convergence matrix, đã được duyệt qua V1PQ-01–04 ngày 2026-09-09 (R-27–R-30 / D-026). [Khảo sát Bridge Quyển I](bridge-feasibility-volume-i.md) cũng đã được duyệt toàn bộ qua BFCQ-01–04 (R-31–R-34 / D-027): Lục Trầm Châu thay trận, relay công khai tối thiểu, ba dải partial order và custody mở với Hạ Nương ở tuyến cứu người. Chỉ Quyển I được điền; II–V là placeholder. V1CAQ-03 hiện chọn Cầu Chỉ Thủy cho relay chính trị; cơ chế Huyền Nguyệt, người/cách cứu Lục, ngày–độ trễ và custody thật vẫn chưa được chọn. Chưa có prose, canon promotion hay hồ sơ Legendary Shadow mới.

[Spec continuity-detail Quyển I](continuity-detail-spec-volume-i.md) đã được duyệt qua CDQ-01–05 (R-36–R-40 / D-029), khóa partial order, state/knowledge handoff và các open slot theo chiến lược giữ mở. D-028/R-35/R-40 đồng thời tái khóa canon Tĩnh Xuyên–Ân Đồng như future invariant: không đổi kết cục hay trách nhiệm, không kéo route này vào Quyển I và chưa chọn hung khí/chronology chi tiết. Quyền đề xuất phase spec từ cổng này đã được thực hiện tại D19; CAPQ-01–06 sau đó mở riêng bước tạo candidate artifacts.

[Chapter-architecture phase spec Quyển I](chapter-architecture-phase-spec-volume-i.md) đã được duyệt qua CAPQ-01–06 (R-41–R-46 / D-030). [Bộ sáu artifact architecture](chapter-architecture/README.md) đã được duyệt qua V1CAQ-01–06 (R-47–R-52 / D-031): 25 function mặc định, V1-CAND-020 deferred, Cầu Chỉ Thủy relay chính trị, irregular causal braid, World Spine footprint và density inference 23–24 minimum / 25–28 recommended / trên 28 overflow risk. Bước proposal số/tên chương và chapter brief đã mở; scene/prose và canon promotion chưa mở.

[Chapter Plan Quyển I](chapter-plan-volume-i/README.md) đã được Tác giả duyệt toàn bộ V1CBQ-01–06 (R-53–R-58 / D-032): baseline 25 chương, 25 tên làm việc, reading order/POV và 25 bounded briefs là planning authority. Không có V1-CAND-020, không exact date/travel, không scene list hoặc prose. Quyền mới chỉ cho phép đề xuất scene-plan phase spec; chưa cho phép tạo scene plan.

[Scene-plan phase spec Quyển I](scene-plan-phase-spec-volume-i.md) đã được duyệt toàn bộ SPQ-01–06 (R-59–R-64 / D-033): bảy nhóm artifact, scene-row schema, 15 invariant, density/split contract và hai cổng độc lập. Được phép tạo candidate `scene-plan-volume-i/`, nhưng lượt ghi nhận này chưa tạo scene row/map; candidate package vẫn phải qua V1SPAQ và prose tiếp tục đóng.

Theo D-034/R-65/R-68, implementation scene-plan được đóng băng làm reference để tránh micro-planning vượt mục tiêu. [Macro authority index](macro-authority-index.md) là điểm vào gọn cho bốn tầng authority đã duyệt: five-volume architecture, 13-Arc map, role map II–V và convergence matrix. Macro design đã hoàn tất; không tự mở thêm artifact macro, route, chapter, scene hay prose. Lượt tiếp theo chỉ có thể là khảo sát sâu trong một phạm vi mới do Tác giả chọn, hoặc một phase thiết kế được mở lại bằng approval mới.

[Writer-Readiness Gate Quyển I](writer-readiness-gate-volume-i.md) là scope mới đang chờ review: contract an toàn cho writer model, pilot 01–03 và reviewer contract/provenance. Dừng tại WRGQ-01–04; không tạo preflight packet, scene plan hay prose.

Theo R-69/D-042/R-70/D-043, WRGQ-01–04 đã duyệt và Gemini là operator chính. Gemini phải fail-closed trước clue/glue và không được tự vượt author gate. Bước được mở duy nhất là một candidate preflight packet mẫu 01–03; scene-plan và prose tiếp tục đóng.

[Candidate preflight packet 01–03](writer-preflight-volume-i/chapters_01_03.md) và [coverage ledger Quyển I](writer-preflight-volume-i/volume-i-coverage-ledger.md) đã được Tác giả duyệt theo D-045. Chúng chỉ ràng buộc preflight Gemini bằng query/result receipt; không mở scene-plan hay prose.

[Deep survey và source-window map Quyển II](writer-preflight-volume-ii/volume-ii-source-window-map.md) cùng [coverage ledger cấp source window](writer-preflight-volume-ii/volume-ii-source-window-coverage-ledger.md) được tạo theo D-046. Chúng chưa là chapter plan/ledger và phải qua author selection trước khi có `V2-CH-*`.

[Chapter architecture Quyển II](chapter-architecture-phase-spec-volume-ii.md) đã được duyệt qua V2CAQ-01–05 theo D-048: functional spine được giữ, avatar mapping không tự mở, Hạ Nương chờ evidence, first convergence chỉ ở cấp Bridge chức năng và count vẫn unresolved. Nó chưa tạo chapter plan, scene hay prose.

[Deep survey Hạ Nương/density Quyển II](writer-preflight-volume-ii/volume-ii-ha-density-deep-survey.md) là D-049/D-050: Bridge Hạ hẹp đã được duyệt với provenance, nhưng không có direct Hạ lane; T118/S267 vẫn bị loại và chapter count chưa chốt. Chỉ proposal `V2-CH-*` được mở; chapter plan, scene và prose vẫn đóng.

[Đề xuất chapter architecture Quyển II](chapter-architecture-volume-ii-proposal.md) là D-051 candidate review: bảy functional container thuộc dải 5–7, không phải seven-chapter plan. Mọi POV allocation là adaptation proposal, Bridge Hạ giữ R-76, first convergence chưa là scene, và Task 225 vẫn chỉ là organization/document handoff. Dừng tại V2CABQ-01–06.

[V2-CH candidate projection và coverage](chapter-architecture-volume-ii/README.md) đã được tự động tiếp tục theo D-052/R-78: không còn cổng duyệt thủ tục trong planning. Ledger chỉ hard-stop Gemini khi implementation thực sự cần author decision về fact, canon, chronology hoặc creative Bridge; nó chưa là chapter plan, scene hay prose.

[Chapter plan source-safe Quyển II](chapter-plan-volume-ii/README.md) được D-057/R-83 mở rộng từ functional spine 5–7 thành baseline **24 chapter-function** sau khảo sát sâu Arc 04/05/07. Phân phối aperture 9 Tiêu / 8 Hạ / 7 Tĩnh; mỗi chương có function, provenance và writer boundary, chưa có scene/beat/prose.

[Chapter plan source-safe Quyển III](chapter-plan-volume-iii/README.md) được D-058/R-84 mở rộng từ functional spine bảy row thành baseline **28 chapter-function**, phân phối 14 Tĩnh / 8 Tiêu / 6 Hạ. Nguồn chỉ gồm Arc 08 và lát cắt Phục Ngưu–quân doanh Arc 09; Đại Lý vẫn thuộc Quyển IV, chưa có scene/beat/prose.

[Chapter plan source-safe Quyển IV](chapter-plan-volume-iv/README.md) được D-059/R-85 mở rộng từ functional spine bảy row thành baseline **28 chapter-function**, phân phối 10 Tĩnh / 10 Tiêu / 8 Hạ. Nguồn chỉ gồm cụm Đại Lý cuối Arc 09, các cửa sổ chọn lọc Arc 10 và Task 352/S527–S536; T330 giữ conflict, quân doanh Quyển III không tái nhập, chưa có scene/beat/prose.

[Chapter plan source-safe Quyển V](chapter-plan-volume-v/README.md) là D-060/R-86: baseline **35 chapter-function**, phân phối 13 Tĩnh / 12 Tiêu / 10 Hạ, dùng Arc 11–12 và protected-canon insert T4/S36–S37. T446/T447 bị loại vì conflict; Task 450–451 giữ reliability/corroboration gate; placement muộn của kết cục Ân Đồng chưa là chronology canon.

[Series Chapter Allocation Index](series-chapter-allocation-index.md) là D-061/R-87: điểm vào hợp nhất cho Gemini trên 140 chapter-function Quyển I–V. Integrity pass xác nhận 52 Tĩnh / 50 Tiêu / 38 Hạ, không có Task/locator dùng xuyên quyển, liệt kê reuse nội quyển và gom các writer hard stop thật; index không thay source packet, ledger hoặc canon.

[Gemini Chapter Workflow Router](gemini-chapter-workflow-router.md) là D-062/R-88: contract dùng index để dựng preflight theo yêu cầu từng chương. Gemini chỉ hỏi Tác giả khi một `WG-*`/`PF-*` thực sự cần thiết; không tạo trước 140 packet hoặc mở scene/prose/canon.

Kiểm tra: `python scripts/build_world_coverage.py --check`, `python scripts/check_route_bible_pilot.py --self-test`, `python scripts/check_bridge_feasibility.py --self-test`, `python scripts/check_continuity_detail_spec.py --self-test`, `python scripts/check_chapter_architecture_phase_spec.py --self-test`, `python scripts/check_chapter_architecture.py --self-test`, `python scripts/build_volume_i_chapter_briefs.py --check`, `python scripts/check_volume_i_chapter_briefs.py --self-test`, `python scripts/check_scene_plan_phase_spec.py --self-test`, `npm run execution:check`. Execution manifest chỉ kiểm sự hiện diện artifact; không thay thế kiểm nguồn hoặc phê duyệt văn học. [Báo cáo kiểm tra](pilot-validation.md) ghi lệnh đã chạy, giới hạn và công việc còn mở.
