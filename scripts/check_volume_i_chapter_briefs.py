"""Validate the author-approved Volume I chapter sequence and bounded briefs."""
from __future__ import annotations

import argparse
import csv
import io
import json
import re
from collections import Counter
from pathlib import Path

from build_volume_i_chapter_briefs import FIELDS, OUT, ROOT, SEQUENCE, packet_refs, read_matrix, result_refs


SEQUENCE_TSV = OUT / "chapter-sequence.tsv"
PROVENANCE_TSV = OUT / "provenance-ledger.tsv"
BRIEFS = OUT / "briefs"
AUTHOR_DECISIONS = ROOT / "migration/restructure_2026_09/author-decisions.md"
DECISION_LOG = ROOT / "author/decision-log.md"
LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
FUNCTION = re.compile(r"V1-CAND-\d{3}")
DATE = re.compile(r"\b(?:11|12)\d{2}-\d{2}-\d{2}\b")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def parse_tsv(body: str, expected_fields: list[str]) -> list[dict[str, str]]:
    reader = csv.DictReader(io.StringIO(body), delimiter="\t")
    require(reader.fieldnames == expected_fields, "Unexpected TSV header")
    return list(reader)


def load_texts() -> dict[str, str]:
    texts = {
        "README.md": read(OUT / "README.md"),
        "chapter-sequence.tsv": read(SEQUENCE_TSV),
        "chapter-sequence.md": read(OUT / "chapter-sequence.md"),
        "provenance-ledger.tsv": read(PROVENANCE_TSV),
        "validation-report.md": read(OUT / "validation-report.md"),
    }
    for number in range(1, 26):
        name = f"briefs/chapter_{number:02}.md"
        texts[name] = read(OUT / name)
    return texts


