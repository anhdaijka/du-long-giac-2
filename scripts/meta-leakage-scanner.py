#!/usr/bin/env python3
"""
meta-leakage-scanner.py — Deterministic Prose Linter & Leakage Scanner for Du Long Giác 2.
Ported directly from D:/Games/Server Client/Server KT/du-long-giac/.tools/evidence/meta_leakage_scanner.py
"""
from __future__ import annotations
import argparse
import re
import sys
from pathlib import Path

# Ensure UTF-8 output
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

# 1. Meta / planning terms forbidden in narrative prose
META_TERMS = [
    r"\broute\b",
    r"\barc\b",
    r"\bbeat\b",
    r"\baperture\b",
    r"\bcivic-martial\b",
    r"\bcivic\b",
    r"\binstitutional\b",
    r"\baccountability\b",
    r"\benvelope\b",
    r"\bblueprint\b",
    r"\brehydration\b",
    r"\bpresence_on_page\b",
    r"\bfact_ref\b",
    r"\bchapter_local\b",
    r"\bserial_durable\b",
    r"\bverified_file\b",
    r"\bsource_claim\b",
    r"\bnegative_guard\b",
    r"\bopen_protected\b",
    r"\bopen_field\b",
    r"\bv\d+_ch\d+\b",
    r"\bch\d{2}\b",
    r"\bfamily\s+\d+\b",
    r"\bsource_family\b",
    r"\bsource_task\b",
    r"\bdisposition\b",
    r"\bprovenance\b",
    r"\bepistemic\b",
    r"\bwriter_packet\b",
    r"\bpreflight\b",
    r"\btask\s+\d+\b",
    r"\bsubtask\s+\d+\b",
    r"\btier\b",
    r"\btier\s+\d+\b",
]

