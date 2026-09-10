> Current temporal/creative authority: migration/restructure_2026_09/temporal-continuity-contract.md and migration/restructure_2026_09/temporal-character-framework.md (D-064/R-90 and D-065/R-91). Read both before chapter operations.
> `canon-registry/` is initialized empty under D-067/R-93. It is a provenance locator, not source authority; every row requires its raw receipt/decision before use.

# Novel OS — Agent Contract

This repository is a long-form fiction project. Follow this contract before any creative task.

## Authority

- The author is the final authority on canon and creative direction.
- You may propose, draft, analyze, review, and recommend.
- Never silently canonize, retcon, delete established canon, or resurrect rejected ideas.

## Source of truth

- Repository story files beat chat memory, latent memory, summaries, and assumptions.
- Story Skills canonical paths are authoritative for structured story state.
- `author/` contains author-level constraints and decisions.
- `research/` is not canon until the author promotes a fact into canonical story files.
- `rejected/` is excluded from normal inspiration and must not be reused unless explicitly requested.

## External source adaptation mode

When the project begins from an existing external narrative corpus — game databases, quest/task scripts, branching dialogue, screenplay material, wiki/lore exports, legacy story bibles, or similar source systems — **do not immediately initialize or populate Story Skills from raw source rows**.

Route first through the Source Adaptation Pipeline:

1. Read `.agents/rules/09-source-adaptation.md`.
2. Read `docs/playbooks/external-source-ingestion.md`.
3. If the source is a game database, also read `docs/playbooks/game-database-novelization.md`.
4. If the source contains mutually exclusive routes/flags/conditional dialogue, also read `docs/playbooks/branching-narrative-migration.md`.
5. Inventory and preserve source provenance.
6. Reconstruct source entities, chronology, branches, flags, dialogue provenance and outcomes before adapting them.
7. Keep `DIRECT SOURCE`, `SOURCE-SUPPORTED INFERENCE`, adaptation decisions and `NOVELIZATION BRIDGE` material distinct.
8. Obtain author approval for the adaptation contract before Story Skills canon promotion.
9. Promote only novel-relevant approved state; raw source databases are evidence, not a second canon database.

Core principle:

> Preserve the source before interpreting it. Reconstruct before adapting. Adapt before canonizing.

Reusable templates live in `templates/migration/`; prompts live in `prompts/migration/`; worked examples live in `examples/migrations/`.

## Before planning or drafting

1. Read the relevant author constraints.
2. Read `story.md` and only the story-state files relevant to the task.
3. Run deterministic checks when a story has been initialized.
4. Use minimum sufficient context; do not load the full manuscript by default.
5. If required canon is missing, flag the gap instead of inventing a durable fact.

## Drafting boundary

The writer may invent wording, gesture, micro-action, sensory realization, and dialogue execution inside an approved scene plan.

The writer may not silently change plot outcomes, established knowledge, world rules, timeline, relationship trajectory, or durable object/character state.

## Review boundary

Review before rewriting. Return issue severity, location, problem, why it matters, evidence, and recommended intervention. Do not regenerate a whole chapter to fix a local issue unless the author requests it.

## Canonization

After an approved revision, prepare a canon diff. Apply only author-approved state changes, then run validation/links/continuity checks again.

For external-source adaptations, canonization also requires consistency with the approved adaptation contract. If a new prose need conflicts with the source contract, stop and present the departure before changing canon.

## Git

Do not create commits unless asked or unless the current task explicitly includes the accepted lifecycle commit. Prefer semantic commit prefixes: `plan:`, `draft:`, `revise:`, `canon:`, `research:`, `style:`.

## Skills

For the 2026-09 restructure, Antigravity chapter operations use `.agents/workflows/dlg-*.md` and the four `dlg-source-*` skills. Read `docs/playbooks/gemini-evidence-review.md` for source-backed draft review and current authority routing. These commands do not grant prose/canon approval. Reviewer must inventory claims from the current full manuscript before trusting the writer's ledger or verdict.

Use Story Skills for story-state operations and deterministic maintenance. Use selected craft skills for diagnosis/craft. Avoid `story-zoom` persistence in v1 because Story Skills already owns continuity state.

