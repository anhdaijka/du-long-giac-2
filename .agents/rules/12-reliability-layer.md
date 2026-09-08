# Rule 12: Reliability Layer v2

> **Single Responsibility**: Prevent agent self-certification, silent claim promotion, stale-manuscript restoration, and shallow review. This rule strengthens verification without restricting the Author's direct editing freedom.

Read `docs/reliability-layer-v2.md` for the full design.

---

## 1. Author Text Supremacy

**Current Author Text Wins.**

Before reviewing, revising, continuing, extracting claims from, or preparing canon changes from a chapter, re-read the current file in `chapters/`.

The current manuscript always outranks:

- an earlier agent-generated draft;
- an earlier review snapshot;
- chat/session memory;
- cached context;
- wording remembered from an approved brief.

If current repository text differs from an earlier agent version, treat the difference as an intentional Author edit unless the Author explicitly says otherwise.

**PROHIBITED**:

- restoring old wording because it matches a previous agent draft;
- overwriting an Author revision while fixing an unrelated passage;
- requiring hashes, revision IDs, reconciliation metadata, or rollback before continuing;
- silently changing prose because a claim fails canon validation.

If prose contains a durable claim that conflicts with source/canon, preserve the prose, flag the claim, and block only unsupported source/canon promotion as appropriate.

---

## 2. Evidence Before Durable Claim

Entity existence is not relation evidence.

Before a plan or canon diff relies on a durable source-derived assertion, distinguish the proposition explicitly and classify it as one of:

- `DIRECT_SOURCE`
- `SOURCE_SUPPORTED_INFERENCE`
- `UNRESOLVED`
- `ADAPTATION_DECISION`
- `NOVELIZATION_BRIDGE`

For Reliability v2 chapters, use:

- `research/evidence/chapter_XX.json`
- `research/claims/chapter_XX.json`

Templates:

- `templates/evidence-packet.json`
- `templates/claim-ledger.json`

SQLite evidence must point to one concrete row and one declared text field. For example, a subtask locator keeps both `task_id` and `subtask_id`; the excerpt is matched only against the declared `field`.

Run:

```bash
python scripts/evidence_guard.py --chapter XX
python scripts/claim-guard.py --chapter XX
```

`evidence_guard.py` proves only that the locator resolves uniquely and that the excerpt matches the declared SQLite field. `claim-guard.py` also invokes this source verification before validating the epistemic claim structure. Neither guard proves semantic entailment.

### Mandatory epistemic rules

- `DIRECT_SOURCE` requires concrete source-verified evidence.
- `SOURCE_SUPPORTED_INFERENCE` requires source-verified evidence + explicit reasoning and cannot be auto-promoted.
- `UNRESOLVED` must remain blocked as a source-truth proposition.
- `ADAPTATION_DECISION` must never be presented as if the raw source required it.
- `NOVELIZATION_BRIDGE` may realize connective prose but may not silently create durable source truth.
- No durable canon state may be inferred merely because all involved entity names are valid.
- Every durable canon promotion still requires Author approval, including `DIRECT_SOURCE`.

### Source truth and novel canon are separate axes

A proposition may be unsupported or unresolved in the raw game source while still being valid **novel canon** because the Author explicitly approved it as an adaptation.

Therefore:

- do not erase or rollback an approved novel-canon decision merely because SQLite lookup does not prove it;
- do not relabel an approved adaptation as `DIRECT_SOURCE` merely because it now exists in `characters/`, `worldbuilding/`, `plot/`, or an earlier chapter;
- when both views matter, keep two explicit propositions: an `UNRESOLVED` raw-source proposition and an `ADAPTATION_DECISION` novel-canon proposition.

Promotion states:

- `author_approval_required` — proposed durable truth; not yet approved;
- `author_approved` — durable novel canon already approved by the Author;
- `blocked` — cannot be promoted in its current epistemic state.

`promotion: author_approved` requires a repository-relative `approval_ref` pointing to a Canon Diff containing a checked Author approval line such as:

```text
- [x] Phê chuẩn toàn văn Đề xuất Canon Diff Chương XX.
```

`claim-guard.py` verifies that the referenced file exists and contains the checked approval marker. This is recorded approval verification; it does not prove raw-source entailment.

---

## 3. Full-Read Review

A reviewer must inspect the **current manuscript**, sequentially from beginning to end.

A review must contain `## Full-Read Coverage` with machine-readable line ranges such as:

```text
- `L1-L90` — concrete observation from this range
- `L91-L180` — concrete observation from this range
```

Rules:

- collectively cover every line of the current chapter;
- each range should be small enough for actual review; `review-guard.py` rejects ranges over 120 lines;
- each range requires a concrete observation;
- mandatory evidence spans must use current `Lx-Ly` locations and verbatim chapter text.

For one standard review:

```bash
python scripts/review-guard.py --chapter-number XX
```

For all forward-only v2 review artifacts (`reviews/**/chapter_*_review_v2.md`):

