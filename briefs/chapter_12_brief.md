# Chapter Brief

## Chapter

- Number: 12
- Working title: **Bầu Rượu Biệt Ly**
- POV: **Tiêu Phùng**
- POV chronological age (aligned with `plot/chronology_matrix.md`): **17 tuổi**
- Exact calendar date (aligned with `plot/timeline.md`): **1191-08-23, rạng sáng đến sáng sớm**
- Delta T from last appearance: **khoảng 2 ngày sau khi Chương 09 kết thúc vào rạng sáng 1191-08-21**
- Primary location: **Bến Cỏ Lau / bãi sậy Giang Tân, Ba Lăng Huyện**
- Arc(s): **Arc 00 → mở hành trình Cái Bang; Road Vignette / Character Transition**

## Reliability v2 evidence / claim contract

- Evidence Packet: `research/evidence/chapter_12.json`
- Claim Ledger: `research/claims/chapter_12.json`
- Source guard before drafting: `python scripts/claim-guard.py --chapter 12`

### Source facts allowed as `DIRECT_SOURCE`

1. `Task 157 / Subtask 307`: ngày Tiêu Phùng dấn thân vào giang hồ đang đến gần; Điềm Tửu Thúc nằm trong chuỗi chuẩn bị xuất hành.
2. `Task 157 / Subtask 309`: Điềm Tửu Thúc trực tiếp nói **“đã đến lúc ngươi đi rèn luyện rồi.”**
3. `Task 157 / Subtask 310`: Bạch Thu Lâm cho Tiêu Phùng tìm hiểu **thập nhị môn phái** và chọn nơi muốn gia nhập; raw source không khóa riêng Cái Bang trong row này.
4. `Task 2 / Subtask 9`: Cái Bang, Thạch Hiên Viên và Yến Tử Ổ là tuyến source có thật.

### Novel-canon / adaptation boundary

- **Bạch Thu Lâm gửi Tiêu Phùng sang Cái Bang Yến Tử Ổ bằng thư tiến cử**: giữ nguyên như **author-approved `ADAPTATION_DECISION`** từ `revisions/chapter_09_canon_diff.md`; tuyệt đối không gọi đây là `DIRECT_SOURCE` của Task 157.
- **Bầu rượu tiễn chân từ Điềm Tửu Thúc**: raw source hiện chưa chứng minh sự kiện tặng bầu rượu. Current working-tree state đã ghi Tiêu Phùng đang mang một `Bầu rượu nếp đầm lau`; để tránh sinh vật phẩm trùng, brief đề xuất Điềm Tửu **châm đầy / thay nút / siết lại dây của chính bầu rượu đang có**, biến vật cũ thành vật tiễn chân. Đây là **`ADAPTATION_DECISION` mới, chờ Tác giả duyệt ở Hard Stop 1**.
- Roadmap cũ ghi `Task 0: Subtask 130` và `Task 157: Subtask 133` cho Chương 12. SQLite xác nhận `sub_id 130` và `133` đều thuộc **Task 19 — Âm Sai Dương Thác**, tuyến Cửu Nghi Khê / Du Long Giác, nên **không được dùng làm provenance cho Chương 12**.

## Temporal continuity verification

- Calendar date alignment: Chương 09 kết thúc rạng sáng 1191-08-21; Chương 12 mở 1191-08-23, cho Tiêu Phùng khoảng hai ngày được nẹp lại và theo dõi sau tái chấn thương.
- Age consistency check: Tiêu Phùng sinh 1174 → **17 tuổi**; Bạch Thu Lâm sinh 1167 → **24 tuổi**.
- Transition requirement (if $\Delta T \ge 3$ days): Không cần transition montage dài; delta dưới 3 ngày. Có thể mở bằng dấu hiệu hai ngày nằm yên: thuốc đắng, nẹp ngực, đồ hành trang được xếp sẵn.
- Travel latency check (`worldbuilding/geography/travel_matrix.md`): Động Đình → Yến Tử Ổ/Tô Châu khoảng **1.800–2.000 dặm**, thuyền buồm xuôi dòng **12–15 ngày**. Chương này chỉ **rời bến**, tuyệt đối không cho Tiêu Phùng tới Yến Tử Ổ trong cùng ngày/chương.
- Injury continuity: `INJ-TP-002` vẫn là **L3**. Tiêu Phùng phải thở nông, đau khi xoay thân/cười/ho, không chạy nhảy, phi thân, vận kình hay mang vác. Xuất hành bằng thuyền chậm là điều kiện bắt buộc để hành trình khả thi.

## NPC Pedigree & Biological Age Verification (Mandatory Gate 1 Check)

