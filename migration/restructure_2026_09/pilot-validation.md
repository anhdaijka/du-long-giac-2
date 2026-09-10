# Báo cáo kiểm tra — World coverage và pilot Quyển I

Ngày kiểm tra: 2026-09-09. Báo cáo bên dưới lưu lượt kiểm trước phê duyệt; phần cập nhật cuối ghi lượt đồng bộ V1PQ/BFCQ. Trạng thái hiện tại: `VOLUME I BRIDGE FEASIBILITY AUTHOR APPROVED / NOT CANON`.

## Đầu ra và phạm vi thay đổi

- World coverage: `world-coverage/ledger.json`, `ledger.tsv`, `README.md`, `editorial-notes.md`; bộ sinh/đối soát `scripts/build_world_coverage.py`.
- Pilot: `route-bibles/README.md`, `tieu-phung.md`, `tinh-xuyen.md`, `ha-nuong.md`, `convergence-matrix.md`; bộ kiểm tra `scripts/check_route_bible_pilot.py`.
- Bridge feasibility: `bridge-feasibility-volume-i.md`; bộ kiểm tra `scripts/check_bridge_feasibility.py`.
- Đồng bộ phê duyệt LWCQ và bàn giao: `author/decision-log.md`, `author/session-state.md`, `author-decisions.md`, `adaptation-contract-draft.md`, `living-wulin-coverage-spec.md`, `route-arc-bible-phase-spec.md`, `volume-architecture-proposal.md`, README của đợt restructure và `execution/restructure_source_survey_2026_09.json`.
- Bổ sung FC-008 vào `foundation-contradictions.md`; không sửa Foundation để tự giải mâu thuẫn.
- Không commit/stage thêm, không chỉnh SQLite, không tạo prose, canon diff hoặc nội dung Quyển II–V. Các thay đổi đã có trước trong worktree được giữ nguyên.

## Lệnh và kết quả

| Kiểm tra đã chạy | Kết quả | Chứng minh được / không chứng minh được |
| --- | --- | --- |
| `python scripts/build_world_coverage.py --check` | PASS: 465 task, 390 nhóm, 27 nhóm nhiều task; 19 unclassified; task 288 thiếu subtask | Tái chạy query SQLite read-only, so toàn bộ packet task/subtask/step/dialogue, đối soát artifact. Không chứng minh semantic review toàn bộ hoặc coverage toàn XML/bảng khác. |
| `python scripts/check_route_bible_pilot.py --self-test` | PASS: 5 file, 58 locator nguồn duy nhất, 18 file link, 8 ca dữ liệu sai bị từ chối | Kiểm quan hệ task–subtask–step, family tồn tại, file links, draft gates, skeleton I–V và placeholder. Không tự phán định ngữ nghĩa đúng, chất lượng văn học, độ khả thi hành trình hoặc continuity đã chứng minh. |
| `python -m py_compile scripts/build_world_coverage.py scripts/check_route_bible_pilot.py` | PASS | Hai công cụ biên dịch được; không phải coverage test mọi nhánh. |
| `npm run execution:check` | PASS: D01–D13 có artifact theo manifest | Manifest ở đây dùng `file_nonempty`; chữ COMPLETE chỉ có nghĩa qua các điều kiện đó, không có nghĩa tác giả đã duyệt pilot hoặc audit toàn repository hoàn tất. |
| `git diff --check` | PASS; có cảnh báo LF/CRLF | Kiểm tracked diff; không kiểm các file untracked. Bộ kiểm pilot đã kiểm riêng whitespace năm artifact mới. |
| `Get-FileHash story_database.sqlite3 -Algorithm SHA256` | Khớp nguồn packet | `b5c30040c9449f2223cf40bfec9866216423a60a82e2333b5cedb4fb5261bdb0`. |

Lần chạy đầu bộ kiểm pilot phát hiện regex nhận nhầm tiền tố I trong II/III/IV. Đã sửa ranh giới chữ số La Mã, chạy lại và đạt cả kiểm tra hiện trạng lẫn tám ca âm tính. Không còn lỗi ở các lệnh kiểm tra cuối.

Tám ca âm tính dùng dữ liệu biến đổi trong bộ nhớ, không sửa artifact: task không tồn tại, subtask thuộc sai task, step thuộc sai subtask, family không tồn tại, file link hỏng, điền nội dung quyển sau, mất nhãn chờ duyệt, mất ràng buộc không gặp trực tiếp.

## Review nguồn có mục tiêu

