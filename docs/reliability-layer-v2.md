# Novel OS Reliability Layer v2

## Status

Approved architecture for `du-long-giac-2`. Implement here first; only proven generic pieces should later be ported back to `anhdaijka/novel-os`.

## Goal

Increase autonomous reliability without turning a single-author fiction repository into a bureaucratic workflow system.

The layer focuses on five primitives:

1. Evidence Packet
2. Claim Ledger
3. Full-Read Review Protocol
4. Completion Verification
5. Author Text Supremacy

## North Laws

### NL-1 — Source truth is evidence-bound

A durable factual assertion derived from the KT2 source corpus must be traceable to concrete source evidence. Entity existence alone does not prove a relation, event, motive, chronology, possession, knowledge state, genealogy, or faction alignment.

### NL-2 — Canon truth is approval-bound

Source evidence, source-supported inference, adaptation decisions and novelization bridges are not automatically novel canon. **Every durable canon promotion, including a `DIRECT_SOURCE` claim, still requires the existing author approval gate.** Evidence strength controls epistemic confidence; it never grants autonomous canon-write authority.

### NL-3 — Agent completion is verifier-bound

An agent may report work performed, but it may not make a workflow step complete merely by saying it is complete. Machine-checkable deliverables decide completion where a deterministic verifier exists.

### NL-4 — Current Author Text Wins

The current manuscript in the repository is authoritative over any previous agent draft, review snapshot, session summary, cached context or remembered wording.

Before reviewing, revising, continuing or deriving canon from a chapter, re-read the current chapter file.

If current text differs from an agent-produced version, treat the difference as an intentional author edit unless the author explicitly says otherwise.

Never restore, overwrite or normalize an author edit merely to match an older plan, review or generated draft.

Canon validation may reject or flag a durable claim without reverting the author's prose.

### NL-5 — Verification must describe what it actually proves

A regex regression scanner must not call itself a zero-hallucination proof. An entity grounder must not imply that relations involving a known entity are grounded. A lexical linter must not imply semantic literary quality.

Verifier names and PASS messages must match their real scope.

---

## 1. Evidence Packet

Default path:

`research/evidence/chapter_XX.json`

The Evidence Packet records source observations used to constrain planning and drafting. It is not canon.

Each evidence item must have:

- stable `evidence_id`
- `source_kind`
- a concrete `locator`
- a short verbatim or normalized `excerpt`
- optional notes about source conditions, branch flags, speaker reliability or ambiguity

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
      "excerpt": "<source excerpt>",
      "notes": "Direct task/subtask evidence; no inferred motive."
    }
  ]
}
```

Evidence IDs identify observations, not conclusions.

---

## 2. Claim Ledger

Default path:

`research/claims/chapter_XX.json`

The Claim Ledger records assertions the chapter plan, prose or proposed canon state depends on.

Allowed epistemic states:

- `DIRECT_SOURCE`
- `SOURCE_SUPPORTED_INFERENCE`
- `UNRESOLVED`
- `ADAPTATION_DECISION`
- `NOVELIZATION_BRIDGE`

Required distinction:

`entity exists` is not equivalent to `claim about entity is supported`.

A claim should be written as an explicit proposition, for example:

```text
Bạch Thu Lâm knows X by the evening of 1191-08-20.
```

not merely:

```text
Bạch Thu Lâm
```

### Claim rules

`DIRECT_SOURCE`
- requires at least one evidence ID;
- must not contain additional causal or motivational conclusions absent from that evidence;
- still uses `promotion: author_approval_required` for durable canon changes.

`SOURCE_SUPPORTED_INFERENCE`
- requires at least one evidence ID;
- requires a non-empty `reasoning` field;
- uses `promotion: author_approval_required` before durable canon promotion.

`UNRESOLVED`
- records contradiction, ambiguity or missing evidence;
- uses `promotion: blocked`;
- cannot be promoted as objective canon truth while unresolved.

`ADAPTATION_DECISION`
- records an author-approved or author-proposed transformation choice;
- must not be misrepresented as something the raw game source requires;
- durable promotion still requires author approval.

`NOVELIZATION_BRIDGE`
- allows connective tissue, gesture, micro-action, sensory realization and other literary bridging;
- must not silently create a durable source fact;
- durable promotion requires explicit author approval.

Example:

```json
{
  "chapter": "10",
  "claims": [
    {
      "claim_id": "CL-10-001",
      "claim": "<explicit proposition>",
      "epistemic_status": "DIRECT_SOURCE",
      "evidence": ["EV-10-001"],
      "durability": "durable",
      "promotion": "author_approval_required",
      "reasoning": ""
    }
  ]
}
```

---

## 3. Claim Verification

`claim-guard` is a structural epistemic verifier, not an oracle.

It may prove:

- referenced Evidence Packet exists;
- evidence IDs are unique;
- claim IDs are unique;
- referenced evidence IDs exist;
- epistemic status is recognized;
- required reasoning/evidence fields are present;
- unresolved claims are blocked from promotion;
- durable source/inference/bridge claims do not bypass author approval structurally.

It may not claim:

- that every sentence in the manuscript is factually true;
- that an inference is logically correct merely because it cites evidence;
- that an evidence locator/excerpt is semantically faithful to the game source merely because the JSON is well-formed;
- that entity grounding proves a relation.

Semantic claim auditing remains a reviewer responsibility, but the reviewer must work against explicit claims and evidence rather than latent memory.

---

## 4. Full-Read Review Protocol

Review must operate on the current chapter file.

The reviewer must read the manuscript sequentially from beginning to end. Reviews contain machine-readable line coverage in addition to literary findings.

Recommended marker format:

```text
- `L1-L96` — concrete observation from this range
- `L97-L188` — concrete observation from this range
- `L189-L281` — concrete observation from this range
- `L282-L374` — concrete observation from this range
```

Coverage ranges must collectively cover the current manuscript. No SHA, immutable version ID or author-edit lock is required.

A deterministic review guard validates coverage structure; it does not claim the literary judgments are correct.

The literary reviewer must still provide issue severity, location, evidence, why it matters and recommended intervention.

### Distinguish verification layers

- lexical/meta scanner: catches known textual patterns;
- entity grounder: catches likely unknown entities;
- claim guard: checks evidence/claim structure;
- review guard: checks full-read coverage/report completeness;
- semantic reviewer: evaluates causality, prose, voice, show-vs-tell, humor execution, continuity and claim meaning.

No lower layer may claim the guarantees of a higher layer.

---

## 5. Comedy / Show-Don't-Tell Evaluation

The 65/25/10 creative direction remains a creative target, not a numeric linter score.

For comic scenes, reviewers should inspect observable execution:

1. setup creates an expectation;
2. misdirection bends the expectation;
3. payoff lands through action/dialogue/image;
4. afterbeat preserves character voice;
5. narrator does not explain why the joke was funny.

A few comic phrases do not prove that a scene achieved the intended comedic register.

---

## 6. Completion Verification

Keep completion state deliberately lightweight.

A workflow step is complete only when its required artifact exists and its relevant verifier passes.

Example conceptual state:

```yaml
tasks:
  source_research: done
  claim_check: done
  brief: done
  draft: done
  full_review: pending
  canon_diff: blocked