| NPC Name | Provenance (Task/Subtask/SQLite) | Role & Kinship (`genealogy_matrix.md`) | Birth Year & Age (1191) | Biological Age Check ($\text{Age}_{\text{parent}} \ge \text{Age}_{\text{child}} + 16$) | Generational Addressing (POV <-> NPC, NPC <-> NPC) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Bạch Thu Lâm (Thu Di)** | `Task 157 / Subtask 310`; novel-canon genealogy cross-check | Nghĩa tỷ kiêm người bảo hộ Tiêu Phùng; con Bạch Phụ | **1167 / 24 tuổi** | N/A — không phải quan hệ cha/mẹ với Tiêu Phùng | Tiêu Phùng gọi **Thu Di / Tỷ**; quan hệ **Tỷ — Đệ** |
| **Điềm Tửu Thúc** | `Task 157 / Subtasks 307, 309`; `characters/supporting_cast.md` | Thợ rèn/chủ tiệm binh khí; tiền bối nghĩa quân, ân sư không chính thức | **~48–50 tuổi theo novel canon; raw-source birth year unresolved** | N/A | Tiêu Phùng gọi **Điềm thúc**; Điềm Tửu gọi thiếu niên bằng khẩu khí tiền bối/thúc phụ |

## Purpose

Biến quyết định “phải rời Ba Lăng” từ thông tin cuối Chương 09 thành **một hành động không thể đảo ngược**: Tiêu Phùng thật sự bước lên thuyền, rời bãi sậy tuổi thơ để tiến vào đại giang hồ.

Chương phải làm ba việc, không hơn:

1. Khép vòng đời thiếu niên Giang Tân bằng một cảnh biệt ly nhỏ, cụ thể, không diễn văn.
2. Cho quan hệ Tiêu Phùng ↔ Điềm Tửu Thúc và Tiêu Phùng ↔ Thu Di có payoff bằng **hành động**, không bằng narrator giải thích tình cảm.
3. Đặt Tiêu Phùng lên tuyến vật lý hợp lý hướng tới Cái Bang, vẫn mang thương L3 và phải chịu 12–15 ngày đường thủy.

## Starting state

- character: Tiêu Phùng 17 tuổi; vừa tái chấn thương xương sườn L3 ở Chương 09; tinh thần muốn đi nhưng thân thể chưa lành.
- relationship: Thu Di đã quyết định gửi chàng đi vì Ba Lăng không còn an toàn; Điềm Tửu Thúc là tiền bối quen chửi mắng nhưng đã nhiều lần chuẩn bị chàng cho giang hồ.
- knowledge: Tiêu Phùng biết mình phải sang Cái Bang Yến Tử Ổ theo **novel canon đã duyệt**; không được biết thêm bí mật mới về Du Long Giác, Trụ Thần Thạch, Hạ Nương hoặc Tĩnh Xuyên.
- object/location: phong thư tiến cử đã ở trong hành trang; current working-tree state ghi một bầu rượu nếp đầm lau đã mang bên hông.
- threat/stakes: Ba Lăng không còn an toàn; nhưng mối nguy của chương là **rời nhà khi thân thể còn đau**, không phải thêm một trận phục kích mới.

## Ending state

- character: Tiêu Phùng đã lên thuyền và rời bến; vẫn đau, vẫn bị giới hạn vận động; không có power-up.
- relationship: Điềm Tửu và Thu Di đều để chàng đi bằng những cử chỉ thực dụng, không nói hộ cảm xúc cho độc giả.
- knowledge: không tăng lore bí mật; chỉ củng cố việc hành trình sẽ dài và gian nan.
- object/location: thư tiến cử vẫn niêm kín; **nếu Tác giả duyệt CL-12-006**, bầu rượu hiện có được Điềm Tửu châm đầy/thay nút/siết dây, không tạo bầu thứ hai.
- threat/stakes: Ba Lăng lùi lại phía sau; rủi ro tiếp theo là quãng đường thủy 12–15 ngày và thân thể L3 chưa hồi phục.

## Scene sequence

1. **Lò rèn trước bình minh — “Không cúi xuống được”**  
   - goal: Tiêu Phùng tự chuẩn bị hành trang như thể mình hoàn toàn khỏe.  
   - conflict: nẹp sườn khiến chàng không cúi buộc dây/nhấc đồ như ý; Điềm Tửu nhìn thấy nhưng không hỏi han kiểu ủy mị.  
   - turn: Điềm Tửu giật món đồ khỏi tay, vừa chửi vừa sửa dây đeo/nút bầu rượu.  
   - outcome: comedy đến từ hành động và khẩu khí; narrator **không giải thích vì sao buồn/cười**.

2. **Bầu rượu cũ — payoff bằng thao tác**  
   - goal: Tiêu Phùng định nói lời cảm ơn nhưng né bằng một câu bắng nhắng.  
   - conflict: Điềm Tửu không cho chàng diễn thuyết.  
   - turn: **nếu CL-12-006 được duyệt**, ông châm đầy/thay nút/siết dây cho chính bầu rượu đang có rồi ném/trả lại, dặn một câu ngắn mang tính thực dụng hơn là “di ngôn”.  
   - outcome: vật cũ đổi nghĩa mà không sinh artifact mới và không giả làm source fact.

