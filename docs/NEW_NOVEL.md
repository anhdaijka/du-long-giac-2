# Starting a Real Novel from Novel OS

`anhdaijka/novel-os` is a public framework/template repository. Unpublished manuscript content should normally live in a separate **private** repository.

## First decide: blank novel or source adaptation?

### Blank/new novel

Use the normal initialization flow below.

### Existing game/database/lore source

If the novel is adapted from an existing narrative corpus — game quest/task databases, branching dialogue, scripts, lore/wiki exports, legacy story bibles, etc. — do **not** immediately translate raw source rows into Story Skills canon.

Before story canonization:

1. read `docs/playbooks/external-source-ingestion.md`;
2. use the game/branching playbooks when applicable;
3. inventory and reconstruct source structure/provenance;
4. create an adaptation contract;
5. obtain author approval;
6. then initialize/promote only the novel-relevant canon needed for the next drafting horizon.

See `examples/migrations/game-quest-database/` for a synthetic worked example.

## Recommended blank-novel flow

1. Create a private repository for the novel from this template/codebase.
2. Clone the private repository locally.
3. Run `npm run bootstrap`.
4. Run `npm run os:doctor`.
5. Initialize the Story Skills project with `npm run init-story -- "Title" ...`.
6. Fill `author/creative-constitution.md`, `author/style-bible.md`, and `author/boundaries.md`.
7. Open the repo root in Antigravity and Obsidian.
8. Run the Phase 3 lifecycle test once to verify local tooling.
9. Start the first real session with `prompts/session/start-session.md`.

## Keep public and private responsibilities separate

Public Novel OS should contain framework code, synthetic fixtures, docs, and tests.

Private novel repositories contain manuscript prose, actual character/world canon, research notes, author decisions, session state, and — for source adaptations — licensed/private raw source material and migration working artifacts.

Do not paste unpublished prose or proprietary source databases into public regression fixtures.