- T1/S7: giữ Hùng Đỉnh là người hướng dẫn avatar chế Tiễn xa; Diêm Bang giúp phía Cao Thủ Đại Nội tìm thư, không phải đồng minh phòng thủ. Đã hiệu chỉnh diễn giải ở bible Tĩnh Xuyên theo đúng source.
- T1/S2: tên trưởng lão là Quý Thúc Ban; pilot dùng đúng tên nguồn.
- T2/S9/E43–44: ngoài việc cùng người mang hai thư, còn có yêu cầu người đó ở lại Cái Bang rèn luyện. PB-01 đã ghi rõ đề xuất thay điều khoản có nguồn này, không che dưới nhãn đổi tên avatar.
- T157/S320/E1431–1432: lời yêu cầu mang chìa khóa, cam kết cử người cứu và mã dẫn về sub312 được giữ riêng với tóm tắt nguy cơ; chưa tự chốt mức ngập/thương vong.
- T12/S89–92: trợ chiến, chuyển chữa, thông cáo và tái thiết có chủ thể ngoài trio; cơ chế mặt trăng được ghi FC-008, chưa chọn Foundation hay source thắng.

Query, bind và kết quả cho các mốc trên được dẫn trong [pilot README](route-bibles/README.md); đây là review các rủi ro cụ thể, không phải tuyên bố đã fresh-review độc lập toàn bộ văn bản.

## Chưa chạy / chưa hoàn tất

- Không chạy Story Skills story validation vì chưa có `story.md`/story state mới được khởi tạo; không lấy continuity đã archive để làm đầu vào kiểm tra.
- Chưa có scene, chronology chi tiết, kiểm chứng thời gian truyền tin/di chuyển hoặc historical ledger mới.
- Tại lượt kiểm trước phê duyệt, V1PQ-01–04 và PB-01–06 chưa được tác giả duyệt; trạng thái này đã được thay bằng D-026/R-27–R-30. FC-008 hiện có cách xử lý tạm được duyệt, công năng vẫn mở.
- Chưa đọc sâu/khóa cách chuyển thể mọi member trong 390 nhóm; chưa kiểm kê hết các bảng NPC/map/item/lore/XML; audit claim Foundation/toàn repository vẫn là phần việc riêng còn mở.
- Chưa chọn nhân vật giao đấu thay Tiêu Phùng, người truyền từng bản tin hoặc hồ sơ Legendary Shadow. Không tự điền để làm cho pilot có vẻ đã kín.

## Bước tiếp theo

Tác giả đã duyệt [pilot và V1PQ-01–04](route-bibles/README.md). Đề xuất phạm vi khảo sát tính khả thi các Bridge Quyển I trước khi mở bước chi tiết kế tiếp; không xin lại quyền LWCQ/RABQ/V1PQ.

## Cập nhật sau phê duyệt V1PQ-01–04 — 2026-09-09

- Chỉ cập nhật sổ quyết định, nhãn planning của năm artifact pilot, các tài liệu trạng thái/contract/spec, FC-008, ghi chú biên tập, manifest D14 và nhãn tương ứng trong bộ kiểm pilot. Không thay sự kiện nguồn, nội dung lựa chọn đã trình hoặc placeholder II–V.
- Đã chạy lại `python scripts/check_route_bible_pilot.py --self-test`: PASS, 58 locator, 18 file link, 8 ca âm tính. Ca mất nhãn đã đổi từ draft/review sang approved-planning/noncanon; đây là kiểm nhất quán nhãn, không tự xác nhận quyền tác giả.
- Đã chạy lại `python scripts/build_world_coverage.py --check`: PASS, đủ 465 task và các query/result không đổi.
- Đã chạy `python -m py_compile scripts/check_route_bible_pilot.py`: PASS.
- Không chạy story validation vì chưa có story mới khởi tạo. Không tạo commit, scene, prose, nhân vật mới hoặc canon promotion.

## Cập nhật sau phê duyệt BFCQ-01–04

- `python scripts/check_bridge_feasibility.py --self-test`: PASS, 21 locator duy nhất, đủ 9 locator bắt buộc và 5 ca âm tính bị từ chối. Assurance chỉ bao phủ locator, nhãn quyết định lưu trên đĩa và ranh giới scope; không chứng minh chất lượng ngữ nghĩa/văn học.
- `python scripts/check_route_bible_pilot.py --self-test`: PASS, 5 file, 58 locator nguồn duy nhất, 20 file link và 8 ca âm tính.
- `python scripts/build_world_coverage.py --check`: PASS, 465 task, 390 family, 27 family nhiều task; 19 task unclassified; source gap T288 giữ nguyên.
- `python -m py_compile scripts/check_bridge_feasibility.py scripts/check_route_bible_pilot.py scripts/build_world_coverage.py`: PASS.
- `npm run execution:check`: PASS D01–D16; trạng thái COMPLETE chỉ nói các contract `file_nonempty` trong manifest đạt, không phải canon hay semantic audit hoàn tất.
- `git diff --check`: PASS; chỉ có cảnh báo chuyển LF/CRLF của các tracked file đã tồn tại trong worktree.
- Không chạy story validation vì chưa có `story.md` mới. Không tạo commit, chapter/scene plan, prose, chronology tuyệt đối, nội dung Quyển II–V, nhân vật mới hoặc canon promotion.

## Cập nhật continuity-detail spec và D-028/R-35