## Next recommended agent — usage-aware handoff

- Cuối mỗi phản hồi bàn giao công việc trong repo, thêm một dòng theo mẫu:
  `Next recommended agent: P0 <model> / <reasoning> | P1 <model> / <reasoning> | P2 <model> / <reasoning> — <bước tiếp theo và lý do lựa chọn ngắn gọn>.`
- Chọn theo **bước tiếp theo cụ thể**, ưu tiên model và mức reasoning thấp nhất đủ năng lực. P0 là lựa chọn chính; P1 rồi P2 là phương án thay thế khi model trước không khả dụng hoặc hết usage. Đây là khuyến nghị, không tự chuyển model, tạo task hay chạy thêm agent.
- Ưu tiên các model tác giả dùng: GPT-5.6 Luna, GPT-5.6 Terra, GPT-5.6 Sol, GPT-6 Astra và Gemini hiện hành. Các mức trong bảng là điểm khởi đầu theo phán đoán công việc, không phải benchmark hay cam kết tiết kiệm quota.

| Bước tiếp theo | P0 | P1 | P2 |
| --- | --- | --- | --- |
| Sửa tài liệu nhỏ, chạy kiểm tra có sẵn, trích xuất theo truy vấn đã xác định | GPT-5.6 Luna / low | Gemini 3.5 Flash-Lite / low | GPT-5.6 Terra / low |
| Khảo sát một phần nguồn, đối soát provenance, chỉnh công cụ phạm vi rõ | GPT-5.6 Terra / medium | Gemini 3.8 Flash / medium | GPT-5.6 Sol / medium |
| Tổng hợp liên Arc, phân tích nhánh/tri thức, spec tái cấu trúc, review fact khó | GPT-5.6 Sol / high | Gemini 3.1 Pro Preview / high | GPT-6 Astra / medium |
| Draft/revise theo brief đã duyệt, cần giữ khẩu khí và continuity | GPT-5.6 Sol / medium | Gemini 3.1 Pro Preview / medium | GPT-6 Astra / medium |
| Nút thắt nhân quả hoặc mâu thuẫn phức tạp chưa giải được bằng evidence và các lượt trước | GPT-6 Astra / high | GPT-5.6 Sol / high | Gemini 3.1 Pro Preview / high |

- Điều chỉnh thứ tự theo model thực sự có trong ứng dụng và phản hồi chất lượng của tác giả. Khi quota có thể dùng chung trong cùng nhà cung cấp, ưu tiên phương án khác nhà cung cấp; không khẳng định đổi model sẽ có quota mới.
- Mặc định dùng `low` hoặc `medium`; dùng `high` khi có nhu cầu suy luận cụ thể. Chỉ đề xuất `xhigh`, `max`, `ultra` khi môi trường hỗ trợ và có lý do rõ ràng từ độ khó hoặc lần thử trước; không dùng chỉ vì corpus dài.
- Gemini dùng đúng mức thinking mà phiên bản và ứng dụng hỗ trợ. Không gán máy móc `xhigh/max/ultra` của Codex sang Gemini. Nếu ứng dụng không cho chỉnh thinking, ghi `mặc định của ứng dụng`.
- Tiết kiệm usage bằng evidence packet vừa đủ, truy vấn có mục tiêu, tái dùng kết quả đã kiểm chứng và kiểm tra tất định. Không cắt giảm độ phủ khảo sát, bỏ đọc steps, thay evidence bằng tóm tắt hoặc bỏ cổng duyệt để tiết kiệm.
- Danh mục tham chiếu được kiểm tra ngày **2026-09-08**: [OpenAI models](https://developers.openai.com/api/docs/models/all), [OpenAI model comparison](https://developers.openai.com/api/docs/models/compare), [Gemini models](https://ai.google.dev/gemini-api/docs/models), [Gemini thinking](https://ai.google.dev/gemini-api/docs/thinking). Khả dụng qua API không chứng minh tài khoản Codex/Antigravity có model đó. Kiểm tra lại khi cần thay phiên bản hoặc khi giao diện khác danh mục; không gọi một snapshot cũ là danh sách hiện hành đã xác minh.
