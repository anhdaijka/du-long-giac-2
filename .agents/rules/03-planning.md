# Rule 03: Planning Engine (Bộ Thiết Kế Kịch Bản Chi Tiết)

> **Trách nhiệm duy nhất (Single Responsibility)**: Thiết lập bản đặc tả kịch bản chương truyện (`IChapterPlan` / Chapter Brief) chuẩn xác từ bản thảo phân cảnh `plot/volume_XX_deck.md` trước khi chấp bút.

---

## 1. ĐẦU VÀO BẮT BUỘC (PLANNING INPUT CONTRACTS)
Trước khi lập plan cho một chương mới, Agent bắt buộc nạp:
1. **Dàn ý phân cảnh**: Tương ứng trong `plot/volume_XX_deck.md`.
2. **Nguồn gốc xác thực**: Truy vấn SQLite theo `.agents/rules/10-provenance-kernel.md` để lấy dữ liệu Task/Subtask và đối thoại gốc.
3. **Hồ sơ nhân vật trung tâm (POV)**: Đọc `characters/<character_id>.md` để nắm rõ ranh giới tri thức (`epistemic ledger`) và tầng bậc võ công hiện hành.
4. **Không - thời gian thực tế**: Tra cứu `worldbuilding/geography/travel_matrix.md` để đảm bảo địa bàn và thời gian di chuyển hợp lý.
5. **Sổ Cái Thương Tật & Thể Trạng**: Tra cứu `worldbuilding/medical/injuries_ledger.md` để kế thừa chính xác các vết thương thực thể (L1 – L5) chưa lành từ các chương trước.
6. **Sổ Động Thái Võ Học**: Tra cứu `worldbuilding/martial/martial_dynamics.md` để đối soát bậc cảnh giới (Tier 0 – Tier 5) và các mầm mống võ học tiềm năng.

---

## 2. CẤU TRÚC ĐẶC TẢ BẢN PLAN (ICHAPTERPLAN SPECIFICATION)
Một bản kế hoạch chương hoàn chỉnh phải bao gồm đầy đủ các mục:
1. **Metadata & Provenance**: Số chương, Tên chương, POV, Địa bàn, Ngày tháng (năm 1191), Mã nguồn Task/Subtask SQLite.
2. **Mục tiêu kịch bản (Chapter Purpose)**: Xung đột trung tâm cần giải quyết; sự biến chuyển tâm lý hoặc mối quan hệ.
3. **Thương Tật Kế Thừa & Rào Cản Sinh Học (Inherited Injuries & Trauma)**: Liệt kê rõ các vết thương từ chương trước (mức độ L1 – L5, vị trí giải phẫu, đau đớn, hạn chế hô hấp hoặc phát lực trong chương này).
4. **Đề Xuất Tiến Trình Võ Học Linh Hoạt (Emergent Martial Proposition)**:
   - Tuyệt đối KHÔNG thao túng đặt sẵn lộ trình thăng cấp cứng nhắc gây nhàm chán cho Tác giả.
   - Agent phân tích bối cảnh nhiệm vụ SQLite xem có "Điểm chạm võ học/kỳ ngộ" tự nhiên không và CHỦ ĐỘNG ĐỀ XUẤT tại Brief:
     + *Có thăng cấp/lĩnh ngộ gì ở chương này không?* (Nếu không, ghi rõ lý do giữ nguyên Tier 0 thô mộc).
     + *Nguồn gốc (Phi nhị-nguyên)*: Kẻ thù sa trường Kim quốc, tử sĩ Tây Hạ, dị nhân tà phái hay mẹo sinh tồn bãi sậy?
     + *Cái giá máu thịt (Cost/Tax)*: Chấn thương L2/L3, nôn ra máu, kiệt sức, hoặc gánh nặng tâm lý.
     + *Câu hỏi mở cho Tác giả*: Trình Tác giả quyết định kích hoạt hay hoãn lại.
5. **Khắc Họa Phe Đối Địch Phi Nhị-Nguyên (Non-Binary Antagonist Dimension)**: Động cơ quân sự, lập trường dân tộc, góc nhìn có thể đồng cảm của đối thủ; xóa bỏ hoàn toàn phản diện hoạt hình một chiều.
6. **Trạng thái Khởi đầu & Kết thúc (Starting & Ending State)**: Điểm bắt đầu và dư ba kết thúc (theo phong cách cảnh ngụ tình Kim Dung).
7. **Danh sách phân cảnh (Scene Beats)**: 3–5 cảnh cụ thể với diễn biến nhân quả (Causal Progression).
8. **Ranh giới Tri thức & Cấm kỵ (Epistemic Boundary & Forbidden Reveals)**: Xác định rõ những bí mật/tình tiết nhân vật CHƯA ĐƯỢC PHÉP biết tại thời điểm này.
9. **Hơi thở Dân sinh (Living Plebeian Anchors)**: Chi tiết nghề nghiệp, giá cả, thời tiết, phong thổ thường dân được đan cài.

---

## 3. NGUYÊN TẮC PHÊ DUYỆT (GOVERNANCE)
- Bản kế hoạch chương là một đề xuất (proposal).
- Khi bản plan làm thay đổi đáng kể cốt truyện hoặc bước ngoặt của nhân vật, bắt buộc phải có sự phê duyệt của Tác giả trước khi chuyển sang khâu chấp bút (`04-drafting.md`).

