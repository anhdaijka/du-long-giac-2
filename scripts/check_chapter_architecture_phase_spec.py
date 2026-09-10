"""Validate the approved Volume I chapter-architecture phase specification.

This checker verifies the persisted approval record, phase boundaries, required
invariants, local links and the exact six-output package shape. It does not
semantically certify CAPQ decisions or candidate chapter quality.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "migration/restructure_2026_09"
DOC = BASE / "chapter-architecture-phase-spec-volume-i.md"
OUTPUT_DIR = BASE / "chapter-architecture"
EXPECTED_OUTPUTS = {
    "README.md",
    "chapter-function-matrix.tsv",
    "chapter-function-matrix.md",
    "interleave-and-dependency-map.md",
    "world-spine-selection.md",
    "validation-report.md",
}
LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def validate(body: str, *, check_output_shape: bool = True) -> dict[str, int]:
    require(body.endswith("\n"), "Missing final newline")
    require("AUTHOR-APPROVED PHASE SPEC / CAPQ-01–06 / NOT A CHAPTER ARCHITECTURE / NOT CANON" in body,
            "Missing approved/non-architecture boundary")
    require("## 14. Kết quả CAPQ-01–06 — APPROVED 2026-09-09" in body,
            "Missing persisted CAPQ approval record")
    require("PHYSICAL_CONVERGENCE_VOLUME_I = NONE" in body,
            "Missing no-physical-convergence invariant")
    require("DU_LONG_OBJECTIVE_CUSTODY = UNRESOLVED" in body,
            "Missing unresolved custody invariant")
    require("Tĩnh Xuyên–Ân Đồng là future canon bất khả thay thế" in body,
            "Missing protected Tinh Xuyen-An Dong invariant")
    require("Task 4 chỉ là **future-invariant audit input**" in body,
            "Missing Task 4 exclusion boundary")
    require("không đặt target chapter count trước" in body,
            "Missing emergent-count proposal")
    require("FIXED_CHAPTER_COUNT" not in body, "Fixed chapter count injected")
    for number in range(1, 13):
        require(f"| CAI-{number:02} |" in body, f"Missing CAI-{number:02}")
    for number in range(1, 7):
        require(f"| CAPQ-{number:02} |" in body, f"Missing CAPQ-{number:02}")
    for movement in range(1, 6):
        require(f"M{movement} —" in body, f"Missing movement M{movement}")

    links = 0
    for target in LINK.findall(body):
        if "://" in target or target.startswith("#"):
            continue
        path = (DOC.parent / target.split("#", 1)[0]).resolve()
        require(path.exists(), f"Broken local link: {target}")
        links += 1
    if check_output_shape and OUTPUT_DIR.exists():
        outputs = {path.name for path in OUTPUT_DIR.iterdir() if path.is_file()}
        require(outputs == EXPECTED_OUTPUTS,
                f"Chapter-architecture output set mismatch: {sorted(outputs)}")
    return {"file_links": links, "invariants": 12, "capq_decisions": 6, "movements": 5}


def self_test(body: str) -> list[str]:
    cases = [
        ("missing-approval-boundary", lambda value: value.replace(
            "AUTHOR-APPROVED PHASE SPEC / CAPQ-01–06 / NOT A CHAPTER ARCHITECTURE / NOT CANON",
            "AUTHOR-APPROVED")),
        ("missing-approval-record", lambda value: value.replace(
            "## 14. Kết quả CAPQ-01–06 — APPROVED 2026-09-09", "## Approval removed")),
        ("missing-no-meeting", lambda value: value.replace(
            "PHYSICAL_CONVERGENCE_VOLUME_I = NONE", "REMOVED")),
        ("missing-custody-lock", lambda value: value.replace(
            "DU_LONG_OBJECTIVE_CUSTODY = UNRESOLVED", "REMOVED")),
        ("missing-an-dong-lock", lambda value: value.replace(
            "Tĩnh Xuyên–Ân Đồng là future canon bất khả thay thế", "future canon removed")),
        ("fixed-count-injection", lambda value: value + "\nFIXED_CHAPTER_COUNT = 24\n"),
    ]
    passed: list[str] = []
    for label, mutate in cases:
        try:
            validate(mutate(body), check_output_shape=False)
        except ValueError:
            passed.append(label)
        else:
            raise ValueError(f"Negative test accepted invalid document: {label}")
    return passed


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    body = DOC.read_text(encoding="utf-8")
    counts = validate(body)
    tests = self_test(body) if args.self_test else []
    print(json.dumps({
        "validation": "PASS",
        "assurance": "PHASE_STRUCTURE_AND_BOUNDARIES_ONLY_NOT_SEMANTIC",
        **counts,
        "negative_tests": tests,
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
