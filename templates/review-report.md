> D-064/R-90: Read migration/restructure_2026_09/temporal-continuity-contract.md first. Exact dates, volume ages and travel estimates require evidence/decision; UNKNOWN is valid. Current allocation: migration/restructure_2026_09/series-chapter-allocation-index.md. Canon diffs must name approved state destinations; never write chapter state into policy/index.

# Báo Cáo Thẩm Định Bản Thảo: Chương [XX] — [Tên Chương]
## Giao Thức Đánh Giá Phản Biện Đối Kháng (Adversarial Red-Team Review Report)

> **Nguyên tắc Reliability v2**: Reviewer phải đọc lại **bản chapter hiện tại trong repository** từ đầu đến cuối. Review cũ, chat memory, draft cũ hoặc kết quả linter không thay thế cho việc đọc toàn văn hiện tại.

---

## 1. Thông Tin Tổng Quan (Scope & Metadata)

- **Tên chương / Bản thảo**: Chương [XX]: *[Tên Chương]* (`chapters/chapter_XX.md`)
- **Nhân vật POV**: [Tiêu Phùng / Tĩnh Xuyên / Hạ Nương] ([Độ tuổi] tuổi)
- **Mốc thời gian**: [relative window / UNKNOWN; exact date only with author decision] (Khớp `migration/restructure_2026_09/temporal-continuity-contract.md`)
- **Dung lượng từ**: [Số từ] từ (Dải vàng: 4.000 – 4.800 từ; Sàn cứng: 3.500 từ; Trần mềm: 5.200 từ)
- **Mã nguồn Engine KT2 (Provenance)**: `Task [ID]: Subtask [ID]`
- **Evidence / Claim packet**:
  - `research/evidence/chapter_XX.json`: [PRESENT / NOT YET REQUIRED]
  - `research/claims/chapter_XX.json`: [PRESENT / NOT YET REQUIRED]
  - `python scripts/claim-guard.py --chapter XX`: [PASS / FAIL / NOT RUN]
- **Bộ kiểm thử cơ học**:
  - `npm run lint:prose`: [PASS / FAIL] — lexical/meta/style-pattern scan, **không phải semantic prose approval**
  - `python scripts/lore-guard.py --scan`: [PASS / FAIL] — known-regression scan, **không phải Zero Hallucination proof**
  - `python scripts/lore-grounder.py --chapter chapters/chapter_XX.md`: [PASS / WARN] — entity plausibility, **không chứng minh relation/event claims**

---

## 2. Full-Read Coverage — Bắt Buộc

> Mỗi range tối đa 120 dòng. Các range phải phủ **toàn bộ file chapter hiện tại từ L1 đến EOF** và mỗi range phải có ít nhất một quan sát cụ thể. Không dùng một range khổng lồ để tự chứng nhận đã đọc.

- `L1-L[XX]` — [Quan sát cụ thể về opening, POV, causality, voice hoặc lỗi phát hiện trong chính range này]
- `L[XX+1]-L[YY]` — [Quan sát cụ thể]
- `L[YY+1]-L[ZZ]` — [Quan sát cụ thể]
- [Thêm range cho đến EOF]

Kiểm tra cấu trúc:

```bash
python scripts/review-guard.py --chapter-number XX
```

---

## 3. Thẩm Định Độc Lập 5 Cổng Duyệt

### Gate A: Provenance, Claim Grounding & Continuity

- **Provenance**: [Task/Subtask nào thực sự support các sự kiện cốt lõi?]
- **Claim audit**: [Claim nào DIRECT_SOURCE? inference? unresolved? bridge? Có entity đúng nhưng relation chưa được source support không?]
- **Không-thời gian**: [Ngày tháng, tuổi, travel/information latency]
- **Epistemic boundary**: [POV có biết đúng những gì đã được reveal không?]
- **Trạng thái**: **[PASS / FAIL]**

### Gate B: Blind Reader, Narrative Propulsion & Genre Discipline

- **Nhịp điệu**: [Có rush quest / exposition dump / filler không?]
- **Causality**: [Hành động có phát sinh tự nhiên từ mục tiêu và áp lực không?]
- **Living texture**: [Dân sinh có phục vụ cảnh hay chỉ trang trí?]
- **Trạng thái**: **[PASS / FAIL]**

### Gate C: Character Agency, Martial Progression & Injury Constraints

