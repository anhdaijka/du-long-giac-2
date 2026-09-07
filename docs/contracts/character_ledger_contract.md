# HỢP ĐỒNG HỒ SƠ NHÂN VẬT (ICHARACTERLEDGER SPECIFICATION)

> **Mục đích (SRP & DIP)**: Cung cấp giao diện trừu tượng và cấu trúc dữ liệu chuẩn mực cho toàn bộ hồ sơ nhân vật trong `characters/`. Các Engine (Drafting, Reviewing, Continuity) đối soát trực tiếp vào các trường dữ liệu này mà không cần hardcode tên tuổi hay chiêu thức.

---

## 1. CẤU TRÚC 4 THÀNH PHẦN BẮT BUỘC

Mỗi hồ sơ nhân vật (`characters/<character_id>.md`) bắt buộc phải triển khai 4 thành phần:

### Thành phần 1: Identity & Core Wound (Căn cước & Vết thương cốt tử)
- Tên, tuổi theo timeline (năm 1191), xuất thân, môn phái/địa bàn khởi đầu.
- Vết thương tâm lý sâu sắc nhất (Core Wound / Tragic Flaw) chi phối mọi động cơ hành vi.
- Giọng điệu và khẩu khí đặc trưng (Dialogue cadence & Voice).

### Thành phần 2: Epistemic Ledger (Sổ cái Tri thức Nhân vật)
- **Điều nhân vật ĐÃ BIẾT (Known Facts)**: Căn cứ cụ thể từ những trải nghiệm trong đời thực hoặc vật chứng đã chạm tới.
- **Điều nhân vật CHƯA ĐƯỢC BIẾT (Unknown / Forbidden Secrets)**: Bí mật thân thế, âm mưu đại cục, những sự kiện phương xa chưa xảy ra đối với nhân vật.
- *Nguyên tắc:* Narrative Camera không được phép hé lộ bất kỳ thông tin nào vượt quá phạm vi "Đã biết".

### Thành phần 3: 5-Volume Martial Progression Table (Bảng Tầng Bậc Võ Học 5 Quyển)
- Định nghĩa rõ ràng cho từng Quyển (Volume 1 đến Volume 5):
  - **Binh khí sử dụng (Weapons)**.
  - **Bộ võ công & chiêu thức (Martial Stances & Techniques)**.
  - **Tầng nội kình / thực lực chiến đấu (Inner Force & Combat Power)**.
  - **Cột mốc giác ngộ nhân sinh (Character Arc Breakthrough)**: Nguyên nhân nội tâm dẫn đến sự chuyển hóa võ đạo.
- *Nguyên tắc:* Cấm tuyệt đối nhân vật vượt cấp hoặc sử dụng võ công ngoài tầng quy định.

### Thành phần 4: Interpersonal Dynamics & Durable State (Quan hệ & Trạng thái Bền vững)
- Mối quan hệ và xung đột giá trị với các nhân vật khác.
- Đồ vật bền vững đang sở hữu (durable inventory).
- Thương tật thể xác còn tồn tại (physical scars / injuries).
