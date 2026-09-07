# Branching Narrative Migration

Use this playbook when the source contains mutually exclusive routes, player-choice outcomes, conditional dialogue, alternate character states, or multiple endings.

Do not force the source into one linear timeline until the adaptation contract chooses how branches should be represented.

## Reconstruct first

For each branch point record:
- branch id/name;
- triggering choice/condition;
- source files/rows;
- prerequisites;
- route-exclusive events;
- character state changes;
- deaths/survivals;
- faction/relationship changes;
- route-exclusive lore;
- convergence point, if any;
- downstream contradictions with other routes.

Use `templates/migration/branch-matrix.md`.

## Branch policy options

The author should explicitly choose one or a hybrid:

### Single-route adaptation
Select one source route as the novel's primary canon.

Use when:
- one route is clearly primary;
- the novel needs one protagonist continuity;
- alternate routes add little unique thematic value.

Record what is omitted and why.

### Parallel-protagonist adaptation
Assign mutually exclusive routes to separate protagonists or timelines, allowing source-exclusive events to coexist without pretending one player performed incompatible actions.

Use when:
- branches contain substantial unique story;
- different routes illuminate the same conflict from different sides;
- convergence can be reconstructed plausibly.

### Braided/alternate-timeline adaptation
Preserve multiple route realities explicitly as alternate timelines/versions.

Use only when the novel's form genuinely supports it; do not choose this merely to avoid adaptation decisions.

### Composite adaptation
Merge compatible material from multiple branches into a new novel sequence.

Highest fidelity risk. Every merged element must be checked for:
- incompatible character knowledge;
- mutually exclusive deaths;
- impossible location/timing;
- duplicated revelations;
- contradictory relationships;
- player agency being reassigned without reason.

## Convergence rules

A game can converge branches because implementation needs a shared next quest. A novel needs causal credibility.

For every convergence ask:
- What different state does each route bring into the shared event?
- Does the shared dialogue assume one specific route?
- Are route-specific consequences silently reset by the game?
- Does the novel need separate variants of the convergence scene?
- Can one route's emotional consequences reasonably disappear?

Do not treat a shared quest id as proof that all branch states are equivalent.

## Conditional dialogue

Preserve condition provenance.

A line available only when `flag_x=true` cannot be reused as generic characterization without checking what that flag means.

Classify dialogue as:
- route-independent;
- route-specific;
- state-specific;
- optional/repeatable;
- localization variant;
- implementation fallback.

## Contradictions

When two branches establish incompatible facts, record both as source truth **within their routes**.

Do not resolve them by declaring one false unless the source itself establishes a hierarchy.

The adaptation contract decides which truth enters novel canon.

## Parallel route timeline

When adapting branches through separate protagonists, build a parallel timeline with:
- shared world events;
- route-local events;
- earliest/latest possible ordering;
- communication opportunities;
- convergence windows;
- impossible overlaps.

Avoid synchronizing events more precisely than source evidence supports.

## Story Skills promotion

Story Skills should represent the **approved novel architecture**, not every source branch.

For a parallel-protagonist novel, create arcs/timeline/state that describe the novel's parallel strands.

Keep rejected/unselected source routes in migration working material, not canonical character state.

## Author approval gate

Before linearization or branch merging, show:
- branch graph;
- material unique to each route;
- irreversible differences;
- proposed branch policy;
- fidelity losses;
- novelization bridges needed for convergence.

Do not choose a branch policy silently.
