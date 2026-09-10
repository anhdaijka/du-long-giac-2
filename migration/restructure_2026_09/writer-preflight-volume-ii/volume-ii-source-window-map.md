# Quyển II — deep survey và chapter-ready source-window map

Trạng thái: `CANDIDATE / AUTHOR REVIEW REQUIRED / SOURCE RECONSTRUCTION ONLY / NOT A CHAPTER PLAN / NOT CANON`.

## Brief và boundary

Macro authority chỉ cho Quyển II ba nhiệm vụ: tin đồn Du Long thành áp lực công cộng; lần gặp vật lý đầu là hợp tác hữu hạn; và Task 225 tạo transition sang Phục Ngưu. Nó **không** cho phép tự phân task thành chapter, gán nhiệm vụ cho trio, tạo chronology, giải custody/cơ chế hoặc biến game alt-history thành lịch sử.

SQLite `story_database.sqlite3` là authority. Mọi row ở đây dùng extraction đã pin SHA `b5c30040c9449f2223cf40bfec9866216423a60a82e2333b5cedb4fb5261bdb0`; query template/result nằm trong `evidence/source-packets/arc_04.json`, `arc_05.json`, `arc_07.json`. Narrative Book không được dùng thay result.

## Quy ước source-window

- `CHAPTER-READY` nghĩa là một đơn vị evidence có thể được **đề xuất** làm input cho chapter architecture sau này; không phải chapter đã được duyệt.
- `RESERVOIR` chỉ là nguồn living wulin có thể được gọi lại khi một chapter đã có causal need.
- `GAMEPLAY/BRANCH` bị loại khỏi linearization mặc định.
- `SOURCE REPORT` là nhân vật/tài liệu trong source nói; không biến thành historical/objective fact nếu thiếu corroboration.
- `UNSURVEYED` không được Gemini trích làm fact, dù title trông hấp dẫn.

## Source windows