```

Do not introduce a workflow database, content hashes, immutable manuscript versions or mandatory author-edit metadata for v2 MVP.

---

## 7. Canon Boundary

Manuscript prose and durable canon are different authority domains.

If the author manually writes a sentence that conflicts with source/canon:

1. preserve the author's current prose;
2. flag the conflicting durable claim during review/canon-diff preparation;
3. do not promote the unsupported claim automatically;
4. do not silently revert the manuscript.

Canon promotion remains governed by the existing author-approved Canon Diff gate.

---

## 8. Existing Tools: Revised Responsibilities

### `lore-guard.py`

Role: known-regression scanner for explicitly encoded lore mistakes.

It must not describe a clean scan as proof of "Zero Hallucination".

### `lore-grounder.py`

Role: closed-world entity plausibility check.

It must not imply that relationships or events involving those entities are verified.

### `meta-leakage-scanner.py`

Role: lexical/meta/style-pattern linter.

A clean result does not equal semantic prose-quality approval.

### `gate-guard.py`

Role: lifecycle gate aggregator.

It should depend on real verifier results rather than considering a review complete merely because a review file contains gate headings.

---

## 9. MVP Scope

Implement first:

1. Evidence/Claim JSON templates.
2. `scripts/claim-guard.py`.
3. Full-read coverage section in `templates/review-report.md`.
4. `scripts/review-guard.py`.
5. Author Text Supremacy in agent/workflow contracts.
6. Rename misleading verifier success messages.
7. Wire deterministic guards into `gate-guard.py` and CI only after the individual guards are stable.

Out of scope for MVP:

- chapter SHA checks;
- content hashes;
- manuscript locking;
- immutable revisions;
- automatic rollback;
- mandatory author-edit metadata;
- event sourcing;
- a workflow database;
- automatic semantic truth judgment.

---

## 10. Acceptance Criteria

The MVP is acceptable when:

- a known entity with an unsupported relation can no longer pass merely because the entity exists;
- direct source, inference, unresolved material, adaptation decisions and bridges remain distinguishable;
- a review missing any manuscript line range cannot be declared structurally complete;
- a lexical linter PASS is never presented as semantic prose PASS;
- a lore regex scan PASS is never presented as "Zero Hallucination";
- current manuscript text always overrides agent memory during subsequent work;
- author manual edits do not trigger version reconciliation or automatic rollback;
- canon promotion can reject/flag a claim without editing the author's prose;
- no new SHA/locking bureaucracy is introduced.
