# Interleave và dependency map — Quyển I

Trạng thái: `AUTHOR-APPROVED CAUSAL BRAID / V1CAQ-01 / RELATIVE ORDER ONLY / NOT CANON`.

Tài liệu này dùng các khóa trong [chapter-function matrix](chapter-function-matrix.tsv). Nó không đặt chapter number, ngày, độ trễ, đường đi hoặc chronology tuyệt đối.

## 1. Lane order bắt buộc

| Lane | Required causal order |
| --- | --- |
| Tĩnh Xuyên | `001 → 005 → 008 → 010 → 013 → 015 → 016 → 018` |
| Tiêu Phùng | `002 → 003`; `002 → 006`; `003 → 009 → 012 → 014 → 017 → 021 → 022 → 023`; `006 → 017`; `018 → 021`; `026` chỉ mở sau `022`, `023` và `025` |
| Hạ Nương | `004 → 007 → 011 → 019 → 024 → 025` |
| Cái Bang/Lục | `018 → CDK-02`; `CDK-02 → 022`; `020`, nếu được duyệt, chỉ chiếu lựa chọn của Lục trong khoảng sau `018` và trước `022` |

`CDK-02` là state contract: Cái Bang giữ Lục sống ngoài màn, không nêu người/cách cứu; Lục tự chọn theo Thạch. Nó tồn tại dù `V1-CAND-020` bị bác.

## 2. Cạnh liên tuyến bắt buộc

| Edge | Loại | Lý do | Điều không cấp |
| --- | --- | --- | --- |
| `018 → 021` | Approved Bridge / continuity | Tĩnh Xuyên đã giao thư và rời cửa sổ trước khi Tiêu Phùng hiện diện trực tiếp tại Cái Bang. | Không cấp ngày, quãng đường hoặc cuộc gặp hai người. |
| `018 → CDK-02 → 022` | Source partial order + Bridge | T2/S9 mở cửa sổ Cái Bang; Lục phải sống và chọn theo Thạch trước lôi đài. | Không cấp rescuer, rescue method hoặc quyền chứng kiến toàn bộ cho Tiêu. |
| `021 → 022` | Approved planning | Muốn dùng POV Tiêu tại lôi đài thì chàng phải vào môi trường Cái Bang trước. | Chưa quyết chàng xem toàn bộ hay một phần. |
| `025 → 026` | Direct source handoff + Bridge | T12/S92/E516 đưa thông cáo tới Thạch; sau đó phần công khai mới có thể relay cho Tiêu. | Không cấp custody, nội dung kín hoặc tri thức cho Tĩnh Xuyên. |
| `022 + 023 → 026` | Character-state dependency | Tiêu đã thấy bang quy và nhận phần việc hữu hạn trước khi phải đánh giá một bản tin chính trị. | Không chứng minh source rằng thông cáo đến sau lôi đài; đây là planning order V1CAQ-01 đã duyệt, không phải game chronology. |

Không có edge `T1/S2 → T12/S92` hoặc edge `T12/S92 → Tĩnh Xuyên`. Hai bản tin Du Long giữ provenance riêng.

## 3. Irregular causal braid đề xuất

Đây là nhịp đọc đề xuất theo **cụm**, không phải danh sách chapter đã khóa. Các candidate trong cùng ngoặc vuông được phép đổi vị trí nếu vẫn giữ lane edges.

1. `M1 / ROOTED WORLDS`: `[001] → [002 → 003] → [004]`.
2. `M2-A / PRESSURE ENTERS`: `[005 → 008] ↔ [006] ↔ [007]`.
3. `M2-B / PEOPLE PAY`: `[009 → 012] ↔ [010 → 013] ↔ [011]`.
4. `M2-C / SYSTEMS STRAIN`: `[014] ↔ [015 → 016]`, trong khi hậu quả của `011` đẩy sang `019`.
5. `M3 / IRREVERSIBLE DEPARTURES`: `[017] ↔ [018] ↔ [019]`; ba lựa chọn không cần đồng thời và không có ngày chung.
6. `M4 / INSTITUTIONS ACT`: `020 deferred`; `017 + 018 → 021`; `CDK-02 + 021 → 022 → 023`; `019 → 024`.
7. `M5 / INDIRECT CONVERGENCE`: `024 → 025 → 026`, đồng thời `022/023 → 026`; kết quả là reader thấy cùng một trường lực nhưng `PHYSICAL_CONVERGENCE_VOLUME_I = NONE`.

Dấu `↔` ở đây chỉ quan hệ đối chiếu nhịp/chủ đề giữa các lane, không phải tương tác nhân vật hoặc cạnh thời gian hai chiều.

## 4. Tại sao braid không round-robin

- Hai row Tiêu Phùng `002 → 003` đi liền vì mạng cộng đồng và món nợ chăm sóc cần tạo nền trước áp lực môn phái.
- Hai row Tĩnh Xuyên `015 → 016` đi liền vì phòng tuyến và kỹ nghệ là một escalation chiến tranh; chèn POV khác giữa chúng có thể làm mất áp lực.
- Hạ Nương có khoảng vắng sau `019`; thế giới tiếp tục vận hành và nàng chỉ trở lại ở `024`, nhấn mạnh cứu người không cho nàng quyền quan sát toàn bộ.
- Cuối Quyển I nghiêng về Tiêu Phùng/Cái Bang vì đây là nơi hai network handoff cùng để lại hậu quả; điều này không biến chàng thành người sở hữu source của hai lane kia.

## 5. Movement exit conditions

| Movement | Điều kiện thoát | Candidates chứng minh |
| --- | --- | --- |
| M1 | Mỗi POV có môi trường sống, giới hạn tri thức và một pressure question riêng. | 001–004 |
| M2 | Mỗi route có một lựa chọn sắp không thể rút lại; NPC/tổ chức đã hành động không phụ thuộc trio. | 005–016 |
| M3 | Tiêu rời quê; Tĩnh giao thư/rời cửa sổ; Hạ chọn chuyển chữa. | 017–019 |
| M4 | Cái Bang tự giữ Lục và thi hành bang quy; Thúy Yên tự chuyển giao/tái thiết; trio không nhận toàn bộ chiến công. | CDK-02, 021–024; 020 deferred |
| M5 | Thông cáo có chủ thể tới Thạch và chỉ phần công khai tới Tiêu; tri thức vẫn bất đối xứng. | 025–026 |

## 6. Cạnh cố ý để mở

- `022` trước hay sau `025` trong chronology khách quan.
- `017`, `018`, `019` cái nào xảy ra trước trên lịch.
- Tĩnh Xuyên đi đâu sau `018`.
- Thời gian Tiêu đi từ quê tới Cái Bang và chàng có xem trọn lôi đài hay không.
- Thời gian/kết quả chuyển chữa Tam Muội và khoảng Hạ Nương vắng mặt.
- Câu chữ, phương tiện và độ trễ của thông cáo; `026` dùng Cầu Chỉ Thủy theo function chính trị đã duyệt.
- Nội dung nội tâm của `V1-CAND-020` không thuộc architecture mặc định; record chỉ được mở lại qua một cổng Tác giả mới.

Không một open edge nào được lấp bằng task number, khoảng cách bản đồ game, archive timeline hoặc convenience của prose.
