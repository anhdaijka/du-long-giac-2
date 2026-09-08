#!/usr/bin/env python3
"""Full-read review structure verifier for Novel OS Reliability Layer v2.

Validates that a review declares sequential coverage of the CURRENT chapter
and contains concrete, line-grounded evidence. No hashes or manuscript locks.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

MAX_RANGE_LINES = 120
COVERAGE_HEADING_RE = re.compile(r"^##\s+.*Full-Read Coverage.*$", re.MULTILINE | re.IGNORECASE)
NEXT_H2_RE = re.compile(r"^##\s+", re.MULTILINE)
RANGE_RE = re.compile(r"`L(\d+)-L(\d+)`")
GATE_HEADING_RE = re.compile(r"^###\s+Gate\s+([A-E]):", re.MULTILINE)
STATUS_RE = re.compile(r"\*\*(PASS|FAIL)\*\*", re.IGNORECASE)
VERDICT_RE = re.compile(r"\*\*(APPROVED|REVISE_REQUIRED)\*\*", re.IGNORECASE)
EVIDENCE_LOC_RE = re.compile(r"\*\*Vị trí\*\*:\s*`L(\d+)-L(\d+)`")
QUOTE_RE = re.compile(r"\*\*Trích đoạn\*\*:\s*(.+)")
V2_REVIEW_NAME_RE = re.compile(r"^chapter_(.+)_review_v2\.md$")


def normalize_text(value: str) -> str:
    value = value.strip()
    value = re.sub(r"^[*_`“”\"'‘’]+|[*_`“”\"'‘’]+$", "", value)
    value = re.sub(r"\s+", " ", value)
    return value.strip()


def section_after_heading(text: str, heading_re: re.Pattern[str]) -> str | None:
    match = heading_re.search(text)
    if not match:
        return None
    start = match.end()
    next_match = NEXT_H2_RE.search(text, start)
    end = next_match.start() if next_match else len(text)
    return text[start:end]


def parse_coverage(section: str) -> tuple[list[tuple[int, int, str]], list[str]]:
    ranges: list[tuple[int, int, str]] = []
    errors: list[str] = []
    for line in section.splitlines():
        match = RANGE_RE.search(line)
        if not match:
            continue
        start, end = map(int, match.groups())
        if start < 1 or end < start:
            errors.append(f"Invalid coverage range L{start}-L{end}")
            continue
        if end - start + 1 > MAX_RANGE_LINES:
            errors.append(
                f"Coverage range L{start}-L{end} spans {end-start+1} lines; "
                f"maximum is {MAX_RANGE_LINES} to discourage one-shot pseudo-review."
            )
        after = line[match.end():].strip(" \t—–-:")
        if len(after) < 12 or after.startswith("["):
            errors.append(
                f"Coverage range L{start}-L{end} needs a concrete observation after the range."
            )
        ranges.append((start, end, after))
    return ranges, errors


def coverage_errors(ranges: list[tuple[int, int, str]], total_lines: int) -> list[str]:
    errors: list[str] = []
    if total_lines <= 0:
        return ["Chapter has no lines"]
    if not ranges:
        return ["No machine-readable coverage ranges found"]

    normalized = sorted((s, e) for s, e, _ in ranges)
    cursor = 1
    for start, end in normalized:
        if start > total_lines:
            errors.append(f"Coverage starts beyond EOF: L{start}-L{end}, EOF is L{total_lines}")
            continue
        end = min(end, total_lines)
        if start > cursor:
            errors.append(f"Coverage gap: L{cursor}-L{start-1}")
        cursor = max(cursor, end + 1)
    if cursor <= total_lines:
        errors.append(f"Coverage gap: L{cursor}-L{total_lines}")
    return errors


def gate_sections(text: str) -> dict[str, str]:
    matches = list(GATE_HEADING_RE.finditer(text))
    result: dict[str, str] = {}
    for idx, match in enumerate(matches):
        gate = match.group(1).upper()
        start = match.end()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
        result[gate] = text[start:end]
    return result


def validate_evidence_spans(review_text: str, chapter_lines: list[str]) -> list[str]:
    errors: list[str] = []
    locations = list(EVIDENCE_LOC_RE.finditer(review_text))
    if len(locations) < 4:
        errors.append(
            f"Mandatory evidence requires at least 4 `Lx-Ly` spans; found {len(locations)}"
        )
        return errors

    for idx, loc in enumerate(locations, 1):
        start, end = map(int, loc.groups())
        if start < 1 or end < start or end > len(chapter_lines):
            errors.append(
                f"Evidence span {idx} L{start}-L{end} is outside current chapter L1-L{len(chapter_lines)}"
            )
            continue

        block_end = locations[idx].start() if idx < len(locations) else len(review_text)
        block = review_text[loc.end():block_end]
        quote_match = QUOTE_RE.search(block)
        if not quote_match:
            errors.append(f"Evidence span {idx} L{start}-L{end} is missing **Trích đoạn**")
            continue

        quote = normalize_text(quote_match.group(1))
        if len(quote) < 8 or quote.startswith("["):
            errors.append(f"Evidence span {idx} L{start}-L{end} has an empty/placeholder quote")
            continue

        source = normalize_text(" ".join(chapter_lines[start - 1:end]))
        if quote not in source:
            errors.append(
                f"Evidence span {idx} quote does not match current chapter text at L{start}-L{end}"
            )

    return errors


def validate_review(chapter_path: Path, review_path: Path, require_approval: bool) -> list[str]:
    errors: list[str] = []
    if not chapter_path.is_file():
        return [f"Missing chapter: {chapter_path}"]
    if not review_path.is_file():
        return [f"Missing review: {review_path}"]

    chapter_lines = chapter_path.read_text(encoding="utf-8").splitlines()
    review_text = review_path.read_text(encoding="utf-8")

    coverage_section = section_after_heading(review_text, COVERAGE_HEADING_RE)
    if coverage_section is None:
        errors.append("Missing `## ... Full-Read Coverage ...` section")
    else:
        ranges, range_errors = parse_coverage(coverage_section)
        errors.extend(range_errors)
        errors.extend(coverage_errors(ranges, len(chapter_lines)))

    sections = gate_sections(review_text)
    missing = [gate for gate in "ABCDE" if gate not in sections]
    if missing:
        errors.append(f"Missing review gate section(s): {', '.join(missing)}")

    gate_statuses: dict[str, str] = {}
    for gate, section in sections.items():
        status_match = STATUS_RE.search(section)
        if not status_match:
            errors.append(f"Gate {gate} is missing explicit **PASS** or **FAIL** status")
        else:
            gate_statuses[gate] = status_match.group(1).upper()

    errors.extend(validate_evidence_spans(review_text, chapter_lines))

    verdict_match = VERDICT_RE.search(review_text)
    verdict = verdict_match.group(1).upper() if verdict_match else None
    if verdict is None:
        errors.append("Missing final **APPROVED** or **REVISE_REQUIRED** verdict")

    if verdict == "APPROVED" and any(v == "FAIL" for v in gate_statuses.values()):
        errors.append("Verdict is APPROVED while at least one Gate is FAIL")

    if require_approval:
        if verdict != "APPROVED":
            errors.append("--require-approval requested but review verdict is not APPROVED")
        failed = [g for g, v in gate_statuses.items() if v != "PASS"]
        if failed:
            errors.append(
                "--require-approval requested but these Gates are not PASS: "
                + ", ".join(sorted(failed))
            )

    return errors


def infer_paths(chapter: str) -> tuple[Path, Path]:
    return (
        Path("chapters") / f"chapter_{chapter}.md",
        Path("reviews") / f"chapter_{chapter}_review.md",
    )


def discover_v2_reviews() -> list[tuple[Path, Path]]:
    reviews_root = Path("reviews")
    if not reviews_root.exists():
        return []

    pairs: list[tuple[Path, Path]] = []
    for review_path in sorted(reviews_root.rglob("chapter_*_review_v2.md")):
        match = V2_REVIEW_NAME_RE.match(review_path.name)
        if not match:
            continue
        chapter_suffix = match.group(1)
        chapter_path = Path("chapters") / f"chapter_{chapter_suffix}.md"
        pairs.append((chapter_path, review_path))
    return pairs


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate full-read review coverage against the current manuscript."
    )
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--chapter-number", help="Chapter suffix, e.g. 10, 08a")
    mode.add_argument(
        "--all-v2",
        action="store_true",
        help="Validate all reviews/**/chapter_*_review_v2.md files without touching legacy reviews",
    )
    parser.add_argument("--chapter", help="Explicit chapter path")
    parser.add_argument("--review", help="Explicit review path")
    parser.add_argument(
        "--require-approval",
        action="store_true",
        help="Also require APPROVED verdict and Gate A-E PASS",
    )
    args = parser.parse_args()

    pairs: list[tuple[Path, Path]] = []
    if args.all_v2:
        if args.chapter or args.review:
            parser.error("--chapter/--review cannot be combined with --all-v2")
        pairs = discover_v2_reviews()
        if not pairs:
            print("[REVIEW-GUARD] No v2 review artifacts found; nothing to validate.")
            return 0
    else:
        chapter_path, review_path = infer_paths(args.chapter_number)
        if args.chapter:
            chapter_path = Path(args.chapter)
        if args.review:
            review_path = Path(args.review)
        pairs = [(chapter_path, review_path)]

    all_errors: list[str] = []
    for chapter_path, review_path in pairs:
        print(f"=== REVIEW CONTRACT: {review_path} ===")
        errors = validate_review(chapter_path, review_path, args.require_approval)
        if errors:
            for error in errors:
                print(f"  [FAIL] {error}")
            all_errors.extend(f"{review_path}: {error}" for error in errors)
        else:
            print(
                "  [PASS] Review structurally covers the current manuscript and contains "
                "line-grounded evidence. Literary judgment remains semantic."
            )

    if all_errors:
        print(f"\n[REVIEW-GUARD FAILED] {len(all_errors)} review-contract issue(s).")
        return 1

    print("\n[REVIEW-GUARD PASS] All selected v2 review contracts satisfied.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