3. **Bến Cỏ Lau — Thu Di kiểm hành trang**  
   - goal: Thu Di chắc chắn Tiêu Phùng lên đường mà không tự làm nặng thêm thương tích.  
   - conflict: chàng muốn tự bước qua ván cầu nhanh để chứng minh mình ổn; cơn đau cắt ngang.  
   - turn: Thu Di chỉ chỉnh lại dây nẹp / nhét thư sâu hơn vào áo / đẩy hành lý sang tay người thuyền, không nói bài diễn văn “ta lo cho đệ”.  
   - outcome: thư vẫn niêm kín; destination Cái Bang là novel canon đã duyệt, không được kể thành “Task 157 nói vậy”.

4. **Thuyền tách bến — không ngoái đầu kiểu trailer**  
   - goal: hoàn tất hành động xuất sơn.  
   - conflict: bãi sậy, lò rèn, tiếng người quen vẫn ngay sau lưng; cơ thể đau khiến mọi tư thế ngồi đều khó chịu.  
   - turn: một chi tiết nhỏ từ bầu rượu / mùi khói lò / tiếng búa xa dần thay cho độc thoại giải nghĩa tuổi thơ.  
   - outcome: thuyền nhập dòng; Ba Lăng nhỏ dần; chapter kết bằng hình ảnh/vật lý, không narrator tuyên bố “từ đây vận mệnh đổi thay”.

## Information movement

### Reader learns

- Điềm Tửu đã chuẩn bị Tiêu Phùng cho ngày này từ trước, phù hợp source 307/309.
- Hành trình tới Yến Tử Ổ không phải “dịch chuyển scene”: còn 12–15 ngày đường thủy.
- Tiêu Phùng rời Ba Lăng khi vẫn mang hậu quả thể chất thật của Chương 09.

### POV character learns

- Không có bí mật cốt truyện mới.
- Chỉ cảm nhận thực tế rằng “đi giang hồ” không giống câu nói hào hùng khi phải bước lên thuyền với xương sườn đang nẹp.

### POV character must NOT learn yet

- Vị trí hiện tại của Du Long Giác.
- Hạ Nương / biến cố Bách Hoa Cốc.
- Tĩnh Xuyên / biến cố Thanh Loa Đảo.
- Bất kỳ thông tin mới nào về chủ mưu Ma Y Cốc hoặc Trụ Thần Thạch ngoài tri thức đã canon hóa.

## Promises / questions

- planted: quãng đường tới Yến Tử Ổ và thử thách sống xa Ba Lăng.
- advanced: tuyến Cái Bang / Thạch Hiên Viên đã mở từ quyết định cuối Chương 09.
- paid off: lời source “ngày dấn thân vào giang hồ ngày càng gần” và “đã đến lúc ngươi đi rèn luyện rồi” được chuyển thành hành động rời bến.
- opened: Tiêu Phùng sẽ được Cái Bang nhìn nhận thế nào khi mang thư tiến cử nhưng đang thương L3?
- partially answered: ý nghĩa của việc “xuất sơn” với Tiêu Phùng.
- resolved: giai đoạn ở nhà chờ ngày lên đường.

## Continuity risks

- **RISK-1 — stale roadmap provenance:** `Task 0/Sub 130` + `Task 157/Sub 133` là sai. Cấm copy lại vào frontmatter/prose/review.
- **RISK-2 — stale existing metadata:** một số ledger/timeline legacy còn ghi `Task 157/Subtask 133` cho Điềm Tửu; không dùng metadata cũ đó làm source authority. Việc sửa durable metadata sẽ là một provenance-repair changeset riêng, không trộn lẫn vào author brief.
- **RISK-3 — duplicate gourd:** current state đã có bầu rượu. Không được cho Điềm Tửu “tặng một bầu mới” nếu chưa giải thích vật cũ.
- **RISK-4 — instant healing:** Chương 12 không có đánh nhau, phi thân, chạy bến, tự vác rương hay “đau một chút rồi thôi”.
- **RISK-5 — travel teleport:** không tới Yến Tử Ổ trong chapter; chỉ rời Ba Lăng.
- **RISK-6 — source/canon conflation:** Cái Bang recommendation route là novel-canon adaptation đã duyệt; raw source 310 chỉ cho lựa chọn 12 môn phái.

## Forbidden changes

- Không viết `chapters/chapter_12.md` trước khi checkbox Hard Stop 1 được Tác giả duyệt.
- Không tạo trận phục kích mới để “cho chapter có action”.
- Không tạo võ công mới, power-up hoặc khỏi thương nhanh.
- Không thêm bí mật Du Long Giác / Trụ Thần Thạch / Ma Y Cốc.
- Không tạo bầu rượu thứ hai nếu current state vẫn giữ bầu cũ.
- Không biến Điềm Tửu thành người diễn thuyết triết lý dài dòng.
- Không để narrator giải thích punchline hoặc tuyên bố ý nghĩa của cảnh biệt ly.
- Không gắn `DIRECT_SOURCE` cho thư tiến cử Cái Bang hoặc bầu rượu tiễn chân.

## Author approval

- [ ] plan approved
