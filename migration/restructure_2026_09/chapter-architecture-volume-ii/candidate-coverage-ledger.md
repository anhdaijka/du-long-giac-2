# Quyển II — V2-CH candidate coverage ledger

Trạng thái: `AUTHOR-DEFAULTED PLANNING / WRITER-FAIL-CLOSED / NOT PROSE / NOT CANON`.

> **Lưu ý hiện hành (D57/R83):** bảy row dưới đây là functional spine đời đầu, không phải chapter allocation đầy đủ. Gemini triển khai theo [baseline 24 chương và provenance ledger mới](../chapter-plan-volume-ii/README.md); chỉ quay lại bảng này để hiểu nguồn gốc kiến trúc.

> Ghi chú hiện hành: bảy row dưới đây là functional spine được lưu để truy vết D-053, không còn là allocation/count của Quyển II. Gemini phải dùng [chapter plan 24 chương](../chapter-plan-volume-ii/README.md) và provenance ledger mới cho triển khai tuần tự.

| Key | Functional use | Receipt / label | Gemini may use | Gemini must not invent | Writer hard stop |
| --- | --- | --- | --- | --- | --- |
| `V2-CH-01` | Relay/aftermath pressure quanh Diêm Bang. | `arc_05.json` T146/S295; `SOURCE REPORT + GAME EVENT`. | Bạch Thu Lâm có report scoped về Từ Bân Kiếm/Diêm Bang và task-local action scope tồn tại. | Avatar = Tiêu; motive/network/truth of report; venue, combat, result, custody. | Sender/recipient, Tiêu's direct involvement, any action or durable outcome. |
| `V2-CH-02` | Relay/aftermath pressure Bang Nguyên và giới hạn an ninh. | `arc_05.json` T150/S299; `SOURCE REPORT + GAME EVENT`. | Bạch Thu Lâm/Lôi Lão Cửu có report scoped và task-local encounter. | Một phe thống nhất với CH-01; scouting truth; Tĩnh action/authority/outcome. | Tĩnh's exact duty, relay, venue, action or any merged plot. |
| `V2-CH-03` | Hạ context: social cost/evidence ceiling. | `arc_05.json` T130/S279; `SOURCE REPORT + GAMEPLAY TRANSLATION`; R-76 Bridge. | Hạ quan sát/đối chiếu/chăm sóc giới hạn quanh pressure cộng đồng. | Diagnosis, Hàn Diêm mechanism, cure, avatar credit, medical-case closure, common time/place with other reports. | Any medical fact, result, named patient relationship, or state change beyond limited care. |
| `V2-CH-04` | Optional living-lore return. | `arc_07.json` T197/S360, T202/S365; `SOURCE REPORT / LEGENDARY LORE`. | A speaker/document may relay a scoped memory/hearsay only. | Historical truth, death/battle certainty, artifact, martial art, genealogy, new legendary character. | Whether it has causal return; any identity/history claim or reader-to-POV handoff. |
| `V2-CH-05` | First limited physical convergence. | R-67/CMQ-01 + R-74 functional Bridge. | Ba POV có thể hợp tác hữu hạn rồi exit non-party, with separate knowledge ceilings. | Who summons whom, venue, chronology, dialogue, combat, custody reveal, outcome, durable relationship. | Every scene implementation detail or change to custody/knowledge/relationship state. |
| `V2-CH-06` | Optional Phục Ngưu healer-context. | `arc_07.json` T223/S398; `DIRECT SOURCE CONTEXT`; R-76 Bridge. | Hạ may hold limited observation/comparison/care context; report can mention Lão Mặc Nhĩ/items in source scope. | Hạ meets/rescues/receives/uses items; medical contents/effect, alliance, timeline, closure. | Direct contact, item possession/use, efficacy, rescue, or any medical resolution. |
| `V2-CH-07` | Organization/document handoff sang Phục Ngưu. | `arc_07.json` T225/S400; `DIRECT GAME EVENT + SOURCE REPORT + GAMEPLAY TRANSLATION`. | Source transition report: hậu Thái Tổ Bảo Khố → preparation pressure. | Historical/objective authority, command, secrecy, path, teleport, dungeon, resource count, combat, trio participation. | Any actor assignment, historical closure, travel/event scene, or outcome beyond transition report. |

## Gemini execution rule

1. Trước khi đưa claim vào prose/draft, Gemini replay query/result packet đúng row và ghi label.
2. `V2-CH-01/02/03/05/07` không tự là five chapters; `04/06` không tự là filler.
3. Nếu row không đủ để dựng scene/draft, Gemini xuất một author question theo cột hard stop, kèm receipt và một Bridge proposal tối thiểu. Nó không bỏ qua row, tự tìm clue lân cận, hay thay fact bằng văn phong.
4. Không có câu trả lời author, Gemini chỉ được tạo noncanon placeholder ghi rõ `OPEN — DO NOT FILL`, không prose thực hiện.
