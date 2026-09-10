"""Validate Volume I continuity-detail spec locators and fail-closed boundaries.

This checker proves document structure, locator ownership and persisted approval
guardrails. It does not solve open slots or certify semantic/literary quality.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "migration/restructure_2026_09"
DOC = BASE / "continuity-detail-spec-volume-i.md"
CITE = re.compile(r"\bT(\d+)/S(\d+)(?:/E(\d+))?\b")
LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
REQUIRED = {
    "T1/S8/E37",
    "T1/S8/E41",
    "T2/S10/E50",
    "T2/S12/E60",
    "T2/S13",
    "T4/S36/E171",
    "T4/S36/E172",
    "T4/S36/E173",
    "T4/S37",
    "T12/S86/E483",
    "T12/S86/E484",
    "T12/S92/E516",
    "T157/S320/E1432",
    "T157/S323",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def source_index() -> dict[tuple[int, int], dict[str, object]]:
    result: dict[tuple[int, int], dict[str, object]] = {}
    for packet in (BASE / "evidence/source-packets").glob("*.json"):
        payload = json.loads(packet.read_text(encoding="utf-8"))
        for task in payload["tasks"]:
            for subtask in task["subtasks"]:
                result[(task["task_id"], subtask["sub_id"])] = {
                    "steps": {step["id"] for step in subtask["steps"]},
                    "describe": subtask["describe_cleaned"],
                }
    return result


def validate(body: str, index: dict[tuple[int, int], dict[str, object]]) -> dict[str, int]:
    require(body.endswith("\n"), "Missing final newline")
    require("AUTHOR-APPROVED PLANNING / CDQ-01–05 / NOT CANON / NOT A CHAPTER PLAN" in body,
            "Missing approved-planning/noncanon boundary")
    require("## 10. Kết quả CDQ-01–05 — APPROVED 2026-09-09" in body,
            "Missing persisted CDQ approval record")
    require("PHYSICAL_CONVERGENCE_VOLUME_I = NONE" in body,
            "Missing no-physical-convergence invariant")
    require("DU_LONG_OBJECTIVE_CUSTODY` | `UNRESOLVED" in body,
            "Missing unresolved objective custody state")
    require("HUYEN_NGUYET_MECHANISM` | `DEFERRED" in body,
            "Missing deferred Huyen Nguyet state")
    require("Tĩnh Xuyên tự tay hạ sát Ân Đồng" in body,
            "Missing protected Tinh Xuyen-An Dong responsibility")
    require("Không tai nạn, không bẫy chông, không người thứ ba ra tay, không giả chết" in body,
            "Missing anti-absolution boundary")
    for number in range(1, 8):
        require(f"| CDI-{number:02} |" in body, f"Missing CDI-{number:02}")
    for number in range(1, 7):
        require(f"| CDK-{number:02}" in body, f"Missing CDK-{number:02}")
    for number in range(1, 6):
        require(f"| CDQ-{number:02} |" in body, f"Missing CDQ-{number:02}")

    found: set[str] = set()
    for match in CITE.finditer(body):
        task_id, sub_id = int(match[1]), int(match[2])
        source = index.get((task_id, sub_id))
        require(source is not None, f"Unknown task/subtask: {match[0]}")
        if match[3]:
            require(int(match[3]) in source["steps"], f"Wrong step owner: {match[0]}")
        else:
            require(bool(source["describe"]), f"Empty default source row: {match[0]}")
        found.add(match[0])
    require(REQUIRED <= found, f"Missing required evidence: {sorted(REQUIRED - found)}")

    links = 0
    for target in LINK.findall(body):
        if "://" in target or target.startswith("#"):
            continue
        path = (DOC.parent / target.split("#", 1)[0]).resolve()
        require(path.exists(), f"Broken local link: {target}")
        links += 1
    return {"citations": len(found), "required_citations": len(REQUIRED), "file_links": links}


def self_test(body: str, index: dict[tuple[int, int], dict[str, object]]) -> list[str]:
    cases = [
        ("bad-task", lambda value: value + "\nT999999/S1\n"),
        ("bad-step-owner", lambda value: value + "\nT4/S36/E516\n"),
        ("missing-approval-record", lambda value: value.replace(
            "## 10. Kết quả CDQ-01–05 — APPROVED 2026-09-09", "## 10. Approval removed")),
        ("missing-no-meeting", lambda value: value.replace("PHYSICAL_CONVERGENCE_VOLUME_I = NONE", "REMOVED")),
        ("missing-custody-lock", lambda value: value.replace("DU_LONG_OBJECTIVE_CUSTODY` | `UNRESOLVED", "REMOVED")),
        ("missing-an-dong-lock", lambda value: value.replace("Tĩnh Xuyên tự tay hạ sát Ân Đồng", "trách nhiệm bị xóa")),
    ]
    passed: list[str] = []
    for label, mutate in cases:
        try:
            validate(mutate(body), index)
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
    index = source_index()
    counts = validate(body, index)
    tests = self_test(body, index) if args.self_test else []
    print(json.dumps({
        "validation": "PASS",
        "assurance": "STRUCTURE_LOCATORS_AND_BOUNDARIES_ONLY_NOT_SEMANTIC",
        **counts,
        "negative_tests": tests,
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
