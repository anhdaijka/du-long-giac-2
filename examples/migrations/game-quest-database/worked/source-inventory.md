# Worked Source Inventory

Status: synthetic migration artifact; not Story Skills canon.

## Source identity

- Project: Synthetic Wuxia Quest DB
- Authority: files under `../source/`
- Version: fixture v1
- Formats: CSV
- Read-only source assumption: yes

## Collections

| Collection | Count | Stable ID | Narrative role | Notes |
|---|---:|---|---|---|
| `tasks.csv` | 5 | `task_id` | quest graph | includes branch + convergence |
| `npcs.csv` | 5 | `npc_id` | entities | all narrative-bearing |
| `dialogue.csv` | 7 | `dialogue_id` | conditional dialogue | route conditions are critical |
| `flags.csv` | 7 | `flag` | state/branch semantics | reveals mutual exclusivity |

## Initial findings

- `T110` and `T120` are mutually exclusive route quests.
- `T130` accepts either route and is a convergence node.
- Captain Lien's dialogue changes materially by route; lines cannot be pooled as unconditional biography.
- `Collect 5 broken courier seals` is likely gameplay-heavy and should not automatically become five literal collection scenes.
- The fixture has no exact dates; chronology should remain relative.

## Risks

- Reading `D010` and `D011` without route conditions creates an apparent contradiction about whether Lien saw the rider.
- A naive linear import would falsely make the protagonist complete both mutually exclusive quests.
