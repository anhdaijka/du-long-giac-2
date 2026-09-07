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
        match = re.match(r"chapter_(\d+)\.md", cf)
        if not match:
            continue
        ch_num = match.group(1)
        brief_file = os.path.join(BRIEFS_DIR, f"chapter_{ch_num}_brief.md")
        review_file = os.path.join(REVIEWS_DIR, f"chapter_{ch_num}_review.md")

        print(f"=== CHECKING GATES FOR CHAPTER {ch_num} ===")

        # Check 1: Brief existence
        if not os.path.exists(brief_file):
            errors.append(f"[GATE-FAIL] Chapter {ch_num} has manuscript ({cf}) but MISSING Chapter Brief ({brief_file})!")
        else:
            # Check if brief is approved
            with open(brief_file, "r", encoding="utf-8") as bf:
                brief_content = bf.read()
                if "- [x] plan approved" not in brief_content and "[x] plan approved" not in brief_content:
                    errors.append(f"[GATE-FAIL] Chapter {ch_num} brief exists but is NOT APPROVED by Author! (Missing '- [x] plan approved')")
                else:
                    print(f"  [PASS] Hard Stop 1 (Brief approved): {brief_file}")

        # Check 2: Review report existence
        if not os.path.exists(review_file):
            errors.append(f"[GATE-FAIL] Chapter {ch_num} has manuscript ({cf}) but MISSING Review Report ({review_file})!")
        else:
            print(f"  [PASS] Hard Stop 2 (Review report exists): {review_file}")

    if errors:
        print("\n[GATE-GUARD FAILED] Violations detected:")
        for err in errors:
            print(f"  - {err}")
        return 1

    print("\n[GATE-GUARD PASS] All chapter manuscripts comply strictly with Novel-OS Hard-Stop Gates!")
    return 0

if __name__ == "__main__":
    sys.exit(check_gates())
