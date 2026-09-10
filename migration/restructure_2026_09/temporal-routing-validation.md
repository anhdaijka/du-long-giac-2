# D-064 routing migration verification

Author approved TCQ-01–05 / CCQ-01–09 with “theo đề xuất”, 2026-09-10. R-90 and the temporal-continuity contract record the full policy.

Changed operational surfaces: AGENTS.md, GEMINI.md, Home.md, rules 03/04/05/07, docs/WORKFLOW.md, central Gemini evidence-review playbook, chapter/review/canon-diff templates, genealogy matrix rule reference, Gemini router and series allocation index. Prior chronology/travel matrices are preserved under archive/pre_restructure_2026_09/temporal_before_D064 with redirect files at former paths.

gate-guard.py no longer hard-codes protagonist ages or assumes the opening year. It checks temporal routing and explicitly reports semantic continuity NOT CHECKED. lore-grounder.py no longer extracts place names from the old travel estimates; entity recognition does not prove route/travel claims. Review requires the actual source/author receipts; no unverified new allowlist was introduced.

Checks performed:

- temporal-routing-test.py: 4 passing regression tests (current route, missing policy, stale reference despite override, missing entry routing).
- temporal-routing-check.py: passed operational route scan.
- Python compile for both changed tools and both new routing scripts: passed.
- npm run gate:check: passed routing; no chapter files found, so no manuscript temporal semantics certified.
- git diff --check: passed; Git emitted existing LF/CRLF normalization warnings.
- npm run execution:check: passed, including D56 artifact-presence checks; not semantic approval.

Residual old-path mentions are archive redirects, historical decision/contradiction evidence, test fixtures and the regression deny-pattern. They are not operational evidence loaders. The current policy does not constitute a full-series timeline, historical/travel audit, initialized story state or Gemini runtime validation. story.md is absent; no state was invented to satisfy that old startup instruction.
