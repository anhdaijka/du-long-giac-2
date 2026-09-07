# External Source Ingestion

Use this playbook when a novel is adapted from an existing narrative corpus rather than created from a blank story bible.

Examples:
- game quest/task databases;
- branching dialogue or visual-novel scripts;
- exported wiki/lore databases;
- screenplay or episode bibles;
- legacy character/world databases;
- mixed folders containing scripts, CSV/JSON/XML/Lua/SQL/Markdown and notes.

This workflow is about **understanding and adapting source material**, not blindly converting files into Story Skills entities.

## Pipeline

`source corpus -> inventory -> extraction/reconstruction -> source graph -> adaptation contract -> author approval -> selective Story Skills canon -> outline/draft`

## Gate 0 — Protect the source

Before interpretation:

- identify the authoritative source location;
- do not modify source files during extraction;
- record source version/commit/build/date when available;
- preserve stable IDs, filenames and paths;
- note encoding, language and format;
- distinguish generated/cache/localization files from authorial content when possible.

If source provenance is unclear, treat that as an explicit risk.

## Gate 1 — Source inventory

Create a source inventory using `templates/migration/source-inventory.md`.

Record:
- source collections and file counts;
- formats and schemas;
- likely narrative-bearing fields;
- identifiers and foreign keys;
- duplicated/localized/generated data;
- known source versions;
- unreadable or missing files;
- confidence in each interpretation.

Do not infer plot yet.

## Gate 2 — Reconstruct the source model

Build a source map and story graph before deciding how the novel should work.

At minimum identify:
- entities: people/NPCs, factions, places/maps, items/artifacts;
- events/tasks/quests;
- prerequisites and outcomes;
- chronology or partial ordering;
- dialogue provenance;
- flags/state changes;
- branch points and mutually exclusive outcomes;
- convergence points;
- repeated or mirrored content;
- contradictions and unresolved gaps.

Use `templates/migration/source-map.md`, `story-graph.md`, and, for branching material, `branch-matrix.md`.

## Evidence classes

Every important reconstructed claim should be marked as one of:

### DIRECT SOURCE
Explicitly present in an authoritative source file/row/dialogue/event.

### SOURCE-SUPPORTED INFERENCE
Not stated directly, but strongly supported by multiple source elements or required by source ordering.

### UNRESOLVED
Source evidence conflicts, is incomplete, or does not permit a stable conclusion.

Do **not** label adaptation inventions here.

## Gate 3 — Separate mechanics from narrative truth

External narrative systems often mix fiction and implementation.

Classify source elements such as:
- gameplay trigger;
- UI/tutorial text;
- repeatable farming task;
- teleport/map transition;
- inventory requirement;
- fail-state/retry logic;
- level gating;
- player convenience duplication;
- canonical event;
- character testimony;
- world lore;
- branch-specific event.

A gameplay rule is not automatically an in-world rule.

## Gate 4 — Adaptation contract

Before promoting anything into Story Skills, write `templates/migration/adaptation-contract.md` and obtain author approval.

The contract should decide:
- fidelity level;
- branch policy;
- chronology policy;
- dialogue policy;
- gameplay-mechanic treatment;
- character merge/split rules;
- source contradiction policy;
- permitted novelization bridges;
- invented-lore boundary;
- ending/outcome preservation policy;
- approval requirements for deviations.

## Adaptation evidence classes

After the contract exists, novel-facing proposals should distinguish:

### DIRECT CANON CANDIDATE
A source fact proposed to survive substantially unchanged in the novel.

### SOURCE-SUPPORTED ADAPTATION
A novel fact or arrangement strongly supported by source evidence but transformed for prose structure.

### NOVELIZATION BRIDGE
New connective material required by prose: internal motivation, transition scene, causal bridge, travel compression, combined encounter, dramatized gameplay action, etc.

Novelization bridges are **not source facts**. They require the level of author approval specified in the adaptation contract.

## Gate 5 — Author approval

Before Story Skills promotion, present:
- reconstructed source summary;
- unresolved contradictions;
- proposed adaptation contract;
- branch/chronology decisions;
- proposed canon promotion set;
- proposed novelization bridges with reasons.

Do not silently resolve source contradictions or branch exclusivity.

## Gate 6 — Selective canon promotion

Story Skills is the novel's state model, not the raw source archive.

Promote only material that the novel needs now:
- central characters;
- durable locations/systems/factions/artifacts;
- approved plot arcs;
- timeline facts;
- continuity questions/promises/state needed for the next drafting horizon;
- glossary terms needed by the prose.

Do not create one Story Skills entity per source row.

After promotion:

```bash
npm run story:check
npm run story:doctor
npm run story:report
```

Fix schema/reference/continuity problems before outlining prose.

## Gate 7 — Draft with provenance intact

During outlining/drafting, keep migration working documents available for traceability but treat Story Skills canon as the current novel truth.

When a draft requires departure from the approved adaptation contract:
1. record the proposed departure;
2. identify affected source facts and canon;
3. get author approval;
4. update Story Skills only after approval.

## Recommended working area

In a real adaptation repository, a project may use a non-canonical working area such as:

```text
migration/
  source-inventory/
  extracted/
  graphs/
  decisions/
```

or another author-approved path.

Do not require this exact directory name. The important boundary is that raw/extracted source data is not confused with Story Skills canon.

## Stop conditions

Stop and ask for author guidance when:
- two authoritative source files disagree on an irreversible outcome;
- branch policy would erase a major source route;
- an inferred chronology changes character responsibility;
- a proposed character merge changes identity/relationships;
- a novelization bridge invents substantial new lore;
- missing source prevents a reliable reconstruction of a major arc.

## Anti-overengineering rule

Do not build a custom parser/ETL framework merely because the source uses a new file format. Agents can often inspect common text/database formats directly.

Automate parsing only after repeated real projects demonstrate a stable recurring transformation worth encoding.
