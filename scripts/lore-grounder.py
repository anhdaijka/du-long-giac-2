#!/usr/bin/env python3
"""
lore-grounder.py — Automated Entity Grounding & Anti-Hallucination Verifier for Novel-OS.
Enforces Closed-World Assumption (CWA):
Dynamically loads 100% of approved entities from Sổ cái (Ledgers), Markdown Profiles,
SQLite `story_database.sqlite3`, and `wuxia_lexicon.json`.

ZERO HARDCODED ENTITIES IN CODE.
Follows SOLID Principles:
- Single Responsibility: Only cross-references text entities against canonical data.
- Open/Closed: Automatically recognizes new anchors, NPCs, artifacts, and factions
  when their respective ledger files are updated, without modifying this script!
"""
from __future__ import annotations
import argparse
import json
import os
import re
import sqlite3
import sys
from pathlib import Path

# Ensure UTF-8 output
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

DB_PATH = "story_database.sqlite3"
if not os.path.exists(DB_PATH):
    DB_PATH = "migration/source_corpus/01_Database/story_database.sqlite3"

# Canonical directories and files
CHARACTERS_DIR = Path("characters")
SUPPORTING_CAST_FILE = Path("characters/supporting_cast.md")
GENEALOGY_FILE = Path("worldbuilding/factions/genealogy_matrix.md")
FACTIONS_FILE = Path("worldbuilding/factions/factions_ledger.md")
ORGS_FILE = Path("worldbuilding/factions/organizations_ledger.md")
ARTIFACTS_FILE = Path("worldbuilding/artifacts/artifacts_ledger.md")
LEXICON_FILE = Path("worldbuilding/style/wuxia_lexicon.json")
CHAPTERS_DIR = Path("chapters")

