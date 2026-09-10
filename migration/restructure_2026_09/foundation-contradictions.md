# Foundation contradiction register — seed audit

Status: `AQ-01–05 RESOLVED / FC-008 INTERIM HANDLING APPROVED / FC-009 CORE CANON LOCKED / FC-010 RESOLVED BY CAPQ-05 / REMEDIATION IN PROGRESS`. This register records both the evidence conflict and the author's ruling; it does not relabel adaptation decisions as game facts.

## Source probe used

The probe searched the direct game-text fields listed below in the SQLite copy with SHA-256 `b5c30040c9449f2223cf40bfec9866216423a60a82e2333b5cedb4fb5261bdb0`:

- `tasks.describe_cleaned`
- `subtasks.describe_cleaned`
- `steps.instruction`, `steps.target_params`
- `dialogues.cleaned_text`
- `world_ambient_dialogues.cleaned_msg`
- `armycamp_lore.cleaned_text`
- `linktask_tales.cleaned_text`
- `faction_primer_stories.cleaned_text`
- `feature_system_stories.cleaned_text`

The probe did not search source XML outside the SQLite export or external historical sources. A zero hit means only that the phrase was absent from these declared fields.

| ID | Foundation occurrence | SQLite probe | Current handling |
| --- | --- | --- | --- |
| FC-001 | `plot/chronology_matrix.md` assigns Tiêu Phùng a Nam Chiếu royal descent. | `Nam Chiếu`: zero hits across the declared fields. Task 450 instead speaks of Nhạc-family blood. | **Resolved:** reject the Nam Chiếu/Đoàn lineage; adopt Nhạc-family lineage as an author-approved Bridge grounded in Task 450. |
| FC-002 | Multiple ledgers/timeline entries describe Trụ Thần Thạch. | `Trụ Thần Thạch`: zero hits across the declared fields. | **Resolved:** move this mechanism to `rejected/unsupported-foundation/`; no live continuity use. |
| FC-003 | Multiple ledgers/timeline entries assign a magnetic/radiation property to Du Long Giác. | `từ trường`: hits exist, but no audited proposition connects those contexts to Du Long Giác. | **Resolved:** reject the magnetic/radiation mechanism unless proposition-level source is later recovered and separately approved. |
| FC-004 | Timeline/ledgers use “trấn quốc” or “trấn yểm” for Du Long Giác. | Both phrases: zero hits across the declared fields. | **Resolved:** move these claims to `rejected/unsupported-foundation/`; no live continuity use. |
| FC-005 | Timeline uses “Mượn đao đào ngọc / Dẫn xà xuất động”. | Both phrases: zero hits across the declared fields. | **Resolved:** reject as unsupported adaptation machinery. |
| FC-006 | `characters/tieu_phung.md` and `plot/chronology_matrix.md` identify the Task-157 player-avatar as Tiêu Phùng, age 17 in 1191, and give the father a name and Nam Chiếu ancestry. | Task 157 calls the avatar `thiếu chủ`/`Đại Hiệp`, repeatedly uses an 18-year interval, and identifies the father only as a gifted disciple connected to Ma Y Cốc in the inspected rows. | **Resolved:** opening age is 18. Avatar↔Tiêu Phùng and the protective name are Novelization Bridges; the exact opening year/birth year awaits new chronology. |
| FC-007 | The protected Tiêu Phùng profile names Tiêu Lăng Phong as father and gives a Nam Chiếu/Đoàn lineage. | Task 450's `Thân Thế Mộng Cảnh` names the father Minh Dương, the mother Tố Trinh and a Nhạc-family lineage; Task 451 leaves the Huyễn Cảnh's truth status unexplained. | **Resolved:** novel adopts Minh Dương–Tố Trinh–Nhạc family as true backstory while preserving the source reliability label. `Tiêu Lăng Phong` survives only as Lệ Thu Thủy's Bridge-level name for Minh Dương. |
| FC-009 | `characters/anchors/an_dong.md` gọi cái chết ở “mũi thương”; hình tượng chiến đấu của Tĩnh Xuyên cũng ưu tiên trường thương. D-004 cũ ghi nhầm tuyến nam ở Task 5. | Query `SELECT sub_id, sub_id_hex, task_id, name, describe_cleaned, file_path, dialog_npc_id, dialog_npc_name FROM subtasks WHERE task_id = ? ORDER BY sub_id` bind `(4)` trả S36 `Vấn Tâm Nhất Kiếm [Nam]` với câu “kiếm ta đã nhuốm máu Ân Đồng”; S37 xác nhận nàng chết dưới tay người mình yêu. Task 5 là route nữ song song. Full result: `evidence/source-packets/arc_00.json`, `tasks[task_id=4].subtasks[sub_id=36/37]`. | **CDQ-05 approved — core canon locked / implement deferred:** Tĩnh Xuyên–Mộc Nhất Lâu tự tay hạ sát Ân Đồng và gánh trách nhiệm; không tai nạn/người thứ ba/giả chết. Hung khí kiếm hay thương hoãn đến phase Mộc Nhất Lâu và không ảnh hưởng Quyển I. |
| FC-010 | `author/creative-constitution.md` mục 6 từng mô tả công thức 3-1-1, trong đó “khoảng lặng” có tương tác bộ ba; đồng thời dễ bị đọc như chu kỳ năm chương cố định. | Đây không phải mâu thuẫn game fact. R-17/CDI-02 cấm trio gặp trong Quyển I; R-03/R-16 giữ số chương linh hoạt. | **RESOLVED — CAPQ-05:** 3-1-1 là heuristic cấp series, không phải quota; khoảng lặng Quyển I là đơn tuyến/world aftermath và không cho trio gặp sớm. Creative constitution đã được làm rõ theo quyết định này. |