# 2. AI Synthetic Telling / Explanatory Scaffolding (disallowed in narrator prose)
EXPLANATORY_SCAFFOLDS = [
    (r"\b[Đđ]ó chính là\b", "Synthetic explanatory phrase ('đó chính là' — show action/identity directly)"),
    (r"\b[Đđ]ây chính là\b", "Synthetic explanatory phrase ('đây chính là')"),
    (r"\b[Kk]ẻ đó chính là\b", "Synthetic introduction scaffold ('kẻ đó chính là')"),
    (r"\b[Nn]gười đó chính là\b", "Synthetic introduction scaffold ('người đó chính là')"),
    (r"\b[Kk]ẻ đang đối diện.*chính là\b", "Synthetic introduction scaffold ('kẻ đang đối diện... chính là')"),
    (r"\bchính là\b", "Synthetic explanatory particle ('chính là' — integrate identity directly without narrator announcement)"),
    (r"\b[Đđ]ó là\b", "Synthetic explanatory phrase ('đó là' — show sensory details directly)"),
    (r"\b[Đđ]ây là\b", "Synthetic explanatory phrase ('đây là')"),
    (r"\b[Ấấ]y là\b", "Synthetic explanatory phrase ('ấy là')"),
    (r"\b[Vv]ốn là\b", "Synthetic biographical exposition ('vốn là')"),
    (r"\bthực chất là\b", "Synthetic explanatory phrase ('thực chất là')"),
    (r"\bthực ra là\b", "Synthetic explanatory phrase ('thực ra là')"),
    (r"\bcó nghĩa là\b", "Discursive explanatory connective ('có nghĩa là')"),
    (r"\bnói cách khác\b", "Discursive explanatory connective ('nói cách khác')"),
    (r"\b[Nn]ơi ấy là\b", "Synthetic spatial exposition ('nơi ấy là')"),
    (r"\b[Nn]ơi đó là\b", "Synthetic spatial exposition ('nơi đó là')"),
    (r"\b[Nn]ơi đây là\b", "Synthetic spatial exposition ('nơi đây là')"),
    (r"\b[Nn]ơi đó chính là\b", "Synthetic explanatory phrase ('nơi đó chính là')"),
    (r"\b[Nn]ơi đây vừa là\b", "Synthetic spatial exposition ('nơi đây vừa là')"),
    (r"\bchàng chính là\b", "Synthetic explanatory phrase ('chàng chính là')"),
    (r"\bnàng chính là\b", "Synthetic explanatory phrase ('nàng chính là')"),
    (r"\by chính là\b", "Synthetic explanatory phrase ('y chính là')"),
    (r"\bhắn chính là\b", "Synthetic explanatory phrase ('hắn chính là')"),
    (r"\bngười thanh niên đó chính là\b", "Synthetic introduction scaffold ('người thanh niên đó chính là')"),
    (r"\b[Cc]hàng hiểu rằng\b", "Narrator cognitive lecturing ('chàng hiểu rằng' — show action/sensory perception directly)"),
    (r"\b[Nn]àng hiểu rằng\b", "Narrator cognitive lecturing ('nàng hiểu rằng')"),
    (r"\b[Yy] hiểu rằng\b", "Narrator cognitive lecturing ('y hiểu rằng')"),
    (r"\b[Hh]ắn hiểu rằng\b", "Narrator cognitive lecturing ('hắn hiểu rằng')"),
    (r"\bchàng nhận ra rằng\b", "Narrator cognitive lecturing ('chàng nhận ra rằng')"),
    (r"\bdường như đã lường trước\b", "Omniscient narrator guesswork ('dường như đã lường trước')"),
    (r"\bkhông ngờ rằng\b", "Narrator expository telling ('không ngờ rằng')"),
    (r"\bthực chất chỉ là một mắt xích\b", "Narrator thematic recap ('thực chất chỉ là một mắt xích')"),
    (r"\bmón nợ đạo đức\b", "Narrator moralizing ('món nợ đạo đức')"),
    (r"\bbàn cờ chính trị\b", "Narrator thematic lecturing ('bàn cờ chính trị')"),
    (r"\bvĩnh viễn không còn là\b", "Narrator thematic moralizing ('vĩnh viễn không còn là')"),
    (r"\bsau một hồi\b", "Sloppy convert translation scaffold ('sau một hồi')"),
    (r"\btrong lúc nhất thời\b", "Sloppy convert translation phrase ('trong lúc nhất thời')"),
    (r"\bđáy lòng không khỏi\b", "Cognitive telling scaffold ('đáy lòng không khỏi')"),
    (r"\blập tức liền\b", "Sloppy convert translation connective ('lập tức liền')"),
    (r"\bnỗi cô đơn sâu sắc\b", "Abstract psychological labeling ('nỗi cô đơn sâu sắc')"),
    (r"\bcảm giác cay đắng\b", "Abstract psychological labeling ('cảm giác cay đắng')"),
    (r"\bsự tuyệt vọng tột cùng\b", "Abstract psychological labeling ('sự tuyệt vọng tột cùng')"),
]

# 3. AI Cliché Narrative Closures / Formulaic Grandstanding
CLICHE_CLOSURES = [
    (r"bánh xe số phận", "AI cliché narrative closure ('bánh xe số phận')"),
    (r"bàn cờ ân oán", "AI cliché narrative closure ('bàn cờ ân oán')"),
    (r"bắt đầu chuyển động", "AI cliché closure ('bắt đầu chuyển động')"),
    (r"chính thức lún sâu", "AI cliché closure ('chính thức lún sâu')"),
    (r"chính thức.*bước vào.*phong ba", "AI cliché closure ('chính thức bước vào phong ba')"),
    (r"bước chân.*chính thức", "AI cliché closure ('bước chân... chính thức')"),
    (r"phong ba bão táp của chốn võ lâm", "AI cliché closure ('phong ba bão táp của chốn võ lâm')"),
    (r"sóng gió giang hồ chính thức", "AI cliché closure ('sóng gió giang hồ chính thức')"),
    (r"hành trình.*chính thức bắt đầu", "AI cliché closure ('hành trình... chính thức bắt đầu')"),
    (r"chính thức khép lại", "AI cliché closure ('chính thức khép lại')"),
    (r"đã chính thức khép lại", "AI cliché closure ('đã chính thức khép lại')"),
]

