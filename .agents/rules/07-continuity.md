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
3. **Khí tài & Không gian**: Ghi nhận tình trạng vật lý, người giữ, vị trí vào `worldbuilding/artifacts/artifacts_ledger.md` và mốc thời gian vào `plot/timeline.md`.
4. **Hạt giống cốt truyện & Giao ca**: Cập nhật tiến độ `plot/promises_tracker.md` (Planted, Advanced, Paid off) và ghi nhận vào `author/session-state.md`.

Multi-POV Continuity & Synchronization Mandates:
1. **Spatiotemporal Distance & Information Propagation Delay**:
   - The world map is governed by physical reality in 1191 (Southern Song dynasty).
   - Before drafting or approving interactions across locations, verify travel times and courier speeds in `worldbuilding/geography/travel_matrix.md`.
   - Strictly prohibit parallel POV characters from knowing or reacting to events occurring simultaneously in distant regions without the physically necessary transit delay.
2. **Character Epistemic Boundaries (Knowledge State Ledger)**:
   - Characters only know what their senses, personal history, and immediate environment provide, as documented in their character sheet (`characters/<character>.md`).
   - Strictly prohibit characters from possessing knowledge of secret origins, far-off events, or conspiratorial connections before their explicit in-world discovery point.
   - Any revelation must occur through concrete in-world artifacts, direct dialogue, or witness experience anchored in canonical source data.
3. **Intentional Exceptions**:
   - Flashbacks, mentions, and posthumous references must be clearly tagged and anchored in concrete memory or dialogue rather than ambiguous narrative exposition.


