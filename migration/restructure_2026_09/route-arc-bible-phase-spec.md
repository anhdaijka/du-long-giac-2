# Spec đề xuất — Phase Route Arc Bible

Trạng thái: `VOLUME I PILOT DELIVERED AND AUTHOR APPROVED / SCENE-PLAN PHASE SPEC AUTHOR APPROVED / CANDIDATE SCENE PLAN IMPLEMENTATION AUTHORIZED`.

Tài liệu này chỉ định nghĩa phạm vi và cách thực hiện phase kế tiếp. Nó không phải Route Arc Bible, không phân chương và không tạo story canon.

## 1. Restate Brief

Sau khi kiến trúc năm quyển được duyệt, phase kế tiếp cần chuyển các task cluster đã khảo sát thành ba đường phát triển POV có provenance, đồng thời bảo toàn:

- quyền sở hữu route theo R-14;
- hội tụ gián tiếp cuối Quyển I và hội tụ vật lý đầu tiên trong Quyển II;
- phân biệt `GAME FACT`, `HISTORICAL FACT`, `GAME ALT-HISTORY` và `NOVELIZATION BRIDGE`;
- các protected unknown về Huyễn Cảnh, công năng Du Long Giác, chronology và endpoint quan hệ.

## 2. Author decisions

### RABQ-01 — phạm vi lượt triển khai đầu

**Đã duyệt:** làm **pilot Quyển I cho cả ba POV**, duyệt cấu trúc và chất lượng provenance trước khi mở rộng sang Quyển II–V. Không làm cả năm quyển trong một lượt.

### RABQ-02 — hình dạng artifact

**Đã duyệt:** dùng ba bible theo nhân vật, mỗi bible về sau trải đủ năm quyển, cộng một convergence matrix và một README/index:

- `route-bibles/tieu-phung.md`;
- `route-bibles/tinh-xuyen.md`;
- `route-bibles/ha-nuong.md`;
- `route-bibles/convergence-matrix.md`;
- `route-bibles/README.md`.

Ở pilot đầu, chỉ phần Quyển I được phép điền; Quyển II–V để placeholder có trạng thái rõ. Cấu trúc này ưu tiên tính liên tục nhân vật và tránh lặp ba lane trong năm file quyển riêng.

### RABQ-03 — quyền tạo Bridge trong bible

**Đã duyệt:** bible chỉ được ghi bridge mới dưới nhãn `BRIDGE-CANDIDATE / AUTHOR APPROVAL REQUIRED`. Agent có thể đề xuất NPC nhỏ, động cơ nối hoặc sự kiện chuyển tiếp không mâu thuẫn source, nhưng không được tự nâng chúng thành planning authority hay canon.

## 3. Assumptions

- Ba profile chính và R-11–R-19 là ràng buộc đầu vào.
- `volume-architecture-proposal.md` là planning authority hiện hành dù tên file lịch sử còn chữ “proposal”.
- Arc membership, source graph, branch matrix và source packets là router; SQLite vẫn là nguồn tối thượng cho proposition fact game.
- Quyển I chủ yếu dùng locator 00–03 và Task 157/ba cổng 158–160 ở locator 06; Task 1, Task 2 và Task 12 là ba lõi đầu vào.
- Living lore được chọn theo chức năng nhân quả/nhân vật, không theo quota và không vì cần kéo dài số chương.
- Phase này chưa cần khóa năm tuyệt đối, lịch sử đối chiếu cho Quyển III–V hoặc hình thức corroboration Task 450.

## 4. Approval Gate

RABQ-01–03 và LWCQ-01–04 đã được Tác giả chốt. Bảng bao phủ sơ bộ và pilot Quyển I đã được giao; V1PQ-01–04 duyệt nội dung pilot/PB-01–06 ngày 2026-09-09. Cổng pilot đã đóng, không xin lại cùng quyền. Phạm vi tiếp nối cần được xác định trước khi mở nội dung Quyển II–V, chronology chi tiết, scene/chapter hoặc prose.

## 5. Draft Spec

### Goal

Dựng ba tuyến Quyển I độc lập nhưng có quan hệ nhân quả, truy được từng claim về evidence hoặc quyết định adaptation đã duyệt.

### Scope

- Route spine Quyển I của Tiêu Phùng, Tĩnh Xuyên và Hạ Nương.
- Mỗi route ghi: source nodes, opening state, pressure chain, irreversible choice, carried consequence, excluded branches và protected unknowns.
- Một convergence matrix ghi tác động gián tiếp giữa ba tuyến; không cho ba POV gặp trực tiếp trong Quyển I.
- Provenance ledger cục bộ trỏ về SQLite query/result đã lưu trong evidence packet hoặc ghi query bổ sung khi packet chưa đủ proposition.
- Danh sách `BRIDGE-CANDIDATE` riêng, không trộn với fact game.

### Out of scope

- Quyển II–V ngoài placeholder trạng thái.
- Chapter count, chapter title, scene order, beat sheet và prose.
- Chronology tuyệt đối và historical ledger cho các quyển sau.
- Võ học chi tiết theo quyển nếu chưa được source/decision hiện hành bảo vệ.
- Canon promotion hoặc hồi sinh nội dung trong archive/rejected.

### Constraints

- Không POV nào hoàn thành mọi quest.
- Không dùng task ID liền kề làm bằng chứng nhân quả nếu source graph không có cạnh.
- Branch mutually exclusive phải được giữ điều kiện hoặc chọn bằng Bridge đã duyệt.
- Mọi fact bền vững phải có lớp evidence và provenance đủ để tái kiểm.
- Claim chưa đủ nguồn phải bị hạ xuống hypothesis/bridge candidate, không được viết như sự thật.

### Expected Output

Năm artifact theo RABQ-02, trong đó ba bible chỉ hoàn thiện phạm vi Quyển I và convergence matrix chứng minh không có hội tụ vật lý sớm.

### Acceptance Criteria

- Mỗi route có ít nhất một lựa chọn không thể hoán đổi và một hậu quả mang sang Quyển II.
- Task 157, Task 1 và Task 12 được dùng đúng vai trò lõi; Task 2 và các cổng 158–160 không bị phân phối chồng chéo vô lý.
- Mọi route ownership được gắn `NOVELIZATION BRIDGE`, không giả làm game fact.
- Mọi direct-source claim có provenance proposition-level.
- Không có chapter plan, scene prose hoặc chi tiết từ archive/rejected lọt vào.
- Validator/scan xác nhận đủ nhãn evidence, đủ ba POV và không có physical convergence trong Quyển I.

## 6. Proposed Plan

1. Tái đọc các source packet liên quan locator 00–03 và 06; trích đúng Task 1, 2, 12, 157–160.
2. Lập bảng node ứng viên theo từng POV và đánh dấu branch condition/reliability.
3. Tạo cấu trúc năm artifact đã duyệt, chỉ mở phần Quyển I.
4. Điền route spine từng POV bằng source node trước, sau đó mới liệt kê Bridge Candidate.
5. Dựng convergence matrix ở mức tác động/tin tức, cấm gặp trực tiếp.
6. Chạy kiểm tra provenance, nhãn lớp fact, route overlap và archive contamination.
7. Trình Tác giả duyệt pilot trước khi mở Quyển II.
