# Gemini / Antigravity Entry Point

Treat `AGENTS.md` as the repository-level operating contract and `.agents/rules/` as the detailed workspace rules.

Use skills installed under `.agents/skills/` when their descriptions match the task. Story Skills owns structured story state; selected craft skills guide prose/character/scene work.

Core order of operations:

1. repository truth
2. deterministic Story Skills checks
3. narrative reasoning
4. proposal / draft / review
5. author approval
6. state update
7. verification

Never use chat memory as a substitute for repository canon.

Mandatory Rule 0: Kỷ Luật 3 Cổng Dừng Cứng (`docs/WORKFLOW.md`).
- **CỔNG DỪNG 1 (Pre-Draft Hard Stop)**: Soạn thảo `briefs/chapter_XX_brief.md` theo mẫu `templates/chapter-brief.md` $\rightarrow$ **DỪNG LẠI TRÌNH TÁC GIẢ**. CẤM TUYỆT ĐỐI tạo mới hoặc viết bất kỳ dòng nào vào `chapters/chapter_XX.md` khi Tác giả chưa phê duyệt Chapter Brief!
- **CỔNG DỪNG 2 (Pre-Canon Hard Stop)**: Chấp bút draft $\rightarrow$ quét `npm run lint:prose` $\rightarrow$ lập Báo cáo Review `reviews/chapter_XX_review.md` $\rightarrow$ **DỪNG LẠI TRÌNH TÁC GIẢ**. CẤM TUYỆT ĐỐI tự ý coi như đã xong hoặc tự ý canon hóa khi Tác giả chưa duyệt Bản thảo và Báo cáo Review!
- **CỔNG DỪNG 3 (State Commit Hard Stop)**: Lập Đề xuất Canon Diff `revisions/chapter_XX_canon_diff.md` $\rightarrow$ **DỪNG LẠI TRÌNH TÁC GIẢ**. Chỉ khi Tác giả duyệt Diff mới được cập nhật Sổ cái trạng thái bền vững trong `characters/` và timeline.
*Mọi hành vi nhảy cóc viết draft trước rồi hồi tố viết ngược brief/review/diff đều là vi phạm quy trình nghiêm trọng!*

Mandatory Rule 1: Source Provenance Kernel (`.agents/rules/10-provenance-kernel.md`). Tuyệt đối KHÔNG BỊA ĐẶT tình tiết rồi tìm cách hợp lý hóa. 100% các chương (Core Plot, Living Lore, Military Lore, Mystery Lore, Road Novel) bắt buộc phải gắn mã nguồn gốc Task ID, Subtask ID, Camp ID từ SQLite `story_database.sqlite3` trong YAML frontmatter theo hợp đồng `docs/contracts/chapter_contract.md`.

Mandatory Rule 2: Prose Quality Contract (`.agents/rules/11-prose-quality-contract.md`). Mọi bản thảo khi soạn thảo bắt buộc phải thực thi Pure Show Don't Tell, camera hạn tri ngôi thứ ba, loại bỏ sạch 7 nhóm sạn AI và văn luận hiện đại ('đó chính là', 'đây là', 'bánh xe số phận'). Phải vượt qua `npm run lint:prose` với 0 lỗi vi phạm.

Mandatory Rule 3: SOLID 5-Gate Review Runner (`.agents/rules/05-review.md`). Mọi bản thảo trước khi trình duyệt Tác giả bắt buộc phải vượt qua độc lập 5 Cổng duyệt (Gate A: Nguồn gốc & Độ trễ không-thời gian; Gate B: Pacing tự nhiên; Gate C: Tầng võ học & Hơi thở dân sinh; Gate D: Văn phong & Linter; Gate E: Dải từ vàng 4.000 – 4.800 từ).

Mandatory Rule 4: Session Auto-Resume Protocol. Khi bắt đầu một session mới (hoặc nhận tin nhắn đầu tiên): Agent luôn tự động đọc `author/session-state.md` để nắm bắt tức thì việc vừa xong và việc tiếp theo cần làm, chào ngắn gọn 2 câu và đề xuất hành động kế tiếp cho Tác giả. Sau mỗi mốc hoàn thành (draft xong, review xong, tác giả duyệt xong), Agent tự động cập nhật `author/session-state.md` (thuần Markdown, nhẹ nhàng, không SHA, không JSON phức tạp).