- `python scripts/check_continuity_detail_spec.py --self-test`: PASS, 24 locator duy nhất, đủ 14 locator bắt buộc, 3 file link và 6 ca âm tính. Assurance chỉ kiểm cấu trúc, owner của locator và ranh giới fail-closed; không tự phê duyệt CDQ.
- Lần chạy đầu phát hiện `T12/S86/E484` bị viết tắt thành `E484`. Đã sửa locator đầy đủ và chạy lại PASS; không đổi nghĩa custody.
- Các kiểm tra bridge, route bible, world coverage, Python compile, execution D01–D17 và `git diff --check` đều PASS trong lượt cuối. `git diff --check` chỉ báo cảnh báo LF/CRLF trên các tracked file của worktree.
- D-028/R-35 khóa chủ thể, kết cục và trách nhiệm Tĩnh Xuyên–Ân Đồng. FC-009 giữ mở riêng hung khí vì SQLite T4/S36 nói “kiếm” trong khi Foundation từng nói “thương”; không dùng spec Quyển I để tự giải xung đột.
- Không chạy story validation vì chưa có `story.md` mới. Không tạo commit, chapter/scene plan, prose, chronology tuyệt đối, nội dung route Quyển II–V hoặc canon promotion.

## Cập nhật sau phê duyệt CDQ-01–05

- Nâng `continuity-detail-spec-volume-i.md` thành `AUTHOR-APPROVED PLANNING / CDQ-01–05 / NOT CANON / NOT A CHAPTER PLAN`; cập nhật D-029, R-36–R-40, adaptation contract, route projections, session state và manifest D18.
- `python scripts/check_continuity_detail_spec.py --self-test`: PASS, 24 locator, đủ 14 locator bắt buộc, 3 file link và 6 ca âm tính. Bộ kiểm chỉ xác nhận nhãn phê duyệt đã được lưu cùng ranh giới/locator; không chứng minh chất lượng semantic hoặc tự duyệt chapter architecture.
- CDQ-01 giữ rescuer của Lục không tên và không thiết kế trong Quyển I; CDQ-02 chỉ cho chọn La/Cầu sau khi biết chức năng; CDQ-03–04 giữ lịch và custody mở; CDQ-05 không chọn hung khí Ân Đồng.
- Chưa tạo chapter architecture, chapter allocation, scene, prose, chronology tuyệt đối, route Quyển II–V hoặc canon promotion.

## Cập nhật Chapter Architecture Phase Spec — D19

- Tạo `chapter-architecture-phase-spec-volume-i.md` ở trạng thái `DRAFT / AUTHOR REVIEW REQUIRED / NOT A CHAPTER ARCHITECTURE / NOT CANON`; chỉ định nghĩa sáu artifact tương lai, schema row, năm movement basket, causal braid, World Spine pass, density pass và hai cổng review.
- Ghi FC-010: công thức 3-1-1 cũ có câu “tương tác bộ ba”, xung đột với cấm gặp trực tiếp trong Quyển I. Đề xuất CAPQ-05 dùng 3-1-1 như heuristic và đổi khoảng lặng Quyển I thành đơn tuyến/world aftermath; chưa chỉnh creative constitution.
- `python scripts/check_chapter_architecture_phase_spec.py --self-test`: PASS, 9 file link, 12 invariant, 6 CAPQ, 5 movement và 6 ca âm tính.
- `npm run execution:check`: PASS D01–D19. Không có thư mục/output `chapter-architecture/` trước phê duyệt CAPQ.
- Chưa sinh chapter candidate, dải số chương, chapter allocation, brief, scene, prose hoặc canon promotion.

## Cập nhật sau phê duyệt CAPQ-01–06 — D20

- Nâng `chapter-architecture-phase-spec-volume-i.md` thành `AUTHOR-APPROVED PHASE SPEC / CAPQ-01–06 / NOT A CHAPTER ARCHITECTURE / NOT CANON`; cập nhật R-41–R-46, D-030, adaptation contract, route projection, session state và manifest D20.
- CAPQ-05 giải quyết FC-010: creative constitution nay xác định 3-1-1 là heuristic cấp series, không phải quota; khoảng lặng Quyển I là đơn tuyến/world aftermath và không được tạo cuộc gặp sớm của trio.
- Bộ kiểm phase xác nhận record phê duyệt, 12 invariant, sáu CAPQ, năm movement và việc thư mục `chapter-architecture/` vẫn chưa tồn tại ở checkpoint ghi nhận phê duyệt. Assurance chỉ kiểm cấu trúc và ranh giới, không chứng minh chất lượng semantic hoặc phê duyệt các row tương lai.
- Phê duyệt này chỉ mở quyền tạo sáu artifact dạng candidate. Chưa sinh candidate row, dải số chương, tên/số chương, chapter brief, scene, prose, chronology tuyệt đối, route Quyển II–V hoặc canon promotion.

## Chapter Architecture candidate draft — D21

