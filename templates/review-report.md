# Báo Cáo Thẩm Định Bản Thảo: Chương [XX] — [Tên Chương]
## Giao Thức Đánh Giá Phản Biện Đối Kháng (Adversarial Red-Team Review Report)

> **Cơ sở thẩm định**: Kế thừa trực tiếp từ [Rule 05: Review](file:///d:/Games/Server%20Client/Server%20KT/Ki%E1%BA%BFm%20Th%E1%BA%BF%202/Server/du-long-giac-2/.agents/rules/05-review.md), [Rule 11: Prose Quality Contract](file:///d:/Games/Server%20Client/Server%20KT/Ki%E1%BA%BFm%20Th%E1%BA%BF%202/Server/du-long-giac-2/.agents/rules/11-prose-quality-contract.md), và [Author Wuxia Aesthetic Rubric](file:///d:/Games/Server%20Client/Server%20KT/Ki%E1%BA%BFm%20Th%E1%BA%BF%202/Server/du-long-giac-2/worldbuilding/style/author_wuxia_rubric.md).

---

## 1. Thông Tin Tổng Quan (Scope & Metadata)

- **Tên chương / Bản thảo**: Chương [XX]: *[Tên Chương]* (`chapters/chapter_XX.md`)
- **Nhân vật POV**: [Tiêu Phùng / Tĩnh Xuyên / Hạ Nương] ([Độ tuổi] tuổi)
- **Mốc thời gian**: [YYYY-MM-DD] (Khớp `plot/timeline.md`)
- **Dung lượng từ**: [Số từ] từ (Dải vàng: 4.000 – 4.800 từ; Sàn cứng: 3.500 từ; Trần mềm: 5.200 từ)
- **Mã nguồn Engine KT2 (Provenance)**: `Task [ID]: Subtask [ID]` (Đối chiếu SQLite `story_database.sqlite3`)
- **Bộ kiểm thử tự động**:
  - `npm run lint:prose`: [PASS / FAIL] (0 rò rỉ meta, 0 từ cấm tiên hiệp/convert)
  - `python scripts/lore-guard.py --scan`: [PASS / FAIL] (0 vi phạm lore/phả hệ)
  - `python scripts/lore-grounder.py --chapter chapters/chapter_XX.md`: [PASS / FAIL] (100% thực thể được ground trong database và sổ cái)

---

## 2. Thẩm Định Độc Lập 5 Cổng Duyệt (SOLID 5-Gate Review Runner)

### Gate A: Minimal Hard Regression, Provenance Lock & Closed-World Grounding
- **Mã nguồn Engine KT2**: [Khớp nối 1-1 với Subtask nào trong database? Có tình tiết bịa đặt ngoài luồng không?]
- **Kiểm định Không - Thời gian (Rule TC-1 đến TC-4)**: [Mốc ngày tháng, tuổi nhân vật, độ trễ di chuyển từ travel_matrix.md]
- **Kiểm định Thực thể Đóng (Closed-World Assumption)**: [Toàn bộ NPC xuất hiện có nằm trong `supporting_cast.md` / `genealogy_matrix.md` hoặc đã được duyệt tại Chapter Brief không?]
- **Trạng thái**: **[PASS / FAIL]**

### Gate B: Blind Reader, Narrative Propulsion & Dramatic Arc
- **Nhịp điệu kịch tính (Pacing)**: [Phát triển tự nhiên hay đốt cháy giai đoạn? Có khoảng lặng nhân gian / thế tục yên hỏa khí không?]
- **Xung đột & Áp lực**: [Nhân vật hành động vì mục tiêu sinh tồn hay đóng vai công cụ?]
- **Trạng thái**: **[PASS / FAIL]**

### Gate C: Character Agency, Martial Progression & Ongoing Injury Constraints
- **Tầng võ học (Bounded Martial Majesty)**: [Đòn thế tuân thủ cơ sinh học, có biến chiêu/phá chiêu; tuyệt đối 0 tiên hiệp/linh hồn/uy áp]
- **Kỷ luật Thương tật (`injuries_ledger.md`)**: [Các chấn thương từ chương trước có gây đau đớn, hạn chế bước chân/hơi thở ở chương này không? Cấm tuyệt đối lành lặn tức thì]
- **Trạng thái**: **[PASS / FAIL]**

### Gate D: Voice, Rhetoric & Author Creative Register
- **Lời dẫn (Narrator Text - Kỷ luật Khắt khe)**:
  - Pure Show-Don't-Tell: [Có dán nhãn tâm lý hay kể lể `đó là`, `đây là`, `chàng hiểu rằng` không?]
  - Camera Hạn Tri (Limited POV): [Có head-hopping sang đầu nhân vật khác không?]
- **Lời thoại (Dialogue Text - Tôn Vinh Sáng Tạo)**:
  - Khẩu khí nhân vật POV: [Có đúng chất bắng nhắng/tự trào của Tiêu Phùng, kỷ luật sa trường của Tĩnh Xuyên, hay y lý thực chứng của Hạ Nương?]
  - Điểm chạm trào lộng (Mo Lei Tau 25% / Gintama 10%): [Có chi tiết hài hước trái khoáy, võ đường phố thực dụng, hay chuyển ngữ đương đại sang áo cổ phong không?]
- **Trạng thái**: **[PASS / FAIL]**

### Gate E: Word Count Band & Substantiality
- **Dung lượng**: [Số từ] từ $\rightarrow$ **[PASS / FAIL]**

---

## 3. Bằng Chứng Trích Xuất Nguyên Văn (Mandatory Evidence Spans)

> ⚠️ *Bắt buộc trích dẫn tối thiểu 4 spans nguyên bản kèm số dòng cụ thể để bài trừ hiện tượng nhận xét chung chung/ảo tưởng tuân thủ.*

1. **Span 1: Khẩu khí độc bản nhân vật (Character Sociolect)**:
   - **Vị trí**: Dòng [XX] – [YY]
   - **Trích đoạn**: *“...”*
   - **Phân tích**: [Chứng minh rõ tính cách bắng nhắng/quân lệnh/y lý của nhân vật POV]

2. **Span 2: Chi tiết đời sống dân sinh / Hài hước Mo Lei Tau (Living Texture & Subversion)**:
   - **Vị trí**: Dòng [XX] – [YY]
   - **Trích đoạn**: *“...”*
   - **Phân tích**: [Chứng minh hơi thở thế tục yên hỏa khí hoặc cú bẻ lái trào lộng thực dụng]

3. **Span 3: Giới hạn sinh học / Cản trở của thương tật (Injury Impact)**:
   - **Vị trí**: Dòng [XX] – [YY]
   - **Trích đoạn**: *“...”*
   - **Phân tích**: [Chứng minh sự đau đớn thể xác thực tế theo injuries_ledger.md, không có plot armor]

4. **Span 4: Cảnh ngụ tình / Dư ba kết chương (Poetic Resonance Closure)**:
   - **Vị trí**: Dòng [XX] – [YY]
   - **Trích đoạn**: *“...”*
   - **Phân tích**: [Chứng minh cái kết tĩnh lặng, không có đại ngôn sáo rỗng hay triết lý giáo điều]

---

## 4. Phát Hiện Của Biên Tập Viên Đối Kháng (Adversarial Findings)

### Mức độ Nghiêm trọng (Critical / Major / Minor)
- **Critical (Lỗi chặn)**: [Head-hopping, bịa fact không có trong database, quên thương tật, rò rỉ meta]
- **Major (Lỗi lớn)**: [Văn phong convert thô, thiếu nhịp thở nhân vật, đòn thế phi lý]
- **Minor (Lỗi nhỏ)**: [Từ ngữ lặp lại, lỗi chính tả]
- **Optional**: [Gợi ý nâng cao độ sắc sảo]

---

## 5. Kết Luận & Phán Quyết (Verdict)

- **Phán quyết**: **[APPROVED / REVISE_REQUIRED]**
- **Đề xuất bước tiếp theo**: [Nếu APPROVED $\rightarrow$ Lập Canon Diff Cổng Dừng 3; nếu REVISE_REQUIRED $\rightarrow$ Chỉ định dòng cần sửa]