def validate(texts: dict[str, str], *, check_links: bool = True) -> dict[str, object]:
    matrix = read_matrix()
    rows = parse_tsv(texts["chapter-sequence.tsv"], FIELDS)
    expected_functions = [function_id for function_id, _ in SEQUENCE]
    expected_titles = [title for _, title in SEQUENCE]

    require(len(rows) == 25, f"Expected 25 sequence rows, got {len(rows)}")
    require([row["chapter_no"] for row in rows] == [f"{number:02}" for number in range(1, 26)],
            "Chapter numbers must be 01..25")
    require([row["chapter_key"] for row in rows] == [f"V1-CH-{number:03}" for number in range(1, 26)],
            "Chapter keys must be V1-CH-001..025")
    require([row["source_function_id"] for row in rows] == expected_functions,
            "Sequence does not match approved braid projection")
    require([row["working_title"] for row in rows] == expected_titles,
            "Working titles drifted from reviewed projection")
    require(len(set(expected_titles)) == 25, "Working titles must be unique")
    require("V1-CAND-020" not in expected_functions, "Deferred satellite entered sequence")

    function_order = {row["source_function_id"]: index for index, row in enumerate(rows, 1)}
    for row in rows:
        function_id = row["source_function_id"]
        source = matrix[function_id]
        require(source["status"] == "AUTHOR-APPROVED PLANNING / NOT CANON",
                f"Unapproved function in sequence: {function_id}")
        for field in ("movement_id", "primary_pov", "narrative_load", "source_nodes", "causal_predecessors", "causal_returns"):
            require(row[field] == source[field], f"Projection drift in {function_id}.{field}")
        require(row["packet_refs"] == ";".join(packet_refs(source["source_nodes"])),
                f"Packet mapping drift in {function_id}")
        require(row["status"] == "AUTHOR-APPROVED PLANNING / V1CBQ-01–06 / NOT CANON",
                f"Bad sequence status in {function_id}")
        for predecessor in FUNCTION.findall(source["causal_predecessors"]):
            if predecessor in function_order:
                require(function_order[predecessor] < function_order[function_id],
                        f"Predecessor {predecessor} is not earlier than {function_id}")

    require(function_order["V1-CAND-018"] < function_order["V1-CAND-021"], "Tĩnh Xuyên must exit before Tiêu arrives")
    require(function_order["V1-CAND-021"] < function_order["V1-CAND-022"], "Tiêu must arrive before the bout")
    require(function_order["V1-CAND-025"] < function_order["V1-CAND-026"], "Notice must leave Bách Hoa before relay")

    provenance_fields = ["chapter_key", "source_function_id", "source_nodes", "packet_refs", "query_record", "result_refs", "evidence_class"]
    provenance = parse_tsv(texts["provenance-ledger.tsv"], provenance_fields)
    require(len(provenance) == 25, "Provenance ledger must have 25 rows")
    for seq, prov in zip(rows, provenance, strict=True):
        source = matrix[seq["source_function_id"]]
        require(prov["chapter_key"] == seq["chapter_key"], "Provenance chapter key drift")
        require(prov["source_nodes"] == source["source_nodes"], "Provenance source-node drift")
        require(prov["packet_refs"] == seq["packet_refs"], "Provenance packet drift")
        require(prov["result_refs"] == ";".join(result_refs(source["source_nodes"])),
                "Provenance full-result references drifted")
        require("query_templates" in prov["query_record"] and "query_binds" in prov["query_record"],
                "Missing SQLite query record")

    brief_names = sorted(name for name in texts if name.startswith("briefs/"))
    require(brief_names == [f"briefs/chapter_{number:02}.md" for number in range(1, 26)],
            "Brief inventory must be exactly chapter_01..chapter_25")
    for row in rows:
        name = f"briefs/chapter_{row['chapter_no']}.md"
        body = texts[name]
        source = matrix[row["source_function_id"]]
        for required in [
            f"# Chương {row['chapter_no']} — {row['working_title']}",
            "AUTHOR-APPROVED PLANNING / V1CBQ-01–05 / NOT CANON / NOT A SCENE PLAN / NOT PROSE",
            f"Source function: `{row['source_function_id']}`",
            f"Primary POV: `{ {'TINH_XUYEN': 'Tĩnh Xuyên', 'TIEU_PHUNG': 'Tiêu Phùng', 'HA_NUONG': 'Hạ Nương'}[row['primary_pov']] }`",
            f"Source nodes: `{source['source_nodes']}`",
            "provenance.query_templates",
            "Full extraction result:",
            source["protected_unknowns"],
            "Exact calendar date: `DEFERRED — RELATIVE ORDER ONLY`",
            "Không lập scene sequence, beat, dialogue, action blocking hoặc ending image",
            "V1CBQ-01–05 / APPROVED 2026-09-09",
        ]:
            require(required in body, f"Missing brief contract in {name}: {required}")
        require(DATE.search(body) is None, f"Exact date injected in {name}")
        require("## Scene sequence" not in body, f"Scene allocation injected in {name}")
        require("PHYSICAL_CONVERGENCE_VOLUME_I = PRESENT" not in body, f"Early trio meeting injected in {name}")
        require("DU_LONG_OBJECTIVE_CUSTODY = LE_THU_THUY" not in body, f"Custody injected in {name}")

    readme = texts["README.md"]
    report = texts["validation-report.md"]
    sequence_md = texts["chapter-sequence.md"]
    require("V1-CAND-020 tiếp tục deferred và không có brief" in readme, "Missing satellite-deferred boundary")
    require("Author approval — V1CBQ-01–06 / 2026-09-09" in report, "Missing V1CBQ approval")
    require("R-53–R-58 / D-032" in report, "Missing durable approval reference")
    require("[Scene-plan phase spec](../scene-plan-phase-spec-volume-i.md)" in report and
            "SPQ-01–06 (R-59–R-64 / D-033)" in report and
            "chỉ mở candidate scene-plan implementation" in report,
            "Scene-plan phase approval boundary missing")
    author_decisions = read(AUTHOR_DECISIONS)
    decision_log = read(DECISION_LOG)
    for decision in range(53, 59):
        require(f"| R-{decision} |" in author_decisions, f"Missing R-{decision}")
    require("QUYẾT ĐỊNH D-032" in decision_log and "V1CBQ-01–06" in decision_log,
            "Missing D-032 approval record")
    require(sequence_md.count("| V1-CAND-") == 25, "Markdown sequence must project 25 rows")
    require("PHYSICAL_CONVERGENCE_VOLUME_I = PRESENT" not in sequence_md,
            "Physical convergence boundary contradiction")

    link_count = 0
    if check_links:
        for name, body in texts.items():
            if not name.endswith(".md"):
                continue
            origin = OUT / name
            for target in LINK.findall(body):
                if "://" in target or target.startswith("#"):
                    continue
                resolved = (origin.parent / target.split("#", 1)[0]).resolve()
                require(resolved.exists(), f"Broken link in {name}: {target}")
                link_count += 1

    return {
        "sequence_rows": len(rows),
        "briefs": len(brief_names),
        "pov_counts": dict(sorted(Counter(row["primary_pov"] for row in rows).items())),
        "movement_counts": dict(sorted(Counter(row["movement_id"] for row in rows).items())),
        "provenance_rows": len(provenance),
        "file_links": link_count,
    }


