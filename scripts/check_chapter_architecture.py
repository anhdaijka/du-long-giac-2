"""Validate the approved Volume I chapter-architecture planning package.

The checker verifies artifact shape, SQLite packet locators, dependency IDs and
fail-closed planning boundaries. It also verifies the persisted V1CAQ approval
record. It does not certify literary quality, choose chronology, or authorize
scenes/prose.
"""
from __future__ import annotations

import argparse
import csv
import io
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "migration/restructure_2026_09"
ARCH = BASE / "chapter-architecture"
MATRIX = ARCH / "chapter-function-matrix.tsv"
LEDGER = BASE / "world-coverage/ledger.tsv"
PACKETS = BASE / "evidence/source-packets"

ARTIFACTS = [
    "README.md",
    "chapter-function-matrix.tsv",
    "chapter-function-matrix.md",
    "interleave-and-dependency-map.md",
    "world-spine-selection.md",
    "validation-report.md",
]
FIELDS = [
    "candidate_id",
    "movement_id",
    "primary_pov",
    "chapter_function",
    "entry_state",
    "exit_state",
    "source_nodes",
    "event_family_ids",
    "bridge_decisions",
    "knowledge_in",
    "knowledge_out",
    "npc_agency",
    "irreversible_change",
    "causal_predecessors",
    "causal_returns",
    "narrative_load",
    "coverage_channel",
    "protected_unknowns",
    "status",
]
POVS = {"TINH_XUYEN", "TIEU_PHUNG", "HA_NUONG", "SATELLITE_CANDIDATE"}
LOADS = {"LIGHT", "MEDIUM", "HEAVY"}
CHANNELS = {
    "DIRECT_TRIO",
    "DOCUMENT_TRACE",
    "WITNESS_RELAY",
    "AFTERMATH",
    "LIVING_LORE",
    "SATELLITE_CANDIDATE",
}
LOCATOR = re.compile(r"T(?P<task>\d+)/S(?P<sub>\d+)(?:/(?P<kind>[ED])(?P<item>\d+))?")
CID = re.compile(r"V1-CAND-\d{3}")
LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
DECISION = re.compile(r"(?:R|PB|BFCQ|CDQ|CAPQ|LWCQ)-\d+")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def read_text(path: Path) -> str:
    body = path.read_text(encoding="utf-8")
    require(body.endswith("\n"), f"Missing final newline: {path.name}")
    return body


