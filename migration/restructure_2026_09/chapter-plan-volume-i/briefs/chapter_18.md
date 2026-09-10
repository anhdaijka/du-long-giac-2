# Chương 18 — Hai Bức Thư Rời Đảo

Trạng thái: `AUTHOR-APPROVED PLANNING / V1CBQ-01–05 / NOT CANON / NOT A SCENE PLAN / NOT PROSE`.

## Routing

- Chapter key: `V1-CH-018`
- Source function: `V1-CAND-018`
- Movement: `M3`
- Primary POV: `Tĩnh Xuyên`
- Narrative load: `HEAVY`
- Coverage channel: `DOCUMENT_TRACE`
- Working word band: 4.400–5.200 từ; bắt buộc split-review nếu dự kiến vượt 5.500 từ

## Provenance

- Evidence class: `DIRECT SOURCE + AUTHOR-APPROVED NOVELIZATION BRIDGE`; hai lớp không được nhập làm một.
- Source nodes: `T1/S8/E37;T1/S8/E40;T1/S8/E41;T1/S8/D11;T2/S9/E42;T2/S9/E43;T2/S9/E44;T2/S9/D12`
- Source packets: [arc_00.json](../../evidence/source-packets/arc_00.json)
- SQLite query record: `provenance.query_templates` và `provenance.query_binds` trong packet.
- Full extraction result: `tasks[task_id=1].subtasks[sub_id=8]; tasks[task_id=2].subtasks[sub_id=9]` trong packet tương ứng.
- Shared ledger: [provenance-ledger.tsv](../provenance-ledger.tsv)
- Approved decisions: `R-17;R-27;PB-01;R-29;PB-05;R-33;BFCQ-03;R-38;CDQ-03;R-47;V1CAQ-01`

## Chapter function

Cho Tĩnh Xuyên rời phòng tuyến để mang hai thư, hoàn tất giao cho Cái Bang rồi rút khỏi cửa sổ hiện diện, chấp nhận mất quyền kiểm soát hậu quả.

## Temporal and spatial boundary

- Exact calendar date: `DEFERRED — RELATIVE ORDER ONLY`.
- Delta time: `DEFERRED`.
- Exact travel duration/route: `DEFERRED`.
- Primary location: chỉ dùng địa điểm được source node hoặc authority hiện hành xác lập; detail pass chưa được tự đặt venue mới.

## Starting state

Thanh Loa bị vây; Tĩnh Xuyên nhận hai thư gửi Thạch Hiên Viên và Cầu Chỉ Thủy.

## Ending state

TX_LETTER_HANDOFF_DELIVERED_TO_CAI_BANG; TX_EXITED_WINDOW; Cái Bang sở hữu thư và tự quyết.

## Knowledge boundary

- POV enters knowing: Biết mục đích hai thư trong phạm vi Dương trực tiếp giao và đảo đang bị vây.
- POV may leave knowing: Biết Thạch/Cầu nhận thư và phản hồi nói trước khi chàng rời; không biết quyết định, lôi đài hoặc Tiêu Phùng tới sau.
- Reader knowledge không tự chuyển thành tri thức của POV hoặc hai tuyến còn lại.

## NPC and world agency

Dương quyết mục tiêu thư; Bùi chuẩn bị phương tiện; ngư phu và La Phong vận hành handoff; Thạch/Cầu tự quyết.

## Irreversible change

Tĩnh Xuyên rời người/phòng tuyến muốn bảo vệ, hoàn tất bàn giao và mất quyền kiểm soát hậu quả.

## Causal routing

- Required predecessors: `V1-CAND-016`
- Required returns: `CDK-02;V1-CAND-021;C-I-01`
- Sequence number chỉ biểu diễn reading order proposal; không chứng minh ngày tháng khách quan.

## Detail-pass load guard

- Bắt buộc đánh giá split sau detail pass; chưa tách ở baseline.
- Không lập scene sequence, beat, dialogue, action blocking hoặc ending image trong brief này.

## Protected unknowns

Đích, đường, phương tiện chặng sau, thời lượng, việc quay lại; câu chữ thư ngoài nguồn; không giữ điều khoản ở lại rèn luyện; không gặp Tiêu Phùng.

## Forbidden changes

- Không lấp protected unknown bằng suy đoán hợp lý, archive continuity hoặc tiện lợi văn xuôi.
- Không đặt objective custody của Du Long Giác, không giải cơ chế Huyền Nguyệt và không đưa T4/S28–S37 vào content Quyển I.
- Không cho bộ ba gặp trực tiếp; không chuyển chiến công Lục–Thôi cho Tiêu Phùng; không nêu người/cách cứu Lục.
- Không chọn hung khí Ân Đồng hoặc làm mềm việc Tĩnh Xuyên/Mộc Nhất Lâu tự tay hạ sát nàng rồi gánh trách nhiệm.
- Không tạo scene, beat, dialogue, prose, chronology tuyệt đối, route Quyển II–V hoặc canon promotion.

## Author approval

- `V1CBQ-01–05 / APPROVED 2026-09-09`: số chương baseline, tên làm việc, chapter function, POV routing và bounded brief này là planning authority.
- Phê duyệt không mở scene/beat/dialogue/prose, chronology tuyệt đối, protected unknown hoặc canon promotion.
