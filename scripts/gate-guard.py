#!/usr/bin/env python3
"""
Gate Guard: Programmatic enforcement of Novel-OS 3 Hard-Stop Gates.
Verifies that no chapter manuscript exists without an approved Chapter Brief and Review Report.
"""
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

CHAPTERS_DIR = "chapters"
BRIEFS_DIR = "briefs"
REVIEWS_DIR = "reviews"
REVISIONS_DIR = "revisions"

def check_gates():
    if not os.path.exists(CHAPTERS_DIR):
        print("[GATE-GUARD] No chapters directory found.")
        return 0

    chapter_files = [f for f in os.listdir(CHAPTERS_DIR) if f.startswith("chapter_") and f.endswith(".md")]
    if not chapter_files:
        print("[GATE-GUARD] No chapters found.")
        return 0

    errors = []

    for cf in chapter_files:
        match = re.match(r"chapter_(\d+[a-z]?)\.md", cf)
        if not match:
            continue
        ch_str = match.group(1)
        base_num = re.match(r"(\d+)", ch_str).group(1)

        # Brief can be chapter_02a_brief.md or chapter_02_brief.md
        brief_file = os.path.join(BRIEFS_DIR, f"chapter_{ch_str}_brief.md")
        if not os.path.exists(brief_file):
            brief_file = os.path.join(BRIEFS_DIR, f"chapter_{base_num}_brief.md")

        # Review can be chapter_02a_review.md or chapter_02_review.md
        review_file = os.path.join(REVIEWS_DIR, f"chapter_{ch_str}_review.md")
        if not os.path.exists(review_file):
            review_file = os.path.join(REVIEWS_DIR, f"chapter_{base_num}_review.md")

        print(f"=== CHECKING GATES FOR CHAPTER {ch_str} ===")


        # Check 1: Brief existence
        if not os.path.exists(brief_file):
            errors.append(f"[GATE-FAIL] Chapter {ch_str} has manuscript ({cf}) but MISSING Chapter Brief ({brief_file})!")
        else:
            # Check if brief is approved
            with open(brief_file, "r", encoding="utf-8") as bf:
                brief_content = bf.read()
                if "- [x] plan approved" not in brief_content and "[x] plan approved" not in brief_content:
                    errors.append(f"[GATE-FAIL] Chapter {ch_str} brief exists but is NOT APPROVED by Author! (Missing '- [x] plan approved')")
                else:
                    print(f"  [PASS] Hard Stop 1 (Brief approved): {brief_file}")

        # Check 2: Review report existence & 5-Gate runner validation
        if not os.path.exists(review_file):
            errors.append(f"[GATE-FAIL] Chapter {ch_str} has manuscript ({cf}) but MISSING Review Report ({review_file})!")
        else:
            with open(review_file, "r", encoding="utf-8") as rf:
                rev_content = rf.read()
                if "Gate A" not in rev_content or "Gate D" not in rev_content:
                    errors.append(f"[GATE-FAIL] Review Report ({review_file}) is incomplete! Missing 5-Gate Review Runner structure.")
                else:
                    print(f"  [PASS] Hard Stop 2 (Review report verified): {review_file}")

        # Check 3: Supporting Cast Protocol in Canon Diff (4-Pillar State Commitment Protocol)
        diff_file = os.path.join(REVISIONS_DIR, f"chapter_{ch_str}_canon_diff.md")
        if not os.path.exists(diff_file):
            diff_file = os.path.join(REVISIONS_DIR, f"chapter_{base_num}_canon_diff.md")
        if os.path.exists(diff_file):
            with open(diff_file, "r", encoding="utf-8") as df:
                diff_content = df.read()
                if "supporting_cast.md" not in diff_content:
                    errors.append(f"[GATE-FAIL] Canon Diff ({diff_file}) VIOLATES Gate 3: Missing mandatory 'characters/supporting_cast.md' update/audit section!")
                else:
                    print(f"  [PASS] Hard Stop 3 (Supporting Cast in Diff): {diff_file}")

    if errors:
        print("\n[GATE-GUARD FAILED] Violations detected:")
        for err in errors:
            print(f"  - {err}")
        return 1

    print("\n[GATE-GUARD PASS] All chapter manuscripts comply strictly with Novel-OS Hard-Stop Gates!")
    
    # Run Lore Guard scan
    print("\n--- Running Programmatic Lore Guard Scan ---")
    try:
        import subprocess
        lore_res = subprocess.run([sys.executable, "scripts/lore-guard.py", "--scan"], capture_output=False)
        if lore_res.returncode != 0:
            print("\n[GATE-GUARD FAILED] Lore Guard detected violations in project files!")
            return 1
    except Exception as e:
        print(f"[GATE-GUARD WARNING] Could not run lore-guard: {e}")

    # Run Lore Grounder check
    print("\n--- Running Programmatic Lore Grounder Check ---")
    try:
        import subprocess
        grounder_res = subprocess.run([sys.executable, "scripts/lore-grounder.py", "--all"], capture_output=False)
        if grounder_res.returncode != 0:
            print("\n[GATE-GUARD FAILED] Lore Grounder detected critical grounding errors!")
            return 1
    except Exception as e:
        print(f"[GATE-GUARD WARNING] Could not run lore-grounder: {e}")

    return 0

