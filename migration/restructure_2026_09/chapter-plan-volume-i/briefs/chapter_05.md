# Chương 05 — Hai Tờ Tin Dữ

Trạng thái: `AUTHOR-APPROVED PLANNING / V1CBQ-01–05 / NOT CANON / NOT A SCENE PLAN / NOT PROSE`.

## Routing

- Chapter key: `V1-CH-005`
- Source function: `V1-CAND-005`
- Movement: `M2`
- Primary POV: `Tĩnh Xuyên`
- Narrative load: `MEDIUM`
- Coverage channel: `DOCUMENT_TRACE`
- Working word band: 4.000–4.800 từ

## Provenance

- Evidence class: `DIRECT SOURCE + AUTHOR-APPROVED NOVELIZATION BRIDGE`; hai lớp không được nhập làm một.
- Source nodes: `T1/S2/E8;T1/S2/E10;T1/S2/E12;T1/S2/E13`
- Source packets: [arc_00.json](../../evidence/source-packets/arc_00.json)
- SQLite query record: `provenance.query_templates` và `provenance.query_binds` trong packet.
- Full extraction result: `tasks[task_id=1].subtasks[sub_id=2]` trong packet tương ứng.
- Shared ledger: [provenance-ledger.tsv](../provenance-ledger.tsv)
- Approved decisions: `R-14;TX-I-B;C-I-04;R-47;V1CAQ-01`

## Chapter function

Buộc Tĩnh Xuyên thấy quân lệnh đang vận hành trên lời tố cáo chưa chứng minh, đồng thời nhận tin Du Long dưới dạng báo cáo cần kiểm chứng.

## Temporal and spatial boundary

- Exact calendar date: `DEFERRED — RELATIVE ORDER ONLY`.
- Delta time: `DEFERRED`.
- Exact travel duration/route: `DEFERRED`.
- Primary location: chỉ dùng địa điểm được source node hoặc authority hiện hành xác lập; detail pass chưa được tự đặt venue mới.

## Starting state

Dương vừa nắm quyền; Cầu Chỉ Thủy chưa có phán quyết đáng tin.

## Ending state

CAU_CHI_THUY_DETAINED_CLAIM_UNPROVEN; DU_LONG_REPORT_RECEIVED_FROM_CHENGDU; Bùi Dực Phi được giao xác minh.

## Knowledge boundary

- POV enters knowing: Biết Cầu bị tố cáo qua lời tổ chức, chưa tự kiểm chứng.
- POV may leave knowing: Biết Quý nghi cáo buộc; thư Thành Đô nói Du Long xuất hiện ở Thúy Yên; không biết tin đúng hoặc custody thật.
- Reader knowledge không tự chuyển thành tri thức của POV hoặc hai tuyến còn lại.

## NPC and world agency

Cầu chọn im lặng; Quý phản biện; sứ giả Thành Đô chuyển thư; Dương dùng mạng tình báo thay vì đóng toàn bộ phán quyết.

## Irreversible change

NONE_PRESSURE_ESCALATION_CUSTODY_AND_GUILT_REMAIN_OPEN

## Causal routing

- Required predecessors: `V1-CAND-001`
- Required returns: `V1-CAND-008`
- Sequence number chỉ biểu diễn reading order proposal; không chứng minh ngày tháng khách quan.

## Detail-pass load guard

- Không tự merge/split nếu chưa chứng minh được state turn vẫn nguyên vẹn.
- Không lập scene sequence, beat, dialogue, action blocking hoặc ending image trong brief này.

## Protected unknowns

Cầu có tội hay không ngoài source; quan hệ giữa tin T1/S2 và T12/S92; custody; lịch tuyệt đối.

## Forbidden changes

- Không lấp protected unknown bằng suy đoán hợp lý, archive continuity hoặc tiện lợi văn xuôi.
- Không đặt objective custody của Du Long Giác, không giải cơ chế Huyền Nguyệt và không đưa T4/S28–S37 vào content Quyển I.
- Không cho bộ ba gặp trực tiếp; không chuyển chiến công Lục–Thôi cho Tiêu Phùng; không nêu người/cách cứu Lục.
- Không chọn hung khí Ân Đồng hoặc làm mềm việc Tĩnh Xuyên/Mộc Nhất Lâu tự tay hạ sát nàng rồi gánh trách nhiệm.
- Không tạo scene, beat, dialogue, prose, chronology tuyệt đối, route Quyển II–V hoặc canon promotion.

## Author approval

- `V1CBQ-01–05 / APPROVED 2026-09-09`: số chương baseline, tên làm việc, chapter function, POV routing và bounded brief này là planning authority.
- Phê duyệt không mở scene/beat/dialogue/prose, chronology tuyệt đối, protected unknown hoặc canon promotion.