- Tạo đúng sáu artifact trong `chapter-architecture/`: README, TSV nguồn, projection Markdown, causal braid, World Spine selection và validation report.
- Matrix có 26 row để review: 25 function mặc định (8 Tĩnh Xuyên, 11 Tiêu Phùng, 6 Hạ Nương) và một satellite option Lục Trầm Châu. World Spine review khuyến nghị không dùng satellite mặc định vì phần causal tối thiểu có thể truyền qua CDK-02 ngoài màn + agency công khai của Lục + POV Tiêu ở lôi đài.
- Density inference là `23–24 minimum / 25–28 recommended / >28 overflow risk`, không phải target. V1-CAND-026 đề xuất Cầu Chỉ Thủy relay vì function chính trị; cả satellite và relay actor đều chờ V1CAQ.
- `python scripts/check_chapter_architecture.py --self-test`: PASS, 26 row, 105 locator, 15 link, đủ M1–M5 và 9 ca âm tính bị từ chối. Assurance chỉ bao phủ structure/locator/dependency/boundary, không chứng minh semantic/literary quality hoặc author approval.
- Không có Task 4 trong matrix; Tĩnh Xuyên–Ân Đồng chỉ hiện ở World Spine như future-invariant audit input. Không chọn hung khí/chronology hoặc làm mềm chủ thể–kết cục–trách nhiệm.
- Chưa đánh số/tên chương, chưa tạo chapter brief, scene, prose, chronology tuyệt đối, Quyển II–V hoặc canon promotion. Dừng tại V1CAQ-01–06.

## Cập nhật sau phê duyệt V1CAQ-01–06 — D22

- Lưu R-47–R-52 / D-031 từ chỉ thị “Duyệt toàn bộ `V1CAQ-01–06` theo đề xuất”; nâng 25 function mặc định, causal braid và World Spine footprint thành `AUTHOR-APPROVED PLANNING / NOT CANON`.
- V1-CAND-020 chuyển thành record deferred, không nằm trong default architecture. Dependency của V1-CAND-022 dùng `CDK-02 + V1-CAND-021`, nên không ép satellite POV để Lục giữ agency và tự đấu Thôi.
- V1-CAND-026 dùng Cầu Chỉ Thủy cho relay chính trị theo CDQ-02/V1CAQ-03; câu chữ, độ trễ và custody vẫn mở. Density envelope được duyệt là `23–24 / 25–28 / >28`, không phải target.
- V1CAQ-06 mở proposal số/tên chương và chapter brief. Chưa tạo các output đó trong lượt ghi nhận phê duyệt; scene, beat, dialogue, prose, chronology tuyệt đối, Quyển II–V và canon promotion vẫn đóng.
- `python scripts/check_chapter_architecture.py --self-test`: PASS, 25 row approved + 1 row deferred, 105 locator, 15 link và 12 ca âm tính. Các kiểm phase/continuity/bridge/route, world coverage, Python compile, execution D01–D22 và `git diff --check` đều PASS; không chạy story validation vì không sửa story canon.

## Chapter sequence và bounded briefs Quyển I — D23

- Tạo `chapter-plan-volume-i/` gồm README, sequence TSV/Markdown, provenance ledger, validation report và 25 brief. Baseline dùng một function approved mỗi chương, không đưa V1-CAND-020 vào sequence.
- Nhịp POV là 8 Tĩnh Xuyên / 11 Tiêu Phùng / 6 Hạ Nương; giữ lane order, Tĩnh Xuyên rời trước Tiêu tới Cái Bang, CDK-02 trước trận Lục–Thôi và thông cáo Bách Hoa trước relay Cầu Chỉ Thủy.
- Mỗi brief trỏ source nodes, packet, query record và full-result location; exact date/travel/location, scene list, beat, dialogue, combat detail và protected unknown đều deferred.
- Bảy lore-guard query mục tiêu cho Giang Tân, Bách Hoa, Cầu Chỉ Thủy, Lục Trầm Châu, Thôi Xuất Trần, La Phong và Thạch Hiên Viên đều exit 0.
- `lore-guard.py --check` đạt 25/25 brief; đây là known-regression scan, không tự chứng minh semantic grounding.
- Package dừng tại V1CBQ-01–06; chưa mở scene-plan spec, scene/prose, chronology tuyệt đối, Quyển II–V hoặc canon promotion.

## Cập nhật sau phê duyệt V1CBQ-01–06 — D24

- Lưu R-53–R-58 / D-032 từ chỉ thị “Duyệt” cho toàn bộ V1CBQ-01–06; nâng baseline 25 chương, 25 tên làm việc, reading order/POV và 25 bounded briefs thành `AUTHOR-APPROVED PLANNING / NOT CANON`.
- Giữ 12 row `HEAVY` chưa split. Chỉ được trình phương án 26–28 chương khi detail pass chứng minh một row vượt 5.500 từ dự kiến hoặc chứa hai irreversible turn; không coi dải này là quota.
- Exact date/travel/location, scene allocation, beat, dialogue, combat detail, protected unknown, prose và canon promotion tiếp tục đóng. Tĩnh Xuyên–Ân Đồng vẫn là protected future invariant; chưa chọn hung khí và không đưa route đó vào Quyển I.
- V1CBQ-06 chỉ mở quyền **đề xuất scene-plan phase spec** Quyển I; lượt ghi nhận này không tạo scene plan hoặc prose.
- Generator, package self-test, các bộ kiểm architecture/phase/continuity/bridge/route/world, Python compile, execution D01–D24 và `git diff --check` phải PASS trước khi bàn giao. Story Skills canon validation không chạy vì không sửa canon.

