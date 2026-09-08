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
- **CỔNG DỪNG 3 (State Commit Hard Stop)**: Lập Đề xuất Canon Diff `revisions/chapter_XX_canon_diff.md` theo mẫu `templates/canon-diff.md` $\rightarrow$ **DỪNG LẠI TRÌNH TÁC GIẢ**. Bản Diff BẮT BUỘC phải chứa đủ 4 trụ cột: (1) Nhân vật chính/Bản lề (`characters/`), (2) Danh bạ nhân vật phụ Tier B/C (`characters/supporting_cast.md` — bắt buộc cập nhật mọi NPC mới hoặc biến chuyển/thương tật NPC cũ), (3) Sổ cái thế giới (`injuries_ledger.md`, `artifacts_ledger.md`, `relationships_matrix.md`), (4) Dòng thời gian & Lời hứa (`plot/timeline.md`, `promises_tracker.md`, `volume_01_deck.md`). Chỉ khi Tác giả duyệt Diff mới được phép commit vào các sổ cái bền vững này!
*Mọi hành vi nhảy cóc viết draft trước rồi hồi tố viết ngược brief/review/diff hoặc bỏ quên cập nhật supporting_cast.md đều là vi phạm quy trình nghiêm trọng!*

Mandatory Rule 1: Source Provenance Kernel (`.agents/rules/10-provenance-kernel.md`). Tuyệt đối KHÔNG BỊA ĐẶT tình tiết rồi tìm cách hợp lý hóa. 100% các chương (Core Plot, Living Lore, Military Lore, Mystery Lore, Road Novel) bắt buộc phải gắn mã nguồn gốc Task ID, Subtask ID, Camp ID từ SQLite `story_database.sqlite3` trong YAML frontmatter theo hợp đồng `docs/contracts/chapter_contract.md`.

Mandatory Rule 2: Prose Quality Contract (`.agents/rules/11-prose-quality-contract.md`). Mọi bản thảo khi soạn thảo bắt buộc phải thực thi Pure Show Don't Tell, camera hạn tri ngôi thứ ba, loại bỏ sạch 7 nhóm sạn AI và văn luận hiện đại ('đó chính là', 'đây là', 'bánh xe số phận'). Phải vượt qua `npm run lint:prose` với 0 lỗi vi phạm.

Mandatory Rule 3: SOLID 5-Gate Review Runner (`.agents/rules/05-review.md`). Mọi bản thảo trước khi trình duyệt Tác giả bắt buộc phải vượt qua độc lập 5 Cổng duyệt (Gate A: Nguồn gốc & Độ trễ không-thời gian; Gate B: Pacing tự nhiên; Gate C: Tầng võ học & Hơi thở dân sinh; Gate D: Văn phong & Linter; Gate E: Dải từ vàng 4.000 – 4.800 từ).

Mandatory Rule 4: Session Auto-Resume Protocol. Khi bắt đầu một session mới (hoặc nhận tin nhắn đầu tiên): Agent luôn tự động đọc `author/session-state.md` để nắm bắt tức thì việc vừa xong và việc tiếp theo cần làm, chào ngắn gọn 2 câu và đề xuất hành động kế tiếp cho Tác giả. Sau mỗi mốc hoàn thành (draft xong, review xong, tác giả duyệt xong), Agent tự động cập nhật `author/session-state.md` (thuần Markdown, nhẹ nhàng, không SHA, không JSON phức tạp).

Mandatory Rule 5: NPC Pedigree & Biological Age Sanity Protocol (`worldbuilding/factions/genealogy_matrix.md`). Tuyệt đối KHÔNG BỊA ĐẶT tuổi tác, phả hệ hoặc xưng hô của NPC theo cảm tính. Trước khi đưa bất kỳ NPC nào vào Chapter Brief, bắt buộc phải tra cứu SQLite `story_database.sqlite3` và đối soát `genealogy_matrix.md` để xác định cây huyết thống, quan hệ phu thê, con cái và thế hệ bối phận môn phái. Bắt buộc tuân thủ Công thức Tuổi Sinh Học: $\text{Tuổi Cha/Mẹ} \ge \text{Tuổi Con} + 16$. Cấm tuyệt đối đệ tử gọi cựu môn chủ đời trước là "sư tỷ" như bạn lứa. Mọi Chapter Brief thiếu bảng kiểm định này hoặc vi phạm bối phận đều bị Cổng Dừng 1 tự động từ chối!

