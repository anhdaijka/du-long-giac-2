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
- **Hồi vừa hoàn thành**: **Chương 01: *Rượu Nếp Giang Tân*** (`chapters/chapter_01.md`).
  - Trạng thái: **ĐÃ ĐƯỢC TÁC GIẢ DUYỆT & CANON HÓA THÀNH CÔNG**.
  - Sổ cái trạng thái: Đã cập nhật `revisions/chapter_01_canon_diff.md` và `characters/tieu_phung.md`.
  - POV: Tiêu Phùng (17 tuổi).
  - Dung lượng: **4.382 từ** (Pass trọn vẹn dải vàng và 5 Cổng duyệt).

## 2. Nhiệm vụ tiếp theo (Next Action)

- **TUÂN THỦ 100% QUY TRÌNH NOVEL-OS**:
  - Soạn thảo bản Kế hoạch chương chi tiết: **`briefs/chapter_02_brief.md`** cho **Chương 02: *Chiến Thuyền Tỷ Võ*** (POV Tĩnh Xuyên, Thanh Loa Đảo Thiên Vương Bang, Task 1 Subtask 1 *Anh Cô Trở Về*).
  - **DỪNG LẠI và trình Brief cho Tác giả duyệt**.
  - Tuyệt đối không nhảy cóc viết draft cho đến khi Tác giả phê duyệt Brief!

## 3. Gợi ý hành động nhanh (Suggested Next Step)

Tác giả chỉ cần gõ:
- `"Lên brief chương 2"` để Agent soạn thảo bản đặc tả `briefs/chapter_02_brief.md` trình Tác giả thẩm duyệt!