## Đề xuất Scene-plan Phase Spec Quyển I — D25

- Tạo `scene-plan-phase-spec-volume-i.md` ở trạng thái `PROPOSAL / AUTHOR REVIEW REQUIRED / NOT A SCENE PLAN / NOT CANON / NOT PROSE`; chưa tạo thư mục/output `scene-plan-volume-i/`.
- Spec đề xuất bảy nhóm artifact tương lai, scene-row schema cấp provenance, 15 invariant và hai cổng độc lập: SPQ trước implementation, V1SPAQ trước mọi prose phase.
- Density dùng 2–4 scene/chương như heuristic, cho phép 1 hoặc 5 có lý do. Tổng estimate trên 5.500 từ hoặc hai irreversible turn độc lập chỉ tạo split proposal, không tự sửa baseline 25 chương.
- Giữ one-POV chapter, cấm satellite insertion, exact chronology, hidden custody, cơ chế Huyền Nguyệt, scene cứu Lục và Task 4/Ân Đồng trong Quyển I. Bridge mới là default-deny; không dùng làm exit state trước phê duyệt.
- `python scripts/check_scene_plan_phase_spec.py --self-test`: PASS 25 chapter input, 25 brief, 15 invariant, 6 SPQ và 9 ca âm tính; assurance chỉ bao phủ cấu trúc/input approval/boundary, không chứng minh chất lượng semantic hoặc scene feasibility.
- Package dừng tại SPQ-01–06. Chưa tạo scene row, chapter scene map, beat, dialogue, prose, chronology tuyệt đối hoặc canon promotion.

## Cập nhật sau phê duyệt SPQ-01–06 — D26

- Lưu R-59–R-64 / D-033 từ chỉ thị “Duyệt toàn bộ SPQ-01–06 theo đề xuất”; nâng `scene-plan-phase-spec-volume-i.md` thành `AUTHOR-APPROVED PHASE SPEC / SPQ-01–06 / NOT A SCENE PLAN / NOT CANON / NOT PROSE`.
- Được tạo bảy nhóm artifact candidate dưới `scene-plan-volume-i/`, nhưng không scene nào được phê duyệt trước; POV 25 chương giữ nguyên và nhu cầu satellite phải quay lại amendment cấp chapter architecture.
- Density dùng 2–4 như heuristic; trên 5.500 từ dự kiến hoặc hai irreversible turn độc lập chỉ được tạo split proposal. Bridge bền vững mới vẫn default-deny; time/location chưa có nguồn chỉ là candidate.
- V1SPAQ tiếp tục là cổng bắt buộc cho toàn bộ candidate package. Phê duyệt SPQ không mở prose-phase spec, prose, chronology tuyệt đối, canon promotion, custody, cơ chế Huyền Nguyệt hoặc chi tiết Tĩnh Xuyên–Ân Đồng.
- Lượt ghi nhận D26 chưa tạo `scene-plan-volume-i/`, scene row, chapter map, beat, dialogue hoặc prose.

## Pivot về bản đồ macro 13 Arc → 5 quyển — D27

- Lưu D-034/R-65 theo chỉ thị Tác giả: dừng micro-planning scene-plan và quay lại mục tiêu chia volume, vai trò POV và living wulin.
- `scene-plan-phase-spec-volume-i.md` vẫn là authority đã duyệt nhưng đóng băng làm reference; không tạo `scene-plan-volume-i/` trong critical path hiện tại.
- Tạo `series-arc-volume-map.md` như một draft review duy nhất, tái sử dụng semantic survey/source graph/five-volume architecture: 13 Arc có quyển chính/phụ, vai trò POV macro, kênh living-wulin và mode xử lý; 19 task unclassified tiếp tục để ngoài.
- Không sinh validator mới, chapter/scene, prose, chronology tuyệt đối hoặc canon promotion. Macro map không tự sửa cấu trúc năm quyển đã duyệt.

## Phê duyệt macro map — D28

- Lưu R-66/D-035 từ chỉ thị “Duyệt macro map theo đề xuất”; nâng `series-arc-volume-map.md` thành `AUTHOR-APPROVED MACRO PLANNING`, không phải route bible, chronology, chapter/scene plan, prose hay canon.
- Giữ bốn kết luận của map: Arc là nguồn lực kịch tính; 19 task unclassified đứng ngoài; Arc 09 phân bố III→IV; satellite POV là ngoại lệ hiếm.
- Scene-plan implementation vẫn frozen. Chỉ mở proposal role map Quyển II–V ở cấp Arc/POV; không tạo validator hay micro-gate mới.