# 4. Modern Essay & Discursive Connectives (disallowed in narrative prose)
MODERN_ESSAY_CONNECTIVES = [
    (r"\b[Tt]uy nhiên\b", "Modern analytical connective ('tuy nhiên' — use 'song', 'nhưng', 'nào ngờ', etc.)"),
    (r"\b[Mm]ặc dù vậy\b", "Modern analytical connective ('mặc dù vậy')"),
    (r"\b[Đđ]áng chú ý là\b", "Modern discursive phrase ('đáng chú ý là')"),
    (r"\b[Cc]ó thể thấy rằng\b", "Modern essay phrase ('có thể thấy rằng')"),
    (r"\b[Kk]hông thể phủ nhận rằng\b", "Modern essay phrase ('không thể phủ nhận rằng')"),
    (r"\b[Hh]ơn thế nữa\b", "Modern discursive phrase ('hơn thế nữa')"),
    (r"\b[Rr]õ ràng là\b", "Modern discursive phrase ('rõ ràng là' — use 'đích thị là', 'chính thị là')"),
    (r"\b[Vv]ề cơ bản\b", "Modern analytical phrase ('về cơ bản')"),
    (r"\b[Tt]rên thực tế\b", "Modern analytical phrase ('trên thực tế')"),
]

# 5. Inflated & Supernatural Martial Arts Exaggerations & Xianxia Tropes
INFLATED_MARTIAL_CLICHES = [
    (r"xé toạc không gian", "Inflated supernatural exaggeration ('xé toạc không gian')"),
    (r"chấn động càn khôn", "Inflated martial exaggeration ('chấn động càn khôn')"),
    (r"uy lực khủng khiếp", "Generic abstract martial cliché ('uy lực khủng khiếp')"),
    (r"bài sơn hải đảo", "Generic inflated cliché ('bài sơn hải đảo')"),
    (r"\buy áp\b", "Xianxia trope ('uy áp' — use physical pressure, stance or environmental tension)"),
    (r"\bchân khí sôi trào\b", "Xianxia cliché ('chân khí sôi trào')"),
    (r"\blinh hồn chấn động\b", "Xianxia cliché ('linh hồn chấn động')"),
    (r"\bkinh hãi tột độ\b", "Melodrama cliché ('kinh hãi tột độ' — show biological/physical reaction)"),
    (r"\bhít sâu một hơi\b", "Translated webnovel cliché ('hít sâu một hơi' — show physical breathing)"),
    (r"\bđồng tử co rút\b", "Translated webnovel cliché ('đồng tử co rút')"),
]

# 6. Syntax / markdown leakages
SYNTAX_PATTERNS = [
    (r"<!--\s*DLG_", "HTML/DLG Comment block"),
    (r"<[A-Z0-9_]{3,}>", "System/Prompt XML tag"),
    (r"\{\{.*?\}\}", "Template tag / Checkpoint variable"),
    (r"```[a-z]*", "Fenced code block inside prose"),
]

def extract_narrator_text(line: str) -> str:
    """
    Extract narrator prose from a line, strictly ignoring character dialogue inside quotes or em-dash tags.
    This protects character voice (bắng nhắng, tự trào, khẩu khí bến bãi) from false-positive linter flags.
    """
    line = line.strip()
    if not line or line.startswith("#"):
        return ""
    
    # 1. Strip content inside quotation marks (Vietnamese curved quotes, ASCII quotes, angle quotes)
    line_no_quotes = re.sub(r'“[^”]*”|"[^"]*"|«[^»]*»', '', line)
    
    # 2. If line starts with dialogue dash (em-dash or en-dash or hyphen)
    if line.startswith("—") or line.startswith("–") or line.startswith("-"):
        parts = re.split(r"\s*[—–-]+\s*", line_no_quotes)
        narrator_parts = []
        for idx, part in enumerate(parts):
            if idx == 0:
                continue
            if idx % 2 == 0:  # narrator action/tag (e.g. — Y vung đao thét lớn — ...)
                narrator_parts.append(part)
        return " ".join(narrator_parts)
    else:
        return line_no_quotes


