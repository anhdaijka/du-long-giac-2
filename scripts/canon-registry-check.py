"""Structural checks for the empty/on-demand D-067 Canon Registry."""
from pathlib import Path
import csv
import sys

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "canon-registry/registry-index.tsv"
README = ROOT / "canon-registry/README.md"
OPEN = ROOT / "canon-registry/registry-open-slots.md"
CHANGE_README = ROOT / "canon-registry/changes/README.md"
HEADERS = ["registry_id", "proposition", "subject", "predicate", "object_or_value", "classification", "certainty", "source_receipt", "decision_ref", "branch_scope", "knowledge_scope", "effective_from", "status", "supersedes", "notes"]


def check(root=ROOT):
    errors = []
    paths = [root / p.relative_to(ROOT) for p in [INDEX, README, OPEN, CHANGE_README]]
    if any(not p.is_file() for p in paths):
        return ["Missing canon-registry required file"]
    rows = list(csv.reader((root / INDEX.relative_to(ROOT)).open(encoding="utf-8"), delimiter="\t"))
    if not rows or rows[0] != HEADERS:
        errors.append("registry-index.tsv header does not match approved schema")
    if len(rows) != 1:
        errors.append("D-067 registry must remain empty; seed rows need separate authority")
    readme = (root / README.relative_to(ROOT)).read_text(encoding="utf-8")
    for phrase in ["INITIALIZED EMPTY", "không chứng minh", "author decision", "canon diff"]:
        if phrase.lower() not in readme.lower():
            errors.append(f"Registry README lacks boundary: {phrase}")
    slots = (root / OPEN.relative_to(ROOT)).read_text(encoding="utf-8")
    for slot in ["OS-DLG-01", "OS-TXAD-01", "OS-TEMP-01", "OS-REL-01", "OS-MART-01", "OS-END-01"]:
        if slot not in slots:
            errors.append(f"Missing open-slot index: {slot}")
    return errors


if __name__ == "__main__":
    failures = check()
    for failure in failures:
        print(f"FAIL: {failure}")
    if not failures:
        print("PASS: empty/on-demand registry structure. NOT CHECKED: source truth, semantic entailment, canon state or prose.")
    sys.exit(bool(failures))
