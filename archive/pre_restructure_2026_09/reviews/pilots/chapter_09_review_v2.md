# Chapter 09 — Reliability Layer v2 Pilot Review

> Pilot artifact only. This does **not** replace `reviews/chapter_09_review.md`, does not edit the manuscript, and does not canonize or de-canonize anything. It evaluates the current `chapters/chapter_09.md` using the v2 contracts.

## 1. Scope

- Manuscript: `chapters/chapter_09.md`
- Review mode: fresh adversarial full-read
- Source packet: `research/evidence/chapter_09.json`
- Claim ledger: `research/claims/chapter_09.json`
- Author-text rule: current manuscript preserved as-is
- Source-verification rule: raw-source support and author-approved novel canon are separate axes; failure of source provenance must not silently erase an approved adaptation decision

## 2. Full-Read Coverage — Bắt Buộc

- `L1-L60` — Read opening recovery scene, medical/injury continuity, Tiêu Phùng–Thẩm Hà Diệp banter, Bạch Thu Lâm entrance, and the setup that sends Tiêu Phùng to Miếu Thần.
- `L61-L120` — Read travel/temple setup, relief supplies, guarded iron chest and sheepskin exposition, prophecy recall, warm comic breathing room, and the transition into the ambush.
- `L121-L180` — Read the full first combat movement: attacker entry, nghĩa quân casualties, Tiêu Phùng's injury-limited decision, fire diversion, chest protection, and renewed rib trauma.
- `L181-L240` — Read rescue/payoff, Bạch Thu Lâm's intervention, treatment aftermath, casualty survival, and forensic staging around the attackers.
- `L241-L300` — Read faction identification, opening of the chest, Vô Danh Mật Tịch / Trụ Thần Thạch / Du Long Giác exposition, threat conclusion, Cái Bang/Yến Tử Ổ departure decision, and closing image.

## 3. Gates

### Gate A: Provenance / Source Discipline
- **Trạng thái**: **FAIL**
- The chapter frontmatter labels its provenance as `Subtask 5–8 (Bảo Vệ Mật Tịch) liên kết Task 157: Subtask 320–323` and marks the result `DIRECT CANON INTEGRATED`.
- The SQLite-backed Evidence Packet verifies that Task 157 is actually **Thân Thế Chi Mê**. Subtasks 320–323 support a different chain: Giới Sơn Tông/mechanism trouble, Bạch Cương being pursued alongside water-mechanism sabotage, strange non-Central-Plains attackers, and scroll fragments used to obtain a prophecy.
- Wider SQLite lookup confirms that **Nhất Phẩm Đường** and **Du Long Giác** are genuine game-source concepts elsewhere, but it does not establish the specific Miếu Thần attacker relation or the asserted Du Long Giác → Trụ Thần Thạch geomagnetic mechanism. Exact searches for `Vô Danh Mật Tịch`, `Thần Thạch`, `Long Cung`, and `thiên thạch` did not yield supporting raw-source hits. The apparent `từ trường` hits were lexical false positives involving the personal name Từ Trường Phúc.
- This does **not** de-canonize the chapter's adaptation. The existing `revisions/chapter_09_canon_diff.md` contains a checked author approval. Accordingly, `CL-09-006` through `CL-09-009` remain unresolved **raw-source assertions**, while `CL-09-010` through `CL-09-012` record the relevant material as author-approved `ADAPTATION_DECISION` novel canon.
- Gate A therefore fails because the source/provenance label overclaims direct evidence, not because the approved novel canon is automatically invalid.

### Gate B: Structure / Causality / Pacing
- **Trạng thái**: **FAIL**
- The chapter has a strong local dramatic curve: recovery comedy → breathing room at the temple → silence/misdirection → ambush → injury-limited improvisation → rescue.
- The final movement changes mode sharply from dramatic aftermath into a dense explanatory lore lecture. The faction reveal, artifact definition, father backstory, Trụ Thần Thạch mechanics, Du Long Giác mechanics, geopolitical threat, and Cái Bang departure are stacked with little dramatic resistance between revelations.
- Frontmatter reports 6,185 words, exceeding the repository's >5,000-word split trigger. This is not automatically a literary defect, but under the current workflow contract it cannot be called a clean substantiality pass without an explicit author override or a structural split/recompression decision.

### Gate C: Character / Agency / Injury Constraint
- **Trạng thái**: **PASS**
- Tiêu Phùng's established comic self-defense voice is recognizable in the medical scene and temple breathing room.
- His rib injury materially changes combat behavior: he does not suddenly win through martial escalation; he uses the lamp/fire and drags the chest instead. The injury then exacts an additional physical cost when the broken furniture strikes the same side.
- Trương Đỉnh receives meaningful agency in the rescue beat rather than existing only as disposable scenery.
- Concern for revision: Bạch Thu Lâm's arrival is highly convenient in timing, so the revised version should seed why her mounted unit is close enough to arrive at the exact lethal beat.

### Gate D: Voice / Show-vs-Tell / Comedy Execution
- **Trạng thái**: **FAIL**
- The comic dialogue often works because the joke arrives through Tiêu Phùng's concrete exaggeration (mushrooms, salted fish, bitter medicine) and other characters answer him rather than the narrator explaining the joke. This is worth preserving.
- However, the narration still labels qualities directly in several places instead of letting behavior carry them: Bạch Thu Lâm is described as having an authoritative presence and warm eyes; Tiêu Phùng's look is labeled as maximally cunning/reckless; the narration directly states strategic conclusions during combat.
- The largest show-vs-tell failure is the ending: Bạch Thu Lâm delivers multiple paragraphs of system/world explanation in one sitting. Even if every fact is approved novel canon, the delivery is encyclopedic rather than dramatized discovery.
- Therefore a lexical clean scan or a few successful comic exchanges cannot justify a blanket `Pure Show Don't Tell` / stylistic PASS.

