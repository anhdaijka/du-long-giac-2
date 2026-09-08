# Editorial Workflow

## State machine

```text
[BƯỚC 1: LÊN KỊCH BẢN & ĐO LƯỜNG ĐỘ HẠT (STORY DECOMPRESSION)]
idea / plot deck (Macro Event Milestones)
  ↓
granularity assessment (Đánh giá độ hạt tự sự: đo lường mật độ kịch tính và dung lượng subtask; chủ động đề xuất phân bản hạt mịn XXa, XXb... bảo đảm dải dung lượng vàng 4.000 – 4.800 từ)
  ↓
lore & pedigree verification (Tra cứu SQLite story_database.sqlite3 và đối soát phả hệ từ worldbuilding/factions/genealogy_matrix.md)
  ↓
plan (templates/chapter-brief.md -> briefs/chapter_XX_brief.md)
  ↓
deterministic check (npm run story:check)
  ↓
🛑 HARD STOP 1: AUTHOR APPROVAL (Phê duyệt Chapter Brief)
   [DỪNG LẠI! Tuyệt đối không được viết draft nếu Brief chưa được duyệt]

[BƯỚC 2: CHẤP BÚT & KIỂM ĐỊNH]
draft (chapters/chapter_XX.md)
  ↓
[NẾU DUNG LƯỢNG VƯỢT TRẦN > 5.000 TỪ]:
  → Kích hoạt Cơ chế Tách Linh Hoạt a/b/c (Quyết định D-019)
  → Tách thành chapter_XXa.md & chapter_XXb.md với dramatic hook nối tiếp
  ↓
static linting (npm run lint:prose)
  ↓
review (templates/review-report.md -> reviews/chapter_XX_review.md)
  ↓
🛑 HARD STOP 2: AUTHOR APPROVAL (Phê duyệt Bản thảo & Review Report)
   [DỪNG LẠI! Tuyệt đối không tự ý canon hóa nếu Bản thảo chưa được duyệt]


[BƯỚC 3: CANON HÓA & LƯU TRỮ TOÀN DIỆN]
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
final check (npm run gate:check -> Gate Guard & Lore Guard Scan)
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

## Drafting

Give the writer minimum sufficient context. Prefer structured current state over old prose. The writer can creatively realize the approved scene but cannot silently change its durable outcome.

## Review

Use fresh review context where practical. Separate:

1. structure / causality / pacing
2. character / agency / arc
3. dialogue / subtext / voice
4. prose / specificity / rhythm
5. continuity & temporal sanity
6. pedigree & generational addressing (Rule PED-1 đến PED-3)
7. genre expectations

Use `templates/review-report.md`. Review first; rewrite second.

## Canon diff & 4-Pillar State Commitment Protocol

After revision, list proposed durable changes with `templates/canon-diff.md`. Author chooses accept all, accept selected, or reject.

Only then execute the **Mandatory 4-Pillar State Commitment Protocol**:
1. **Trụ cột 1 - Nhân vật chính & Bản lề (Protagonists & Anchors)**: Update `characters/<protagonist>.md` and affected `characters/anchors/*.md`.
2. **Trụ cột 2 - Danh bạ nhân vật phụ Tier B/C (Supporting Cast Directory)**: Append newly introduced characters or update existing ones in `characters/supporting_cast.md`.
3. **Trụ cột 3 - Sổ cái thế giới (World Ledgers)**: Update physical injuries in `worldbuilding/medical/injuries_ledger.md`, artifacts in `worldbuilding/artifacts/artifacts_ledger.md`, and faction alignments in `worldbuilding/factions/relationships_matrix.md`.
4. **Trụ cột 4 - Dòng thời gian & Lời hứa (Chronology & Narrative Threads)**: Record exact date and verify age against `plot/timeline.md`, `plot/chronology_matrix.md` & `plot/volume_01_deck.md`, update promises in `plot/promises_tracker.md`, and conclude session in `author/session-state.md`.

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
author decision
  ↓
canonical Story Skills file
```

Never let external research bypass author interpretation and become story canon automatically.
