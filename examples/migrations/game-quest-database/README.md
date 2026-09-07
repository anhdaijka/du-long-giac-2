# Synthetic Game Quest Database Migration Example

This public-safe fixture demonstrates the Source Adaptation Pipeline without using any real game IP.

## Scenario

A small wuxia-style RPG database encodes a level-20 main-story branch. The player can help either **Captain Lien** or **Scholar Vu** investigate the same burned courier station. The routes are mutually exclusive but later converge at **Stone Gate Pass**.

The fixture intentionally includes:
- quest prerequisites;
- mutually exclusive routes;
- route-specific dialogue;
- one shared convergence quest;
- an implementation-heavy collect task;
- a source ambiguity around who first saw the masked rider.

## Source files

- `source/tasks.csv`
- `source/npcs.csv`
- `source/dialogue.csv`
- `source/flags.csv`

These files are the synthetic external source corpus. They are **not** Story Skills canon.

## Worked migration artifacts

- `worked/source-inventory.md`
- `worked/story-graph.md`
- `worked/branch-matrix.md`
- `worked/adaptation-contract.md`
- `worked/migration-report.md`

The worked example chooses **parallel protagonists** so both route-exclusive storylines can survive in prose without pretending one player performed mutually exclusive actions.

## What this example teaches

1. Read the source before inventing novel structure.
2. Preserve quest/dialogue/flag provenance.
3. Do not treat `collect 5 seals` literally if it is only a progression mechanic.
4. A shared quest after two routes is a convergence point, not proof that both routes leave characters in identical states.
5. Record the masked-rider contradiction instead of choosing a convenient truth.
6. Promote only novel-relevant entities after the adaptation contract is approved.

This fixture is documentation, not a regression test for game-file parsing.
