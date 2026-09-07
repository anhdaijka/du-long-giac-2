# Game Database Novelization

Use after `external-source-ingestion.md` when the source is a game data/script corpus containing quests/tasks, NPC dialogue, maps, items, flags, triggers or related implementation data.

The objective is to reconstruct the **story the game encodes** before deciding how prose should adapt it.

## Minimum reconstruction domains

### 1. Source schema
Identify:
- task/quest tables/files;
- subtask/objective structures;
- NPC definitions;
- dialogue/localization tables;
- map/location IDs;
- faction/reputation fields;
- item/artifact references;
- triggers/flags/conditions;
- rewards/fail states;
- level or progression gates.

Preserve stable IDs and source paths in migration notes.

### 2. Quest graph
For every narrative-bearing quest/task, capture:
- source id;
- prerequisites;
- starter/source NPC/event;
- objectives;
- completion condition;
- outcome/state changes;
- follow-up tasks;
- mutually exclusive alternatives;
- whether repeatable or one-shot;
- whether the task is main story, side story, tutorial, grind, transport or utility.

Do not infer chapter structure yet.

### 3. Dialogue provenance
For each important line or exchange, preserve:
- source file/table/id;
- speaker;
- recipient/player context;
- required state/flag;
- branch/route;
- localization/version if relevant.

Repeated lines may be implementation duplication rather than repeated story events.

### 4. Partial chronology
Games often encode order indirectly.

Use:
- prerequisite chains;
- level gates;
- state flags;
- map unlocks;
- NPC state changes;
- dialogue references to earlier events;
- reward/item dependencies;
- mutually exclusive route conditions.

Represent uncertain order as a partial order instead of inventing exact dates.

### 5. Branches and convergence
Record:
- player choices;
- route-exclusive quests;
- alternate NPC outcomes;
- branch-specific deaths/alliances;
- shared later quests;
- convergence points;
- data that exists only because all routes must be supported by the executable game.

Use the branching playbook for non-trivial route systems.

## Gameplay mechanic translation

Classify each mechanic before adapting it.

| Game element | Novel treatment candidates |
|---|---|
| Kill N enemies | compress into one consequential conflict, montage, report, or omit |
| Collect N items | convert to search, preparation, evidence gathering, bargaining, or omit |
| Level gate | replace with elapsed time, training, social permission, capability, or remove |
| Teleport/map transition | dramatize travel only when story-relevant |
| Repeatable quest | usually non-canon routine/background unless source says otherwise |
| Respawn/retry | normally implementation-only unless explicitly diegetic |
| Reward item | keep only if it matters to plot/character/world |
| Quest marker | replace with character motive/information source |
| NPC standing idle | implementation-only unless narratively meaningful |

Never preserve a mechanic just because it was mechanically required in the game.

## Narrative reconstruction questions

Before adaptation, answer:
- Who wants what at each main-story node?
- Why does the next event happen causally, not merely because a quest unlocked?
- What does the player avatar know at that point?
- Which NPCs know more than they say?
- Which outcomes are route-specific?
- Which scenes are absent because gameplay jumps over travel, waiting, grief or aftermath?
- Which repeated interactions are abstractions of longer relationships?
- Which bosses/combat encounters are plot events versus progression checks?

## Source fidelity classes for novelization

Use these three labels in adaptation working notes:

### DIRECT CANON
The source explicitly establishes the fact/outcome/dialogue meaning.

### SOURCE-SUPPORTED INFERENCE
The source strongly supports the conclusion, but no single row/file states it completely.

### NOVELIZATION BRIDGE
New prose material required to connect source events naturally without contradicting them.

Examples of bridges:
- internal monologue;
- a farewell before a quest transition;
- travel between maps;
- showing the emotional aftermath of an NPC death;
- combining mechanically duplicated encounters into one scene;
- causal dialogue explaining why a character takes the next source-mandated action.

## Fidelity risks

Flag before author approval:
- merging two NPCs with distinct source histories;
- moving an event across a branch boundary;
- making optional side lore mandatory to the main plot;
- treating all possible player actions as having happened;
- using a later-state NPC line in an earlier scene;
- turning a gameplay reward into an important artifact without source support;
- choosing one ambiguous source explanation as objective truth;
- removing a route whose outcome materially changes later canon.

## Suggested output before canon promotion

Produce:
1. source inventory;
2. quest/story graph;
3. branch matrix where needed;
4. entity/source map;
5. contradiction register;
6. proposed adaptation contract;
7. proposed novel structure at arc/POV level;
8. explicit list of novelization bridges;
9. selective Story Skills promotion plan.

Only after author approval should the agent create/update canonical character, worldbuilding, plot and continuity files.

## Large-source strategy

For hundreds or thousands of task files:

1. reconstruct the main progression backbone first;
2. identify branch roots and convergence points;
3. attach side content only when it changes character/world understanding or later causality;
4. keep raw source searchable rather than copying it into canon;
5. expand the graph incrementally by narrative region/level/act.

Do not summarize a huge database from a handful of convenient files and call the story reconstructed.
