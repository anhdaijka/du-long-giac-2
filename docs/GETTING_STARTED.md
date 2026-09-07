# Getting Started

## 1. Clone

```bash
git clone https://github.com/anhdaijka/novel-os.git
cd novel-os
```

## 2. Install agent skills

```bash
npm run bootstrap
```

Optional prose skill:

```bash
npm run bootstrap -- --with-better-writing
```

The bootstrap uses exact commits from `config/upstreams.json` and copies skills to `.agents/skills/`.

## 3. Choose the project entry path

### Blank/new novel

Initialize the Story Skills schema:

```bash
npm run init-story -- "The Tide Room" \
  --genre mystery \
  --sub-genre coastal \
  --setting-era near-future \
  --pov third-person-limited \
  --tense past \
  --theme truth \
  --theme memory \
  --synopsis "A diver finds a sealed room under a storm-damaged harbor."
```

`init-story` runs the pinned Story Skills CLI in a temporary directory and merges its generated canonical paths into this repo root. This deliberately avoids maintaining a second copy of the Story Skills schema in Novel OS.

### Existing external narrative source

If the project starts from a game database, quest scripts, branching dialogue, lore/wiki export, legacy story bible, or another structured narrative corpus, **do not immediately populate Story Skills from the raw source**.

First read:

1. `AGENTS.md`
2. `.agents/rules/09-source-adaptation.md`
3. `docs/playbooks/external-source-ingestion.md`
4. the closest source-specific playbook under `docs/playbooks/`

Use the migration prompts/templates to inventory, reconstruct and propose an adaptation contract. Story Skills canon promotion happens only after author approval.

For an already-written prose manuscript, Story Skills `story import` may be the shorter route; structured source databases still use the Source Adaptation Pipeline.

## 4. Fill the author layer

Complete, at minimum:

- `author/creative-constitution.md`
- `author/style-bible.md`
- `author/boundaries.md`

Record important decisions in `author/decisions.md`.

For an external-source adaptation, also preserve the approved adaptation contract and source/provenance working artifacts outside Story Skills canon.

## 5. Validate

After Story Skills has been initialized/populated:

```bash
npm run story:check
npm run story:doctor
npm run story:report
```

## 6. Open the same folder in Obsidian

Use the repository root as the vault. Recommended plugins are documented in `docs/OBSIDIAN.md`.

## 7. Start Antigravity

Open the repository root as the workspace. Ask the agent to read `AGENTS.md`, `GEMINI.md`, and relevant rules before acting.

Recommended first prompt for a blank/initialized story:

```text
Act as Narrative Director. Read the repository contract and current story state. Run deterministic story checks. Do not draft prose. Tell me what is incomplete before we can safely outline the first chapter.
```

For an external source corpus, start with `prompts/migration/inspect-source.md` instead.

## 8. Keep skills updated intentionally

```bash
npm run upstreams:check
```

Do not casually update dependencies during an active revision. Pin changes, reinstall with `npm run bootstrap -- --clean`, then rerun all story checks.
