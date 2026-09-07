# Worked Reconstructed Story Graph

Status: reconstructed source model; not Story Skills canon.

## Nodes

| Node | Source | Summary | Preconditions | Outcome | Next | Evidence |
|---|---|---|---|---|---|---|
| S0 | T100 | Inspect burned courier station | level >=20 | station seen | S1A or S1B | DIRECT SOURCE |
| S1A | T110 | Work with Captain Lien | S0 + LIEN choice | Lien route; rider claim | S2 | DIRECT SOURCE |
| S1B | T120 | Work with Scholar Vu | S0 + VU choice | Vu route; ledger found | S2 | DIRECT SOURCE |
| S2 | T130 | Reach Stone Gate Pass | either route complete | convergence | S3 | DIRECT SOURCE |
| S3 | T140 | Confront masked courier | pass reached | courier flees | — | DIRECT SOURCE |

## Partial order

`S0 -> (S1A XOR S1B) -> S2 -> S3`

The source does **not** support `S1A -> S1B` or `S1B -> S1A`.

## Route-specific knowledge

### Lien route

- Captain Lien's route-specific line claims direct sighting of a masked rider (`D010`).
- The player does not recover Scholar Vu's ledger through source task `T120`.

### Vu route

- Scholar Vu's ledger introduces the unexplained third seal (`D020`).
- Captain Lien's route-specific alternate dialogue says he only heard about a rider (`D011`).

These statements must stay attached to their route conditions.

## Gameplay-heavy node

`T110` objective `Collect 5 broken courier seals` is DIRECT SOURCE as a mechanic, but the source does not establish that five separate dramatic collection incidents matter to story causality.

Novel treatment remains an adaptation decision.

## Convergence risk

`T130` is a shared quest id, but incoming characters possess different knowledge:
- Lien route brings the direct-rider claim.
- Vu route brings the ledger/third-seal evidence.

A novel convergence cannot simply erase those differences.

## Unresolved source question

The source does not establish an objective answer to whether Captain Lien actually saw the masked rider. It only establishes route-conditioned statements. Treat objective sighting status as **UNRESOLVED** unless another source resolves it.