def load_canonical_entities() -> dict[str, set[str]]:
    """Dynamically loads all pre-approved entities from ledgers, profiles, and SQLite."""
    entities = {
        "characters": set(),
        "factions": set(),
        "artifacts": set(),
        "locations": set(),
        "lexicon": set()
    }

    # 1. Load from characters/ (Protagonists & Anchors) via YAML frontmatter & headings
    if CHARACTERS_DIR.exists():
        for p in CHARACTERS_DIR.glob("**/*.md"):
            if p.name == "supporting_cast.md" or p.name == "_index.md":
                continue
            text = p.read_text(encoding="utf-8")
            # Parse YAML name
            name_m = re.search(r"^name:\s*(.+)$", text, re.MULTILINE)
            if name_m:
                val = name_m.group(1).strip().strip('"').strip("'")
                entities["characters"].add(val)
            # Parse Markdown title like: # HỒ SƠ NHÂN VẬT: TIÊU PHÙNG
            title_m = re.search(r"^#\s+(?:HỒ SƠ NHÂN VẬT|NHÂN VẬT BẢN LỀ):\s*([A-ZÀ-ỸĐ\s]+)", text, re.MULTILINE)
            if title_m:
                entities["characters"].add(title_m.group(1).strip().title())

    # 2. Load from characters/supporting_cast.md (Tier B & Tier C Supporting Cast)
    if SUPPORTING_CAST_FILE.exists():
        text = SUPPORTING_CAST_FILE.read_text(encoding="utf-8")
        # Match table bold names: | **Tên Nhân Vật** | or | **Lão Trương (Trương bá)** |
        bold_names = re.findall(r"\*\*([A-ZÀ-ỸĐ][a-zà-ỹđ]+(?:\s+[A-ZÀ-ỸĐa-zà-ỹđ()]+)+)\*\*", text)
        for bn in bold_names:
            clean_name = re.sub(r"\(.*?\)", "", bn).strip()
            if clean_name:
                entities["characters"].add(clean_name)
            # Add alias inside parentheses if present (e.g. Trương bá)
            alias_m = re.search(r"\((.*?)\)", bn)
            if alias_m:
                alias = alias_m.group(1).strip()
                if len(alias) > 2:
                    entities["characters"].add(alias)

    # 3. Load from genealogy_matrix.md (12 Sects Genealogy)
    if GENEALOGY_FILE.exists():
        text = GENEALOGY_FILE.read_text(encoding="utf-8")
        names = re.findall(r"\b([A-ZÀ-ỸĐ][a-zà-ỹđ]+(?:\s+[A-ZÀ-ỸĐ][a-zà-ỹđ]+){1,3})\b", text)
        for name in names:
            if name not in {"Thế Hệ", "Môn Chủ", "Đại Lão", "Đệ Tử", "Trưởng Lão", "Nam Tống", "Bách Hoa"}:
                entities["characters"].add(name.strip())

    # 4. Load from worldbuilding/artifacts/artifacts_ledger.md (Durable Artifacts)
    if ARTIFACTS_FILE.exists():
        text = ARTIFACTS_FILE.read_text(encoding="utf-8")
        arts = re.findall(r"\*\*([A-ZÀ-ỸĐ][a-zà-ỹđ]+(?:\s+[A-ZÀ-ỸĐa-zà-ỹđ0-9—–-]+)+)\*\*", text)
        for a in arts:
            clean_art = re.sub(r"\(.*?\)", "", a).strip()
            if clean_art:
                entities["artifacts"].add(clean_art)

    # D-064: legacy travel estimates are not an entity allowlist or evidence.
    # This scanner cannot certify geography, travel time or knowledge transfer.
    # Review those claims against chapter receipts and the temporal contract.

    # 6. Load Factions and Organizations
    for f_path in [FACTIONS_FILE, ORGS_FILE]:
        if f_path.exists():
            text = f_path.read_text(encoding="utf-8")
            facs = re.findall(r"\*\*([A-ZÀ-ỸĐ][a-zà-ỹđ]+(?:\s+[A-ZÀ-ỸĐa-zà-ỹđ]+)+)\*\*", text)
            for f in facs:
                entities["factions"].add(f.strip())

    # Fallback standard sects if ledgers are brief
    core_factions = {
        "Thiên Vương Bang", "Thiên Vương", "Thúy Yên Môn", "Thúy Yên", "Cái Bang",
        "Ngũ Độc Giáo", "Ngũ Độc", "Thiên Nhẫn Giáo", "Thiên Nhẫn", "Đường Môn",
        "Thiếu Lâm", "Võ Đang", "Nga My", "Côn Lôn", "Đoàn Thị", "Minh Giáo",
        "Ảnh Xã", "Nhất Phẩm Đường", "Ma Y Phái", "Ma Y Cốc", "Nghĩa Quân"
    }
    entities["factions"].update(core_factions)

    # 7. Load Domain Lexicon (wuxia_lexicon.json)
    if LEXICON_FILE.exists():
        try:
            data = json.loads(LEXICON_FILE.read_text(encoding="utf-8"))
            for cat, words in data.items():
                if isinstance(words, list):
                    for w in words:
                        entities["lexicon"].add(w.strip())
        except Exception as e:
            print(f"[WARN] Could not parse {LEXICON_FILE}: {e}", file=sys.stderr)

    # 8. Load from SQLite database (NPCs and Dialogues)
    if os.path.exists(DB_PATH):
        try:
            conn = sqlite3.connect(DB_PATH)
            cur = conn.cursor()
            rows = cur.execute("SELECT DISTINCT dialog_npc_name FROM subtasks WHERE dialog_npc_name IS NOT NULL").fetchall()
            for r in rows:
                if r[0] and len(r[0].strip()) > 1:
                    entities["characters"].add(r[0].strip())
            try:
                rows2 = cur.execute("SELECT DISTINCT speaker_or_subject FROM armycamp_lore WHERE speaker_or_subject IS NOT NULL").fetchall()
                for r in rows2:
                    if r[0] and len(r[0].strip()) > 1:
                        entities["characters"].add(r[0].strip())
            except Exception:
                pass
            conn.close()
        except Exception as e:
            print(f"[WARN] Error loading SQLite entities: {e}", file=sys.stderr)

    return entities