| ID | Source container và query/result | Direct source scope đã đọc sâu | Phân loại | Có thể phục vụ Quyển II | Cấm Gemini tự suy |
| --- | --- | --- | --- | --- | --- |
| V2-SW-01 | `arc_04.json` → Tasks 76–78, S225–227; `tasks[76..78].subtasks[225..227]` | Cầu thân, thư/rương của Vô Niệm và xung đột Cừu Tuyết–Kim Tiền Báo là các local event/avatar task khác nhau. | `RESERVOIR / BRANCH-SENSITIVE` | Chỉ làm living-lore/aftermath khi có causal return đã duyệt. | Không gộp ba task thành một biến cố, không gán trio, không biến combat objective thành chronology. |
| V2-SW-02 | `arc_04.json` → Task 93/S242; `tasks[93].subtasks[242]` | Nhạn Xảo Vân báo nhóm người quanh Thúy Yên; dialogue nêu nghi ngờ về người biết công phu Thúy Yên và suy đoán Tát Mãn Giáo. | `SOURCE REPORT / OPEN` | Có thể là pressure/witness quanh Thúy Yên, nếu future chapter cần một report. | Không xác nhận nhóm là do thám, không xác nhận danh tính, phe, mục tiêu hay người đó thực sự biết võ công Thúy Yên. |
| V2-SW-03 | `arc_04.json` → Tasks 96,100,103,106,110; `tasks[*].subtasks[245,249,252,255,259]` | Các vignettes nói về bóc lột khoáng, bắt lính/chuộc người, lộ information bang, Bách quan phổ, và cược giữa quân. | `RESERVOIR / MIXED REPORTS` | World Spine: nhìn giá xã hội của quyền lực, quân doanh và thông tin qua witness/aftermath. | Không ghép thành một chính biến; không gọi mọi lời kể là sử thật; không đặt cùng thời điểm/cùng địa bàn. |
| V2-SW-04 | `arc_05.json` → Task 146/S295; `tasks[146].subtasks[295]` | Bạch Thu Lâm nói Từ Bân Kiếm/Diêm Bang nhiều lần muốn đoạt Du Long; source giao avatar đi dằn mặt bang chúng Diêm Bang/Bắc Mã ở Tiến Cúc Động. | `CHAPTER-READY / SOURCE REPORT + GAME EVENT` | Hook pursuit: pressure quanh nghĩa quân và Du Long. | Không xác nhận toàn bộ động cơ/đường dây Diêm Bang, không gán event cho Tiêu hay biến “dạy dỗ” thành massacre/chiến thắng bền vững. |
| V2-SW-05 | `arc_05.json` → Task 150/S299; `tasks[150].subtasks[299]` | Bạch Thu Lâm nói Từ Bân Kiếm tụ tập người từng tham gia tranh đoạt; Lôi Lão Cửu do thám; source giao avatar tiếp xúc nhóm ở Bang Nguyên Bí Động. | `CHAPTER-READY / SOURCE REPORT + GAME EVENT` | Hook pursuit/rumor, có thể đối chiếu với V2-SW-04 nhưng chưa mặc định cùng event. | Không kết luận đám người là một phe thống nhất, không xác nhận “ý đồ chống nghĩa quân” là objective fact, không gán scouting result ngoài row. |
| V2-SW-06 | `arc_07.json` → Tasks 197,202 / S360,365; `tasks[197,202].subtasks[360,365]` | Long Ngũ/Kiếm Nô kể về Tàng Kiếm, Ngũ Nhạc Sảnh và Độc Cô Kiếm; việc mất tích/chết ở Thái Thạch được kể như ký ức/lời nói “nghe nói”. | `LIVING-LORE / SOURCE REPORT` | Chỉ dùng qua người kể, tư liệu hoặc nghi lễ; có thể mở rộng world depth mà không bắt trio gánh event. | Không phong canon một “Độc Cô” mới, không xác nhận cái chết/trận đánh là historical fact, không bịa di vật/sức mạnh/genealogy. |
| V2-SW-07 | `arc_07.json` → Tasks 203–214 / S366–389 | Tiếp dẫn 12 môn phái, tu luyện châu, đấu trường và reward/tutorial. | `GAMEPLAY/BRANCH — EXCLUDED DEFAULT` | Chỉ một chi tiết tổ chức cụ thể mới có thể được khảo sát lại theo amendment. | Không linearize 12 route, không trao tu luyện châu/danh hiệu/quy tắc UI thành state bền vững của trio. |
| V2-SW-08 | `arc_07.json` → Task 215/S390 | Source giới thiệu reputation Nghĩa quân/Bao Vạn Đồng qua lời Bạch Thu Lâm và một nhiệm vụ lặp 10 lần. | `REPEATABLE / SOURCE REPORT` | Texture reputation, không làm plot event mặc định. | Không biến 10 lượt thành chronology, không suy Bao Vạn Đồng xuất hiện/trực tiếp quen trio. |
| V2-SW-09 | `arc_07.json` → Task 225/S400; `tasks[225].subtasks[400]` | Source kể hậu Thái Tổ Bảo Khố, cảnh giác Kim, lời Bạch Thu Lâm về triều đình/mật chỉ, và việc dựng Phục Ngưu. Objective game task còn có thu thập tài nguyên, teleport, dungeon và combat. | `CHAPTER-READY TRANSITION / MIXED SOURCE` | V2 exit handoff: công chúng/tổ chức chuyển từ tranh bảo sang chuẩn bị chiến tranh. | Không coi toàn bộ lời Bạch Thu Lâm là historical fact, không xác nhận danh tính/authority bằng suy luận, không dùng teleport/resource-count/dungeon route làm tiểu thuyết chronology. |
| V2-SW-10 | `arc_05.json` → Tasks 111–145 / S260–294 | Chỉ T118/S267 và T130/S279 đã deep-read cho gap y chứng; phần còn lại chưa khảo sát proposition-level. | `PARTIALLY SURVEYED — LOCKED EXCEPT V2-HS-01` | `V2-HS-01` chỉ là source-supported medical-context candidate. | Không dùng phần còn lại theo title/task adjacency; T130 không tự map sang Hạ hoặc xác nhận medical mechanism. |
| V2-SW-11 | `arc_07.json` → Tasks 191–196, 198–201, 216–224 / S354–359,361–364,391–399 | Chỉ T223/S398 đã deep-read cho gap y chứng; phần còn lại chưa khảo sát proposition-level. | `PARTIALLY SURVEYED — LOCKED EXCEPT V2-HS-02` | `V2-HS-02` chỉ là source-supported healer-context candidate. | Không lấy danh xưng/mystery title làm nhân vật, event hay timeline; T223 không tự trao đồ phổ/kim châm cho Hạ. |

## Candidate causal map (không phải chronology)

```text
V2-SW-04  Diêm Bang / Du Long pressure (report + action)
      \                         /
       \                       /
        V2-SW-05  Bang Nguyên report + scouting
                  |
                  |  no same-event assumption
                  v
       AUTHOR-SELECTED V2 ARCHITECTURE REQUIRED
                  |
                  v
V2-SW-09  hậu Thái Tổ Bảo Khố -> Phục Ngưu transition
```

`V2-SW-02`, `03`, `06`, `08` chỉ có thể đi vào qua organization action/document/witness/aftermath. `07`, `10`, `11` không tham gia cho đến khi deep-read + author decision.

## Hard stops trước chapter architecture

1. Chưa có evidence nào ở đây chọn cảnh gặp đầu của trio, địa điểm, ai mời ai, duration, dialogue, hay kết quả hợp tác.
2. Du Long objective custody và cơ chế Huyền Nguyệt tiếp tục `OPEN — DO NOT FILL`.
3. Không đồng nhất avatar với Tiêu ở bất kỳ task mới nào ngoài Bridge đã duyệt mà không kiểm tra scope/mapping riêng.
4. Không tạo historical fact từ game alt-history, Long Ngũ/Kiếm Nô/Bạch Thu Lâm report, Bách quan phổ hay lời NPC.
5. Task 225 là explicit source transition ở cấp game narrative, nhưng phần dungeon/teleport/collect-count là gameplay translation candidate, không factual novel sequence.
