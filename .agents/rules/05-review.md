> D-064/R-90: Read migration/restructure_2026_09/temporal-continuity-contract.md first. Exact dates, volume ages and travel estimates require evidence/decision; UNKNOWN is valid. Current allocation: migration/restructure_2026_09/series-chapter-allocation-index.md. Canon diffs must name approved state destinations; never write chapter state into policy/index.

# Review Rule & Adversarial Red-Team Review Protocol

Review before rewriting.

Mandatory Quality Binding:
- Audit all drafts against [`author/creative-constitution.md`](file:///d:/Games/Server%20Client/Server%20KT/Ki%E1%BA%BFm%20Th%E1%BA%BF%202/Server/du-long-giac-2/author/creative-constitution.md), [`author/style-bible.md`](file:///d:/Games/Server%20Client/Server%20KT/Ki%E1%BA%BFm%20Th%E1%BA%BF%202/Server/du-long-giac-2/author/style-bible.md), [`worldbuilding/style/author_wuxia_rubric.md`](file:///d:/Games/Server%20Client/Server%20KT/Ki%E1%BA%BFm%20Th%E1%BA%BF%202/Server/du-long-giac-2/worldbuilding/style/author_wuxia_rubric.md), [`worldbuilding/style/dialogue_register_matrix.md`](file:///d:/Games/Server%20Client/Server%20KT/Ki%E1%BA%BFm%20Th%E1%BA%BF%202/Server/du-long-giac-2/worldbuilding/style/dialogue_register_matrix.md), and `.agents/rules/11-prose-quality-contract.md`.
- Automated tooling gates: `npm run lint:prose`, `python scripts/lore-guard.py --scan`, and `python scripts/lore-grounder.py --chapter <chapter_path>`.

---

## 1. Adversarial Red-Team Review Protocol (Giao Thức Phản Biện Đối Kháng)

1. **Phân rã Tư duy & Triệt tiêu Ảo tưởng Tự khen (Anti-Sycophancy)**:
   - Khi bước vào vai Reviewer, Agent BẮT BUỘC rũ bỏ góc nhìn của người viết (Drafter) để nhập vai **Biên tập viên Đối kháng Khắc nghiệt**.
   - Giả định bản thảo **CÓ LỖI TIỀM ẨN** (head-hopping ngầm, dán nhãn tâm lý trá hình, quên thương tật, bịa fact) cho đến khi tìm đủ bằng chứng chứng minh điều ngược lại.
   - CẤM TUYỆT ĐỐI phán quyết "PASS" chung chung không có dẫn chứng số dòng.
2. **Kỷ luật Cưỡng chế Bằng chứng (Mandatory Span-Level Evidence)**:
   - Mọi báo cáo Review BẮT BUỘC phải trích dẫn tối thiểu 4 spans nguyên bản kèm số dòng cụ thể:
     - *Span 1*: Khẩu khí độc bản nhân vật POV (bắng nhắng/quân lệnh/y lý).
     - *Span 2*: Chi tiết đời sống dân sinh (Yên hỏa khí) hoặc điểm chạm trào lộng Mo Lei Tau (25%).
     - *Span 3*: Cản trở vật lý của thương tật theo `injuries_ledger.md`.
     - *Span 4*: Cảnh ngụ tình / Dư ba kết chương.
3. **Bảo vệ Khẩu khí Sáng tạo Độc bản (Creative Voice Protection)**:
   - Phân biệt rõ hai không gian:
     - *Lời dẫn người kể chuyện*: Bắt buộc khách quan, hạn tri sâu, pure show-don't-tell.
     - *Lời thoại trong ngoặc kép `“...”`*: Tôn trọng 100% ngữ khí nhân vật (Tiêu Phùng bắng nhắng đốp chát, Tĩnh Xuyên sắc lạnh, Hạ Nương duy lý). Tuyệt đối không bắt bẻ thoại nhân vật thành bản sao Quách Tĩnh nghiêm trang khô cứng!

---

## 2. 5 Cổng Duyệt Thẩm Mỹ (SOLID 5-Gate Review Runner)

- **Gate A: Minimal Hard Regression, Provenance Lock & Closed-World Grounding**
  - Provenance: YAML frontmatter BẮT BUỘC khớp 1-1 với Task ID/Subtask ID trong SQLite `story_database.sqlite3`.
  - Closed-World Assumption: 100% nhân vật, địa danh xuất hiện phải có trong SQLite, `genealogy_matrix.md`, hoặc `supporting_cast.md`. Báo động ngay nếu phát hiện thực thể "tự sinh".
  - Không - thời gian: Tuân thủ D-064 temporal contract (`migration/restructure_2026_09/temporal-continuity-contract.md` và `migration/restructure_2026_09/temporal-continuity-contract.md`).
  - Ranh giới tri thức: Nhân vật chỉ biết những gì ngũ quan tiếp nhận; không có rò rỉ toàn tri.
- **Gate B: Blind Reader, Narrative Propulsion & Genre Discipline**
  - Nhịp điệu kịch tính tự nhiên (organic pacing), không đốt cháy giai đoạn, có khoảng thở sinh hoạt.
  - Xung đột và động cơ sinh tồn chân thực; áp dụng chuẩn thể loại chuyên biệt (trinh thám có chuỗi vật chứng vật lý; kinh dị qua giác quan hạn tri; tình cảm low-burn).
- **Gate C: Character Agency, Martial Progression & Ongoing Injury Constraints**
  - Võ học có giới hạn (Bounded Martial Majesty): Quyền cước có biến chiêu, phá chiêu, cương nhu tương khắc; cấm tuyệt đối tiên hiệp/linh hồn/uy áp.
  - Kỷ luật thương tật (`injuries_ledger.md`): Vết thương từ các chương trước phải gây cản trở thể chất thực tế; cấm tuyệt đối instant healing.
  - Phản diện đa chiều, không hoạt hình một màu.
- **Gate D: Voice, Rhetoric & Author Creative Register**
  - Lời dẫn: Pure show-don't-tell, 0 filter words, 0 explanatory scaffolds (`đó là`, `đây là`, `chàng hiểu rằng`).
  - Lời thoại: Khẩu khí độc bản bộ ba (Tiêu Phùng / Tĩnh Xuyên / Hạ Nương) theo `dialogue_register_matrix.md`.
  - Tích hợp công thức trào lộng 65% - 25% - 10% (Mo Lei Tau & Gintama DNA khoác áo cổ phong).
- **Gate E: Word Count Band & Substantiality**
  - Dải Dung Lượng Vàng: **4.000 – 4.800 từ** (Sàn cứng: 3.500 từ; Trần mềm: 5.200 từ).
  - Vượt trần > 5.000 từ tự động kích hoạt Cơ chế Tách Phân Đoạn a/b/c có hook nối tiếp.

---

## 3. Quy Chuẩn Đề Xuất & Báo Cáo

Mọi vấn đề phát hiện phải ghi rõ:
- severity: critical / major / minor / optional
- location: dòng cụ thể trong bản thảo
- context_type: NARRATOR (Lời dẫn) / DIALOGUE (Thoại)
- problem: bản chất vi phạm
- why it matters: tác động đến cốt truyện hoặc thẩm mỹ
- evidence: trích đoạn nguyên bản
- recommended intervention: cách sửa chi tiết

Sử dụng biểu mẫu chuẩn tại [`templates/review-report.md`](file:///d:/Games/Server%20Client/Server%20KT/Ki%E1%BA%BFm%20Th%E1%BA%BF%202/Server/du-long-giac-2/templates/review-report.md).




