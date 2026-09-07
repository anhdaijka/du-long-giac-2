# Agent Role Prompts

These are reusable role contracts for Antigravity sessions/subagents. They are not a second rules system: `.agents/rules/` remains authoritative.

Use the smallest role that matches the task:

- [`director.md`](roles/director.md) — orchestrate, inspect state, merge feedback
- [`planner.md`](roles/planner.md) — plan arcs/chapters/scenes without drafting prose
- [`writer.md`](roles/writer.md) — execute an approved scene plan
- [`reviewer.md`](roles/reviewer.md) — diagnose without immediately rewriting
- [`researcher.md`](roles/researcher.md) — gather evidence without canonizing it

Recommended pattern:

`Director -> Planner -> Author approval -> Writer -> Reviewer(s) -> Director synthesis -> Author approval -> Revision -> Canon diff -> Author approval`

Do not let parallel subagents write canonical state concurrently.

## External source migration prompts

When adapting an existing game/database/lore corpus, use the Source Adaptation Pipeline rather than the normal blank-story flow:

1. [`inspect-source.md`](migration/inspect-source.md) — inventory source structure/provenance without adapting it.
2. [`reconstruct-story-graph.md`](migration/reconstruct-story-graph.md) — recover entities, events, chronology, branches, flags and contradictions.
3. [`propose-adaptation.md`](migration/propose-adaptation.md) — propose branch/fidelity/mechanics/bridge policy and stop at author approval.
4. [`migrate-approved-canon.md`](migration/migrate-approved-canon.md) — selectively promote only approved novel state into Story Skills and validate it.

Read `docs/playbooks/external-source-ingestion.md` before using these prompts. Game databases and branching narratives have additional playbooks under `docs/playbooks/`.
