# Validation report — Chapter Plan Quyển I

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