def self_test(texts: dict[str, str]) -> list[str]:
    cases = [
        ("missing-brief", lambda t: {k: v for k, v in t.items() if k != "briefs/chapter_25.md"}),
        ("satellite-in-sequence", lambda t: {**t, "chapter-sequence.tsv": t["chapter-sequence.tsv"].replace("V1-CAND-021", "V1-CAND-020", 1)}),
        ("wrong-pov", lambda t: {**t, "chapter-sequence.tsv": t["chapter-sequence.tsv"].replace("TINH_XUYEN", "HA_NUONG", 1)}),
        ("title-drift", lambda t: {**t, "chapter-sequence.tsv": t["chapter-sequence.tsv"].replace("Ngôi Chủ Chưa Yên", "Tên Khác", 1)}),
        ("bad-dependency-order", lambda t: {**t, "chapter-sequence.tsv": t["chapter-sequence.tsv"].replace("V1-CAND-017\tM3", "V1-CAND-021\tM3", 1)}),
        ("exact-date", lambda t: {**t, "briefs/chapter_01.md": t["briefs/chapter_01.md"] + "\n1191-01-01\n"}),
        ("scene-injection", lambda t: {**t, "briefs/chapter_01.md": t["briefs/chapter_01.md"] + "\n## Scene sequence\n"}),
        ("custody-injection", lambda t: {**t, "briefs/chapter_04.md": t["briefs/chapter_04.md"] + "\nDU_LONG_OBJECTIVE_CUSTODY = LE_THU_THUY\n"}),
        ("missing-result-ref", lambda t: {**t, "provenance-ledger.tsv": t["provenance-ledger.tsv"].replace("tasks[task_id=1].subtasks[sub_id=1]", "RESULT_MISSING", 1)}),
        ("wrong-brief-function", lambda t: {**t, "briefs/chapter_01.md": t["briefs/chapter_01.md"].replace("Source function: `V1-CAND-001`", "Source function: `V1-CAND-002`", 1)}),
        ("early-meeting", lambda t: {**t, "briefs/chapter_25.md": t["briefs/chapter_25.md"] + "\nPHYSICAL_CONVERGENCE_VOLUME_I = PRESENT\n"}),
        ("approval-regression", lambda t: {**t, "chapter-sequence.tsv": t["chapter-sequence.tsv"].replace("AUTHOR-APPROVED PLANNING / V1CBQ-01–06 / NOT CANON", "PROPOSAL / AUTHOR REVIEW REQUIRED / NOT CANON", 1)}),
    ]
    passed: list[str] = []
    for label, mutate in cases:
        try:
            validate(mutate(dict(texts)), check_links=False)
        except ValueError:
            passed.append(label)
        else:
            raise ValueError(f"Negative test accepted invalid package: {label}")
    return passed


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    texts = load_texts()
    counts = validate(texts)
    tests = self_test(texts) if args.self_test else []
    print(json.dumps({
        "validation": "PASS",
        "assurance": "SEQUENCE_BRIEFS_PROVENANCE_AND_BOUNDARIES_ONLY_NOT_SEMANTIC",
        **counts,
        "negative_tests": tests,
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
