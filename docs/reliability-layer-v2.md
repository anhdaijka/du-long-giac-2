# Novel OS Reliability Layer v2

## Status

Approved architecture for `du-long-giac-2`. Implement and prove it here first; only stable generic pieces should later be ported back to `anhdaijka/novel-os`.

## Goal

Increase autonomous reliability without turning a single-author fiction repository into a bureaucratic workflow system.

Reliability v2 is built around six primitives:

1. Evidence Packet
2. Claim Ledger
3. SQLite Evidence Guard
4. Full-Read Review Protocol
5. Forward-Only State Commit Guard
6. Author Text Supremacy

The governing idea is:

> **Autonomous execution, zero autonomous trust.**

An agent may perform work automatically, but it must not certify semantic truth, author approval, review completeness, or durable state promotion merely by saying that it did so.

---

## North Laws

### NL-1 — Source truth is evidence-bound

A durable factual assertion derived from the KT2 source corpus must be traceable to concrete source evidence. Entity existence alone does not prove a relation, event, motive, chronology, possession, knowledge state, genealogy, or faction alignment.

### NL-2 — Source truth and novel canon are different authority axes

Raw game-source support and novel-canon authority are not the same thing.

A proposition may be unresolved in the game source while remaining valid novel canon because the Author explicitly approved it as an adaptation decision.

Therefore:

- source failure must not silently erase approved novel canon;
- novel-canon presence must not be recycled as proof that the raw source said the same thing;
- an adaptation must never be relabeled `DIRECT_SOURCE` merely because it already appears in ledgers or earlier chapters.

### NL-3 — Canon truth is approval-bound

Source evidence, source-supported inference, adaptation decisions and novelization bridges are not automatically novel canon.

Every durable canon promotion requires the existing Author approval gate.

Evidence strength controls epistemic confidence; it never grants autonomous canon-write authority.

### NL-4 — Agent completion is verifier-bound

An agent may report work performed, but it may not make a workflow step complete merely by saying it is complete. Machine-checkable deliverables decide completion where a deterministic verifier exists.

### NL-5 — Current Author Text Wins

The current manuscript in the repository is authoritative over any previous agent draft, review snapshot, session summary, cached context or remembered wording.

Before reviewing, revising, continuing or deriving canon from a chapter, re-read the current chapter file.

Never restore, overwrite or normalize an Author edit merely to match an older plan, review or generated draft.

Canon validation may reject or reclassify a durable claim without reverting the Author's prose.

### NL-6 — Verification must describe what it actually proves

A regex regression scanner must not call itself a zero-hallucination proof. An entity grounder must not imply that relations involving a known entity are grounded. A lexical linter must not imply semantic literary quality. A checked approval marker does not prove raw-source entailment.

---

## 1. Evidence Packet

Default path:

`research/evidence/chapter_XX.json`

The Evidence Packet records source observations used to constrain planning and drafting. It is not canon.

Each evidence item contains:

- stable `evidence_id`
- `source_kind`
- concrete `locator`
- declared source `field`
- short excerpt
- match mode
- optional notes about branch flags, speaker reliability or ambiguity

Example:

```json
{
  "chapter": "10",
  "evidence": [
    {
      "evidence_id": "EV-10-001",
      "source_kind": "sqlite.subtasks",
      "locator": {
        "task_id": 157,
        "subtask_id": 320
      },
      "field": "describe_cleaned",
      "excerpt": "<source excerpt>",
      "match": "contains_normalized",
      "notes": "Direct row observation; no inferred motive."
    }
  ]
}
```

Evidence IDs identify observations, not conclusions.

### Evidence Guard

Run:

```bash
python scripts/evidence_guard.py --chapter XX
```

or for all registered packets:

```bash
npm run evidence:check
```

The guard verifies:

- the SQLite table/source kind is allowed;
- the locator resolves to exactly one row;
- required lineage context is present, e.g. `task_id + subtask_id` for subtasks;
- the declared field exists;
- the excerpt matches that declared field.

It does **not** prove that the excerpt semantically entails a later claim.

---

## 2. Claim Ledger

Default path:

`research/claims/chapter_XX.json`

The Claim Ledger records explicit propositions that a plan, manuscript or proposed canon state depends on.

Allowed epistemic states:

- `DIRECT_SOURCE`
- `SOURCE_SUPPORTED_INFERENCE`
- `UNRESOLVED`
- `ADAPTATION_DECISION`
- `NOVELIZATION_BRIDGE`

A claim should be a proposition such as:

```text
Bạch Thu Lâm knows X by the evening of 1191-08-20.
```

not merely an entity name such as:

```text
Bạch Thu Lâm
```

### Promotion states

`author_approval_required`
- proposition is proposed for durable canon;
- the Author has not yet approved that promotion.

`author_approved`
- proposition is already durable novel canon;
- requires `approval_ref` pointing to a Canon Diff with a checked Author approval line.

`blocked`
- proposition cannot be promoted in its current epistemic state.

### Claim rules

`DIRECT_SOURCE`
- requires source-verified evidence;
- may not contain extra causal/motivational conclusions absent from that evidence;
- durable promotion requires Author approval.

`SOURCE_SUPPORTED_INFERENCE`
- requires source-verified evidence;
- requires non-empty reasoning;
- durable promotion requires Author approval.

`UNRESOLVED`
- records contradiction, ambiguity or missing evidence;
- uses `promotion: blocked`;
- cannot be declared durable source truth.

`ADAPTATION_DECISION`
- records a novelization choice that is not asserted as a raw-source requirement;
- may become durable canon through Author approval;
- an already approved decision uses `promotion: author_approved` + `approval_ref`.

`NOVELIZATION_BRIDGE`
- allows connective tissue, gesture, micro-action, sensory realization and other literary bridging;
- may not silently create durable source truth;
- durable promotion requires Author approval.

### Two-proposition pattern

When a source claim is unsupported but the Author has already canonized an adaptation, keep both facts explicit rather than forcing one label to do two jobs.

Example conceptually:

```json
[
  {
    "claim": "The raw game source establishes relation X.",
    "epistemic_status": "UNRESOLVED",
    "durability": "ephemeral",
    "promotion": "blocked"
  },
  {
    "claim": "Novel canon intentionally uses relation X.",
    "epistemic_status": "ADAPTATION_DECISION",
    "durability": "durable",
    "promotion": "author_approved",
    "approval_ref": "revisions/chapter_XX_canon_diff.md"
  }
]
```

This prevents both failure modes:

1. hallucinated source provenance becoming canon truth;
2. an overzealous verifier erasing an Author-approved adaptation.

### Claim Guard

Run:

```bash
python scripts/claim-guard.py --chapter XX
```

or:

```bash
npm run claim:check
```

The guard verifies:

- Evidence/Claim files exist and agree on chapter ID;
- IDs are unique and references resolve;
- SQLite evidence passes Evidence Guard;
- epistemic status / durability / promotion combinations are legal;
- required evidence/reasoning exists;
- unresolved claims are blocked;
- `author_approved` claims have a repository-relative `approval_ref`;
- the referenced Canon Diff contains a checked Author approval line.

It does **not** prove semantic entailment or authenticate who physically ticked the checkbox.

---

## 3. Full-Read Review Protocol

Review operates on the current chapter file.

The reviewer must read the manuscript sequentially from beginning to end. Reviews contain machine-readable line coverage in addition to literary findings.

Example:

```text
- `L1-L96` — concrete observation from this range
- `L97-L188` — concrete observation from this range
- `L189-L281` — concrete observation from this range
```

Coverage ranges must collectively cover the current manuscript. Ranges over 120 lines are rejected to discourage one-shot pseudo-review.

Mandatory evidence findings use current `Lx-Ly` ranges and verbatim text from those lines.

Run one review:

```bash
python scripts/review-guard.py --chapter-number XX
```

Batch-check forward-only v2 reviews:

```bash
npm run review:check
```

The guard verifies review structure, coverage and quote grounding. It does not judge whether the literary analysis is intelligent.

### Semantic review still owns

- causality
- pacing
- character agency
- injury constraints
- voice
- show-vs-tell
- humor execution
- continuity
- claim meaning
- ending resonance

A lexical PASS can never substitute for this layer.

---

## 4. Comedy / Show-Don't-Tell Evaluation

The project's 65/25/10 creative direction remains a creative target, not a numeric linter score.

For comic scenes, inspect observable execution:

1. setup creates an expectation;
2. misdirection bends the expectation;
3. payoff lands through action/dialogue/image;
4. afterbeat preserves character voice;
5. narrator does not explain why the joke was funny.

