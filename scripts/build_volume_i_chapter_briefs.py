"""Build the noncanonical Volume I chapter sequence and bounded briefs.

The generator projects the author-approved V1CAQ architecture. It does not
create scenes, prose, exact dates, exact travel, canon state, or later-volume
content.
"""
from __future__ import annotations

import argparse
import csv
import io
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MATRIX = ROOT / "migration/restructure_2026_09/chapter-architecture/chapter-function-matrix.tsv"
OUT = ROOT / "migration/restructure_2026_09/chapter-plan-volume-i"
BRIEFS = OUT / "briefs"

SEQUENCE = [
    ("V1-CAND-001", "Ngôi Chủ Chưa Yên"),
    ("V1-CAND-002", "Những Bếp Lửa Nuôi Người"),
    ("V1-CAND-003", "Món Nợ Bên Giường"),
    ("V1-CAND-004", "Một Lời Về Ngọc"),
    ("V1-CAND-005", "Hai Tờ Tin Dữ"),
    ("V1-CAND-008", "Người Bị Đuổi, Kẻ Nhận Lệnh"),
    ("V1-CAND-006", "Chọn Một Nẻo Đi"),
    ("V1-CAND-007", "Lửa Dưới Mái Hoa"),
    ("V1-CAND-009", "Hai Mươi Chìa Khóa"),
    ("V1-CAND-012", "Chìa Khóa Rời Tay"),
    ("V1-CAND-010", "Thủy Đạo Không Tên"),
    ("V1-CAND-013", "Cỏ Độc, Cờ Quan"),
    ("V1-CAND-011", "Người Giữ Cửa Bách Hoa"),
    ("V1-CAND-014", "Trục Cuốn Rách"),
    ("V1-CAND-015", "Một Bãi Giữ Được"),
    ("V1-CAND-016", "Tiễn Xa Và Quân Lệnh"),
    ("V1-CAND-017", "Bốn Câu Trên Giấy Rách"),
    ("V1-CAND-018", "Hai Bức Thư Rời Đảo"),
    ("V1-CAND-019", "Đường Chữa Xa Nhà"),
    ("V1-CAND-021", "Người Đến Sau"),
    ("V1-CAND-022", "Lôi Đài Không Thuộc Về Chàng"),
    ("V1-CAND-023", "Một Người Trong Đoàn Áp Giải"),
    ("V1-CAND-024", "Sau Khi Khói Tắt"),
    ("V1-CAND-025", "Kim Chỉ Và Tin Dữ"),
    ("V1-CAND-026", "Dư Chấn Bách Hoa"),
]

POV_LABELS = {
    "TINH_XUYEN": "Tĩnh Xuyên",
    "TIEU_PHUNG": "Tiêu Phùng",
    "HA_NUONG": "Hạ Nương",
}

WORD_BANDS = {
    "LIGHT": "3.500–4.200 từ; không kéo dài chỉ để đủ quota",
    "MEDIUM": "4.000–4.800 từ",
    "HEAVY": "4.400–5.200 từ; bắt buộc split-review nếu dự kiến vượt 5.500 từ",
}

PACKET_BY_TASK = {
    1: "../evidence/source-packets/arc_00.json",
    2: "../evidence/source-packets/arc_00.json",
    12: "../evidence/source-packets/arc_01.json",
    157: "../evidence/source-packets/arc_06.json",
}

FIELDS = [
    "chapter_no",
    "chapter_key",
    "working_title",
    "source_function_id",
    "movement_id",
    "primary_pov",
    "narrative_load",
    "word_band",
    "source_nodes",
    "packet_refs",
    "causal_predecessors",
    "causal_returns",
    "status",
]