def source_index() -> dict[int, dict[int, tuple[set[int], set[int]]]]:
    index: dict[int, dict[int, tuple[set[int], set[int]]]] = {}
    for path in sorted(PACKETS.glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        for task in data["tasks"]:
            task_id = int(task["task_id"])
            subs = index.setdefault(task_id, {})
            for sub in task["subtasks"]:
                sub_id = int(sub["sub_id"])
                require(sub_id not in subs, f"Duplicate source subtask T{task_id}/S{sub_id}")
                subs[sub_id] = (
                    {int(item["id"]) for item in sub["steps"]},
                    {int(item["id"]) for item in sub["dialogues"]},
                )
    return index


def event_families() -> set[str]:
    with LEDGER.open(encoding="utf-8", newline="") as handle:
        return {row["event_family_id"] for row in csv.DictReader(handle, delimiter="\t")}


def parse_rows(tsv_body: str) -> list[dict[str, str]]:
    reader = csv.DictReader(io.StringIO(tsv_body), delimiter="\t")
    require(reader.fieldnames == FIELDS, "Unexpected chapter-function matrix header")
    rows = list(reader)
    require(len(rows) == 26, f"Expected 26 review rows, got {len(rows)}")
    return rows


def validate(
    texts: dict[str, str],
    rows: list[dict[str, str]],
    *,
    check_links: bool = True,
) -> dict[str, object]:
    readme = texts["README.md"]
    projection = texts["chapter-function-matrix.md"]
    braid = texts["interleave-and-dependency-map.md"]
    world = texts["world-spine-selection.md"]
    report = texts["validation-report.md"]
    combined = "\n".join(texts.values())
    author_decisions = read_text(BASE / "author-decisions.md")
    decision_log = read_text(ROOT / "author/decision-log.md")

    require("AUTHOR-APPROVED PLANNING / V1CAQ-01–06 / NOT A CHAPTER PLAN / NOT CANON" in readme,
            "Missing approved-planning/noncanon package boundary")
    require("R-47" in author_decisions and "R-52" in author_decisions,
            "Missing V1CAQ author-decision records")
    require("QUYẾT ĐỊNH D-031" in decision_log and "V1CAQ-01–06" in decision_log,
            "Missing D-031 approval record")
    require("PHYSICAL_CONVERGENCE_VOLUME_I = NONE" in readme, "Missing no-meeting invariant")
    require("DU_LONG_OBJECTIVE_CUSTODY = UNRESOLVED" in readme, "Missing custody invariant")
    require("HUYEN_NGUYET_MECHANISM = DEFERRED" in readme, "Missing Huyen Nguyet invariant")
    for forbidden in [
        "PHYSICAL_CONVERGENCE_VOLUME_I = PRESENT",
        "FIXED_CHAPTER_COUNT",
        "LUC_RESCUER =",
        "DU_LONG_OBJECTIVE_CUSTODY = LE_THU_THUY",
        "DU_LONG_OBJECTIVE_CUSTODY = HA_NUONG",
    ]:
        require(forbidden not in combined, f"Forbidden planning injection: {forbidden}")
    require("FUTURE-INVARIANT AUDIT INPUT ONLY" in world, "Missing Task 4 future-only boundary")
    require("T4/S28–S37" in world, "Missing Tinh Xuyen-An Dong audit locator boundary")
    require("V1CAQ-01–06 APPROVED" in report, "Missing approved author gate in validation report")

    ids = [row["candidate_id"] for row in rows]
    expected_ids = [f"V1-CAND-{number:03}" for number in range(1, 27)]
    require(ids == expected_ids, "Candidate IDs must be unique and ordered V1-CAND-001..026")
    id_set = set(ids)
    sources = source_index()
    families = event_families()

    for row in rows:
        cid = row["candidate_id"]
        for field in FIELDS:
            require(row.get(field, "").strip(), f"Blank {field} in {cid}")
        require(row["movement_id"] in {"M1", "M2", "M3", "M4", "M5"}, f"Bad movement in {cid}")
        require(row["primary_pov"] in POVS, f"Bad primary POV in {cid}")
        require(row["narrative_load"] in LOADS, f"Bad narrative load in {cid}")
        require(row["coverage_channel"] in CHANNELS, f"Bad coverage channel in {cid}")
        if cid == "V1-CAND-020":
            require(row["status"] == "DEFERRED / NOT IN DEFAULT ARCHITECTURE", f"Bad deferred status in {cid}")
            require("V1CAQ-02" in row["bridge_decisions"], f"Missing V1CAQ-02 in {cid}")
        else:
            require(row["status"] == "AUTHOR-APPROVED PLANNING / NOT CANON", f"Bad approved status in {cid}")
            require("V1CAQ-01" in row["bridge_decisions"], f"Missing V1CAQ-01 in {cid}")
        require(DECISION.search(row["bridge_decisions"]) is not None, f"Missing decision anchor in {cid}")

        locators = list(LOCATOR.finditer(row["source_nodes"]))
        require(locators, f"No source locator in {cid}")
        for match in locators:
            task_id = int(match.group("task"))
            sub_id = int(match.group("sub"))
            require(task_id != 4, f"Task 4 contaminated Volume I row {cid}")
            require(task_id in sources, f"Unknown task T{task_id} in {cid}")
            require(sub_id in sources[task_id], f"Wrong/unknown subtask T{task_id}/S{sub_id} in {cid}")
            if match.group("item"):
                item_id = int(match.group("item"))
                steps, dialogues = sources[task_id][sub_id]
                owner_set = steps if match.group("kind") == "E" else dialogues
                require(item_id in owner_set,
                        f"Wrong {match.group('kind')} owner T{task_id}/S{sub_id}/{match.group('kind')}{item_id} in {cid}")

        for family in row["event_family_ids"].split(";"):
            require(family in families, f"Unknown event family {family} in {cid}")
        for field in ("causal_predecessors", "causal_returns", "irreversible_change"):
            for ref in CID.findall(row[field]):
                require(ref in id_set, f"Unknown dependency {ref} in {cid}.{field}")

        if row["primary_pov"] == "SATELLITE_CANDIDATE":
            require(row["coverage_channel"] == "SATELLITE_CANDIDATE", f"Satellite channel mismatch in {cid}")
            require("LWCQ-02" in row["bridge_decisions"], f"Satellite missing LWCQ-02 in {cid}")
        else:
            require(row["coverage_channel"] != "SATELLITE_CANDIDATE", f"Non-satellite channel mismatch in {cid}")

    by_id = {row["candidate_id"]: row for row in rows}
    require("V1-CAND-020" not in by_id["V1-CAND-022"]["causal_predecessors"],
            "Default Lục–Thôi function still depends on deferred satellite")
    require("CDK-02" in by_id["V1-CAND-022"]["causal_predecessors"],
            "Default Lục–Thôi function must depend on CDK-02")
    require("V1CAQ-03" in by_id["V1-CAND-026"]["bridge_decisions"],
            "Missing approved Cầu relay decision")
    require("BRIDGE-CANDIDATE_CAU_RELAY" not in by_id["V1-CAND-026"]["bridge_decisions"],
            "Cầu relay still marked candidate")

    pov_counts = Counter(row["primary_pov"] for row in rows)
    require(pov_counts == Counter({"TIEU_PHUNG": 11, "TINH_XUYEN": 8, "HA_NUONG": 6, "SATELLITE_CANDIDATE": 1}),
            f"Unexpected POV counts: {dict(pov_counts)}")
    movement_counts = Counter(row["movement_id"] for row in rows)
    require(set(movement_counts) == {"M1", "M2", "M3", "M4", "M5"}, "Movement coverage incomplete")
    status_counts = Counter(row["status"] for row in rows)
    require(status_counts == Counter({"AUTHOR-APPROVED PLANNING / NOT CANON": 25,
                                      "DEFERRED / NOT IN DEFAULT ARCHITECTURE": 1}),
            f"Unexpected status counts: {dict(status_counts)}")
    for cid in ids:
        require(projection.count(f"| {cid} |") == 1,
                f"Projection table must contain {cid} exactly once")
        require(re.search(rf"\b{cid[-3:]}\b", braid) is not None, f"Braid omits {cid}")

    link_count = 0
    if check_links:
        for name, body in texts.items():
            if not name.endswith(".md"):
                continue
            origin = ARCH / name
            for target in LINK.findall(body):
                if "://" in target or target.startswith("#"):
                    continue
                path = (origin.parent / target.split("#", 1)[0]).resolve()
                require(path.exists(), f"Broken local link in {name}: {target}")
                link_count += 1

    return {
        "rows": len(rows),
        "pov_counts": dict(sorted(pov_counts.items())),
        "movement_counts": dict(sorted(movement_counts.items())),
        "status_counts": dict(sorted(status_counts.items())),
        "source_locators": sum(len(LOCATOR.findall(row["source_nodes"])) for row in rows),
        "file_links": link_count,
    }


def self_test(texts: dict[str, str], tsv_body: str) -> list[str]:
    cases = [
        ("bad-task", lambda t, s: (t, s.replace("T1/S1/E3", "T999/S1/E3", 1))),
        ("bad-step-owner", lambda t, s: (t, s.replace("T1/S1/E3", "T1/S2/E3", 1))),
        ("task4-contamination", lambda t, s: (t, s.replace("T1/S1/E3", "T4/S36/E171", 1))),
        ("early-meeting", lambda t, s: ({**t, "README.md": t["README.md"] + "\nPHYSICAL_CONVERGENCE_VOLUME_I = PRESENT\n"}, s)),
        ("fixed-count", lambda t, s: ({**t, "README.md": t["README.md"] + "\nFIXED_CHAPTER_COUNT = 26\n"}, s)),
        ("named-luc-rescuer", lambda t, s: ({**t, "README.md": t["README.md"] + "\nLUC_RESCUER = LA_PHONG\n"}, s)),
        ("custody-holder", lambda t, s: ({**t, "README.md": t["README.md"] + "\nDU_LONG_OBJECTIVE_CUSTODY = LE_THU_THUY\n"}, s)),
        ("satellite-without-policy", lambda t, s: (t, s.replace("R-31;BFCQ-01;R-36;CDQ-01;LWCQ-02;CAPQ-04", "R-31;BFCQ-01;R-36;CDQ-01;CAPQ-04", 1))),
        ("missing-projection-row", lambda t, s: ({**t, "chapter-function-matrix.md": t["chapter-function-matrix.md"].replace("V1-CAND-026", "ROW-REMOVED", 1)}, s)),
        ("satellite-reintroduced", lambda t, s: (t, s.replace("DEFERRED / NOT IN DEFAULT ARCHITECTURE", "AUTHOR-APPROVED PLANNING / NOT CANON", 1))),
        ("missing-cdk02-predecessor", lambda t, s: (t, s.replace("CDK-02;V1-CAND-021\tV1-CAND-023;V1-CAND-026", "V1-CAND-020;V1-CAND-021\tV1-CAND-023;V1-CAND-026", 1))),
        ("missing-cau-approval", lambda t, s: (t, s.replace("V1CAQ-03", "RELAY_UNAPPROVED", 1))),
    ]
    passed: list[str] = []
    for label, mutate in cases:
        mutated_texts, mutated_tsv = mutate(dict(texts), tsv_body)
        mutated_texts["chapter-function-matrix.tsv"] = mutated_tsv
        try:
            validate(mutated_texts, parse_rows(mutated_tsv), check_links=False)
        except ValueError:
            passed.append(label)
        else:
            raise ValueError(f"Negative test accepted invalid package: {label}")
    return passed


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    for name in ARTIFACTS:
        require((ARCH / name).is_file(), f"Missing artifact: {name}")
    texts = {name: read_text(ARCH / name) for name in ARTIFACTS}
    tsv_body = texts["chapter-function-matrix.tsv"]
    rows = parse_rows(tsv_body)
    counts = validate(texts, rows)
    tests = self_test(texts, tsv_body) if args.self_test else []
    print(json.dumps({
        "validation": "PASS",
        "assurance": "STRUCTURE_LOCATORS_DEPENDENCIES_AND_BOUNDARIES_ONLY_NOT_SEMANTIC",
        **counts,
        "negative_tests": tests,
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
