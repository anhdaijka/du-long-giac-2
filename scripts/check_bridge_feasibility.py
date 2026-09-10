"""Read-only validation of Volume I Bridge Feasibility citations and boundaries.

This validates locators, persisted decision labels and scope boundaries only.
It does not certify literary quality, actual chronology, or semantic fitness.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'migration/restructure_2026_09'
DOC = BASE / 'bridge-feasibility-volume-i.md'
CITE = re.compile(r'\bT(\d+)/S(\d+)(?:/E(\d+))?\b')
REQUIRED = {'T1/S8/E37', 'T1/S8/E41', 'T2/S10/E50', 'T2/S12/E60',
            'T2/S13/E65', 'T12/S86/E483', 'T12/S86/E484', 'T12/S92/E516',
            'T157/S320/E1432'}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def source_index():
    result = {}
    for packet in (BASE / 'evidence/source-packets').glob('*.json'):
        for task in json.loads(packet.read_text(encoding='utf-8'))['tasks']:
            for subtask in task['subtasks']:
                result[(task['task_id'], subtask['sub_id'])] = {
                    'steps': {step['id'] for step in subtask['steps']},
                    'describe': subtask['describe_cleaned'],
                }
    return result


def validate(body, index):
    require(body.endswith('\n'), 'Missing final newline')
    require('AUTHOR-APPROVED PLANNING / BFCQ-01–04 / NOT CANON' in body,
            'Missing approved-planning/noncanon boundary')
    require('không phân chương' in body.casefold(), 'Missing no-chapter boundary')
    require('## Kết quả BFCQ-01–04 — APPROVED 2026-09-09' in body,
            'Missing persisted BFCQ decision record')
    require(body.count('AUTHOR-APPROVED NOVELIZATION BRIDGE — VOLUME I FEASIBILITY SCOPE') >= 4,
            'Missing scoped approval labels')
    found = set()
    for match in CITE.finditer(body):
        tid, sid = int(match[1]), int(match[2])
        source = index.get((tid, sid))
        require(source is not None, f'Unknown task/subtask: {match[0]}')
        if match[3]:
            require(int(match[3]) in source['steps'], f'Wrong step owner: {match[0]}')
        else:
            require(bool(source['describe']), f'Empty default row: {match[0]}')
        found.add(match[0])
    require(REQUIRED <= found, f'Missing required evidence: {sorted(REQUIRED - found)}')
    for number in range(1, 5):
        require(f'| BFCQ-{number:02} |' in body, f'Missing BFCQ-{number:02}')
    require('`NO SOURCE EDGE`' in body, 'Missing cross-arc chronology limit')
    require('`UNRESOLVED SOURCE CONTRADICTION`' in body, 'Missing custody contradiction limit')
    require('`REJECTED AS UNSUPPORTED`' in body, 'Missing unsupported-fighter guard')
    return {'citations': len(found), 'required_citations': len(REQUIRED)}


def self_test(body, index):
    cases = [
        ('unknown-task', lambda value: value + '\nT999999/S1\n'),
        ('wrong-subtask-owner', lambda value: value + '\nT1/S320\n'),
        ('wrong-step-owner', lambda value: value + '\nT157/S320/E37\n'),
        ('missing-decision-record', lambda value: value.replace(
            '## Kết quả BFCQ-01–04 — APPROVED 2026-09-09', '## Decision removed')),
        ('missing-custody-limit', lambda value: value.replace('`UNRESOLVED SOURCE CONTRADICTION`', '')),
    ]
    passed = []
    for label, mutate in cases:
        try:
            validate(mutate(body), index)
        except ValueError:
            passed.append(label)
        else:
            raise ValueError(f'Negative test accepted invalid document: {label}')
    return passed


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--self-test', action='store_true')
    args = parser.parse_args()
    body = DOC.read_text(encoding='utf-8')
    index = source_index()
    counts = validate(body, index)
    tests = self_test(body, index) if args.self_test else []
    print(json.dumps({'validation': 'PASS', 'assurance': 'LOCATORS_AND_SCOPE_ONLY_NOT_SEMANTIC',
                      **counts, 'negative_tests': tests}, ensure_ascii=False))


if __name__ == '__main__':
    main()