- **Agency**: [Nhân vật chủ động theo đuổi mục tiêu hay chỉ làm công cụ chuyển quest?]
- **Võ học**: [Có vượt tier / plot armor / đòn thế vô căn cứ không?]
- **Thương tật**: [Vết thương hiện hữu có tạo giới hạn vật lý thật không?]
- **Trạng thái**: **[PASS / FAIL]**

### Gate D: Voice, Show-vs-Tell & Creative Register

- **Narrator**: [Có recap, psychological labeling, explanatory scaffold, head-hopping không?]
- **Character voice**: [Khẩu khí có phân biệt đúng nhân vật không?]
- **Comedy execution**: [Setup → misdirection → payoff → afterbeat có hoạt động không? Narrator có giải thích punchline làm mất bất ngờ không?]
- **65/25/10**: [Đánh giá bằng hành vi quan sát được, không đếm vài câu joke rồi suy ra tỷ lệ]
- **Trạng thái**: **[PASS / FAIL]**

### Gate E: Substantiality & Word Count

- **Dung lượng**: [Số từ]
- **Nếu vượt trần**: [Có lý do nghệ thuật thực sự hay đang nhồi/không chịu split?]
- **Nếu dưới sàn**: [Thiếu chiều sâu ở đâu?]
- **Trạng thái**: **[PASS / FAIL]**

---

## 4. Bằng Chứng Trích Xuất Nguyên Văn — Bắt Buộc

> Tối thiểu 4 spans. `review-guard.py` sẽ kiểm tra range nằm trong **chapter hiện tại** và trích đoạn có xuất hiện thật trong range đó. Hãy dùng nguyên văn, không paraphrase.

1. **Span 1 — Khẩu khí / Agency nhân vật**
   - **Vị trí**: `L[XX]-L[YY]`
   - **Trích đoạn**: [dán nguyên văn một đoạn liên tục từ range]
   - **Phân tích**: [Điều span này chứng minh hoặc làm lộ ra]

2. **Span 2 — Living texture / Comedy execution**
   - **Vị trí**: `L[XX]-L[YY]`
   - **Trích đoạn**: [nguyên văn]
   - **Phân tích**: [Có show hay narrator đang giải thích? Punchline có được để tự rơi không?]

3. **Span 3 — Injury / Physical constraint / Martial reality**
   - **Vị trí**: `L[XX]-L[YY]`
   - **Trích đoạn**: [nguyên văn]
   - **Phân tích**: [Đối chiếu injuries ledger / martial tier]

4. **Span 4 — Ending resonance / Concrete closure**
   - **Vị trí**: `L[XX]-L[YY]`
   - **Trích đoạn**: [nguyên văn]
   - **Phân tích**: [Dư ba có đến từ hình ảnh/hành động hay narrator thuyết minh ý nghĩa?]

---

## 5. Phát Hiện Của Biên Tập Viên Đối Kháng

Mỗi finding phải có:

- **severity**: `critical | major | minor | optional`
- **location**: `Lx-Ly`
- **context_type**: `NARRATOR | DIALOGUE`
- **problem**: lỗi cụ thể
- **why_it_matters**: tác động đến độc giả/canon/craft
- **evidence**: nguyên văn
- **recommended_intervention**: sửa ở phạm vi nhỏ nhất hợp lý

### Findings

1. [Finding cụ thể]
2. [Finding cụ thể]
3. [...]

Không bắt buộc phải tìm lỗi cho đủ số lượng. Nhưng **cấm** kết luận PASS chung chung nếu chưa chứng minh bằng coverage + spans + phân tích semantic.

---

## 6. Kết Luận & Phán Quyết

- **Phán quyết**: **[APPROVED / REVISE_REQUIRED]**
- **Critical còn mở**: [0 / số lượng]
- **Major còn mở**: [0 / số lượng]
- **Đề xuất bước tiếp theo**:
  - `APPROVED` → trình Tác giả tại Hard Stop 2; chỉ sau khi Tác giả duyệt mới chuẩn bị Canon Diff.
  - `REVISE_REQUIRED` → sửa đúng findings, sau đó **đọc lại current chapter** và review lại các vùng bị ảnh hưởng.

Khi cần xác nhận cấu trúc review đã đủ để trình duyệt:

```bash
python scripts/review-guard.py --chapter-number XX --require-approval
```
