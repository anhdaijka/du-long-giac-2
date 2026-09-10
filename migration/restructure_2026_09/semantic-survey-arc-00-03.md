# Semantic source survey — Arc locators 00–03

Status: partial reconstruction only. This document covers Arc locators 00–03; it does not complete the 13-Arc survey, select a novel route, or propose volumes.

## Method and coverage

Each source packet contains every SQLite task, subtask, step and dialogue attached to the task IDs listed by the corresponding Narrative Book file. It is the reading packet for this survey.

| Locator | Packet | Tasks | Subtasks | Steps | Dialogues |
| --- | --- | ---: | ---: | ---: | ---: |
| 00 | `evidence/source-packets/arc_00.json` | 9 | 74 | 397 | 84 |
| 01 | `evidence/source-packets/arc_01.json` | 16 | 99 | 553 | 109 |
| 02 | `evidence/source-packets/arc_02.json` | 24 | 24 | 87 | 65 |
| 03 | `evidence/source-packets/arc_03.json` | 26 | 27 | 72 | 68 |

The labels “Arc 00” through “Arc 03” below denote Narrative Book membership locators. They are not an independently verified chronology, POV assignment, or volume boundary.

## Arc locator 00 — direct-source reconstruction

### Task 1: Thiên Vương Bang cluster

`tasks.task_id=1`, `subtasks.sub_id=1–8`, and their attached steps/dialogue establish this sequence within the task:

1. The player-avatar arrives at Thanh Loa Đảo under Quý Thúc Ban's introduction and Bạch Thu Lâm is named as the sender (`subtask 1`, `dialogues.phase=start`).
2. Dương Thiết Tâm becomes bang chủ after a contest; Cầu Chỉ Thủy is accused of collusion, then remains a disputed case (`subtasks 1–2`).
3. A court guard brings a sealed message; Bùi Dực Phi reports signs of an insider and argues for intervention (`subtask 3`).
4. The player-avatar helps escort Hàn Thác Trụ through attacks attributed in dialogue to Ngũ Độc figures (`subtasks 4–5`).
5. The island is besieged; the player-avatar helps its defense and leaves toward Yến Tử Ổ/Cái Bang (`subtasks 6–8`).

This is a faction and crisis cluster attached to the player-avatar. It does not directly establish that it belongs to Tiêu Phùng, Tĩnh Xuyên, or a pre-existing novel date.

### Task 2: Cái Bang cluster

`tasks.task_id=2`, `subtasks.sub_id=9–24` begins in Cái Bang material and includes La Phong, Thạch Hiên Viên, Lãnh Thu Vân and Ảnh Xã-related items. It contains Cái Bang internal matters, investigation and training-style content. The task-level description refers to Cái Bang reform and political activity, but that description must not be read as an exact sequence of every subtask without its individual steps.

### Tasks 4 and 5: route candidate

`tasks.task_id=4` and `5` have matching 13-subtask structures. The paired subtask names explicitly contain `[Nam]` and `[Nữ]` at corresponding positions: for example `Kế Phản Gián`, `Bí Mật Bảo Đồ`, and `Kết Cục Ly Kỳ` appear as male/female variants. NPC names also differ at parts of the pair, including Ân Đồng versus Ân Phương.

**BR-001 — gender-route candidate:** the SQLite names establish parallel-looking variants. The current export does not expose an authoritative condition/flag that proves their selection rule, so the novel may not place both variants on one protagonist's linear timeline. The later branch matrix must inspect original task XML/condition data before choosing a route policy.

### Tasks 6–9: distinct faction/lore clusters

- Task 6 supplies Tây Hạ/Nhất Phẩm Đường political background and a five-subtask sequence.
- Task 7 supplies Võ Đang material concerning a missing leader, identity/betrayal and later Du Long Giác discussion.
- Task 8 supplies Thiếu Lâm/Hoàng Hà flood and social-displacement material.
- Task 9 supplies Kim/Hoàng Lăng material.