## Role map Quyển II–V proposal — D29

- Tạo `volume-ii-v-role-map-proposal.md`: bốn hàng Quyển II–V, mỗi hàng giữ POV primary pressure/non-ownership, World Spine channel, source boundary và Arc trọng tâm.
- Không ghi direct task allocation, chronology, satellite cụ thể hoặc Bridge mới. Giữ Arc 09 III→IV, Huyễn Cảnh reliability lock, endpoint aperture và canon Tĩnh Xuyên–Ân Đồng.
- Dừng tại V2VRQ-01–04. Không tạo validator mới, Route Arc Bible II–V, detailed convergence matrix, chapter, scene, prose hoặc canon.

## Phê duyệt role map Quyển II–V — D30

- Lưu R-67/D-037 từ chỉ thị “Chốt toàn bộ theo đề xuất”; nâng `volume-ii-v-role-map-proposal.md` thành macro planning authority trong ranh giới Arc/POV.
- Chốt bounded convergence II, mobilization ethic III, ba trục độc lập IV và legacy-choice climax V. Không biến bất kỳ điểm nào thành task allocation, chronology hay route bible.
- Chỉ mở proposal cross-volume convergence matrix cấp pressure/knowledge/world-return; scene-plan vẫn frozen, không tạo validator/micro-gate mới.

## Cross-volume convergence matrix proposal — D31

- Tạo `cross-volume-convergence-matrix.md` gồm bốn hàng II–V với pressure chung, knowledge handoff tối thiểu, World Spine return, convergence/divergence và exit state.
- Giữ `READER_KNOWLEDGE != CHARACTER_KNOWLEDGE`, Arc 09 III→IV, satellite ngoại lệ, Huyễn Cảnh reliability lock, endpoint aperture và protected core Tĩnh Xuyên–Ân Đồng.
- Dừng tại CMQ-01–03. Không tạo validator mới, task allocation, route bible, chronology, chapter, scene, prose hay canon.

## Phê duyệt cross-volume convergence matrix — D32

- Lưu R-68/D-039 từ chỉ thị “duyệt toàn bộ theo đề xuất”; nâng `cross-volume-convergence-matrix.md` thành macro planning authority.
- Khép macro design II–V. Không tự sinh thêm artifact macro, route bible, task allocation, chronology, chapter, scene, prose, Bridge mới hay canon.
- Scene-plan vẫn frozen. Bước sau chỉ là consolidation review không đổi quyết định hoặc khảo sát sâu do Tác giả chọn; không tạo validator/micro-gate mới.

## Macro consolidation review — D33

- Tạo `macro-authority-index.md` để nén đường đọc authority R-16/R-66/R-67/R-68 và bất biến chung; review không tạo claim/design mới.
- Chuẩn hóa hai tham chiếu trạng thái: macro map không còn draft; scene-plan freeze là hậu consolidation. Không thay đổi boundary hoặc mở implementation.
- Sau D33, không có bước tự động. Cần Tác giả chọn scope khảo sát sâu hoặc phase cần mở lại.

## Writer-Readiness Gate proposal — D34

- Tạo `writer-readiness-gate-volume-i.md`: contract năm khối, pilot 01–03, Gemini non-canon writer, Terra reviewer và gateway SPQ → V1SPAQ giữ nguyên.
- Dừng tại WRGQ-01–04. Không tạo preflight packet, `scene-plan-volume-i/`, prose, canon hay validator mới.

## Phê duyệt Writer-Readiness Gate — D35

- Lưu R-69/D-042: contract năm khối, pilot 01–03, Gemini non-canon writer và Terra reviewer được duyệt.
- Chỉ mở một preflight packet mẫu 01–03; scene-plan, prose, canon và validator mới tiếp tục đóng.

## Gemini-first author-gated protocol — D36

- Lưu R-70/D-043: Gemini là operator toàn thời gian, tự đọc source/tạo candidate packet/self-check; không dùng model khác làm reviewer bắt buộc.
- Fail-closed với clue/glue: chỉ proposition-level provenance mới thành fact; inference/Bridge/open slot không tự nâng; author gate/canon/amendment/V1SPAQ không thể bị bỏ qua.
- Không tạo packet, scene plan, prose hay canon trong lượt ghi nhận policy.

## Candidate preflight packet 01–03 — D37

- Tạo `writer-preflight-volume-i/README.md` và `chapters_01_03.md` theo R-69/R-70; không scene/prose.
- Chương 03 tách rõ lời kể bệnh sử của Hứa là `SOURCE REPORT`, cấm nâng thành fact khách quan.
- Dừng tại review packet; không mở scene plan, prose, canon hay validator mới.

## Volume I preflight coverage ledger — D38

