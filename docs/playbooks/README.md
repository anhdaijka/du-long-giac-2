# Novel OS Playbooks

Playbooks describe reusable workflows that do not fit the normal blank-novel chapter lifecycle.

Use them as operational procedures, not as a second canon system.

## Source Adaptation Pipeline

When the project starts from an existing narrative source rather than a blank novel, begin here:

1. [`external-source-ingestion.md`](external-source-ingestion.md) — universal source inventory, provenance, reconstruction and approval workflow.
2. [`game-database-novelization.md`](game-database-novelization.md) — quest/task/NPC/map/item/script databases.
3. [`branching-narrative-migration.md`](branching-narrative-migration.md) — mutually exclusive routes, flags, conditional dialogue and convergence.

For an existing prose manuscript, prefer Story Skills `story import` first; use the ingestion playbook only when additional lore/source databases must also be reconciled.

## Core principle

> Preserve the source before interpreting it.  
> Reconstruct before adapting.  
> Adapt before canonizing.

## What belongs where

- Raw or extracted source material stays outside Story Skills canonical state.
- Migration working documents record provenance, source graphs, branch matrices and adaptation proposals.
- Story Skills receives only approved, novel-relevant canon.
- Author decisions remain authoritative over automated extraction or agent inference.

Templates live in `templates/migration/`; reusable prompts live in `prompts/migration/`; synthetic worked examples live in `examples/migrations/`.