## Source normalization questions

### FC-008 — Huyền Nguyệt mechanism versus the no-fantasy Foundation

- **Foundation:** `author/creative-constitution.md`, section 3.2 forbids xianxia/fantasy mechanics.
- **GAME FACT evidence:** Task 12/subtask 89 `describe_cleaned` describes reflecting moon energy into the formation. Query: `SELECT sub_id, sub_id_hex, task_id, name, describe_cleaned, file_path, dialog_npc_id, dialog_npc_name FROM subtasks WHERE task_id = ? ORDER BY sub_id`, bind `[12]`. Full extracted row and linked step/dialogue results are in `evidence/source-packets/arc_01.json`, `tasks[task_id=12].subtasks[sub_id=89]`; packet provenance stores the remaining query templates and DB identity.
- **Scope:** this is a formation claim, not evidence that Du Long Giác itself powers it. Do not attach it to the artifact by proximity.
- **Current handling:** `INTERIM HANDLING APPROVED / MECHANISM DEFERRED`. On 2026-09-09 the author approved PB-06 / V1PQ-04 (R-30 / D-026): retain the defensive event and formation name while leaving the mechanism unexplained, pending a later fidelity decision before staging its operation. Keep source and Foundation unchanged. No replacement optics, magic or artifact mechanism has been approved; this does not resolve the mechanism conflict itself.

### Other source normalization

| ID | SQLite inconsistency | Current handling |
| --- | --- | --- |
| SQ-001 | Task 92 / subtask 241 uses `Lệ Thu Thủy` in `describe_cleaned` but `Lịch Thu Thủy` in `dialogues.cleaned_text` for the same seventh-generation sect leader. | Do not silently alter the source packet. Use `Lệ Thu Thủy` only as the author/Foundation normalization and retain this discrepancy in provenance. |

## Direct-source anchor already observed

`dialogues.cleaned_text` for decimal subtask `86`, phase `start`, states that Ma Y Thần Tướng identifies an “ngọc khí” and directs the player to Bách Hoa Trận. It does not by itself establish the rejected concepts above. The full event must still be read with its surrounding steps and dialogue before it enters the reconstructed model.
