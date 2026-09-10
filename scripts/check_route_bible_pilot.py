"""Read-only structural/locator checks, not semantic or literary certification.

Run build_world_coverage.py --check separately to replay SQLite evidence. This
checker validates references into that evidence and the approved Volume I boundary.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'migration/restructure_2026_09'
PILOT = BASE / 'route-bibles'
ROUTES = {'tieu-phung.md': {157, 2}, 'tinh-xuyen.md': {1}, 'ha-nuong.md': {12}}
FILES = set(ROUTES) | {'README.md', 'convergence-matrix.md'}
STATUS = 'AUTHOR-APPROVED PLANNING / VOLUME I PILOT / NOT CANON'
PLACEHOLDER = '`PLACEHOLDER / NOT AUTHORIZED IN THIS PILOT`.'
CITE = re.compile(r'\bT(\d+)/S(\d+)(?:/E(\d+))?\b')


def require(condition, message):
    if not condition:
        raise ValueError(message)


def load_sources():
    tasks = {}
    for path in (BASE / 'evidence/source-packets').glob('*.json'):
        for task in json.loads(path.read_text(encoding='utf-8'))['tasks']:
            require(task['task_id'] not in tasks, f'Duplicate task {task["task_id"]}')
            tasks[task['task_id']] = task
    ledger = json.loads((BASE / 'world-coverage/ledger.json').read_text(encoding='utf-8'))
    return tasks, {f['event_family_id'] for f in ledger['families']}


def validate(documents, tasks, families):
    require(set(documents) == FILES, 'Expected exactly the five approved pilot artifacts')
    checked, links = set(), 0
    for name, body in documents.items():
        require(STATUS in body, f'Missing approved-planning/noncanon boundary: {name}')
        require(body.endswith('\n'), f'Missing final newline: {name}')
        require(not any(line.rstrip() != line for line in body.splitlines()), f'Trailing whitespace: {name}')
        cited_tasks = set()
        for match in CITE.finditer(body):
            tid, sid = int(match[1]), int(match[2])
            require(tid in tasks, f'Unknown task: {name} {match[0]}')
            sub = next((s for s in tasks[tid]['subtasks'] if s['sub_id'] == sid), None)
            require(sub is not None, f'Wrong task/subtask relationship: {name} {match[0]}')
            if match[3]:
                eid = int(match[3])
                require(any(s['id'] == eid for s in sub['steps']), f'Wrong step owner: {name} {match[0]}')
            else:
                require(bool(sub['describe_cleaned']), f'Empty default source field: {name} {match[0]}')
            checked.add(match[0])
            cited_tasks.add(tid)
        for fid in re.findall(r'\bEF-(?:T\d{4}|DEPARTURE)\b', body):
            require(fid in families, f'Unknown family: {fid}')
        for target in re.findall(r'\[[^\]\n]+\]\(([^)\n]+)\)', body):
            require('://' not in target, f'Unexpected external dependency in pilot: {target}')
            relative = unquote(target.split('#', 1)[0])
            if relative:
                path = (PILOT / relative).resolve()
                require(path.is_relative_to(ROOT), f'Link escapes repo: {target}')
                require(path.is_file(), f'Broken file link: {name} {target}')
                links += 1
        if name in ROUTES:
            require(ROUTES[name] <= cited_tasks, f'Missing approved core evidence: {name}')
            require('AUTHOR-APPROVED NOVELIZATION BRIDGE — PILOT SCOPE' in body, f'Missing scoped bridge label: {name}')
            for title in ('Opening state', 'Source nodes', 'Pressure chain', 'Lựa chọn', 'Võ lâm'):
                require(title in body, f'Missing required route section: {name}: {title}')
            volumes = re.findall(r'^## Quyển (I|II|III|IV|V)\b[^\n]*$', body, re.M)
            require(volumes == ['I', 'II', 'III', 'IV', 'V'], f'Wrong volume skeleton: {name}')
            for volume in ('II', 'III', 'IV', 'V'):
                section = re.search(rf'^## Quyển {volume}\n(.*?)(?=^## |\Z)', body, re.M | re.S)
                require(section and section[1].strip() == PLACEHOLDER, f'Future volume expanded: {name} {volume}')
    index = documents['README.md']
    for number in range(1, 7):
        require(f'| PB-{number:02} |' in index, f'Missing bridge register row PB-{number:02}')
    for number in range(1, 5):
        require(f'### V1PQ-{number:02}' in index, f'Missing author question V1PQ-{number:02}')
    matrix = documents['convergence-matrix.md']
    require('PHYSICAL_CONVERGENCE_VOLUME_I = NONE' in matrix, 'Missing no-meeting constraint')
    require('SHARED_TEAM = NONE' in matrix, 'Missing no-team constraint')
    return {'files': len(documents), 'unique_source_locators': len(checked), 'file_links': links}


def self_test(documents, tasks, families):
    trials = [
        ('bad-task', 'README.md', lambda s: s + '\nT999999/S1\n'),
        ('bad-subtask-owner', 'README.md', lambda s: s + '\nT1/S320\n'),
        ('bad-step-owner', 'README.md', lambda s: s + '\nT157/S320/E37\n'),
        ('bad-family', 'README.md', lambda s: s + '\nEF-T9999\n'),
        ('broken-link', 'README.md', lambda s: s + '\n[missing](nonexistent-pilot-file.md)\n'),
        ('future-content', 'ha-nuong.md', lambda s: s.replace('## Quyển II\n', '## Quyển II\nNew plot.\n')),
        ('missing-planning-boundary', 'tieu-phung.md', lambda s: s.replace(STATUS, 'COMPLETE')),
        ('missing-no-meeting-constraint', 'convergence-matrix.md', lambda s: s.replace('PHYSICAL_CONVERGENCE_VOLUME_I = NONE', '')),
    ]
    passed = []
    for label, name, mutate in trials:
        candidate = dict(documents)
        candidate[name] = mutate(candidate[name])
        try:
            validate(candidate, tasks, families)
        except ValueError:
            passed.append(label)
        else:
            raise ValueError(f'Negative test accepted invalid document: {label}')
    return passed


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--self-test', action='store_true')
    args = parser.parse_args()
    tasks, families = load_sources()
    documents = {path.name: path.read_text(encoding='utf-8') for path in PILOT.glob('*.md')}
    counts = validate(documents, tasks, families)
    tests = self_test(documents, tasks, families) if args.self_test else []
    print(json.dumps({'validation': 'PASS', 'assurance': 'STRUCTURE_AND_LOCATORS_ONLY_NOT_SEMANTIC',
                      **counts, 'negative_tests': tests}, ensure_ascii=False))


if __name__ == '__main__':
    main()