Mandatory Rule 6: Adversarial Review, Evidence Grounding & Creative Voice Protection Protocol (`worldbuilding/style/author_wuxia_rubric.md`, `.agents/rules/05-review.md`). Cấm tuyệt đối Agent tự review hời hợt, tự khen hoặc đánh giá checklist cơ học thiếu trích dẫn span có số dòng cụ thể. Báo cáo Review tại Cổng Dừng 2 bắt buộc phải áp dụng tư duy Adversarial Red-Team, trích dẫn tối thiểu 4 spans nguyên bản chứng minh: (1) Khẩu khí độc bản nhân vật (bảo vệ cá tính bắng nhắng/tự trào của Tiêu Phùng, kỷ luật sa trường của Tĩnh Xuyên, y lý thực chứng của Hạ Nương; cấm đồng hóa nhân vật thành bản sao Quách Tĩnh nghiêm trang khô cứng), (2) Điểm chạm trào lộng Mo Lei Tau (25%) / Yên hỏa khí dân sinh, (3) Giới hạn sinh học & cản trở thực tế của thương tật theo `injuries_ledger.md`, (4) Dư ba kết chương. Linter và Reviewer chỉ áp dụng kỷ luật Show-Don't-Tell khắt khe lên Lời dẫn (Narrator Text); tuyệt đối cấm bắt bẻ lời thoại nhân vật trong ngoặc kép `“...”`.

Mandatory Rule 7: Reliability Layer v2 (`.agents/rules/12-reliability-layer.md`, `docs/reliability-layer-v2.md`).
- **Current Author Text Wins**: trước khi review/revise/continue/canon-diff phải đọc lại file chapter hiện tại. Current repository text luôn thắng draft/review/chat memory cũ. CẤM rollback hoặc overwrite revision của Tác giả để khớp bản Agent từng sinh.
- **Entity existence ≠ claim grounding**: claim bền vững phải được phân loại `DIRECT_SOURCE`, `SOURCE_SUPPORTED_INFERENCE`, `UNRESOLVED`, `ADAPTATION_DECISION`, hoặc `NOVELIZATION_BRIDGE`; inference/unresolved/bridge không được âm thầm tự nâng thành fact.
- **Source truth ≠ novel canon authority**: một proposition có thể `UNRESOLVED` ở raw game source nhưng đồng thời tồn tại như `ADAPTATION_DECISION` đã được Tác giả duyệt trong novel canon. CẤM xóa/rollback canon đã duyệt chỉ vì raw-source lookup không chứng minh được; ngược lại CẤM gọi adaptation là `DIRECT_SOURCE`.
- **Recorded approval is explicit**: claim đã canon hóa dùng `promotion: author_approved` + `approval_ref` trỏ tới Canon Diff có dòng `[x] Phê chuẩn...`. `author_approved` không được tự khai báo nếu approval ref không pass `claim-guard.py`.
- **Full-Read Review**: review mới phải có `Full-Read Coverage` phủ toàn bộ chapter hiện tại và trích dẫn span `Lx-Ly` nguyên văn; dùng `scripts/review-guard.py`.
- **Verifier-bound completion**: có verifier thì Agent không được tự tuyên bố phase hoàn tất nếu artifact/verifier tương ứng chưa PASS.
- **Execution Manifest cho plan nhiều bước**: với kế hoạch có nhiều deliverable vật chất, dùng `templates/execution-manifest.json` → `execution/<scope>.json`. CẤM tự ghi `status/done/complete`; `scripts/execution-guard.py` tính `COMPLETE/INCOMPLETE/BLOCKED`. Trước khi nói toàn bộ plan đã xong, bắt buộc chạy `npm run execution:complete -- --manifest execution/<scope>.json`; nếu fail thì phải tiếp tục phần thiếu hoặc báo partial, không được thu nhỏ lại scope sau sự thật.
- **Forward-only State Commit Gate**: mọi thay đổi mới trong `characters/`, `worldbuilding/`, hoặc `plot/` phải có Canon Diff `[x]`, current v2 review APPROVED và Evidence/Claim contract pass; CI dùng `scripts/state-commit-guard.py --base <base-ref>`. Nếu chapter cùng changeset đã đổi thì v2 review cũng phải được refresh. Guard này không hồi tố audit legacy state.
- **Không quan liêu hóa manuscript**: cấm thêm chapter SHA, content hash, immutable revision lock, automatic rollback hoặc metadata bắt buộc cho author edit.
