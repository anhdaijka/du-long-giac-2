"""Check current routing only; never certify manuscript temporal semantics."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = "migration/restructure_2026_09/temporal-continuity-contract.md"
SURFACES = ["AGENTS.md", "GEMINI.md", "Home.md", "docs/WORKFLOW.md",
            "docs/playbooks/gemini-evidence-review.md",
            "worldbuilding/factions/genealogy_matrix.md",
            "migration/restructure_2026_09/gemini-chapter-workflow-router.md",
            "migration/restructure_2026_09/series-chapter-allocation-index.md"]
FORBIDDEN = re.compile(r"plot/(?:timeline|chronology_matrix|volume_\w+_deck)\.md|"
                       r"worldbuilding/geography/travel_matrix\.md|"
                       r"Rule TC-[1-4]|expected_ages_v1")


def check(root=ROOT):
    errors = []
    policy = root / CONTRACT
    if not policy.is_file() or "D-064" not in policy.read_text(encoding="utf-8"):
        errors.append("Missing approved D-064 temporal contract")
    for name in SURFACES:
        p = root / name
        if not p.is_file() or CONTRACT not in p.read_text(encoding="utf-8"):
            errors.append(f"Missing current authority routing: {name}")
    files = [root / name for name in SURFACES]
    for folder in [".agents/rules", ".agents/workflows", "prompts/roles", "templates"]:
        files.extend((root / folder).rglob("*.md"))
    files.extend(root / name for name in ["scripts/gate-guard.py", "scripts/lore-grounder.py"])
    for p in files:
        if not p.is_file():
            continue
        for i, line in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
            if FORBIDDEN.search(line):
                errors.append(f"Legacy operational reference: {p.relative_to(root)}:{i}")
    return errors


if __name__ == "__main__":
    failures = check()
    for failure in failures:
        print(f"FAIL: {failure}")
    if not failures:
        print("PASS: temporal authority routing. NOT CHECKED: manuscript chronology, travel, age and knowledge semantics; use chapter receipts and full review.")
    sys.exit(bool(failures))
