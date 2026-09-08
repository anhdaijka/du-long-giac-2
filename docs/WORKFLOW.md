# Editorial Workflow

> Reliability v2 rollout is **forward-only**. Existing briefs/reviews are historical artifacts and are not mass-invalidated or forced through migration. New chapter planning/review rounds use the Reliability v2 contracts below.
>
> Evidence/Claim artifacts are for **durable source-dependent assertions** (relations, events, knowledge, genealogy, possession, chronology, faction alignment, persistent state). They are not required for every gesture, sensory detail, joke, or other non-durable prose realization.

## State machine

```text
[BƯỚC 1: LÊN KỊCH BẢN & ĐO LƯỜNG ĐỘ HẠT (STORY DECOMPRESSION)]
idea / plot deck (Macro Event Milestones)
  ↓
granularity assessment (Đánh giá độ hạt tự sự: đo lường mật độ kịch tính và dung lượng subtask; chủ động đề xuất phân bản hạt mịn XXa, XXb... bảo đảm dải dung lượng vàng 4.000 – 4.800 từ)
  ↓
lore & pedigree verification (Tra cứu SQLite story_database.sqlite3 và đối soát phả hệ từ worldbuilding/factions/genealogy_matrix.md)
  ↓
Reliability v2 evidence packet (research/evidence/chapter_XX.json)
  ↓
claim ledger for durable source-dependent assertions (research/claims/chapter_XX.json)
  ↓
structural epistemic check (python scripts/claim-guard.py --chapter XX)
  ↓
plan (templates/chapter-brief.md -> briefs/chapter_XX_brief.md)
  ↓
deterministic check (npm run story:check)
  ↓
🛑 HARD STOP 1: AUTHOR APPROVAL (Phê duyệt Chapter Brief)
   [DỪNG LẠI! Tuyệt đối không được viết draft nếu Brief chưa được duyệt]

[BƯỚC 2: CHẤP BÚT & KIỂM ĐỊNH]
re-read CURRENT author-controlled chapter if it already exists
  ↓
draft / continue / revise (chapters/chapter_XX.md)
  ↓
[NẾU DUNG LƯỢNG VƯỢT TRẦN > 5.000 TỪ]:
  → Kích hoạt Cơ chế Tách Linh Hoạt a/b/c (Quyết định D-019)
  → Tách thành chapter_XXa.md & chapter_XXb.md với dramatic hook nối tiếp
  ↓
static lexical/meta linting (npm run lint:prose — kiểm tra pattern cơ học; KHÔNG đồng nghĩa semantic prose PASS)
  ↓
known lore-regression scan (python scripts/lore-guard.py --check chapters/chapter_XX.md — KHÔNG phải Zero Hallucination proof)
  ↓
entity plausibility check (python scripts/lore-grounder.py --chapter chapters/chapter_XX.md — entity tồn tại KHÔNG chứng minh relation/event claim)
  ↓
claim contract check (python scripts/claim-guard.py --chapter XX)
  ↓
re-read CURRENT chapter sequentially from L1 to EOF
  ↓
adversarial red-team review (templates/review-report.md -> reviews/chapter_XX_review.md)
  ↓
full-read structural verification (python scripts/review-guard.py --chapter-number XX --require-approval)
  ↓
🛑 HARD STOP 2: AUTHOR APPROVAL (Phê duyệt Bản thảo & Review Report)
   [DỪNG LẠI! Tuyệt đối không tự ý canon hóa nếu Bản thảo chưa được duyệt]

[BƯỚC 3: CANON HÓA & LƯU TRỮ TOÀN DIỆN]
re-read CURRENT author-controlled chapter
  ↓
extract/reconcile proposed durable claims against Evidence Packet + Claim Ledger
  ↓
canon diff (templates/canon-diff.md -> revisions/chapter_XX_canon_diff.md)
  ↓
🛑 HARD STOP 3: AUTHOR APPROVAL (Phê duyệt Canon Diff)
   [DỪNG LẠI! Chỉ cập nhật Sổ cái sau khi Tác giả duyệt Diff]
  ↓
[GIAO THỨC COMMIT STATE 4 TRỤ CỘT BẮT BUỘC]:
   1. Trụ cột 1 - Nhân vật chính & Bản lề: characters/<core>.md & characters/anchors/
   2. Trụ cột 2 - Danh bạ nhân vật phụ Tier B/C: characters/supporting_cast.md
   3. Trụ cột 3 - Sổ cái thế giới: worldbuilding/ (injuries_ledger.md, artifacts_ledger.md, relationships_matrix.md)
   4. Trụ cột 4 - Dòng thời gian & Lời hứa: plot/ (timeline.md, promises_tracker.md, volume_01_deck.md) & author/session-state.md
  ↓
final check (npm run gate:check -> lifecycle aggregation)
  ↓
accept chapter
  ↓
git commit
```