A few comic phrases do not prove that the scene achieved the intended comedic register.

---

## 5. Forward-Only State Commit Guard

Historical state is not re-audited merely because Reliability v2 exists.

The guard only inspects a selected git changeset.

If that changeset modifies durable state under:

- `characters/`
- `worldbuilding/`
- `plot/`

then the same changeset must also contain at least one changed:

`revisions/chapter_XX_canon_diff.md`

with a checked Author approval line.

Run locally:

```bash
python scripts/state-commit-guard.py --base <base-ref>
```

CI supplies the base commit automatically.

The guard proves only:

- a new durable-state write occurred or did not occur;
- a changed Canon Diff accompanies that write;
- the changed Canon Diff contains a recorded checked approval marker.

It does not:

- re-audit legacy canon;
- authenticate the human identity behind the checkbox;
- semantically prove that every ledger edit matches the Canon Diff;
- alter manuscript prose.

This is intentionally lightweight. No event-sourcing database, manuscript locks or content hashes are introduced.

---

## 6. Completion Verification

A workflow step is complete only when its required artifact exists and its relevant verifier passes.

Examples:

```text
source evidence prepared
  -> Evidence Packet + Evidence Guard PASS

claim contract prepared
  -> Evidence Packet + Claim Ledger + Claim Guard PASS

structural full review prepared
  -> full current-manuscript coverage + Review Guard PASS

new durable state committed
  -> checked Canon Diff in same changeset + State Commit Guard PASS
```

An agent saying “done” has no authority over these checks.

---

## 7. Existing Tools: Exact Responsibilities

### `meta-leakage-scanner.py`

Lexical/meta/style-pattern scanner.

A clean result is not semantic prose approval.

### `lore-grounder.py`

Closed-world entity plausibility check.

It does not verify relations or events involving known entities.

### `lore-guard.py`

Known-regression scanner plus source-search helper.

A clean scan is not “Zero Hallucination”. Search hits are candidate evidence, not automatic claim proof.

### `evidence_guard.py`

SQLite locator / row / field / excerpt verification.

### `claim-guard.py`

Epistemic structure + source-verified evidence + recorded approval-ref verification.

### `review-guard.py`

Full-read coverage and current-line quote grounding.

### `state-commit-guard.py`

Forward-only durable-state changeset approval check.

### Semantic Reviewer

Actual prose, causality, voice, continuity, humor and claim-meaning judgment.

---

## 8. Chapter 09 Pilot Lesson

The pilot demonstrated why source support and novel canon must be separated.

Task 157 / Subtasks 320–323 did not directly prove the entire Chapter 09 Miếu Thần / Vô Danh Mật Tịch / Nhất Phẩm Đường sequence. Wider SQLite lookup confirmed that Nhất Phẩm Đường and Du Long Giác are genuine source concepts elsewhere, while the specific Chapter 09 relations/mechanics were not established by the registered evidence.

At the same time, the existing Chapter 09 Canon Diff contains a checked Author approval. Therefore Reliability v2 preserves those choices as current novel canon while refusing to mislabel them as direct Task 157 source truth.

That is the intended behavior.

---

## 9. MVP Acceptance Criteria

The MVP is acceptable when:

- a known entity with an unsupported relation cannot pass merely because the entity exists;
- SQLite evidence locators/excerpts are checked against the actual source DB;
- direct source, inference, unresolved material, adaptation decisions and bridges remain distinguishable;
- approved adaptation canon can coexist with unresolved raw-source provenance;
- a review missing manuscript coverage cannot be declared structurally complete;
- a lexical linter PASS is never presented as semantic prose PASS;
- a lore regex scan PASS is never presented as “Zero Hallucination”;
- current manuscript text always overrides agent memory during subsequent work;
- Author manual prose edits do not trigger version reconciliation or automatic rollback;
- new durable-state writes cannot pass CI without a changed checked Canon Diff;
- no new SHA/locking/workflow-database bureaucracy is introduced.

---

## 10. Out of Scope for MVP

- automatic semantic truth judgment;
- chapter SHA checks;
- content hashes;
- manuscript locking;
- immutable revisions;
- automatic rollback;
- mandatory Author-edit metadata;
- event sourcing;
- workflow databases;
- cryptographic authentication of the Canon Diff checkbox.