- Lưu R-71/D-045: packet mẫu 01–03 được Tác giả duyệt và phạm vi Quyển I được mở ở mức **coverage safety index**, không phải implementation chapter-by-chapter.
- Tạo `writer-preflight-volume-i/volume-i-coverage-ledger.md`, dùng brief và SQLite result container hiện hữu làm evidence authority; tất cả durable proposition của Gemini phải có receipt và failure code fail-closed.
- Không tạo scene plan, scene, beat, dialogue, prose, chronology, Bridge mới hoặc canon.

## Volume II deep survey and source-window coverage — D39

- Lưu R-72/D-046: Tác giả chọn khảo sát sâu Quyển II trước, sau đó mới tạo coverage theo cùng nguyên tắc query/result.
- Tạo `writer-preflight-volume-ii/volume-ii-source-window-map.md` và ledger cùng tên. `V2-SW-*` không là `V2-CH-*`; source map không tạo chapter allocation hay author-approved chapter architecture.
- Kiểm `SOURCE REPORT`, `GAMEPLAY/BRANCH`, `REPEATABLE`, `UNSURVEYED` và open source boundaries trước khi Gemini dùng một proposition. Không scene, prose, canon, chronology, custody/cơ chế hoặc Bridge mới.

## Volume II chapter architecture proposal — D40

- Lưu R-73/D-047: Tác giả duyệt ba source window candidate và yêu cầu đề xuất architecture Quyển II.
- Tạo `chapter-architecture-phase-spec-volume-ii.md`: năm functional candidates, trong đó first physical convergence là Bridge-gated, density unresolved và mapping avatar/POV, lane Hạ Nương phải qua V2CAQ riêng.
- Dừng tại `V2CAQ-01`–`05`; không tạo `V2-CH-*`, scene, prose, canon, chronology hoặc Bridge implementation.

## Phê duyệt Volume II functional architecture — D41

- Lưu R-74/D-048: Tác giả duyệt V2CAQ-01–05 theo default fail-closed của proposal.
- Không map avatar sang POV; Hạ Nương tiếp tục unassigned; first convergence chỉ là functional Bridge; count unresolved.
- Chỉ mở một targeted deep survey cho gap Hạ/density; không tạo chapter, scene, prose, canon hoặc Bridge implementation.

## Deep survey Hạ/density Quyển II — D42

- Lưu R-75/D-049: survey chỉ đọc T118/S267, T130/S279, T223/S398 thay vì mở cả source family.
- T130/S279 và T223/S398 trở thành Bridge-context candidate có provenance; Hạ presence, medical mechanism/outcome, possession và chapter count vẫn fail-closed.
- Dừng tại V2HDAQ-01–03; không `V2-CH-*`, scene, prose, canon hoặc chronology.

## Phê duyệt V2HDAQ-01–03 — D50

- Lưu R-76/D-050: Bridge Hạ chỉ là observation/comparison/community-care context quanh V2-HS-01/02; không avatar credit, y-kết luận/cure, possession/use vật phẩm hay medical-case closure.
- T118/S267 tiếp tục không vào architecture; `COUNT = UNRESOLVED`.
- Chỉ mở proposal chapter architecture/`V2-CH-*`; chưa tạo chapter, scene, prose, chronology, combat hay canon.

## Đề xuất chapter architecture Quyển II — D51

- Lưu R-77/D-051: architecture chỉ gồm bảy candidate-function trong dải 5–7; không có chapter count, title, number hay brief.
- `V2-ARCH-CAND-01/02` là proposed relay/aftermath allocation, không avatar mapping; `03/06` bị giới hạn bởi R-76; `04/06` optional; `05` không hơn functional convergence; `07` chỉ là organization/document handoff.
- Dừng tại V2CABQ-01–06; không có `V2-CH-*` projection/coverage ledger, chapter, scene, prose, chronology, combat hoặc canon.

## Default progress + V2-CH coverage — D52/D53

- R-78 bỏ hard stop thủ tục trong source/planning; author question chỉ dành cho Gemini writer khi cần fact/canon/chronology/creative Bridge chưa được evidence hoặc decision chứng minh.
- R-79/D-053 tạo `V2-CH-01`–`07` candidate coverage với receipt, label, permitted use, prohibited inference và writer hard stop; key không là chapter number/count/title/brief.
- Không scene, prose, chronology, canon hoặc factual/creative resolution mới.

## Mở rộng chapter allocation Quyển II — D57

- Theo phản hồi mật độ của Tác giả, baseline 5–7 D-054 được phân loại lại thành functional spine; allocation hiện hành là 24 chapter-function.
- Deep survey Arc 04/05/07 được lưu tại `writer-preflight-volume-ii/volume-ii-expanded-source-windows.md`; `chapter-plan-volume-ii/` ghi thứ tự, aperture, chức năng, receipt và writer boundary cho đủ 24 chương.
- Kiểm tra yêu cầu: đủ `V2-CH-01`–`24`, 24 row sequence/ledger, T118 không được tái nhập, T225 chỉ được dùng hai lát cắt khác chức năng. Không scene, prose, canon hoặc chronology mới.

