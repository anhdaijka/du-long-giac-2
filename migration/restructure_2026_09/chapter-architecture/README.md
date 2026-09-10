# Chapter Architecture Quyển I — approved planning

Trạng thái: `AUTHOR-APPROVED PLANNING / V1CAQ-01–06 / NOT A CHAPTER PLAN / NOT CANON`.

Tác giả đã duyệt toàn bộ V1CAQ-01–06 ngày 2026-09-09. Hai mươi lăm chapter-function mặc định, causal braid, state/knowledge boundary và World Spine footprint trở thành planning authority; V1-CAND-020 được giữ như record deferred, không thuộc architecture mặc định. Bộ hồ sơ chưa đặt số/tên chương và chưa tạo chapter brief, scene, beat, lời thoại hoặc prose; mọi candidate ID chỉ là khóa ổn định của bảng.

## Bộ sáu artifact

1. `README.md` — authority, provenance, cách đọc, density và cổng duyệt.
2. `chapter-function-matrix.tsv` — bảng nguồn máy đọc được, 25 function mặc định đã duyệt và 1 satellite record deferred.
3. `chapter-function-matrix.md` — projection phục vụ review, không thêm fact ngoài TSV.
4. `interleave-and-dependency-map.md` — causal braid, cạnh bắt buộc và cạnh cố ý để mở.
5. `world-spine-selection.md` — footprint sự kiện thế giới, kênh kể và các nguồn deferred/excluded.
6. `validation-report.md` — kiểm tra tự động, adversarial review, unresolved register và author gate.

## Authority order

1. SQLite `story_database.sqlite3`, SHA-256 `b5c30040c9449f2223cf40bfec9866216423a60a82e2333b5cedb4fb5261bdb0`, là nguồn tối thượng cho game fact.
2. [Author decisions](../author-decisions.md), đặc biệt R-11–R-52.
3. [Continuity-detail contract](../continuity-detail-spec-volume-i.md), CDQ-01–05.
4. [Bridge feasibility](../bridge-feasibility-volume-i.md), BFCQ-01–04.
5. [Route Bibles](../route-bibles/README.md) và [convergence matrix](../route-bibles/convergence-matrix.md).
6. [Chapter Architecture phase spec](../chapter-architecture-phase-spec-volume-i.md), CAPQ-01–06.
7. [World Coverage ledger](../world-coverage/README.md) chỉ là preliminary disposition; một hàng ledger không tự chứng minh scene readiness.

Archive/rejected không phải authority hoặc nguồn cảm hứng mặc định.

## Provenance ledger

Mỗi `source_nodes` trong TSV dùng mã `T#/S#/E#` hoặc `T#/S#/D#`. Query, bind và toàn bộ kết quả nằm trong các packet sau:

| Cụm | Packet kết quả | Query bind |
| --- | --- | --- |
| T1, T2 | [arc_00.json](../evidence/source-packets/arc_00.json) | task `(1)`/`(2)`; subtasks `(task_id)`; steps/dialogues `(sub_id)` |
| T12 | [arc_01.json](../evidence/source-packets/arc_01.json) | task `(12)`; subtasks `(12)`; steps/dialogues `(sub_id)` |
| T157 | [arc_06.json](../evidence/source-packets/arc_06.json) | task `(157)`; subtasks `(157)`; steps/dialogues `(sub_id)` |

```sql
SELECT task_id, task_id_hex, name, describe_cleaned, category, category_desc, order_type, repeat, task_type_code, file_path FROM tasks WHERE task_id = ?;
SELECT sub_id, sub_id_hex, task_id, name, describe_cleaned, file_path, dialog_npc_id, dialog_npc_name FROM subtasks WHERE task_id = ? ORDER BY sub_id;
SELECT id, sub_id, step_index, instruction, target_function, target_params FROM steps WHERE sub_id = ? ORDER BY step_index, id;
SELECT id, sub_id, phase, cleaned_text FROM dialogues WHERE sub_id = ? ORDER BY id;
```

