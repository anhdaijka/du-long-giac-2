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

If prose contains a durable claim that conflicts with source/canon, preserve the prose, flag the claim, and block only unsupported canon promotion.

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

Run:

```bash
python scripts/claim-guard.py --chapter XX
```

`claim-guard` validates structural epistemic discipline. A PASS does **not** prove that the interpretation is semantically true.

### Mandatory epistemic rules

- `DIRECT_SOURCE` requires concrete evidence.
- `SOURCE_SUPPORTED_INFERENCE` requires evidence + explicit reasoning and cannot be auto-promoted.
- `UNRESOLVED` must remain blocked.
- `ADAPTATION_DECISION` must never be presented as if the source required it.
- `NOVELIZATION_BRIDGE` may realize connective prose but may not silently create durable source truth.
- No durable canon state may be inferred merely because all involved entity names are valid.

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

Run:

```bash
python scripts/review-guard.py --chapter-number XX
```

When an approved review is required:

```bash
python scripts/review-guard.py --chapter-number XX --require-approval
```

A structural PASS means only that coverage/evidence/report structure is valid. It does not replace literary judgment.

---

## 4. Verification Vocabulary

Every verifier must describe only what it actually checks.

- `meta-leakage-scanner.py`: lexical/meta/style-pattern scan.
- `lore-grounder.py`: entity plausibility / closed-world entity check.
- `lore-guard.py`: known-regression scan for encoded lore mistakes.
- `claim-guard.py`: evidence/claim structural discipline.
- `review-guard.py`: review coverage and current-line evidence structure.
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

- claim preparation complete -> Evidence Packet + Claim Ledger + `claim-guard` PASS;
- structural review complete -> current chapter fully covered + `review-guard` PASS;
- approved review complete -> `review-guard --require-approval` PASS plus Author approval under Hard Stop 2.

Do not add manuscript hashes, immutable revision locks, workflow databases, or mandatory Author-edit metadata.

---

## 6. Failure Behavior

When a guard fails:

1. report the smallest concrete failure;
2. do not rationalize it into PASS;
3. fix only the relevant artifact unless a broader change is genuinely required;
4. re-read current Author-controlled files before applying any prose edit;
5. never use a failed verifier as justification to overwrite Author revisions.