## Planning gate

Do not move into prose until the chapter has enough information to constrain it safely:

- purpose
- POV & exact chronological age (aligned with `plot/chronology_matrix.md` — Rule TC-1 Zero Age Drift)
- temporal continuity verification:
  - exact calendar date (aligned with `plot/timeline.md` — Rule TC-2)
  - delta T elapsed from last POV appearance (Rule TC-3: mandatory transition narrative if $\Delta T \ge 3$ days)
  - travel velocity & information latency (aligned with `worldbuilding/geography/travel_matrix.md` — Rule TC-4)
- NPC pedigree & biological age verification:
  - kinship & lineage check (aligned with `worldbuilding/factions/genealogy_matrix.md` — Rule PED-1)
  - biological age sanity formula ($\text{Tuổi Cha/Mẹ} \ge \text{Tuổi Con} + 16$ — Rule PED-2)
  - generational hierarchy & addressing rules (Rule PED-3)
- starting state
- ending state
- scene order
- causal progression
- character movement
- revelations/information movement
- active promises/questions
- forbidden reveals
- continuity risks

### Reliability v2 planning input

For newly planned chapters, durable source-dependent assertions must be externalized before they become hidden assumptions in a Chapter Brief:

- evidence: `research/evidence/chapter_XX.json`
- claims: `research/claims/chapter_XX.json`
- verifier: `python scripts/claim-guard.py --chapter XX`

Use the epistemic statuses from `.agents/rules/12-reliability-layer.md`:

- `DIRECT_SOURCE`
- `SOURCE_SUPPORTED_INFERENCE`
- `UNRESOLVED`
- `ADAPTATION_DECISION`
- `NOVELIZATION_BRIDGE`

**Entity existence is never sufficient proof of a relationship, motive, event, knowledge state, genealogy, possession, chronology or faction alignment.**

Every durable canon promotion, including `DIRECT_SOURCE`, remains author-approval-bound.

Use `templates/chapter-brief.md`.

## Deterministic gate

Before and after accepted state changes:

```bash
npm run story:check
```

For diagnostics:

```bash
npm run story:doctor
npm run story:next
npm run story:report
```

Reliability v2 guard scopes:

```bash
python scripts/claim-guard.py --chapter XX
python scripts/review-guard.py --chapter-number XX
```

These tools verify structure within their documented scope. They do not replace source-aware semantic judgment.

## Drafting

Give the writer minimum sufficient context. Prefer structured current state over old prose. The writer can creatively realize the approved scene but cannot silently change its durable outcome.

### Author Text Supremacy

Before modifying, continuing or reviewing an existing chapter, **re-read the current repository file**.

The current manuscript outranks old agent drafts, old reviews, chat/session memory and cached wording. If it differs from an earlier agent version, treat the difference as an intentional Author edit unless the Author explicitly says otherwise.

Never restore or overwrite an Author revision merely to match an older plan or agent-generated draft. If an Author-written sentence creates a source/canon conflict, preserve the prose and flag/block only the unsupported canon promotion.

No chapter SHA, content hash, immutable revision lock, automatic rollback or mandatory Author-edit metadata is required.

## Review & Adversarial Red-Team Protocol

Use fresh, decoupled review context. The reviewer acts as an Adversarial Critic looking for defects rather than an agreeable assistant.

Before reviewing, re-read the **current** chapter sequentially from L1 to EOF. A new Reliability v2 review must include `Full-Read Coverage` ranges that collectively cover the entire current file and machine-verifiable verbatim evidence spans. Run:

