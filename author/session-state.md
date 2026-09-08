# Session State (Sổ tay giao ca)

> Trạng thái làm việc của dự án `du-long-giac-2`. Tự động nạp khi bắt đầu session mới hoặc khi dùng lệnh `/resume`.

## 1. Trạng thái hiện tại (Current Status)

- **Trạng thái hệ thống**: Đã TÁI THIẾT KIẾN TRÚC TOÀN DIỆN (System Architecture Reboot — Quyết định D-015, D-016, D-017, D-018).
- **Kiến trúc Workflow SOLID**: Đã hoàn tất tái thiết lập toàn bộ quy trình Agent theo chuẩn mực SOLID:
  - *Single Responsibility (SRP)*: Tách bạch rõ rệt từng phase; hợp nhất `10-provenance-kernel.md` duy nhất.
  - *Open/Closed (OCP) & Dependency Inversion (DIP)*: Chuyển dữ liệu sang `travel_matrix.md` và `characters/`; rules chỉ phụ thuộc vào Abstract Contracts.
  - *Liskov Substitution (LSP)*: Ban hành chuẩn `docs/contracts/chapter_contract.md` cho mọi thể loại chương.
  - *Interface Segregation (ISP)*: Phân rã context, từng role chỉ nạp đúng contract của mình.
