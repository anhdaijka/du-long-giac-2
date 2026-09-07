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
  - **Phản diện Phi Nhị-Nguyên**: Tích hợp nhân tính, kỷ luật sa trường và góc nhìn dân tộc vào phe đối địch.
- **Hồi vừa hoàn thành**: **Chương 06: *Hộ Đê Cứu Nạn*** (`chapters/chapter_06.md`).
  - Trạng thái: **ĐÃ HOÀN TẤT CANON HÓA 100% & COMMIT STATE THÀNH CÔNG** (Vượt trọn vẹn cả 3 Cổng Dừng Cứng: Brief $\rightarrow$ Draft & Review $\rightarrow$ Canon Diff & State Commit).
  - Quy mô: **4.974 từ** (Đạt chuẩn 5 Cổng thẩm định SOLID, 0 lỗi linter `npm run lint:prose`, `npm run gate:check` PASS 100%).
  - Tổng dung lượng tích lũy tác phẩm: **39.422 từ** (Vượt 8/18 chương theo kế hoạch Quyển 1).
  - Sổ cái trạng thái đã cập nhật:
    - [worldbuilding/medical/injuries_ledger.md](file:///d:/Games/Server%20Client/Server%20KT/Ki%E1%BA%BFm%20Th%E1%BA%BF%202/Server/du-long-giac-2/worldbuilding/medical/injuries_ledger.md) (kích hoạt `INJ-TP-003` L1 chuột rút cơ hoành; cập nhật `INJ-TP-002` L3 rạn xương sườn tuần 2/6; thêm `INJ-GST-001` L3 đứt gân gót chân Giới Sơn Tông).
    - [worldbuilding/martial/martial_dynamics.md](file:///d:/Games/Server%20Client/Server%20KT/Ki%E1%BA%BFm%20Th%E1%BA%BF%202/Server/du-long-giac-2/worldbuilding/martial/martial_dynamics.md) (giữ vững Tier 0 cho Tiêu Phùng; bổ sung kinh nghiệm cơ quan học & mẹo then khóa cơ hoành dã chiến).
    - [characters/tieu_phung.md](file:///d:/Games/Server%20Client/Server%20KT/Ki%E1%BA%BFm%20Th%E1%BA%BF%202/Server/du-long-giac-2/characters/tieu_phung.md) (mốc thời gian 19-08-1191 sáng, biến dạng đoản côn, giác ngộ về quốc nạn).
    - [worldbuilding/artifacts/artifacts_ledger.md](file:///d:/Games/Server%20Client/Server%20KT/Ki%E1%BA%BFm%20Th%E1%BA%BF%202/Server/du-long-giac-2/worldbuilding/artifacts/artifacts_ledger.md) (đoản côn mẻ thêm rãnh sắt, bàn giao xâu chìa khóa cửu môn).
    - [plot/promises_tracker.md](file:///d:/Games/Server%20Client/Server%20KT/Ki%E1%BA%BFm%20Th%E1%BA%BF%202/Server/du-long-giac-2/plot/promises_tracker.md) (đóng `TH-010` RESOLVED; mở `TH-011` sang Cái Bang Yến Tử Ổ).
    - [plot/timeline.md](file:///d:/Games/Server%20Client/Server%20KT/Ki%E1%BA%BFm%20Th%E1%BA%BF%202/Server/du-long-giac-2/plot/timeline.md) (mốc ngày 19-08-1191 giải cứu Giới Sơn Tông và đóng cửa lũ đê Ba Lăng).
  - POV: Tiêu Phùng (17 tuổi — Đê quai Ba Lăng & Thạch thất ngầm sông Động Đình).

## 2. Nhiệm vụ hiện tại (Current Active Gate)

- **CỔNG DỪNG 1 (Pre-Draft Hard Stop) — CHỜ DUYỆT CHAPTER BRIEF CHƯƠNG 07**:
  - **Mục tiêu**: **Chương 07: *Ám Toán Trong Đêm***.
  - **Tuyến nhân vật / POV**: **Tĩnh Xuyên** (Thanh Loa Đảo — Thiên Vương Bang).
  - **Tập tin Brief**: [briefs/chapter_07_brief.md](file:///d:/Games/Server%20Client/Server%20KT/Ki%E1%BA%BFm%20Th%E1%BA%BF%202/Server/du-long-giac-2/briefs/chapter_07_brief.md).
  - **Nguồn KT2 Engine**: `Task 1: Subtask 2` (*Thông Địch Phản Bang* — XML `Stories/task_publish/sub/0000000000000002.xml`).
  - **Hạt giống thu hoạch & kích hoạt**: `TH-003` (Mối nghi kỵ chia rẽ ngầm của Lâu Nhất Quan) & `TH-004` (Sự tin cậy của Dương Thiết Tâm với Tĩnh Xuyên).
  - **Nội dung trọng tâm**: Thích khách tập kích hụt Lâu Nhất Quan trong đêm bão; lời khai man vu cáo Cầu Chỉ Thủy thông đồng Thiên Nhẫn Giáo; phái bảo thủ Lâu Nhất Quan đòi chém Cầu lão; Dương Thiết Tâm điềm tĩnh nhìn ra bẫy ly gián, cử Tĩnh Xuyên mang giỏ trái cây vào thạch ngục thăm dò; cuộc đối thoại khẳng khái với Cầu lão; đệ tử Phân đà Thành Đô vượt 800 dặm mang mật thư báo tin **hung ngọc Du Long Giác xuất hiện tại Thúy Yên Môn**; Bùi Dực Phi nhận lệnh xuất hành Tây Nam.
  - **Trạng thái**: **ĐÃ SOẠN XONG CHAPTER BRIEF — ĐANG DỪNG CHỜ TÁC GIẢ THẨM DUYỆT (CỔNG DỪNG 1)**. Cấm tuyệt đối chấp bút `chapters/chapter_07.md` trước khi Tác giả phê duyệt.

## 3. Gợi ý hành động cho Tác giả (Suggested Next Step)

Tác giả xem xét bản thảo Chapter Brief tại [briefs/chapter_07_brief.md](file:///d:/Games/Server%20Client/Server%20KT/Ki%E1%BA%BFm%20Th%E1%BA%BF%202/Server/du-long-giac-2/briefs/chapter_07_brief.md) và có thể:
- Phản hồi: **`"Duyệt brief chương 07, tiến hành chấp bút"`** để Agent chuyển sang giai đoạn soạn thảo bản thảo (Drafting).
- Hoặc yêu cầu bổ sung, tinh chỉnh bất kỳ tình tiết/nhân vật nào theo ý đồ nghệ thuật của Tác giả.