def read_matrix() -> dict[str, dict[str, str]]:
    with MATRIX.open("r", encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    return {row["candidate_id"]: row for row in rows}


def source_tasks(source_nodes: str) -> list[int]:
    return sorted({int(value) for value in re.findall(r"T(\d+)/S\d+", source_nodes)})


def packet_refs(source_nodes: str) -> list[str]:
    return sorted({PACKET_BY_TASK[task] for task in source_tasks(source_nodes)})


def result_refs(source_nodes: str) -> list[str]:
    refs = []
    for task, sub in sorted({(int(t), int(s)) for t, s in re.findall(r"T(\d+)/S(\d+)", source_nodes)}):
        refs.append(f"tasks[task_id={task}].subtasks[sub_id={sub}]")
    return refs


def sequence_rows(matrix: dict[str, dict[str, str]]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for number, (function_id, title) in enumerate(SEQUENCE, 1):
        source = matrix[function_id]
        rows.append({
            "chapter_no": f"{number:02}",
            "chapter_key": f"V1-CH-{number:03}",
            "working_title": title,
            "source_function_id": function_id,
            "movement_id": source["movement_id"],
            "primary_pov": source["primary_pov"],
            "narrative_load": source["narrative_load"],
            "word_band": WORD_BANDS[source["narrative_load"]],
            "source_nodes": source["source_nodes"],
            "packet_refs": ";".join(packet_refs(source["source_nodes"])),
            "causal_predecessors": source["causal_predecessors"],
            "causal_returns": source["causal_returns"],
            "status": "AUTHOR-APPROVED PLANNING / V1CBQ-01–06 / NOT CANON",
        })
    return rows


def build_sequence_tsv(rows: list[dict[str, str]]) -> str:
    output = io.StringIO(newline="")
    writer = csv.DictWriter(output, fieldnames=FIELDS, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return output.getvalue()


def build_sequence_md(rows: list[dict[str, str]]) -> str:
    lines = [
        "# Chapter sequence Quyển I — author-approved planning",
        "",
        "Trạng thái: `AUTHOR-APPROVED PLANNING / V1CBQ-01–06 / NOT CANON / NOT PROSE`.",
        "",
        "Tác giả đã duyệt baseline 25 chương, mỗi chương giữ một function đã duyệt, cùng 25 tên làm việc và reading order tương đối ngày 2026-09-09. Đây là planning authority, không phải chronology tuyệt đối hay canon. V1-CAND-020 không được đưa vào sequence.",
        "",
        "| Chương | Tên làm việc | POV | Function | Movement | Load |",
        "| ---: | --- | --- | --- | --- | --- |",
    ]
    for row in rows:
        lines.append(
            f"| {int(row['chapter_no'])} | {row['working_title']} | {POV_LABELS[row['primary_pov']]} | "
            f"{row['source_function_id']} | {row['movement_id']} | {row['narrative_load']} |"
        )
    lines.extend([
        "",
        "## Nhịp POV",
        "",
        "`TX → TP → TP → HN → TX → TX → TP → HN → TP → TP → TX → TX → HN → TP → TX → TX → TP → TX → HN → TP → TP → TP → HN → HN → TP`.",
        "",
        "Nhịp này cố ý không round-robin: các cặp 2–3, 5–6, 9–10, 11–12, 15–16, 20–22 và 23–24 bảo toàn một pressure chain trước khi đổi camera. Chương 18 hoàn tất handoff và đưa Tĩnh Xuyên rời cửa sổ trước khi Tiêu tới Cái Bang ở chương 20. Chương 25 chỉ nhận phần công khai từ Bách Hoa, không tạo cuộc gặp bộ ba.",
        "",
        "## Split/merge boundary",
        "",
        "- Không merge trong baseline vì mỗi function đang giữ một state/knowledge turn riêng.",
        "- Row `HEAVY` chỉ mang cờ split-review; chưa tự tách chương ở phase brief.",
        "- Nếu detail pass dự kiến vượt 5.500 từ, trình split proposal trong dải 26–28; không tạo hậu tố a/b/c trước review.",
        "- Mọi đổi sequence phải giữ lane order, `018 → 021`, `CDK-02 + 021 → 022`, `025 → 026` và `022 + 023 → 026`.",
        "",
    ])
    return "\n".join(lines)


def build_provenance(rows: list[dict[str, str]]) -> str:
    fields = ["chapter_key", "source_function_id", "source_nodes", "packet_refs", "query_record", "result_refs", "evidence_class"]
    output = io.StringIO(newline="")
    writer = csv.DictWriter(output, fieldnames=fields, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    for row in rows:
        writer.writerow({
            "chapter_key": row["chapter_key"],
            "source_function_id": row["source_function_id"],
            "source_nodes": row["source_nodes"],
            "packet_refs": row["packet_refs"],
            "query_record": "packet.provenance.query_templates + packet.provenance.query_binds",
            "result_refs": ";".join(result_refs(row["source_nodes"])),
            "evidence_class": "DIRECT_SOURCE + AUTHOR_APPROVED_NOVELIZATION_BRIDGE",
        })
    return output.getvalue()


def build_brief(row: dict[str, str], source: dict[str, str]) -> str:
    number = int(row["chapter_no"])
    packets = ", ".join(f"[{Path(ref).name}](../{ref})" for ref in packet_refs(source["source_nodes"]))
    results = "; ".join(result_refs(source["source_nodes"]))
    split_note = (
        "Bắt buộc đánh giá split sau detail pass; chưa tách ở baseline."
        if source["narrative_load"] == "HEAVY"
        else "Không tự merge/split nếu chưa chứng minh được state turn vẫn nguyên vẹn."
    )
    return f"""# Chương {number:02} — {row['working_title']}

Trạng thái: `AUTHOR-APPROVED PLANNING / V1CBQ-01–05 / NOT CANON / NOT A SCENE PLAN / NOT PROSE`.

## Routing

- Chapter key: `{row['chapter_key']}`
- Source function: `{row['source_function_id']}`
- Movement: `{source['movement_id']}`
- Primary POV: `{POV_LABELS[source['primary_pov']]}`
- Narrative load: `{source['narrative_load']}`
- Coverage channel: `{source['coverage_channel']}`
- Working word band: {WORD_BANDS[source['narrative_load']]}

## Provenance

- Evidence class: `DIRECT SOURCE + AUTHOR-APPROVED NOVELIZATION BRIDGE`; hai lớp không được nhập làm một.
- Source nodes: `{source['source_nodes']}`
- Source packets: {packets}
- SQLite query record: `provenance.query_templates` và `provenance.query_binds` trong packet.
- Full extraction result: `{results}` trong packet tương ứng.
- Shared ledger: [provenance-ledger.tsv](../provenance-ledger.tsv)
- Approved decisions: `{source['bridge_decisions']}`

## Chapter function

{source['chapter_function']}

## Temporal and spatial boundary

- Exact calendar date: `DEFERRED — RELATIVE ORDER ONLY`.
- Delta time: `DEFERRED`.
- Exact travel duration/route: `DEFERRED`.
- Primary location: chỉ dùng địa điểm được source node hoặc authority hiện hành xác lập; detail pass chưa được tự đặt venue mới.

## Starting state

{source['entry_state']}

## Ending state

{source['exit_state']}

## Knowledge boundary

- POV enters knowing: {source['knowledge_in']}
- POV may leave knowing: {source['knowledge_out']}
- Reader knowledge không tự chuyển thành tri thức của POV hoặc hai tuyến còn lại.

## NPC and world agency

{source['npc_agency']}

## Irreversible change

{source['irreversible_change']}

## Causal routing

- Required predecessors: `{source['causal_predecessors']}`
- Required returns: `{source['causal_returns']}`
- Sequence number chỉ biểu diễn reading order proposal; không chứng minh ngày tháng khách quan.

## Detail-pass load guard

- {split_note}
- Không lập scene sequence, beat, dialogue, action blocking hoặc ending image trong brief này.

## Protected unknowns

{source['protected_unknowns']}

## Forbidden changes

- Không lấp protected unknown bằng suy đoán hợp lý, archive continuity hoặc tiện lợi văn xuôi.
- Không đặt objective custody của Du Long Giác, không giải cơ chế Huyền Nguyệt và không đưa T4/S28–S37 vào content Quyển I.
- Không cho bộ ba gặp trực tiếp; không chuyển chiến công Lục–Thôi cho Tiêu Phùng; không nêu người/cách cứu Lục.
- Không chọn hung khí Ân Đồng hoặc làm mềm việc Tĩnh Xuyên/Mộc Nhất Lâu tự tay hạ sát nàng rồi gánh trách nhiệm.
- Không tạo scene, beat, dialogue, prose, chronology tuyệt đối, route Quyển II–V hoặc canon promotion.

## Author approval

- `V1CBQ-01–05 / APPROVED 2026-09-09`: số chương baseline, tên làm việc, chapter function, POV routing và bounded brief này là planning authority.
- Phê duyệt không mở scene/beat/dialogue/prose, chronology tuyệt đối, protected unknown hoặc canon promotion.
"""


def build_readme(rows: list[dict[str, str]]) -> str:
    return """# Chapter Plan Quyển I — sequence và bounded briefs

Trạng thái: `AUTHOR-APPROVED PLANNING / V1CBQ-01–06 / NOT CANON / NOT A SCENE PLAN / NOT PROSE`.

## Restate brief

V1CAQ-01–06 đã duyệt 25 function mặc định; V1CBQ-01–06 ngày 2026-09-09 tiếp tục duyệt baseline 25 chương, 25 tên làm việc, reading order/POV và 25 bounded briefs. Package này là planning authority nhưng không biến partial order thành lịch tuyệt đối.

## Assumptions đã dùng

- Baseline 25 chương, một function đã duyệt mỗi chương; đây là planning baseline trong dải recommended 25–28, không phải fixed count canon.
- V1-CAND-020 tiếp tục deferred và không có brief.
- Row HEAVY chưa tự split; chỉ mang cờ review nếu detail pass dự kiến vượt 5.500 từ.
- Số/tên chương là working planning authority. Exact date, travel, venue chưa có source và scene structure tiếp tục deferred.

## Output

- [chapter-sequence.tsv](chapter-sequence.tsv): nguồn máy đọc cho 25 số/tên/route.
- [chapter-sequence.md](chapter-sequence.md): projection đọc nhanh và nhịp POV.
- [provenance-ledger.tsv](provenance-ledger.tsv): source nodes, packet, query record và full-result references.
- `briefs/chapter_01.md` tới `briefs/chapter_25.md`: brief hữu hạn, không có scene list hoặc prose.
- [validation-report.md](validation-report.md): kết quả kiểm và biên bản phê duyệt V1CBQ-01–06.

## Scope và constraints

- In scope: approved planning number/title, one-POV routing, function, entry/exit state, knowledge, agency, causal edge, load guard và protected unknowns.
- Out of scope: exact chronology, exact travel, new venue, scene/beat/dialogue, prose, detailed combat, medical outcome, objective custody, Huyền Nguyệt mechanism, Tĩnh Xuyên–Ân Đồng route detail, Volume II–V và canon promotion.
- SQLite packet tiếp tục là authority cho game fact. Assignment, order và title là planning/Bridge, không phải game fact.

## Acceptance criteria

- Đúng 25 brief cho 25 function approved; không có V1-CAND-020.
- Mỗi brief chỉ có một POV và trỏ source packet/query/full-result reference.
- Sequence giữ mọi lane edge cùng các handoff bắt buộc.
- Không khóa ngày, hành trình, custody, mechanism hoặc scene wording.
- Tất cả artifact dừng ở planning authority sau V1CBQ. [Scene-plan phase spec](../scene-plan-phase-spec-volume-i.md) đã được duyệt qua SPQ-01–06 và mở candidate implementation; chưa scene nào được phê duyệt và prose vẫn đóng.
"""


def build_validation_report() -> str:
    return """# Validation report — Chapter Plan Quyển I

Trạng thái: `V1CBQ-01–06 APPROVED / STRUCTURAL VALIDATION / NOT SEMANTIC CERTIFICATION / NOT CANON`.

## Automated checks

- `python scripts/build_volume_i_chapter_briefs.py --check`
- `python scripts/check_volume_i_chapter_briefs.py --self-test`
- `python scripts/check_chapter_architecture.py --self-test`
- `npm run execution:check`

Kết quả checkpoint D24 (kế thừa package D23):

- Generator check: **PASS**, 30 file gồm 25 brief.
- Package check: **PASS**, 25 sequence row, 25 brief, 25 provenance row, 58 local link và 12 negative tests.
- Lore Guard file check: **PASS 25/25 brief**; đây là known-regression scan, không phải semantic grounding proof.
- POV count: 8 Tĩnh Xuyên, 11 Tiêu Phùng, 6 Hạ Nương.
- Movement count: M1 4, M2 12, M3 4, M4 3, M5 2.

Các kiểm tra xác nhận projection, source IDs, dependency order, packet/result references, 25 brief và negative boundaries. Chúng không chứng minh chất lượng tiêu đề, nhịp văn học, lịch sử/địa lý, scene feasibility hoặc quyền viết prose.

## Author approval — V1CBQ-01–06 / 2026-09-09

| ID | Đề xuất khuyến nghị | Hệ quả nếu duyệt |
| --- | --- | --- |
| V1CBQ-01 | Duyệt baseline 25 chương theo `chapter-sequence.tsv`, mỗi function approved giữ một chương. | Sequence trở thành planning authority; số vẫn có thể split theo load gate. |
| V1CBQ-02 | Duyệt 25 tên làm việc trong projection; cho phép đổi riêng từng tên mà không đảo function. | Có naming layer để tham chiếu, chưa phải tên canon trên manuscript. |
| V1CBQ-03 | Duyệt nhịp POV hiện tại và các cụm liên tiếp cố ý; không round-robin. | Khóa reading order tương đối, không khóa calendar chronology. |
| V1CBQ-04 | Giữ row HEAVY chưa split; chỉ trình split 26–28 khi detail pass chứng minh tải vượt 5.500 từ hoặc có hai irreversible turn. | Tránh phình chương theo dự cảm và vẫn giữ cửa fluid expansion. |
| V1CBQ-05 | Duyệt 25 bounded briefs làm planning authority với exact date/travel/location và scene allocation tiếp tục deferred. | Mở một đầu vào ổn định cho detail pass mà không lấp khoảng chưa chọn. |
| V1CBQ-06 | Sau khi V1CBQ-01–05 được duyệt, cho phép đề xuất **scene-plan phase spec** cho Quyển I; chưa tự mở scene plan hoặc prose. | Giữ thêm một cổng trước khi phân scene/beat/dialogue. |

Tác giả đã phê duyệt toàn bộ V1CBQ-01–06 bằng chỉ thị “Duyệt”. Quyết định được lưu tại R-53–R-58 / D-032. [Scene-plan phase spec](../scene-plan-phase-spec-volume-i.md) sau đó đã được duyệt qua SPQ-01–06 (R-59–R-64 / D-033), chỉ mở candidate scene-plan implementation. Chưa scene/beat/dialogue/prose, exact chronology, protected unknown, Volume II–V hoặc canon promotion nào được duyệt.
"""


def build_files() -> dict[Path, str]:
    matrix = read_matrix()
    rows = sequence_rows(matrix)
    files: dict[Path, str] = {
        OUT / "README.md": build_readme(rows),
        OUT / "chapter-sequence.tsv": build_sequence_tsv(rows),
        OUT / "chapter-sequence.md": build_sequence_md(rows),
        OUT / "provenance-ledger.tsv": build_provenance(rows),
        OUT / "validation-report.md": build_validation_report(),
    }
    for row in rows:
        source = matrix[row["source_function_id"]]
        files[BRIEFS / f"chapter_{row['chapter_no']}.md"] = build_brief(row, source)
    return files


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    files = build_files()
    if args.check:
        missing = [str(path.relative_to(ROOT)) for path, body in files.items() if not path.is_file() or path.read_text(encoding="utf-8") != body]
        if missing:
            raise SystemExit("STALE_OR_MISSING: " + ", ".join(missing))
        print({"validation": "PASS", "mode": "check", "files": len(files), "briefs": len(files) - 5})
        return
    for path, body in files.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(body, encoding="utf-8", newline="\n")
    print({"generated": len(files), "briefs": len(files) - 5, "output": str(OUT.relative_to(ROOT))})


if __name__ == "__main__":
    main()
