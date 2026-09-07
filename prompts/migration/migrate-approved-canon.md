# Migrate Approved Adaptation into Story Skills Canon

Act as the canon migration operator.

Do not run this workflow unless the adaptation contract and the relevant migration decisions are explicitly author-approved.

Read:
- `AGENTS.md`
- `.agents/rules/09-source-adaptation.md`
- the approved adaptation contract
- the latest migration report
- current Story Skills state

Then:

1. Confirm exactly which proposed items are approved for promotion.
2. Promote only the minimum novel-relevant set needed for the next drafting horizon.
3. Preserve source IDs/provenance in descriptive notes where useful, without turning raw source rows into canon entities.
4. Keep unselected routes, raw data, implementation mechanics and unresolved contradictions outside Story Skills canon.
5. Update author decisions when the approved adaptation choice is durable.
6. Run deterministic validation:
   - `npm run story:check`
   - `npm run story:doctor`
   - `npm run story:report`
7. Report every created/updated canonical entity and any remaining migration-only material.
8. Do not draft prose in the same operation unless the author explicitly requested drafting after validation.

If approved adaptation decisions conflict with existing Story Skills canon, stop and present a canon diff instead of silently overwriting state.