```bash
python scripts/review-guard.py --all-v2
```

When an approved review is required:

```bash
python scripts/review-guard.py --chapter-number XX --require-approval
```

A structural PASS means only that coverage/evidence/report structure is valid. It does not replace literary judgment. Legacy reviews are historical artifacts and are not forced through the v2 batch scan.

---

## 4. Verification Vocabulary

Every verifier must describe only what it actually checks.

- `meta-leakage-scanner.py`: lexical/meta/style-pattern scan.
- `lore-grounder.py`: entity plausibility / closed-world entity check.
- `lore-guard.py`: known-regression scan for encoded lore mistakes.
- `evidence_guard.py`: SQLite row/field/excerpt provenance verification.
- `claim-guard.py`: source-verified evidence + claim structural discipline + recorded approval-ref validation.
- `review-guard.py`: full-read coverage and current-line evidence structure.
- `state-commit-guard.py`: forward-only changeset check for new durable-state writes and their review/claim/approval prerequisites.
- `execution-guard.py`: computes execution-plan completion from declared deliverables and allowlisted deterministic checks; it does not permit self-certified status fields or arbitrary shell commands.
- semantic Reviewer: prose, causality, voice, show-vs-tell, humor, continuity, and claim meaning.

**PROHIBITED**: translating a lower-level PASS into claims such as:

- “Zero Hallucination”
- “Pure Show Don't Tell 100%”
- “all facts verified”
- “reviewed comprehensively”

unless the corresponding semantic work was actually performed and evidenced.

---

## 5. Completion Discipline

The agent may not mark a phase complete merely because it created a file or wrote a PASS paragraph.

Where a deterministic verifier exists, completion requires its relevant artifact and verifier result.

Examples:

- source evidence preparation complete -> Evidence Packet + `evidence_guard` PASS;
- claim preparation complete -> Evidence Packet + Claim Ledger + `claim-guard` PASS;
- structural review complete -> current chapter fully covered + `review-guard` PASS;
- approved review complete -> `review-guard --require-approval` PASS plus Author approval under Hard Stop 2;
- new durable state commit complete -> checked Canon Diff + current approved v2 review + Claim/Evidence contract + `state-commit-guard` PASS.

### Execution Manifest — verifier-owned completion

For a multi-step plan where skipping one deliverable would materially change the result, create a lightweight execution manifest from:

`templates/execution-manifest.json`

Default working location:

`execution/<scope>.json`

The manifest contains only:

- `manifest_id`
- optional `scope`
- `deliverables[]`
- each deliverable's `id`, `description`, `requires`, and `checks`

**Do not store `status`, `done`, `complete`, `completed`, or equivalent completion fields.** `execution-guard.py` rejects them. Completion is computed at runtime:

- `COMPLETE` — all declared checks pass;
- `INCOMPLETE` — one or more checks fail;
- `BLOCKED` — a required prior deliverable is not complete.

Allowed check types are deliberately small:

- `file_exists`
- `file_nonempty`
- `evidence`
- `claim`
- `review`

Arbitrary shell commands are prohibited. This is a completion contract, not a workflow engine.

Tracking/report mode:

```bash
python scripts/execution-guard.py --manifest execution/<scope>.json
```

or:

```bash
npm run execution:check
```

Tracking mode may report incomplete work without making CI red; this allows genuine work-in-progress manifests.

Before telling the Author that the **whole approved execution plan is finished**, run:

```bash
npm run execution:complete -- --manifest execution/<scope>.json
```

If any deliverable is `INCOMPLETE` or `BLOCKED`, the agent must report the partial state and continue the missing work instead of saying “done”.

### Forward-only State Commit Gate

Reliability v2 does **not** re-audit all historical state before work can continue.

For new changes only, if a changeset modifies any file under:

- `characters/`
- `worldbuilding/`
- `plot/`

then the same changeset must also contain the relevant changed `revisions/chapter_XX_canon_diff.md` with a checked Author approval line, a current approved v2 full-read review, and a passing Evidence/Claim contract.

Run locally with an explicit base ref:

```bash
python scripts/state-commit-guard.py --base <base-ref>
```

CI calculates the base commit and enforces this automatically.

This guard proves recorded promotion prerequisites. It does not authenticate the human identity behind the checkbox and does not semantically prove that every ledger edit matches every sentence in the diff; those remain separate workflow responsibilities.

Do not add manuscript hashes, immutable revision locks, workflow databases, or mandatory Author-edit metadata.

---

## 6. Failure Behavior

When a guard fails:

1. report the smallest concrete failure;
2. do not rationalize it into PASS;
3. fix only the relevant artifact unless a broader change is genuinely required;
4. re-read current Author-controlled files before applying any prose edit;
5. never use a failed verifier as justification to overwrite Author revisions;
6. when `execution-guard --require-complete` fails, do not rewrite the plan as if fewer deliverables had been intended — finish or explicitly renegotiate the scope with the Author.