def scan_manuscript(path: Path) -> tuple[list[str], int]:
    errors = []
    if not path.is_file():
        return [f"manuscript file not found: {path}"], 0

    content = path.read_text(encoding="utf-8")
    lines = content.splitlines()

    # Strip YAML frontmatter for pure prose checks
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

    full_prose = "\n".join(l for _, l in prose_lines)
    # Count words in prose (strip markdown headers & symbols)
    clean_text = re.sub(r"(?m)^#{1,6}\s.*$", "", full_prose)
    clean_text = re.sub(r"\*{1,3}|_{1,3}", "", clean_text)
    words = re.findall(r"[0-9A-Za-zÀ-ỹĐđ]+", clean_text)
    word_count = len(words)

    # 1. Check syntax leaks
    for pattern, desc in SYNTAX_PATTERNS:
        for line_num, line in prose_lines:
            if re.search(pattern, line):
                errors.append(f"Line {line_num}: {desc} detected ('{line.strip()[:60]}')")

    # 2. Check meta/planning terms (Forbidden in prose)
    for pattern in META_TERMS:
        for line_num, line in prose_lines:
            if line.startswith("#"):
                continue
            m = re.search(pattern, line, re.IGNORECASE)
            if m:
                errors.append(f"Line {line_num}: Meta planning term '{m.group(0)}' detected: \"{line.strip()[:70]}\"")

    # 3. Check AI Explanatory Scaffolds (Forbidden in narrator prose)
    for pattern, desc in EXPLANATORY_SCAFFOLDS:
        for line_num, line in prose_lines:
            narrator_prose = extract_narrator_text(line)
            if not narrator_prose:
                continue
            m = re.search(pattern, narrator_prose, re.IGNORECASE)
            if m:
                errors.append(f"Line {line_num}: {desc} detected in narrator prose: \"{narrator_prose[:70]}\"")

    # 4. Check AI Cliché Closures (Forbidden everywhere in prose)
    for pattern, desc in CLICHE_CLOSURES:
        for line_num, line in prose_lines:
            if line.startswith("#"):
                continue
            m = re.search(pattern, line, re.IGNORECASE)
            if m:
                errors.append(f"Line {line_num}: {desc} detected: \"{line.strip()[:70]}\"")

    # 5. Check Modern Essay Connectives (Forbidden in narrator prose)
    for pattern, desc in MODERN_ESSAY_CONNECTIVES:
        for line_num, line in prose_lines:
            narrator_prose = extract_narrator_text(line)
            if not narrator_prose:
                continue
            m = re.search(pattern, narrator_prose, re.IGNORECASE)
            if m:
                errors.append(f"Line {line_num}: {desc} detected in narrator prose: \"{narrator_prose[:70]}\"")

    # 6. Check Inflated Martial Clichés
    for pattern, desc in INFLATED_MARTIAL_CLICHES:
        for line_num, line in prose_lines:
            if line.startswith("#"):
                continue
            m = re.search(pattern, line, re.IGNORECASE)
            if m:
                errors.append(f"Line {line_num}: {desc} detected: \"{line.strip()[:70]}\"")

    # 7. Substantiality floor (3500 words)
    if word_count < 3500:
        errors.append(f"Substantiality floor warning: {word_count} words (expected >= 3500 words of rich living wulin)")

    return errors, word_count

def main():
    parser = argparse.ArgumentParser(description="Scan prose manuscript for meta-vocabulary and literary purity.")
    parser.add_argument("--manuscript", default=None, help="Path to manuscript file (default: scan all chapters)")
    args = parser.parse_args()

    if args.manuscript:
        targets = [Path(args.manuscript)]
    else:
        chapters_dir = Path("chapters")
        targets = sorted(chapters_dir.glob("chapter_*.md"))
        if not targets:
            targets = [Path("chapters/chapter_01.md")]

    has_failure = False
    for ms_path in targets:
        errors, word_count = scan_manuscript(ms_path)
        print(f"=== SCANNING MANUSCRIPT: {ms_path.as_posix()} ===")
        print(f"Total word count: {word_count} words")
        
        if errors:
            has_failure = True
            print(f"\n[FAIL] Found {len(errors)} issues:")
            for err in errors:
                print(f"  - {err}")
            print()
        else:
            print("[PASS] 0 leaks, 0 explanatory scaffolds, 0 modern connectives, valid substantiality floor!\n")

    if has_failure:
        sys.exit(1)
    else:
        print("[ALL PASS] All scanned chapters passed quality contracts.")
        sys.exit(0)

if __name__ == "__main__":
    main()

