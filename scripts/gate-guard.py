#!/usr/bin/env python3
"""
Gate Guard: legacy repository gate-shape checks plus temporal/lore helpers.

Important Reliability v2 boundary:
- this file does NOT prove semantic review completeness;
- this file does NOT prove new durable-state approval;
- forward-only durable state approval is enforced by state-commit-guard.py;
- v2 full-read review structure is enforced by review-guard.py.
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

        print(f"=== CHECKING LEGACY GATE SHAPE FOR CHAPTER {ch_str} ===")

        # Check 1: Brief existence + recorded approval marker.
        if not os.path.exists(brief_file):
            errors.append(f"[GATE-FAIL] Chapter {ch_str} has manuscript ({cf}) but MISSING Chapter Brief ({brief_file})!")
        else:
            with open(brief_file, "r", encoding="utf-8") as bf:
                brief_content = bf.read()
                if "- [x] plan approved" not in brief_content and "[x] plan approved" not in brief_content:
                    errors.append(f"[GATE-FAIL] Chapter {ch_str} brief exists but is NOT APPROVED by Author! (Missing '- [x] plan approved')")
                else:
                    print(f"  [PASS] Recorded Brief approval marker present: {brief_file}")

        # Check 2: Legacy review-file shape only.
        # This does NOT prove a full semantic/full-read review. v2 reviews use review-guard.py.
        if not os.path.exists(review_file):
            errors.append(f"[GATE-FAIL] Chapter {ch_str} has manuscript ({cf}) but MISSING Review Report ({review_file})!")
        else:
            with open(review_file, "r", encoding="utf-8") as rf:
                rev_content = rf.read()
                if "Gate A" not in rev_content or "Gate D" not in rev_content:
                    errors.append(f"[GATE-FAIL] Review Report ({review_file}) is incomplete! Missing legacy Gate A/Gate D structure.")
                else:
                    print(
                        f"  [PASS] Legacy review shape present: {review_file} "
                        "(not semantic/full-read verification)"
                    )

        # Check 3: Legacy Canon Diff shape only.
        # This checks the historical 4-pillar/supporting-cast convention, NOT Author approval.
        # New state writes are approval-gated by state-commit-guard.py.
        diff_file = os.path.join(REVISIONS_DIR, f"chapter_{ch_str}_canon_diff.md")
        if not os.path.exists(diff_file):
            diff_file = os.path.join(REVISIONS_DIR, f"chapter_{base_num}_canon_diff.md")
        if os.path.exists(diff_file):
            with open(diff_file, "r", encoding="utf-8") as df:
                diff_content = df.read()
                if "supporting_cast.md" not in diff_content:
                    errors.append(f"[GATE-FAIL] Canon Diff ({diff_file}) violates legacy 4-pillar shape: missing 'characters/supporting_cast.md' update/audit section!")
                else:
                    print(
                        f"  [PASS] Legacy Canon Diff shape includes supporting_cast.md: {diff_file} "
                        "(not Author-approval proof)"
                    )

    if errors:
        print("\n[GATE-GUARD FAILED] Violations detected:")
        for err in errors:
            print(f"  - {err}")
        return 1

    print(
        "\n[GATE-GUARD PASS] Legacy artifact-shape checks passed. "
        "This does not certify semantic review or new durable-state approval."
    )

    # Run Lore Guard scan
    print("\n--- Running Programmatic Lore Regression Scan ---")
    try:
        import subprocess
        lore_res = subprocess.run([sys.executable, "scripts/lore-guard.py", "--scan"], capture_output=False)
        if lore_res.returncode != 0:
            print("\n[GATE-GUARD FAILED] Lore regression scanner detected encoded violations in project files!")
            return 1
    except Exception as e:
        print(f"[GATE-GUARD WARNING] Could not run lore-guard: {e}")

    # Run Lore Grounder check
    print("\n--- Running Entity Grounder Check ---")
    try:
        import subprocess
        grounder_res = subprocess.run([sys.executable, "scripts/lore-grounder.py", "--all"], capture_output=False)
        if grounder_res.returncode != 0:
            print("\n[GATE-GUARD FAILED] Lore Grounder detected critical entity-grounding errors!")
            return 1
    except Exception as e:
        print(f"[GATE-GUARD WARNING] Could not run lore-grounder: {e}")

    return 0

def check_temporal_continuity():
    """Validate authority routing; semantic temporal review remains chapter-scoped."""
    import runpy
    from pathlib import Path
    checker = runpy.run_path(str(Path(__file__).with_name("temporal-routing-check.py")))
    errors = checker["check"]()
    for error in errors:
        print(f"[TEMPORAL-ROUTING FAIL] {error}")
    if not errors:
        print("[TEMPORAL-ROUTING PASS] Current authority references checked.")
    print("[TEMPORAL SEMANTICS NOT CHECKED] Review checkpoint ages, before/after "
          "edges, travel and knowledge receipts against the current manuscript.")
    return errors

if __name__ == "__main__":
    gate_ret = check_gates()
    temporal_errors = check_temporal_continuity()
    if gate_ret != 0 or len(temporal_errors) > 0:
        sys.exit(1)
    sys.exit(0)