- **Lưu trữ nguyên mẫu**: Các bản nháp Chapter 01, 02, 03 ban đầu đã được chuyển an toàn vào `chapters/archive/v1_prototypes/` làm tài liệu tham khảo đối soát.
- **Quy chuẩn mới**:
  - Dải Dung Lượng Vàng: **4.000 – 4.800 từ / chương** (Sàn cứng 3.500 từ, Trần mềm 5.200 từ).
  - Công thức nhịp 3-1-1: 3 Core Plot + 1 Living Lore/Mystery + 1 Road/Character.
  - Kỷ luật Nguồn (Strict Provenance): 100% tình tiết, tên chương đối soát từ SQLite `story_database.sqlite3`.
  - Mở rộng quy mô linh hoạt (Fluid Expansion): Khung cơ sở 18 chương, tự do mở rộng lên 20-30 chương để đào sâu thế sự và phát triển tự nhiên (low-burn), khép lại theo Thematic Climax trọn vẹn.
  - **Khắc chế Hào quang Vô đối & Quản lý Thương tật (Quyết định D-022)**: Ban hành `worldbuilding/medical/injuries_ledger.md` (chuẩn L1 – L5, Zero Instant Healing, Tier Gap Damage Tax).
  - **Cơ chế Đề xuất Võ học Linh hoạt (Emergent Martial Proposition)**: Ban hành `worldbuilding/martial/martial_dynamics.md`; tuyệt đối không đóng khung lộ trình thăng cấp cứng nhắc; Agent chủ động khảo sát điểm chạm võ học & đề xuất kèm cái giá sinh học/tâm lý tại Chapter Brief để Tác giả quyết định.
  - **Đồng bộ Phả hệ & Chống ảo tưởng NPC (Quyết định D-023) — HOÀN TẤT RETROFIT 100%**:
    - Ban hành Sổ cái Phả hệ & Bối phận Giang Hồ: [`worldbuilding/factions/genealogy_matrix.md`](file:///d:/Games/Server%20Client/Server%20KT/Ki%E1%BA%BFm%20Th%E1%BA%BF%202/Server/du-long-giac-2/worldbuilding/factions/genealogy_matrix.md) (khóa chặt phả hệ 12 môn phái, Công thức Tuổi Sinh học $\text{Tuổi Cha/Mẹ} \ge \text{Tuổi Con} + 16$).
    - Ban hành Mandatory Rule 5 (`GEMINI.md`) & Cập nhật `docs/WORKFLOW.md`, `templates/chapter-brief.md`.
    - Tích hợp Pedigree Linter vào `scripts/lore-guard.py` (quét tự động 47 tệp dự án, 0 lỗi vi phạm, bổ sung rule PED-3 cấm bịa đặt Bạch Cương là cha Bạch Thu Lâm, rule PED-4 cấm xưng Di - con phi sinh học giữa Tiêu Phùng 17t và Thu Lâm 24t).
    - **Hoàn tất Source Audit & Retrofit Bạch Cương - Bạch Thu Lâm & Xưng hô Tỷ - Đệ**:
      - Khảo sát mã nguồn engine `baijiang.lua` và SQLite Task 157, 450: Thân phụ Bạch Thu Lâm là Tướng quân Bạch Phụ tại Biện Kinh; Bạch Cương (~45t) là nghĩa quân tiền bối, cựu thuộc hạ của cha Tiêu Phùng, xưng đệ với Bạch Thu Lâm ("Thu Lâm tỷ") và Trâu Đức Khoái ("Đức Khoái huynh").
      - Bổ sung **Section 7: Convergence Matrix** tích hợp đầy đủ mạng lưới quan hệ đa tuyến của **Protagonist Trio** (Tiêu Phùng - Tĩnh Xuyên - Hạ Nương).
      - Khử sạch triệt để lối xưng "Di - con" tại `chapters/chapter_01.md` và `chapters/chapter_04b.md`, đồng bộ 100% chuẩn xưng hô **Thu Di / Tỷ — Đệ** xuyên suốt toàn bộ các chương.
      - Retrofit bản thảo `chapters/chapter_01.md`, `chapters/chapter_04b.md`, `chapters/chapter_05.md`, chuẩn hóa `characters/anchors/bach_thu_lam.md`, `characters/supporting_cast.md`.
    - Hoàn tất Retrofit toàn bộ các chương và brief liên quan:
      - `chapters/chapter_08a.md`: Thay "vị Chưởng môn trẻ tuổi" thành "vị Chưởng môn đoan trang trầm tĩnh".
      - `chapters/chapter_08b.md`: Bỏ "Tân Chưởng môn", sửa "Sư bá" thành "Sư tỷ", bỏ nhãn "một già một trẻ" đối với Lệ Thu Thủy.
      - `chapters/chapter_03.md`: Chuẩn hóa 10 phân đoạn miêu tả Doãn Hàm Yên 40 tuổi uy nghi gánh vác kinh tài.
      - `briefs/chapter_03_brief.md`, `briefs/chapter_08a_brief.md`, `briefs/chapter_08b_brief.md`, `briefs/chapter_11_brief.md`: Tích hợp 100% bảng `## NPC Pedigree & Biological Age Verification`.
    - Kiểm định tự động: `npm run lint:prose` PASS 15/15 chương, `python scripts/lore-guard.py --scan` PASS 47/47 tệp, `npm run gate:check` PASS 100%.
- **Hồi vừa hoàn thành**: **Chương 10: *Hình Thiên Lĩnh Huyết Lộ*** (`chapters/chapter_10.md`).
  - Trạng thái: **ĐÃ HOÀN TẤT CANON HÓA 100% & COMMIT STATE THÀNH CÔNG VÀO 4 TRỤ CỘT BỀN VỮNG**.
  - Quy mô: **5.835 từ** (0 lỗi linter `npm run lint:prose`, `npm run gate:check` PASS 100%).

## 2. Nhiệm vụ hiện tại (Current Active Gate)

- **CỔNG DỪNG 2 (Pre-Canon Hard Stop) — CHỜ TÁC GIẢ PHÊ DUYỆT BẢN THẢO & BÁO CÁO REVIEW CHƯƠNG 11**:
  - **Tên chương**: **Chương 11: *Tuyệt Bích Kỳ Hoa***.
  - **Bản thảo**: [`chapters/chapter_11.md`](file:///d:/Games/Server%20Client/Server%20KT/Ki%E1%BA%BFm%20Th%E1%BA%BF%202/Server/du-long-giac-2/chapters/chapter_11.md) — **6.665 từ** (Đã đồng bộ xưng hô Doãn Hàm Yên 40 tuổi và Hạ Nương 16 tuổi; Pure Show Don't Tell, không lỗi AI).
  - **Báo cáo Thẩm định 5 Cổng**: [`reviews/chapter_11_review.md`](file:///d:/Games/Server%20Client/Server%20KT/Ki%E1%BA%BFm%20Th%E1%BA%BF%202/Server/du-long-giac-2/reviews/chapter_11_review.md) — **PASS 5 Cổng duyệt**.
  - **Đề xuất Canon Diff sẵn sàng**: [`revisions/chapter_11_canon_diff.md`](file:///d:/Games/Server%20Client/Server%20KT/Ki%E1%BA%BFm%20Th%E1%BA%BF%202/Server/du-long-giac-2/revisions/chapter_11_canon_diff.md).
  - **Trạng thái Linter & Gate Guard**: `npm run lint:prose` PASS 100% (15/15 chương); `npm run gate:check` PASS 100% (47 tệp).
  - **KỶ LUẬT CỔNG DỪNG 2**: ĐÃ DỪNG LẠI TRÌNH TÁC GIẢ. CẤM TUYỆT ĐỐI tự ý coi như đã xong hoặc tự ý canon hóa khi Tác giả chưa duyệt Bản thảo và Báo cáo Review!

## 3. Gợi ý hành động cho Tác giả (Suggested Next Step)

Tác giả thẩm duyệt bản thảo và báo cáo review Chương 11, sau đó ra lệnh:
👉 **`"Duyệt bản thảo chapter 11"`** để hoàn tất Cổng Dừng 2, sẵn sàng tiến sang Cổng Dừng 3 (Canon Diff & State Commit)!