The direct source supports these as available narrative clusters. It does not establish that they occur consecutively after Task 1–2, nor that a single novel protagonist experienced all of them.

### Arc-00 conclusion

The locator's “Tân Thủ Thôn” label is not a sufficient description of its actual task content. The source packet contains at least Thiên Vương, Cái Bang, Ngũ Độc, Tây Hạ, Võ Đang, Thiếu Lâm and Kim clusters, plus a gender-route candidate. It must be treated as a menu of source routes pending graph and branch reconstruction.

## Arc locator 01 — direct-source reconstruction

The 16 listed tasks, `task_id=10–25`, span 99 subtasks. The direct source presents a dense cross-faction web rather than a simple “join a sect” sequence:

- Task 10: Nga My / Ngô Hy / Cừu Tuyết material.
- Task 11: Đường Môn, Đường Nhất Trần, Đường Khuyết and Du Long Giác-related claims in the source's own dialogue.
- Task 12: Thúy Yên material, including `subtask 85` (*La Bàn Định Bảo*) and `subtask 86` (*Du Long Xuất Thế*). The direct dialogue at decimal `sub_id=86` uses “ngọc khí” and Bách Hoa Trận; it is the anchor for source-level Du Long Giác reconstruction.
- Tasks 13–18: Tào Bang, court, Cái Bang, Nghĩa Quân, Thiên Vương and other connected local events.
- Tasks 19–25: explicit pursuit/escort/secret/investigation clusters around Cái Bang, Thiên Vương, Đường Môn, Ngũ Độc, Côn Lôn and Đại Lý.

The source mentions Bạch Thu Lâm in multiple start dialogues, but those mentions alone do not assign every task to Tiêu Phùng or establish a trio chronology. The novel's future parallel-protagonist architecture remains a proposed adaptation choice, not direct source.

### Du Long Giác discipline observed in this locator

The source itself contains competing character assertions and rumors around Du Long Giác. For example, the player-avatar and NPCs use broad phrases about its effects, while `subtask 86` gives an on-site “ngọc khí”/Bách Hoa Trận scene. These are character statements and event evidence with different force. The reconstructed model must preserve speaker, location, and state instead of flattening all statements into a single objective property of the object.

## Arc locator 02 — direct-source reconstruction

Tasks `26–49` are 24 one-subtask tasks. The material is predominantly compact encounters, errands and local stories rather than a demonstrably continuous macro route. It includes:

- Cái Bang and Thanh Loa matters: Tasks 26–36.
- local conflict, competition and commerce: Tasks 37–42.
- Ngũ Độc / forest / Côn Lôn stories: Tasks 43–49.

Examples that can later supply living-world material include the friend under pursuit in Task 27, Hầu Nhi Tửu in Task 29, a missing child/crocodile danger in Task 33, and Mộ Dung Tương Quân's unreciprocated attraction to Điệp Phiêu Phiêu in Task 41. None is assigned to a chapter or a trio POV here.

## Arc locator 03 — direct-source reconstruction

Tasks `50–75` are also mostly one-subtask compact stories. The packet spans snow-cave material, Thiếu Lâm, Võ Đang, Kim court/Hoàng Lăng and Nga My-related content. It therefore cannot yet be called a single uninterrupted Thiên Vương-Đảo crisis from its locator title alone.

The packet includes social and side-story material suitable for later consideration as living lore: a trapped couple in Task 51, a sickness and medical search in Task 55, disciples endangered by mechanisms in Tasks 58–60, and local political/ethical conflicts in Tasks 64–75. Their later dramatic use remains undecided.

## Open reconstruction work from this batch

1. Read original XML or condition-bearing source for BR-001 and every later route candidate.
2. Extract each task's prerequisites/outcomes; current SQLite export does not expose them as explicit relational fields.
3. Establish whether the task ordering represents game progression, faction route, repeatable optional content or a combination.
4. Survey Arc locators 04–12 and all unclassified tasks before any volume proposal.