```bash
python scripts/review-guard.py --chapter-number XX
```

Before presenting an APPROVED review at Hard Stop 2:

```bash
python scripts/review-guard.py --chapter-number XX --require-approval
```

Core review dimensions:
1. provenance / claim meaning / source-vs-inference discipline
2. structure / causality / pacing (organic dramatic curve, living wulin breathing room)
3. character / agency / arc (bounded martial majesty, zero instant level-up)
4. dialogue / subtext / voice (Trio Unique Sociolects: Tiêu Phùng witty/sarcastic, Tĩnh Xuyên military/cold, Hạ Nương medical/empirical)
5. prose / specificity / rhythm (show-don't-tell, zero explanatory scaffolds in narrator text)
6. comedy execution (setup → misdirection → payoff → afterbeat; narrator must not explain the punchline)
7. continuity & temporal sanity (Rule TC-1 đến TC-4, travel velocity from `travel_matrix.md`)
8. pedigree & generational addressing (Rule PED-1 đến PED-4)
9. injury continuity & physical damage tax (Rule from `injuries_ledger.md`)
10. mandatory span-level evidence (minimum 4 verbatim spans with exact line numbers)

The 65/25/10 creative direction is a creative register target, not a mechanical percentage score inferred from a few jokes or keywords.

Use `templates/review-report.md`. Review first; rewrite second.

## Canon diff & 4-Pillar State Commitment Protocol

After revision, re-read the current manuscript and list proposed durable changes with `templates/canon-diff.md`. Author chooses accept all, accept selected, or reject.

Before proposing a durable source-derived change, reconcile it against the current Evidence Packet / Claim Ledger. A verifier failure may block canon promotion, but **must never be used to silently revert Author prose**.

Only after Hard Stop 3 approval execute the **Mandatory 4-Pillar State Commitment Protocol**:
1. **Trụ cột 1 - Nhân vật chính & Bản lề (Protagonists & Anchors)**: Update `characters/<protagonist>.md` and affected `characters/anchors/*.md`.
2. **Trụ cột 2 - Danh bạ nhân vật phụ Tier B/C (Supporting Cast Directory)**: Append newly introduced characters or update existing ones in `characters/supporting_cast.md`.
3. **Trụ cột 3 - Sổ cái thế giới (World Ledgers)**: Update physical injuries in `worldbuilding/medical/injuries_ledger.md`, artifacts in `worldbuilding/artifacts/artifacts_ledger.md`, and faction alignments in `worldbuilding/factions/relationships_matrix.md`.
4. **Trụ cột 4 - Dòng thời gian & Lời hứa (Chronology & Narrative Threads)**: Record exact date and verify age against `plot/timeline.md`, `plot/chronology_matrix.md` & `plot/volume_01_deck.md`, update promises in `plot/promises_tracker.md`, and conclude session in `author/session-state.md`.

## Completion discipline

An agent cannot make a phase complete merely by writing “PASS” or creating a nominal artifact.

Where a deterministic verifier exists, phase completion requires the relevant artifact plus a successful verifier run. Verifier success never expands beyond that verifier's documented scope.

Examples:

- evidence/claim structure complete → Evidence Packet + Claim Ledger + `claim-guard` PASS;
- structural full-read review complete → current manuscript coverage + `review-guard` PASS;
- approved review ready for Hard Stop 2 → `review-guard --require-approval` PASS, then Author decision.

Keep this lightweight. Do not introduce a workflow database or manuscript version bureaucracy.

## Commit discipline

Recommended sequence:

```text
plan: approve chapter 08
draft: chapter 08 first pass
revise: tighten chapter 08 confrontation
canon: accept chapter 08 state transition
```

You do not need a commit for every agent action. Commits should correspond to meaningful recoverable states.

## Research lifecycle

```text
external source
  ↓
research/inbox
  ↓
verification
  ↓
research/verified
  ↓
Reliability v2 Evidence Packet / Claim Ledger (for durable source-dependent assertions)
  ↓
author decision
  ↓
canonical Story Skills file
```

Never let external research bypass author interpretation and become story canon automatically.
