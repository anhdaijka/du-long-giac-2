"""Build/check preliminary editorial coverage; SQLite and survey packets are read-only.

Classification is a reproducible first-pass disposition, NOT a semantic audit or
canon decision. Every source row survives inside its family. --check replays all
stored source queries against SQLite and compares generated outputs without writes.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
import sqlite3
from collections import Counter, defaultdict
from pathlib import Path

from restructure_source_survey import PACKET_QUERIES

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'migration/restructure_2026_09'
OUT = BASE / 'world-coverage'
DB = ROOT / 'story_database.sqlite3'
CHANNELS = {'DIRECT_TRIO', 'SATELLITE_POV', 'WITNESS_RELAY', 'DOCUMENT_TRACE',
            'AFTERMATH', 'LIVING_LORE', 'LEGENDARY_ECHO', 'EXCLUDE_GAMEPLAY'}
SECTS = ['Thiên Vương', 'Cái Bang', 'Ngũ Độc', 'Côn Lôn', 'Võ Đang', 'Thiếu Lâm',
         'Thiên Nhẫn', 'Nga My', 'Đường Môn', 'Thúy Yên', 'Minh Giáo', 'Đoàn Thị']
VARIANTS = {
    'NGUDOC-SEX': [4, 5], 'DEPARTURE': [158, 159, 160],
    'TAM-DAC': [161, 162, 163], 'PREP-WAR': [226, 227],
    'CO-HOA': [333, 334, 337, 338], 'CAM-DIA': [335, 336],
    'HAI-LANG': [363, 364, 365, 366, 367, 368],
    'NGHI-CHUNG': [219, 345], 'MISSING': [220, 346],
    'ESCAPE': [224, 347], 'TUY-TANG': [301, 348],
    'CHESS': [369, 370, 371], 'ILLUSION': [372, 373, 374],
    'LUU-NHAT-BAN': [375, 376, 377], 'QUAN-HUONG': [268, 343, 380],
}
CORE = {1: ('tinh-xuyen', 'I'), 2: ('tieu-phung', 'I'),
        12: ('ha-nuong', 'I'), 157: ('tieu-phung', 'I')}
POLITICAL = set(range(231, 268)) | set(range(291, 301))
MACRO = {225, 228, 332, 352, 382} | set(range(395, 405)) | set(range(442, 463))
UTILITY = {342, 349, 350, 351, 429, 464, 465, 466, 467, 468, 469}


def verify_packets():
    digest = hashlib.sha256(DB.read_bytes()).hexdigest()
    tasks, locations = {}, {}
    conn = sqlite3.connect(DB.as_uri() + '?mode=ro', uri=True)
    conn.row_factory = sqlite3.Row
    try:
        expected_ids = {r[0] for r in conn.execute('SELECT task_id FROM tasks')}
        for path in sorted((BASE / 'evidence/source-packets').glob('*.json')):
            packet = json.loads(path.read_text(encoding='utf-8'))
            assert packet['provenance']['sqlite_sha256'] == digest, f'Stale packet: {path}'
            assert packet['provenance']['query_templates'] == PACKET_QUERIES
            assert packet['task_ids'] == packet['provenance']['query_parameters']['task_ids']
            assert packet['task_ids'] == [t['task_id'] for t in packet['tasks']]
            for index, task in enumerate(packet['tasks']):
                tid = task['task_id']
                assert tid not in tasks, f'Duplicate task {tid}'
                live = dict(conn.execute(PACKET_QUERIES['task'], (tid,)).fetchone())
                live['subtasks'] = []
                for sub in conn.execute(PACKET_QUERIES['subtasks'], (tid,)).fetchall():
                    item = dict(sub)
                    for kind in ('steps', 'dialogues'):
                        item[kind] = [dict(r) for r in conn.execute(PACKET_QUERIES[kind], (item['sub_id'],))]
                    live['subtasks'].append(item)
                assert task == live, f'SQLite/packet mismatch at Task {tid}'
                tasks[tid] = task
                locations[tid] = {'packet': path.relative_to(ROOT).as_posix(),
                                  'json_pointer': f'/tasks/{index}',
                                  'arc_locator': path.stem.removeprefix('arc_')}
        assert set(tasks) == expected_ids, 'Packet coverage differs from SQLite task IDs'
        return tasks, locations, digest
    finally:
        conn.close()


def family(task):
    tid, name = task['task_id'], task['name']
    for key, ids in VARIANTS.items():
        if tid in ids:
            return 'EF-' + key, 'VARIANT_REVIEW_GROUP', 'Explicit variant set; see branch matrix and member titles; no event merge approved.'
    if (203 <= tid <= 214 or 383 <= tid <= 394 or 405 <= tid <= 428 or 430 <= tid <= 441):
        sect = next((s for s in SECTS if s.casefold() in name.casefold()), None)
        assert sect, f'Cannot resolve sect from source title: {tid}'
        return f'EF-SECT-{SECTS.index(sect)+1:02}', 'SECT_ROUTE_COLLECTION', 'Source title identifies same sect; entry/training/skill stages remain distinct, not duplicate events.'
    return f'EF-T{tid:04}', 'SINGLE_TASK', 'No proven variant merge; retain one task including every subtask.'


def classify(task, fid):
    tid = task['task_id']
    # Editorial rules are intentionally explicit and conservative. No inference
    # from an Arc name or numeric adjacency establishes chronology or ownership.
    if tid in CORE:
        who, volume = CORE[tid]
        return 'A', 'DIRECT_TRIO', ['WITNESS_RELAY', 'AFTERMATH'], who, volume, 'CORE_APPROVED', 'Core role from R-14 and approved volume architecture; subtask allocation remains draft.'
    if fid.startswith('EF-SECT'):
        return 'B', 'LIVING_LORE', ['WITNESS_RELAY'], '', '', 'SECT_FAMILY', 'Preserve institutions, practices and NPC material; strip level/reward loops; select narrative pieces after branch review.'
    if tid in (158, 159, 160):
        return 'B', 'DOCUMENT_TRACE', ['WITNESS_RELAY'], '', 'I', 'BRANCH_OPEN', 'Three source departure alternatives; retain all, allocate none until route conditions are checked.'
    if 197 <= tid <= 202:
        return 'A', 'LEGENDARY_ECHO', ['WITNESS_RELAY'], '', 'II', 'TANG_KIEM', 'Priority recollection bank for autonomous wulin; no new legendary identity or objective legend truth selected.'
    if tid in (450, 451):
        return 'A', 'DIRECT_TRIO', ['WITNESS_RELAY', 'DOCUMENT_TRACE'], 'tieu-phung', 'V', 'VISION_LOCK', 'R-12/R-18 select parentage; source vision stays uncertain; external corroboration still a candidate.'
    if tid in POLITICAL:
        return 'A', 'DOCUMENT_TRACE', ['SATELLITE_POV', 'AFTERMATH'], '', 'III', 'POLITICAL_BANK', 'Source-graph political cluster; NPC-led event, choose actual witness and private knowledge only after evidence review.'
    if tid in MACRO or 1 <= tid <= 25:
        volume = 'II' if tid == 225 else 'IV' if tid in (332, 352) else 'V' if tid >= 382 else ''
        return 'A', 'WITNESS_RELAY', ['SATELLITE_POV', 'AFTERMATH'], '', volume, 'WORLD_EVENT', 'Preserve substantial source event independently of trio; scene owner and eligible satellite POV not selected.'
    if fid in ('EF-CO-HOA', 'EF-HAI-LANG'):
        return 'B', 'LEGENDARY_ECHO', ['DOCUMENT_TRACE'], '', '', 'VARIANT_LORE', 'Keep lore premise; daily/main/level rows are variants, not repeated historical occurrences.'
    if tid in UTILITY:
        return 'C', 'EXCLUDE_GAMEPLAY', ['LIVING_LORE'], '', '', 'UTILITY_REVIEW', 'Provisional omission of tutorial/live-event wrapper; retain source for any reusable social material.'
    if task['repeat']:
        return 'C', 'LIVING_LORE', ['AFTERMATH'], '', '', 'REPEAT_LORE_REVIEW', 'Exclude repeated occurrence, preserve potential labor, economy, medicine or local conflict; repeat flag alone does not erase lore.'
    return 'B', 'LIVING_LORE', ['WITNESS_RELAY', 'AFTERMATH'], '', '', 'RESERVOIR_REVIEW', 'Retain independent local/sect story for close reading; channel is a preliminary editorial suggestion, no event or scene approved.'


def outputs():
    tasks, loc, digest = verify_packets()
    rows, groups = [], defaultdict(list)
    for tid, task in sorted(tasks.items()):
        fid, kind, basis = family(task)
        tier, channel, secondary, owner, volume, rule, reason = classify(task, fid)
        row = {
            'task_id': tid, 'task_name': task['name'], 'event_family_id': fid,
            'family_kind': kind, 'family_basis': basis,
            'repeat': task['repeat'], 'source_path': task['file_path'],
            'source_subtask_ids': [s['sub_id'] for s in task['subtasks']],
            'source_contact_npcs': sorted({s['dialog_npc_name'] for s in task['subtasks'] if s['dialog_npc_name']}),
            'evidence': loc[tid], 'source_fact_class': 'GAME_FACT_WITH_SPEAKER_SCOPE',
            'coverage_tier': tier, 'primary_channel': channel, 'secondary_channels': secondary,
            'trio_owner': owner or 'UNASSIGNED', 'actual_event_actor': 'READ_SOURCE_BEFORE_ASSIGNMENT',
            'volume_candidate': volume or 'OPEN', 'disposition_rule': rule, 'reason': reason,
            'adaptation_status': 'PRELIMINARY_EDITORIAL_CANDIDATE',
            'review_depth': 'QUERY_REPLAY_AND_SURVEY_TRIAGE_NOT_FULL_SEMANTIC_REVIEW',
            'branch_state': 'DO_NOT_LINEARIZE', 'representative_task': None,
            'reader_knowledge': 'CHANNEL_PROPOSED_REVEAL_WINDOW_OPEN',
            'trio_knowledge': 'NO_AUTOMATIC_TRANSFER_FROM_READER',
            'open_work': 'Check speaker/medium, conditions, outcomes and unique member lore before scene selection.',
        }
        if not task['subtasks']:
            row['open_work'] = 'SOURCE_GAP: no subtask row; retain task-level evidence, no invented completion.'
        assert channel in CHANNELS
        rows.append(row)
        groups[fid].append(row)
    families = [{
        'event_family_id': fid, 'family_kind': members[0]['family_kind'],
        'task_ids': [m['task_id'] for m in members], 'basis': members[0]['family_basis'],
        'merge_status': 'NO_NARRATIVE_MERGE', 'representative_task': None,
        'member_evidence': [m['evidence'] for m in members],
    } for fid, members in sorted(groups.items())]
    stats = {'tasks': len(rows), 'families': len(families),
             'multi_member_families': sum(len(f['task_ids']) > 1 for f in families),
             'channels': dict(sorted(Counter(r['primary_channel'] for r in rows).items())),
             'tiers': dict(sorted(Counter(r['coverage_tier'] for r in rows).items())),
             'unclassified_tasks': sum(r['evidence']['arc_locator'] == 'unclassified' for r in rows),
             'source_gaps': [r['task_id'] for r in rows if not r['source_subtask_ids']]}
    result = {'status': 'PRELIMINARY_COMPLETE_NOT_CANON_NOT_SCENE_COVERAGE',
              'authority': 'LWCQ-01–04 / R-23–R-26', 'sqlite_sha256': digest,
              'coverage_scope': 'tasks table and linked subtasks/steps/dialogues only; not all SQLite tables or XML corpus',
              'statistics': stats, 'tasks': rows, 'families': families}
    table = io.StringIO(newline='')
    keys = ['task_id', 'task_name', 'event_family_id', 'coverage_tier', 'primary_channel',
            'trio_owner', 'volume_candidate', 'disposition_rule', 'reason']
    writer = csv.DictWriter(table, fieldnames=keys, delimiter='\t', lineterminator='\n', extrasaction='ignore')
    writer.writeheader()
    writer.writerows(rows)
    lines = ['# World Event Coverage Ledger — bảng sơ bộ', '',
             'Trạng thái: `PRELIMINARY COMPLETE / NOT CANON / NOT SCENE COVERAGE`.', '',
             f"Đã kiểm kê {len(rows)} task thành {len(families)} nhóm lưu trữ; {stats['multi_member_families']} nhóm nhiều task.",
             'Nhóm lưu trữ không khẳng định các thành viên là cùng một biến cố. Chưa chọn representative hoặc gộp outcome.', '',
             'Bảng phân loại sơ bộ dùng metadata và khảo sát đã lưu. Kiểm tra tái chạy toàn bộ query chứng minh dữ liệu trùng SQLite; không chứng minh đã đọc sâu mọi proposition.', '',
             'Phạm vi: bảng tasks và subtasks/steps/dialogues liên kết. Các bảng NPC/map/item/lore độc lập và XML flags chưa được kiểm kê toàn bộ ở đây.', '',
             '## Kết quả', '', '| Kênh chính đề xuất | Task |', '| --- | ---: |']
    lines += [f'| {key} | {value} |' for key, value in stats['channels'].items()]
    lines += ['', 'A = ưu tiên bảo toàn biến cố/hồi cố; B = kho truyện chờ chọn; C = gameplay/routine cần tách lore. Đây là độ ưu tiên biên tập, không phải mức tin cậy fact.', '',
              '## Cách đọc và tái kiểm', '',
              '- [ledger.tsv](ledger.tsv): một dòng cho mỗi task, dễ lọc theo kênh/POV.',
              '- [ledger.json](ledger.json): thêm family, NPC liên hệ nguồn, subtask IDs, evidence pointer và giới hạn tri thức.',
              '- [editorial-notes.md](editorial-notes.md): ba cụm mẫu và các rủi ro cần xử lý.',
              '- `python scripts/build_world_coverage.py --check`: mở SQLite read-only, chạy lại query task/subtasks/steps/dialogues, so toàn bộ kết quả với packet và so artifact sinh ra.', '',
              'Query, bind task_ids và toàn bộ kết quả nằm trong source packet được trỏ ở từng dòng; `json_pointer` chọn chính xác task. NPC liên hệ nguồn không đồng nghĩa người gây biến cố hoặc POV đã chọn.', '',
              f"SQLite SHA-256: `{digest}`.", '',
              f"Giữ đủ {stats['unclassified_tasks']} task ngoài Arc locator. Task thiếu subtask: {stats['source_gaps']}.", '',
              'Không tự chuyển kiến thức độc giả sang trio. Satellite POV là kênh ứng viên; mỗi cảnh vẫn phải thỏa sáu tiêu chí đã duyệt.', '',
              'Quyền nguồn, family và sự kiện phải kiểm chứng trước khi chuyển một hàng sơ bộ thành cảnh. Cột OPEN là khoảng chưa quyết định, không phải nội dung bị bỏ quên.', '']
    return {'ledger.json': json.dumps(result, ensure_ascii=False, indent=2) + '\n',
            'ledger.tsv': table.getvalue(), 'README.md': '\n'.join(lines)}, stats


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    generated, stats = outputs()
    if args.check:
        for filename, body in generated.items():
            path = OUT / filename
            assert path.is_file() and path.read_text(encoding='utf-8') == body, f'Stale output: {path}'
    else:
        OUT.mkdir(parents=True, exist_ok=True)
        for filename, body in generated.items():
            (OUT / filename).write_text(body, encoding='utf-8', newline='\n')
    print(json.dumps({'validation': 'PASS', 'mode': 'check' if args.check else 'build', **stats}, ensure_ascii=False))


if __name__ == '__main__':
    main()