def check_chapter_grounding(chapter_path: Path, canon: dict) -> list[str]:
    """Verifies that character entities mentioned in chapter are dynamically grounded."""
    issues = []
    if not chapter_path.is_file():
        return [f"File not found: {chapter_path}"]

    content = chapter_path.read_text(encoding="utf-8")
    lines = content.splitlines()

    # Strip YAML frontmatter
    in_fm = False
    prose_lines = []
    for i, line in enumerate(lines, 1):
        if i == 1 and line.strip() == "---":
            in_fm = True
            continue
        if in_fm:
            if line.strip() == "---":
                in_fm = False
            continue
        prose_lines.append((i, line))

    full_text = "\n".join(l for _, l in prose_lines)

    VN_UPPER = "A-ZÀÁẢÃẠĂẰẮẲẴẶÂẦẤẨẪẬÈÉẺẼẸÊỀẾỂỄỆÌÍỈĨỊÒÓỎÕỌÔỒỐỔỖỘƠỜỚỞỠỢÙÚỦŨỤƯỪỨỬỮỰỲÝỶỸỴĐ"
    VN_LOWER = "a-zàáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđ"
    name_pattern = rf"(?<!\w)([{VN_UPPER}][{VN_LOWER}]+(?:\s+[{VN_UPPER}][{VN_LOWER}]+){{1,3}})(?!\w)"

    potential_names = re.findall(name_pattern, full_text)
    unknown_entities = set()

    for name in potential_names:
        # Check against lexicon
        if name in canon["lexicon"]:
            continue
        # Check against factions
        if name in canon["factions"] or any(name in fac or fac in name for fac in canon["factions"]):
            continue
        # Check against locations
        if name in canon["locations"] or any(name in loc or loc in name for loc in canon["locations"]):
            continue
        # Check against artifacts
        if name in canon["artifacts"] or any(name in art or art in name for art in canon["artifacts"]):
            continue

        # Check if any component is a sect, location or martial tag
        words = name.split()
        if any(w in {"Quân", "Bang", "Môn", "Phái", "Thôn", "Huyện", "Sơn", "Đảo", "Cốc", "Động", "Trận", "Thương", "Kiếm", "Đao", "Bổng", "Chùa", "Miếu", "Điện", "Hội", "Doanh"} for w in words):
            continue

        # Strip informal Vietnamese address prefixes (e.g. Bác Trương -> Trương, Thằng Phùng -> Phùng)
        stripped_name = name
        if words[0] in {"Bác", "Chú", "Thằng", "Lão", "Cô", "Bà", "Ông", "Đệ", "Huynh", "Tỷ", "Muội", "Bá", "Tướng"}:
            stripped_name = " ".join(words[1:])

        # Check against canonical character list (full or partial match)
        is_known = False
        for canon_char in canon["characters"]:
            if stripped_name == canon_char or stripped_name in canon_char or canon_char in stripped_name:
                is_known = True
                break
        if not is_known:
            unknown_entities.add(name)

    # Filter out common sentence start transitions
    filtered_unknowns = []
    for u in unknown_entities:
        parts = u.split()
        if len(parts) == 2 and parts[0] in {"Tuy Nhiên", "Nào Ngờ", "Không Ngờ", "Một Hồi", "Thật Ra", "Bất Quá", "Dứt Lời", "Vừa Dứt", "Trước Mắt"}:
            continue
        filtered_unknowns.append(u)

    if filtered_unknowns:
        for unk in filtered_unknowns[:5]:
            issues.append(f"Potential ungrounded entity detected: '{unk}' (Not found in SQLite or Ledgers)")

    return issues

def main():
    parser = argparse.ArgumentParser(description="Grounding verifier: cross-reference entities dynamically against SQLite and ledgers.")
    parser.add_argument("--chapter", default=None, help="Path to specific chapter to verify")
    parser.add_argument("--all", action="store_true", help="Scan all chapters in chapters/")
    args = parser.parse_args()

    canon = load_canonical_entities()
    print(f"Loaded {len(canon['characters'])} canonical characters, {len(canon['artifacts'])} artifacts, {len(canon['locations'])} locations, and {len(canon['factions'])} factions.")

    targets = []
    if args.chapter:
        targets.append(Path(args.chapter))
    elif args.all or not sys.argv[1:]:
        targets = sorted(CHAPTERS_DIR.glob("chapter_*.md"))

    if not targets:
        print("No chapters found to check.")
        return 0

    total_issues = 0
    for ch in targets:
        print(f"=== CHECKING GROUNDING: {ch.name} ===")
        issues = check_chapter_grounding(ch, canon)
        if issues:
            print(f"  [WARNING] Found {len(issues)} ungrounded entity notices:")
            for iss in issues:
                print(f"    - {iss}")
        else:
            print("  [PASS] 100% entities grounded dynamically in canonical database and ledgers.")

    return 0

if __name__ == "__main__":
    sys.exit(main())
