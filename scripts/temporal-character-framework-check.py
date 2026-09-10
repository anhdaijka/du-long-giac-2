"""Structural guard for D-065/R-91; it does not validate story semantics."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
FRAMEWORK = ROOT / "migration/restructure_2026_09/temporal-character-framework.md"
REQUIRED = [
    *(f"TQ-{i:02d}" for i in range(1, 7)),
    *(f"CQ-{i:02d}" for i in range(1, 6)),
    *(f"RQ-{i:02d}" for i in range(1, 6)),
    *(f"MQ-{i:02d}" for i in range(1, 7)),
    *(f"WQ-{i:02d}" for i in range(1, 6)),
    *(f"HQ-{i:02d}" for i in range(1, 5)),
    *(f"SQ-{i:02d}" for i in range(1, 6)),
]
ROUTERS = [
    "AGENTS.md",
    "docs/playbooks/gemini-evidence-review.md",
    "migration/restructure_2026_09/gemini-chapter-workflow-router.md",
    "migration/restructure_2026_09/series-chapter-allocation-index.md",
]


def check(root=ROOT):
    errors = []
    framework = root / FRAMEWORK.relative_to(ROOT)
    if not framework.is_file():
        return ["Missing D-065 framework"]
    text = framework.read_text(encoding="utf-8")
    if "D-065" not in text or "R-91" not in text:
        errors.append("Framework lacks D-065/R-91 authority marker")
    for key in REQUIRED:
        if not re.search(rf"\|\s*{key}\s*\|", text):
            errors.append(f"Framework lacks approved decision {key}")
    for name in ROUTERS:
        content = (root / name).read_text(encoding="utf-8")
        if "temporal-character-framework.md" not in content:
            errors.append(f"Router does not load D-065 framework: {name}")
    for phrase in ["NOT GAME FACT", "NOT PROSE AUTHORIZATION", "không thay receipt", "Không tạo registry"]:
        if phrase not in text:
            errors.append(f"Framework lacks boundary: {phrase}")
    return errors


if __name__ == "__main__":
    failures = check()
    for failure in failures:
        print(f"FAIL: {failure}")
    if not failures:
        print("PASS: D-065 framework keys and router boundaries are present. NOT CHECKED: source entailment, chronology, prose or canon state.")
    sys.exit(bool(failures))
