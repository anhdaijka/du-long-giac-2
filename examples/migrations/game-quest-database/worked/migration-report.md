# Worked Migration Report

Status: synthetic example.

## Executive summary

The source encodes one shared opening task, two mutually exclusive level-20 routes, and a shared Stone Gate convergence. The approved adaptation uses two parallel protagonists so both source routes survive without violating mutual exclusivity.

## Reconstructed backbone

`Burned Station -> (Captain Lien route XOR Scholar Vu route) -> Stone Gate Pass -> Masked Courier confrontation`

## Important source distinction

Captain Lien's masked-rider testimony is route-conditioned. The source does not justify promoting `Lien definitely saw the rider` into objective novel canon.

## Adaptation decisions

| Decision | Class | Status |
|---|---|---|
| Preserve burned station and Stone Gate outcomes | DIRECT CANON CANDIDATE | approved |
| Give Lien route and Vu route to separate protagonists | NOVELIZATION BRIDGE / structural adaptation | approved |
| Compress five-seal collection into one investigation sequence | SOURCE-SUPPORTED ADAPTATION | approved |
| Make masked-rider sighting objectively true | unsupported | rejected/unresolved |
| Synchronize protagonists exactly to the same hour | unsupported detail | keep flexible |

## Proposed Story Skills promotion

### Promote when initializing the novel fixture

- two novel protagonists;
- Captain Lien;
- Scholar Vu;
- Warden Pham where needed for first shared arc;
- Burned Courier Station / Willow Crossing;
- Stone Gate Pass;
- Lien-route arc;
- Vu-route arc;
- shared Stone Gate convergence arc;
- open continuity question: `Did Captain Lien actually see the masked rider?`

### Keep migration-only

- raw CSV rows;
- level>=20 gate;
- exact `collect 5` counter;
- implementation flags;
- unused fallback dialogue;
- exact parallel timing not established by source.

## Required novelization bridges

1. Give each protagonist an ordinary motive for choosing their source route.
2. Dramatize or compress the seal/ledger investigations without changing their source outcomes.
3. Create a credible convergence at Stone Gate Pass that preserves different knowledge states.
4. Let route-specific evidence affect the shared masked-courier scene.

## Validation after real promotion

Run:

```bash
npm run story:check
npm run story:doctor
npm run story:report
```

The source files remain evidence; Story Skills becomes the approved novel state.
