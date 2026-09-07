# Inspect External Narrative Source

Act as the source-ingestion analyst for this repository.

Before adapting or canonizing anything:

1. Read `AGENTS.md`, `.agents/rules/09-source-adaptation.md`, and `docs/playbooks/external-source-ingestion.md`.
2. Inspect the supplied external source corpus without modifying it.
3. Build or update a source inventory from `templates/migration/source-inventory.md`.
4. Identify stable IDs, schemas, narrative-bearing collections, branch/state fields, duplicate/generated/localized content, unreadable areas and source-version risks.
5. Do not infer the novel structure yet.
6. Do not create Story Skills entities yet.
7. Report source coverage, unknowns and the safest next reconstruction action.

Keep direct source evidence separate from inference. If the source is a game database, route next to `docs/playbooks/game-database-novelization.md`.
