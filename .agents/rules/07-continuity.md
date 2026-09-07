# Rule 07: Continuity & State Persistence Engine

> **Trách nhiệm duy nhất (Single Responsibility)**: Quản lý tính bất biến của không - thời gian, đồng bộ hóa dòng thời gian đa góc nhìn (multi-POV), và lưu trữ trạng thái thế giới bền vững (durable state persistence) sau mỗi chương được phê duyệt.

Preferred deterministic checks:
1. `story validate .`
2. `story links .`
3. `story continuity .`
4. interpret findings
5. propose the smallest repair

Durable State Update Protocol (Sau khi một chương được Author duyệt):
- Cập nhật đồ vật bền vững (durable items, tiền bạc, vũ khí).
- Cập nhật thương tật thể chất & biến chuyển tâm lý.
- Cập nhật sổ cái tri thức nhân vật (`characters/<character>.md` - Epistemic Ledger).
- Cập nhật mốc thời gian và vị trí vật lý trên bản đồ.

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


