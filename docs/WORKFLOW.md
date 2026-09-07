# Editorial Workflow

## State machine

```text
[BƯỚC 1: LÊN KỊCH BẢN]
idea / plot deck
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
[GIAO THỨC COMMIT STATE 4 BƯỚC BẮT BUỘC]:
   1. Cập nhật Nhân vật chính (characters/<core>.md) & Trụ cột liên quan (characters/anchors/)
   2. Bổ sung/Cập nhật Nhân vật phụ Tier B/C vào characters/supporting_cast.md
   3. Cập nhật Khí tài bền vững (worldbuilding/artifacts/artifacts_ledger.md) & plot/timeline.md
   4. Cập nhật Hạt giống cốt truyện (plot/promises_tracker.md) & author/session-state.md
  ↓
final check (npm run gate:check)
  ↓
accept chapter
  ↓
git commit
```

## Planning gate

Do not move into prose until the chapter has enough information to constrain it safely:

- purpose
- POV
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
5. continuity
6. genre expectations

Use `templates/review-report.md`. Review first; rewrite second.

## Canon diff & 4-Step State Persistence Protocol

After revision, list proposed durable changes with `templates/canon-diff.md`. Author chooses accept all, accept selected, or reject.

Only then execute the **Mandatory 4-Step Diff Commitment Protocol**:
1. **Protagonists & Anchors**: Update `characters/<protagonist>.md` and affected `characters/anchors/*.md`.
2. **Supporting Cast (Tier B & C)**: Append newly introduced characters or update existing ones in `characters/supporting_cast.md`.
3. **Durable Artifacts & Spatiotemporal State**: Record physical status, bearer, and location in `worldbuilding/artifacts/artifacts_ledger.md`, and record exact date in `plot/timeline.md`.
4. **Narrative Threads & Session State**: Update `plot/promises_tracker.md` (active promises, payoffs, planted clues) and conclude chapter in `author/session-state.md`.

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
