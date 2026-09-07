# Rule 03: Planning Engine (Bộ Thiết Kế Kịch Bản Chi Tiết)

> **Trách nhiệm duy nhất (Single Responsibility)**: Thiết lập bản đặc tả kịch bản chương truyện (`IChapterPlan` / Chapter Brief) chuẩn xác từ bản thảo phân cảnh `plot/volume_XX_deck.md` trước khi chấp bút.

---

## 1. ĐẦU VÀO BẮT BUỘC (PLANNING INPUT CONTRACTS)
Trước khi lập plan cho một chương mới, Agent bắt buộc nạp:
1. **Dàn ý phân cảnh**: Tương ứng trong `plot/volume_XX_deck.md`.
2. **Nguồn gốc xác thực**: Truy vấn SQLite theo `.agents/rules/10-provenance-kernel.md` để lấy dữ liệu Task/Subtask và đối thoại gốc.
3. **Hồ sơ nhân vật trung tâm (POV)**: Đọc `characters/<character_id>.md` để nắm rõ: Vết thương cốt tử, ranh giới tri thức (`epistemic ledger`), và tầng bậc võ công hiện hành.
4. **Không - thời gian thực tế**: Tra cứu `worldbuilding/geography/travel_matrix.md` để đảm bảo địa bàn và thời gian di chuyển hợp lý.

---

## 2. CẤU TRÚC ĐẶC TẢ BẢN PLAN (ICHAPTERPLAN SPECIFICATION)
Một bản kế hoạch chương hoàn chỉnh phải bao gồm đầy đủ các mục:
1. **Metadata & Provenance**: Số chương, Tên chương, POV, Địa bàn, Ngày tháng (năm 1191), Mã nguồn Task/Subtask.
2. **Mục tiêu kịch bản (Chapter Purpose)**: Xung đột trung tâm cần giải quyết; sự biến chuyển tâm lý hoặc mối quan hệ.
3. **Trạng thái Khởi đầu & Kết thúc (Starting & Ending State)**: Điểm bắt đầu và dư ba kết thúc (theo phong cách cảnh ngụ tình Kim Dung).
4. **Danh sách phân cảnh (Scene Beats)**: 3–5 cảnh cụ thể với diễn biến nhân quả (Causal Progression).
5. **Ranh giới Tri thức & Cấm kỵ (Epistemic Boundary & Forbidden Reveals)**: Xác định rõ những bí mật/tình tiết nhân vật CHƯA ĐƯỢC PHÉP biết tại thời điểm này.
6. **Hơi thở Dân sinh (Living Plebeian Anchors)**: Chi tiết nghề nghiệp, giá cả, thời tiết, phong thổ thường dân được đan cài.

---

## 3. NGUYÊN TẮC PHÊ DUYỆT (GOVERNANCE)
- Bản kế hoạch chương là một đề xuất (proposal).
- Khi bản plan làm thay đổi đáng kể cốt truyện hoặc bước ngoặt của nhân vật, bắt buộc phải có sự phê duyệt của Tác giả trước khi chuyển sang khâu chấp bút (`04-drafting.md`).

