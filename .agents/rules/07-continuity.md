> D-064/R-90: Read migration/restructure_2026_09/temporal-continuity-contract.md first. Exact dates, volume ages and travel estimates require evidence/decision; UNKNOWN is valid. Current allocation: migration/restructure_2026_09/series-chapter-allocation-index.md. Canon diffs must name approved state destinations; never write chapter state into policy/index.

# Rule 07: Continuity & State Persistence Engine

> **Trách nhiệm duy nhất (Single Responsibility)**: Quản lý tính bất biến của không - thời gian, đồng bộ hóa dòng thời gian đa góc nhìn (multi-POV), và lưu trữ trạng thái thế giới bền vững (durable state persistence) sau mỗi chương được phê duyệt.

Preferred deterministic checks:
1. `story validate .`
2. `story links .`
3. `story continuity .`
4. interpret findings
5. propose the smallest repair

Mandatory 4-Step State Persistence Protocol (Sau khi Tác giả duyệt Canon Diff):
1. **Nhân vật Chính & Trụ cột**: Cập nhật `characters/<protagonist>.md` và các tệp `characters/anchors/*.md` liên quan (tâm lý, thương tật, sổ cái tri thức Epistemic Ledger).
2. **Nhân vật Phụ trợ (Tier B & C)**: Bổ sung nhân vật mới hoặc cập nhật trạng thái/vết thương vào `characters/supporting_cast.md`.
3. **Khí tài & Không gian**: Đề xuất state vật phẩm/vị trí và checkpoint thời gian vào đúng file state được canon diff chỉ định và Tác giả duyệt. Contract temporal chỉ là policy đọc, không phải nơi ghi sự kiện chương.
4. **Hạt giống cốt truyện & Giao ca**: Cập nhật tiến độ `plot/promises_tracker.md` (Planted, Advanced, Paid off) và ghi nhận vào `author/session-state.md`.

Multi-POV Continuity & Synchronization Mandates:
1. **Spatiotemporal Distance & Information Propagation Delay**:
   - The world map is governed by source-backed geography and approved relative chronology.
   - Follow `migration/restructure_2026_09/temporal-continuity-contract.md`, then verify travel/courier claims against chapter evidence receipts and approved estimates. The contract contains no speed table.
   - Strictly prohibit parallel POV characters from knowing or reacting to events occurring simultaneously in distant regions without the physically necessary transit delay.
2. **Character Epistemic Boundaries (Knowledge State Ledger)**:
   - Characters only know what their senses, personal history, and immediate environment provide, as documented in their character sheet (`characters/<character>.md`).
   - Strictly prohibit characters from possessing knowledge of secret origins, far-off events, or conspiratorial connections before their explicit in-world discovery point.
   - Any revelation must occur through concrete in-world artifacts, direct dialogue, or witness experience anchored in canonical source data.
3. **Intentional Exceptions**:
   - Flashbacks, mentions, and posthumous references must be clearly tagged and anchored in concrete memory or dialogue rather than ambiguous narrative exposition.


