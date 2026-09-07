# Review Rule

Review before rewriting.

Mandatory Quality Binding:
- Audit all drafts against `.agents/rules/11-prose-quality-contract.md` and run `npm run lint:prose`.
- Structure review according to the 5 Literary Review Gates, rigorously checking the 5 Workflow Safeguards:
  - **Gate A: Minimal Hard Regression & Provenance Lock**
    - Provenance verification: YAML frontmatter MUST declare valid `provenance` referencing verifiable Task ID/Subtask ID in `story_database.sqlite3`.
    - Spatiotemporal Verification: Check movements, couriers, and news against `worldbuilding/geography/travel_matrix.md`. Flag any instantaneous travel or ungrounded cross-regional rumors.
    - Epistemic Horizon Check: Check POV character's knowledge boundary in `characters/<character>.md`. Flag any authorial omniscience, premature lore reveals, or characters knowing facts they have not learned in-world.
  - **Gate B: Blind Reader & Narrative Propulsion**
    - Pacing check: Ensure scenes develop organically within their assigned scope without premature climaxes or rushing past emotional beats.
    - Dramatic propulsion, human pressure, scene arc (clear beginning, mounting tension, Kim Dung atmospheric ending).
  - **Gate C: Character Agency, Martial Progression & Living Texture**
    - Martial Tier Check: Cross-check combat techniques, inner force, and weapons against the character's designated tier in `characters/<character>.md`. Flag any premature unlocks or power creep disconnected from character growth.
    - Living Plebeian Texture: Check integration of everyday life (local trades, prices, dialect, ambient dialogue from the corpus). Ensure the scene is not a dry "quest turn-in".
    - Authentic character voice and interpersonal dynamics.
  - **Gate D: Voice, Rhetoric & Naturalness**
    - Pure show-don't-tell enforcement (zero filter words, sensory anchoring).
    - Camera boundary (strict third-person limited, no head-hopping).
    - No explanatory scaffolds (`đó là`, `đây là`, `đó chính là`, `vốn là`, `chính là`).
    - Classical Kim Dung tone with subtle wuxia atmosphere.
  - **Gate E: Word Count & Structural Substantiality**
    - Golden Word Count Band: **4,000 – 4,800 words** (Hard floor: 3,500 words; Soft ceiling: 5,200 words).
    - If words < 3,500: Flag as defect (insufficient scene texture or rushed beats).
    - If words > 5,200: Flag for chapter split into two distinct, well-paced chapters.
    - Ensure zero empty filler; every paragraph must advance character, texture, or conflict.

Every actionable issue should include:
- severity: critical / major / minor / optional
- location
- problem
- why it matters
- evidence
- recommended intervention

Do not use an opaque aggregate quality score as the acceptance decision.

Review Report Contract:
```markdown
# Review Report: Chapter [XX]

## Gate Status:
- Gate A (Hard Regression & Provenance): PASS / FAIL (Notes)
- Gate B (Blind Reader & Pacing): PASS / FAIL (Notes)
- Gate C (Agency, Martial Tier & Living Texture): PASS / FAIL (Notes)
- Gate D (Voice, Rhetoric & Linters): PASS / FAIL (Notes)
- Gate E (Word Count Band: [Count] words): PASS / FAIL (Notes)

## Findings & Action Items:
[List of issues by severity]

## Verdict:
[APPROVED / REVISE_REQUIRED]
```