## Mở rộng chapter allocation Quyển III — D58

- Baseline bảy chức năng D-055 được phân loại lại thành functional spine; allocation hiện hành có 28 chapter-function, aperture 14 Tĩnh / 8 Tiêu / 6 Hạ.
- `writer-preflight-volume-iii/volume-iii-expanded-source-windows.md` giữ ranh giới Arc 08 và slice quân doanh Arc 09; Task 303+ cùng Đại Lý không được nhập, repeatable chỉ làm texture.
- Kiểm tra yêu cầu: đủ `V3-CH-01`–`28`, receipt tồn tại trong packet, POV count khớp, không scene/prose/canon/chronology và không diễn route Tĩnh Xuyên–Ân Đồng.

## Mở rộng chapter allocation Quyển IV — D59

- Baseline bảy chức năng D-056 được phân loại lại thành functional spine; allocation hiện hành có 28 chapter-function, aperture 10 Tĩnh / 10 Tiêu / 8 Hạ.
- `writer-preflight-volume-iv/volume-iv-expanded-source-windows.md` giữ ranh giới cụm Đại Lý cuối Arc 09, các cửa sổ chọn lọc Arc 10 và Task 352/S527–S536; quân doanh Quyển III không tái nhập.
- Kiểm tra yêu cầu: đủ `V4-CH-01`–`28`, receipt tồn tại trong packet, POV count khớp, T330 vắng mặt và chuỗi Task 352 phủ đúng S527–S536. Không scene/prose/canon/chronology hay placement Tĩnh Xuyên–Ân Đồng.

## Chapter allocation đầy đủ Quyển V — D60

- Allocation hiện hành có 35 chapter-function, aperture 13 Tĩnh / 12 Tiêu / 10 Hạ; không tạo functional spine trung gian.
- `writer-preflight-volume-v/volume-v-expanded-source-windows.md` phân biệt Task 382, task huy động 395–404, chiến dịch 442–462 và protected-canon insert T4/S36–S37.
- Kiểm tra yêu cầu: đủ `V5-CH-01`–`35`, receipt tồn tại trong packet, T446/T447 vắng mặt, T450–T451 giữ reliability/corroboration gate, T4/S36–S37 chỉ dùng cho outcome/responsibility đã khóa. Không scene/prose/canon/chronology hoặc giải Du Long.

## Cross-volume allocation integrity — D61

- Kiểm đủ 140 row sequence và 140 row ledger theo phân bố 25/24/28/28/35; chuẩn hóa `Tiêu Phùng — limited convergence` về Tiêu cho kết quả 52 Tĩnh / 50 Tiêu / 38 Hạ.
- Replay locator cho 193 lượt tham chiếu: tất cả resolve trong packet được row khai báo; có 183 locator duy nhất và một row decision-only (`V2-CH-21`).
- Không có exact `T/S` hoặc Task ID dùng xuyên quyển. Chín locator reuse nội quyển được ghi guard tại `series-chapter-allocation-index.md`; không reuse nào được hiểu là biến cố mới.
- Không tạo scene, prose, chronology, canon hoặc source claim mới. Foundation claim audit vẫn tách riêng.

## Gemini chapter-workflow router — D62

- Tạo `gemini-chapter-workflow-router.md` dùng authority chain index → sequence → ledger → packet → receipt cho đúng chapter được yêu cầu.
- Router buộc Gemini xuất một trong `PREFLIGHT READY`, `QUESTION ONLY` hoặc `DRAFT READY`; preflight mặc định không thành scene/beat/prose.
- Câu hỏi Tác giả chỉ phát sinh khi detail cần thiết chạm WG/PF gate; routine wording, gesture và micro-action không tạo durable state được tiếp tục.

## Antigravity workflows và skills — D63

- Bốn workflows và bốn skills dùng chung docs/playbooks/gemini-evidence-review.md; hướng dẫn gọi lệnh ở docs/antigravity-novel-workflows.md. Reviewer inventory claim từ toàn văn trước verdict writer, đối chiếu raw source/author decisions và rà requirement/continuity.
- quick_validate.py: bốn skills hợp lệ. node --check scripts/bootstrap.mjs: PASS. Kiểm logic bootstrap bằng filesystem giả: chỉ xóa upstream skill, giữ cả bốn project skills và từ chối copy đè; không chạy bootstrap thật.
- scripts/evidence-test.py: 7 test PASS (locator sai, excerpt bịa/sai field, thiếu lineage và claim integration). scripts/claim-approval-test.py: 3 test PASS.
- review-guard functions: coverage và quotes hợp lệ PASS; bỏ phần cuối manuscript hoặc quote bịa bị từ chối. Đây là kiểm cơ học, không phải test Gemini hiểu source.
- Chưa kiểm UI slash discovery hoặc thực thi Gemini trong Antigravity. Không có prose/canon mới.
