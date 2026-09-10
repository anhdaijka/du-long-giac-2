# Quyển II — source-window coverage ledger

Trạng thái: `CANDIDATE / EVIDENCE SAFETY ONLY / NOT CHAPTER COVERAGE / NOT CANON`.

## Vì sao chưa có chapter ledger

Quyển II chưa có chapter architecture hay bounded briefs được Tác giả duyệt. Một “coverage ledger theo chapter” bây giờ sẽ buộc agent bịa chapter number, POV, state hoặc causal exit. Ledger này chỉ là lớp tương đương ở cấp source-window: nó khóa cách Gemini được đọc evidence trước khi author-approved chapter map tồn tại.

## Receipt và default-deny

Gemini dùng y hệt receipt và `PF-FACT-01` đến `PF-BRANCH-07` của [coverage ledger Quyển I](../writer-preflight-volume-i/volume-i-coverage-ledger.md), với thay đổi duy nhất: `chapter_key` bắt buộc là `V2-SW-*`, không được tự đẻ `V2-CH-*`.

| Window | Query/result receipt tối thiểu | Fact scope có thể kiểm tra | Mandatory label | Escalate nếu cần |
| --- | --- | --- | --- | --- |
| V2-SW-01 | `arc_04.json`, task/subtask 76/225, 77/226, 78/227 | Chỉ từng local task đúng result. | `DIRECT SOURCE` hoặc `GAMEPLAY TRANSLATION CANDIDATE` | Causal return, POV, merge ba local task, combat outcome. |
| V2-SW-02 | `arc_04.json`, 93/242 | Lời Nhạn Xảo Vân/chưởng môn và dấu hiệu được source nêu. | `SOURCE REPORT` | Identity, faction, motive, truth of surveillance/martial knowledge. |
| V2-SW-03 | `arc_04.json`, 96/245,100/249,103/252,106/255,110/259 | Từng witness report/event scope, không across-task synthesis. | `SOURCE REPORT` / `GAME EVENT` theo proposition | Historical/political truth, common chronology, claim that one organization controls all events. |
| V2-SW-04 | `arc_05.json`, 146/295 | Bạch Thu Lâm's stated report; task action against named game groups. | `SOURCE REPORT + GAME EVENT` | Tiêu participation, Diêm Bang motive/network, outcome beyond result. |
| V2-SW-05 | `arc_05.json`, 150/299 | Bạch Thu Lâm/Lôi Lão Cửu report and task-local encounter. | `SOURCE REPORT + GAME EVENT` | Common organization with SW-04, scouting truth, violence/outcome detail. |
| V2-SW-06 | `arc_07.json`, 197/360,202/365 | Người kể và content scoped as memory/hearsay. | `SOURCE REPORT` / `LEGENDARY LORE` | Historical fact, definitive death, new legendary character/profile. |
| V2-SW-07 | `arc_07.json`, 203–214/366–389 | Faction/tutorial UI facts only if a future request isolates a row. | `GAMEPLAY/BRANCH` | All linear narrative use; default `ESCALATE QUESTION`. |
| V2-SW-08 | `arc_07.json`, 215/390 | Reputation claim of Bạch Thu Lâm and repeatable-task framing. | `SOURCE REPORT + REPEATABLE` | Specific mission chronology, Bao Vạn Đồng scene/relationship. |
| V2-SW-09 | `arc_07.json`, 225/400 | Source transition reports and organization preparation; game mechanics separately marked. | `DIRECT GAME EVENT + SOURCE REPORT + GAMEPLAY TRANSLATION` | Objective history, exact secrecy/authority, travel/path, resource quantities, assignment to a POV. |
| V2-SW-10/11 | Không có receipt cho toàn family; chỉ T130/S279 và T223/S398 được tách thành `V2-HS-01/02` dưới đây. | Không dùng các row còn lại. | `PARTIALLY SURVEYED` | Bất kỳ use ngoài V2-HS-01/02. |
| V2-HS-01 | `arc_05.json`, 130/279 | Đỗ Tân/giếng/Hàn Diêm trong đúng speaker + task scope. | `SOURCE REPORT + GAMEPLAY TRANSLATION` | Hạ presence, diagnosis/mechanism, outcome, chronology or any complete medical case. |
| V2-HS-02 | `arc_07.json`, 223/398 | Lão Mặc Nhĩ, đồ phổ/kim châm trong đúng task scope. | `DIRECT SOURCE CONTEXT` | Hạ possession/knowledge/use, full medical contents, treatment efficacy or alliance. |

## Required author gates after this ledger

1. **Source-window selection gate:** select which `CHAPTER-READY` windows enter a Volume II architecture; no reservoir/unsurveyed window is automatically selected.
2. **Chapter architecture gate:** decide number/functions/POV and separate state/knowledge boundaries without treating source-window order as chronology.
3. **Chapter preflight gate:** only then create `V2-CH-*` packets with chapter-specific query/result receipts.
4. Existing scene-plan/prose/canon gates remain separate and closed.
