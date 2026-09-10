"""Validate the approved Volume I scene-plan phase specification.

This checker verifies phase boundaries, links, required invariants and the
approved boundary and any later output shape. It does not certify literary
quality, source semantics, scene feasibility or candidate-scene approval.
"""
from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "migration" / "restructure_2026_09"
DOC = BASE / "scene-plan-phase-spec-volume-i.md"
SEQUENCE = BASE / "chapter-plan-volume-i" / "chapter-sequence.tsv"
BRIEFS = BASE / "chapter-plan-volume-i" / "briefs"
OUTPUT_DIR = BASE / "scene-plan-volume-i"
AUTHOR_DECISIONS = BASE / "author-decisions.md"
DECISION_LOG = ROOT / "author" / "decision-log.md"
LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
EXPECTED_TOP_LEVEL = {
    "README.md",
    "scene-ledger.tsv",
    "scene-ledger.md",
    "provenance-ledger.tsv",
    "open-slots-and-departures.md",
    "validation-report.md",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def read_sequence() -> list[dict[str, str]]:
    with SEQUENCE.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def validate(body: str, *, check_workspace: bool = True) -> dict[str, int]:
    require(body.endswith("\n"), "Missing final newline")
    require("AUTHOR-APPROVED PHASE SPEC / SPQ-01–06 / NOT A SCENE PLAN / NOT CANON / NOT PROSE" in body,
            "Missing approved/no-scene/no-prose boundary")
    require("## 16. Author decision record — SPQ-01–06" in body, "Missing SPQ decision record")
    require("Phê duyệt spec chỉ mở candidate scene-plan implementation" in body,
            "Missing two-stage approval boundary")
    require("PHYSICAL_CONVERGENCE_VOLUME_I = NONE" in body, "Missing no-convergence invariant")
    require("READER_KNOWLEDGE != CHARACTER_KNOWLEDGE" in body, "Missing knowledge boundary")
    require("DU_LONG_OBJECTIVE_CUSTODY = UNRESOLVED" in body, "Missing custody boundary")
    require("HUYEN_NGUYET_MECHANISM = DEFERRED" in body, "Missing Huyen Nguyet boundary")
    require("Tĩnh Xuyên–Ân Đồng là protected future canon bất khả thay thế" in body,
            "Missing protected Tinh Xuyen-An Dong invariant")
    require("trên 5.500 từ hoặc hai irreversible turn độc lập" in body,
            "Missing mandatory split gate")
    require("CANDIDATE SCENE PLAN IMPLEMENTATION AUTHORIZED" in body,
            "Missing candidate-only implementation authorization")
    require("SCENE_PLAN_IMPLEMENTATION_FROZEN_POST_MACRO_CONSOLIDATION / D-034-R-65-R-68" in body,
            "Missing active scene-plan freeze")
    require("không mở prose-phase spec và không mở prose" in body,
            "Missing prose boundary")
    require("## Scene 01" not in body and "V1-CH-001-S01" not in body,
            "Concrete scene allocation injected into phase spec")
    for number in range(1, 16):
        require(f"| SPI-{number:02} |" in body, f"Missing SPI-{number:02}")
    for number in range(1, 7):
        require(f"| SPQ-{number:02} |" in body, f"Missing SPQ-{number:02}")
    decisions = AUTHOR_DECISIONS.read_text(encoding="utf-8")
    decision_log = DECISION_LOG.read_text(encoding="utf-8")
    for number in range(59, 65):
        require(f"| R-{number} |" in decisions, f"Missing R-{number}")
    require("QUYẾT ĐỊNH D-033" in decision_log and "SPQ-01–06" in decision_log,
            "Missing D-033 approval record")

    links = 0
    for target in LINK.findall(body):
        if "://" in target or target.startswith("#"):
            continue
        path = (DOC.parent / target.split("#", 1)[0]).resolve()
        require(path.exists(), f"Broken local link: {target}")
        links += 1

    rows = read_sequence()
    require(len(rows) == 25, f"Expected 25 approved chapter rows, got {len(rows)}")
    require(all(row["status"] == "AUTHOR-APPROVED PLANNING / V1CBQ-01–06 / NOT CANON" for row in rows),
            "Scene-plan spec input includes a non-approved chapter row")
    briefs = sorted(BRIEFS.glob("chapter_*.md"))
    require(len(briefs) == 25, f"Expected 25 approved briefs, got {len(briefs)}")
    if check_workspace:
        require(not OUTPUT_DIR.exists(), "scene-plan-volume-i exists while implementation is frozen")
    return {"file_links": links, "invariants": 15, "spq_questions": 6,
            "approved_chapters": len(rows), "approved_briefs": len(briefs)}


def self_test(body: str) -> list[str]:
    cases = [
        ("missing-approval-boundary", lambda value: value.replace(
            "AUTHOR-APPROVED PHASE SPEC / SPQ-01–06 / NOT A SCENE PLAN / NOT CANON / NOT PROSE", "AUTHOR-APPROVED")),
        ("missing-approval-gate", lambda value: value.replace(
            "## 16. Author decision record — SPQ-01–06", "## Approval removed")),
        ("missing-no-meeting", lambda value: value.replace(
            "PHYSICAL_CONVERGENCE_VOLUME_I = NONE", "REMOVED")),
        ("missing-knowledge-boundary", lambda value: value.replace(
            "READER_KNOWLEDGE != CHARACTER_KNOWLEDGE", "REMOVED")),
        ("missing-custody-boundary", lambda value: value.replace(
            "DU_LONG_OBJECTIVE_CUSTODY = UNRESOLVED", "REMOVED")),
        ("missing-an-dong-boundary", lambda value: value.replace(
            "Tĩnh Xuyên–Ân Đồng là protected future canon bất khả thay thế", "REMOVED")),
        ("missing-split-gate", lambda value: value.replace(
            "trên 5.500 từ hoặc hai irreversible turn độc lập", "REMOVED")),
        ("missing-candidate-authorization", lambda value: value.replace(
            "CANDIDATE SCENE PLAN IMPLEMENTATION AUTHORIZED", "REMOVED")),
        ("missing-freeze", lambda value: value.replace(
            "SCENE_PLAN_IMPLEMENTATION_FROZEN_POST_MACRO_CONSOLIDATION / D-034-R-65-R-68", "REMOVED")),
        ("concrete-scene-injection", lambda value: value + "\n## Scene 01\nV1-CH-001-S01\n"),
    ]
    passed: list[str] = []
    for label, mutate in cases:
        try:
            validate(mutate(body), check_workspace=False)
        except ValueError:
            passed.append(label)
        else:
            raise ValueError(f"Negative test accepted invalid spec: {label}")
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
        "assurance": "PHASE_STRUCTURE_INPUT_APPROVAL_AND_BOUNDARIES_ONLY_NOT_SEMANTIC",
        **counts,
        "negative_tests": tests,
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
