# Source Adaptation Agent Eval

Purpose: verify that a new agent/runtime can discover and follow Novel OS's Source Adaptation Pipeline without being hand-held through every file.

Use the synthetic fixture at `examples/migrations/game-quest-database/`.

## Setup

Start a fresh agent session in the repository root. Do not pre-explain the migration rules beyond this user request:

> I have a small game quest database under `examples/migrations/game-quest-database/source/`. I want to novelize it with Novel OS. Inspect it and tell me the safest next steps. Do not write prose yet.

## Pass criteria — discovery / routing

The agent should:

- read `AGENTS.md` and discover external-source adaptation mode;
- route to `.agents/rules/09-source-adaptation.md` and relevant playbooks;
- avoid immediately running Story Skills init/canon promotion from raw CSV rows;
- preserve source provenance and stable IDs;
- recognize that raw source data and novel canon are different layers.

## Pass criteria — reconstruction

The agent should correctly identify:

- `T110` and `T120` as mutually exclusive routes;
- `T130` as a convergence node;
- Captain Lien's dialogue as route-conditioned rather than unconditional biography;
- `collect 5 broken courier seals` as a likely gameplay-heavy mechanic rather than five mandatory novel scenes;
- the source does not establish an objective answer to whether Lien truly saw the masked rider.

## Pass criteria — epistemic labeling

The agent should distinguish at least:

- direct source evidence;
- source-supported inference;
- unresolved source contradiction/gap;
- adaptation decisions;
- novelization bridges.

It should not present the parallel-protagonist worked solution as if the raw source itself required it unless it explicitly inspected the worked example and labels it as an example/adaptation choice.

## Pass criteria — adaptation gate

When asked to continue adaptation planning, the agent should:

- propose an adaptation contract;
- surface branch-policy choices rather than silently linearize the game;
- explain fidelity risks;
- propose a selective canon promotion set;
- stop at author approval before writing Story Skills canon.

## Fail conditions

Fail if the agent:

- creates one Story Skills entity per raw row without approval;
- treats both mutually exclusive quests as actions of one protagonist by default;
- strips dialogue conditions and declares Lien both saw and did not see the rider;
- invents lore to reconcile the source without labeling it;
- treats source flags as magical/in-world facts automatically;
- copies all source data into canonical directories;
- drafts prose before source/adaptation policy is sufficiently reconstructed;
- claims `story import` or `story migrate` automatically solves structured game database adaptation.

## Optional second-turn prompt

> Preserve both major routes if possible. Propose the adaptation architecture and show which parts are source facts versus novelization bridges.

A strong result should consider parallel protagonists as one viable option, while still presenting it as an adaptation decision requiring author approval.

## Notes

This is a qualitative model/runtime eval, not a parser or CI fixture. Passing it should not modify the repository's story state.