Packet lưu query nguyên văn tại `provenance.query_templates` và full result tại `tasks[task_id=…].subtasks[sub_id=…]`. Validator tái kiểm task/subtask/step ownership; planning statement vẫn phải ghi decision IDs và không được đổi nhãn thành game fact.

## Cách đọc matrix

- `candidate_id` không phải chapter number và thứ tự ID không phải chronology tuyệt đối.
- `movement_id` là nhóm chức năng M1–M5, không phải act cứng.
- `primary_pov` chỉ có một chủ thể; `SATELLITE_CANDIDATE` cần duyệt riêng theo LWCQ-02.
- `entry_state`/`exit_state` là planning state, không phải câu văn canon.
- `source_nodes` chỉ chứng minh proposition nguồn; việc giao nó cho một POV nằm ở `bridge_decisions`.
- `protected_unknowns` là hàng rào fail-closed, không phải TODO được phép tự điền.

## Density inference — không phải khóa số chương

Matrix hiện có **25 function mặc định đã duyệt**: 8 Tĩnh Xuyên, 11 Tiêu Phùng và 6 Hạ Nương. `V1-CAND-020` là một **satellite record deferred** cho Lục Trầm Châu, được giữ để bảo toàn audit trail nhưng không thuộc dải chương mặc định.

| Chỉ báo | Dải suy ra | Điều kiện |
| --- | --- | --- |
| Minimum viable | 23–24 | Chỉ đạt nếu gộp một số cặp cùng POV/cùng causal function mà không làm mất tri thức, agency hoặc hai cao trào độc lập; không dùng satellite deferred. |
| Recommended | 25–28 | Giữ 25 function mặc định; cho phép tách tối đa ba row `HEAVY`. V1-CAND-020 không nằm trong architecture mặc định. |
| Overflow risk | Trên 28 | Có nguy cơ kể tuần tự gameplay, lặp briefing/relay hoặc biến living lore thành filler; phải chứng minh causal return cho mỗi phần tăng thêm. |

Đây là `recommended count band`, không phải target, cam kết hay số chương chính thức. 3-1-1 chỉ được dùng như heuristic kiểm nghẹt; nó không làm thay đổi dải bằng phép nhân quota.

## Invariant không thương lượng

- `PHYSICAL_CONVERGENCE_VOLUME_I = NONE`.
- `DU_LONG_OBJECTIVE_CUSTODY = UNRESOLVED`.
- `HUYEN_NGUYET_MECHANISM = DEFERRED`.
- Lục Trầm Châu tự đấu Thôi Xuất Trần; việc Cái Bang giữ ông sống là hành động ngoài màn không nêu người/cách cứu trong Quyển I.
- Tiêu Phùng không nhận tiền sử Thiên Vương, chiến công Lục–Thôi hoặc toàn bộ việc avatar.
- T4/S28–S37 và Ân Đồng không phải content pool Quyển I. Future canon vẫn tuyệt đối: Tĩnh Xuyên/Mộc Nhất Lâu tự tay hạ sát Ân Đồng, rồi mới biết nàng sẽ không tiết lộ; hung khí và chronology chi tiết tiếp tục để mở.
- Reader knowledge không tự trở thành tri thức của trio.

## Quyền bước kế tiếp

[Validation report](validation-report.md) lưu quyết định `V1CAQ-01–06`. [Chapter Plan Quyển I](../chapter-plan-volume-i/README.md) sau đó đã được duyệt qua V1CBQ-01–06 (R-53–R-58 / D-032). [Scene-plan phase spec](../scene-plan-phase-spec-volume-i.md) đã được duyệt qua SPQ-01–06 (R-59–R-64 / D-033), mở candidate implementation; mọi scene vẫn chờ V1SPAQ và prose, chronology tuyệt đối, kết quả open slot, route Quyển II–V, canon promotion còn đóng.
