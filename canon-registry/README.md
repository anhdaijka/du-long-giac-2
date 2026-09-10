# Canon Registry

Trạng thái: `INITIALIZED EMPTY / D-067 / R-93 / SOURCE-SAFE LOCATOR / NOT A SECOND CANON DATABASE`.

Registry này phục vụ Gemini tìm nhanh proposition/state bền vững đã được nhận. Nó không thay SQLite packet, author decision, source receipt, review semantic hoặc canon diff. Đọc [proposal](../migration/restructure_2026_09/canon-registry-proposal.md), [temporal contract](../migration/restructure_2026_09/temporal-continuity-contract.md) và [framework](../migration/restructure_2026_09/temporal-character-framework.md) trước khi dùng.

## Nội dung hiện tại

- `registry-index.tsv` chỉ có schema header, chưa có fact/state row.
- `registry-open-slots.md` là index các rào chưa chọn; không chứa candidate answer.
- `changes/` chỉ nhận change receipt sau canon diff được Tác giả duyệt.

Registry trống không chứng minh một fact không tồn tại. Gemini phải quay về chapter source packet/author decision khi không tìm thấy row.

## Đọc và ghi

1. Preflight query index hẹp theo proposition cần dùng, sau đó mở raw receipt/decision của mọi row được dùng.
2. `GAME_FACT`, `HISTORICAL_FACT`, `APPROVED_BRIDGE`, `CANON_STATE` và attributed report chỉ vào index khi đúng điều kiện trong proposal.
3. `AUTHOR_DIRECTION`, draft, clue, title task, inference chưa duyệt và open answer không thành row fact.
4. Chỉ canon diff được Tác giả duyệt mới tạo/sửa `CANON_STATE` hay change receipt. Một Bridge planning-only không là quyền ghi row state.
5. Không sửa/xóa row cũ; thêm row thay thế với `supersedes`, đánh row cũ `SUPERSEDED`/`RETRACTED` theo decision thật.

## Cách dùng Gemini

Trước khi viết claim bền vững, Gemini dùng registry như locator rồi xác minh receipt. Nếu query chạm ID trong `registry-open-slots.md`, không tự chọn answer. Nếu không có row, dùng `UNKNOWN` hoặc tạo author question/proposal theo router.