def check_temporal_continuity():
    """Programmatic enforcement of Rule TC-1 to TC-4: Zero Age Drift & Temporal Continuity."""
    print("\n=== [TEMPORAL-GUARD] SCANNING TEMPORAL CONTINUITY & AGE CONSISTENCY ===")
    chronology_file = os.path.join("plot", "chronology_matrix.md")
    if not os.path.exists(chronology_file):
        print("  [FAIL] Missing master chronology matrix: plot/chronology_matrix.md")
        return ["[TEMPORAL-FAIL] Missing plot/chronology_matrix.md!"]

    expected_ages_v1 = {
        "tĩnh xuyên": 20,
        "tiêu phùng": 17,
        "hạ nương": 16,
    }

    errors = []
    if os.path.exists(BRIEFS_DIR):
        for bf_name in sorted(os.listdir(BRIEFS_DIR)):
            if not bf_name.endswith("_brief.md"):
                continue
            bf_path = os.path.join(BRIEFS_DIR, bf_name)
            with open(bf_path, "r", encoding="utf-8") as f:
                content = f.read()

            # Check age consistency in Volume 1
            for char_name, exp_age in expected_ages_v1.items():
                # Check for wrong age like "Tĩnh Xuyên (20 tuổi)"
                wrong_age_matches = re.findall(rf"{char_name}\s*[\(—–\s]*(\d+)\s*tuổi", content, re.IGNORECASE)
                for age_str in wrong_age_matches:
                    age_val = int(age_str)
                    if age_val != exp_age:
                        errors.append(
                            f"[TEMPORAL-FAIL] {bf_name}: Character '{char_name.title()}' has age {age_val} tuổi, "
                            f"expected {exp_age} tuổi in Volume 1 (1191) per plot/chronology_matrix.md!"
                        )

            # Check for pov_age field in YAML frontmatter if present
            pov_age_match = re.search(r"pov_age:\s*(\d+)", content)
            pov_match = re.search(r"pov:\s*[\"']?([^\"'\n\r]+)[\"']?", content)
            if pov_age_match and pov_match:
                pov_name = pov_match.group(1).strip().lower()
                declared_age = int(pov_age_match.group(1))
                if pov_name in expected_ages_v1:
                    exp = expected_ages_v1[pov_name]
                    if declared_age != exp:
                        errors.append(
                            f"[TEMPORAL-FAIL] {bf_name}: Declared pov_age {declared_age} does not match "
                            f"canonical age {exp} for {pov_name.title()}!"
                        )

    if errors:
        for err in errors:
            print(f"  {err}")
        return errors
    else:
        print("  [PASS] All Chapter Briefs comply with Rule TC-1 (Zero Age Drift) & Chronology Matrix!")
        return []

if __name__ == "__main__":
    gate_ret = check_gates()
    temporal_errors = check_temporal_continuity()
    if gate_ret != 0 or len(temporal_errors) > 0:
        sys.exit(1)
    sys.exit(0)