### Gate E: Substantiality / Chapter Closure
- **Trạng thái**: **FAIL**
- The chapter does achieve a real state transition: Tiêu Phùng can no longer remain in the Ba Lăng childhood space and is directed toward Cái Bang/Yến Tử Ổ.
- The closing autumn/lake image gives an effective emotional exit.
- Nevertheless the 6,185-word size conflicts with the current >5,000 split mechanism, and too much durable lore is introduced immediately before the departure decision. The closure is substantial, but the current artifact does not satisfy the repository's own size/verification contract cleanly.

## 4. Evidence

1.
- **Vị trí**: `L1-L60`
- **Trích đoạn**: Gương mặt nữ thủ lĩnh nghĩa quân tuy lộ vẻ phong trần mệt mỏi
- **Phân tích**: This is an example of narrator-side labeling. It does not invalidate the scene, but it disproves a blanket claim that the chapter is purely show-don't-tell.

2.
- **Vị trí**: `L61-L120`
- **Trích đoạn**: Bên trong chiếc tráp chứa cuốn da dê cổ ghi chép mật mã quân cơ
- **Phân tích**: A durable artifact assertion is introduced as narrator fact. Under v2 it must be classified explicitly: the raw-source proposition is unresolved, while the current novel-canon artifact is preserved because the Chapter 09 Canon Diff is author-approved.

3.
- **Vị trí**: `L121-L180`
- **Trích đoạn**: Chàng không thể lao vào đánh tay đôi với những cỗ máy giết người sa trường này!
- **Phân tích**: The injury constraint itself is good, but this sentence tells the tactical conclusion directly. The stronger material immediately after it is the action choice: using the lamp and environment rather than overpowering the attackers.

4.
- **Vị trí**: `L181-L240`
- **Trích đoạn**: Ai cần ngươi liều mạng giữ đồ? Ta cần chiếc tráp nát này hay cần tính mạng của ngươi?
- **Phân tích**: Strong character evidence. Bạch Thu Lâm's attachment is shown through conflict, action and priority rather than abstract explanation; this should survive revision.

5.
- **Vị trí**: `L241-L280`
- **Trích đoạn**: Là mật thám của Tây Hạ Nhất Phẩm Đường.
- **Phân tích**: This relation is not directly established by the registered Task 157 evidence even though Nhất Phẩm Đường is a real source faction elsewhere. The statement remains valid current novel canon through author approval, but its fidelity label must be adaptation/canon decision rather than DIRECT_SOURCE from Task 157.

6.
- **Vị trí**: `L241-L280`
- **Trích đoạn**: Du Long Giác mang từ trường địa cực cực mạnh, đóng vai trò chiếc chìa khóa duy nhất
- **Phân tích**: This is a high-impact mechanical/cosmological assertion not established by the registered raw-source evidence. The Chapter 09 Canon Diff nevertheless records the mechanism as approved novel canon, so v2 preserves it as an `ADAPTATION_DECISION` while preventing the agent from presenting it as direct SQLite truth.

## 5. Priority Findings

### P0 — Source/canon boundary
1. Correct future provenance language for Chapter 09: Task 157/Subtasks 320–323 cannot be used as if they directly prove the entire Miếu Thần / Vô Danh Mật Tịch / Nhất Phẩm Đường sequence.
2. Preserve the existing author-approved Chapter 09 canon unless the Author explicitly reopens it.
3. Keep two parallel records where needed: an `UNRESOLVED` raw-source proposition and an `ADAPTATION_DECISION / author_approved` novel-canon proposition with `approval_ref`.
4. Do not convert a zero-result keyword search into proof that a concept cannot exist elsewhere in unindexed/raw material; the verifier should say only that the searched SQLite corpus did not establish it.

### P1 — Literary revision
1. Preserve the opening banter and Tiêu Phùng's physical comedy; it is one of the chapter's strongest voice sections.
2. Reduce narrator labels after behavior already communicates the trait.
3. Let the combat injury limitation emerge primarily from failed breath, restricted movement and tactical choice rather than narrator explanation.
4. Break the late lore dump into discovery, uncertainty, objection, physical evidence and deferred questions. Do not explain every system consequence in the same scene.
5. Seed Bạch Thu Lâm's proximity/response path before the rescue to reduce deus-ex-machina timing.

### P2 — Structure
- Either split/recompress the chapter to respect the existing >5,000-word rule, or record an explicit author override if this 6,185-word chapter is intentionally allowed to exceed that rule. Do not silently reinterpret the threshold after the fact.

## 6. Pilot Comparison With Legacy Review Behavior

The v2 result differs from a mechanical/self-confirming review in four important ways:

1. Existing entity names are not treated as proof of relationships, motives or events.
2. A source citation label in frontmatter is not trusted until its exact Task/Subtask locators and excerpts resolve against SQLite.
3. Author-approved novel canon is not erased merely because its raw-source provenance was mislabeled.
4. Successful comedy/injury beats do not cause the reviewer to wave through unrelated show-vs-tell, provenance and substantiality failures.

## 7. Verdict

- **Phán quyết**: **REVISE_REQUIRED**
- Manuscript is preserved unchanged under Author Text Supremacy.
- Existing Chapter 09 author-approved novel canon remains in force.
- `UNRESOLVED` raw-source claims remain blocked from being presented as source truth; corresponding author-approved adaptation claims may remain durable novel canon through their recorded approval reference.
- Recommended next action: fix the forward workflow so new durable-state writes require a checked Canon Diff in the same changeset, then revise Chapter 09 provenance/style only if the Author chooses to reopen the manuscript.
