# Rule 10: Source Provenance Kernel (Nhân Kiểm Chứng Nguồn Gốc)

> **Trách nhiệm duy nhất (Single Responsibility)**: Thiết lập kỷ luật truy vết nguồn gốc 100% bất di bất dịch, bảo đảm mọi tình tiết, nhân vật, địa danh và sự kiện đều có căn cứ xác thực từ database Kiếm Thế 2 (`story_database.sqlite3`).
> **Nguyên tắc cốt lõi: "Không tra source, không hạ bút. Tuyệt đối không bịa đặt, không suy diễn hợp lý hóa."**

---

## 1. NGUYÊN TẮC BẤT BIẾN (ZERO-FABRICATION INVARIANT)

1. **Bắt nguồn 100% từ Database**:
   - Mọi chương truyện (dù là Core Plot, Living Lore, Mystery Lore, Military Lore hay Road Novel) đều **BẮT BUỘC** phải bắt nguồn từ các nhiệm vụ, phụ tuyến, quân doanh, dã luyện hoặc kịch bản có thật trong database Kiếm Thế 2:
     - `migration/source_corpus/01_Database/story_database.sqlite3`
     - `migration/source_corpus/02_Narrative_Book/`
     - Source XML: `D:\Games\Server Client\Server KT\Stories\task_publish\sub\`
   - Tuyệt đối cấm Agent tự ý tạo ra nhiệm vụ không tồn tại hoặc dùng tên chương bay bướm mơ hồ để che giấu tình tiết tự chế.

2. **Ranh giới giữa "Văn học hóa" và "Bịa đặt cốt truyện"**:
   - **Được phép (Văn học hóa)**: Miêu tả cảm giác giác quan (mùi rượu, gió lạnh, ánh mắt), đào sâu tâm lý nhân vật theo lăng kính ngôi thứ ba hạn tri, đối thoại đời thường đốp chát (chuẩn Kim Dung + Châu Tinh Trì + Gintama) dựa trên khung cốt truyện game.
   - **Nghiêm cấm tuyệt đối (Bịa đặt cốt truyện)**: Tự nghĩ ra một vụ án không có trong game, tự gán ghép quan hệ sư đồ/huyết thống trái ngược với SQLite, tự ý cho nhân vật học những võ công chưa từng có căn cứ ở thời điểm đó.

3. **Phân biệt rạch ròi giữa Sự thật (Fact) và Lời khai phiến diện của NPC**:
   - **Fact**: Sự thật khách quan đã được chứng minh qua chuỗi hành động và cốt lõi kịch bản.
   - **Tin đồn / Nghi ngờ / Bẫy hãm hại**: Lời khai của kẻ thù bị tra tấn, cáo buộc một chiều từ một phe phái (ví dụ: Lời thích khách vu cáo Cầu Chỉ Thủy thông đồng Thiên Nhẫn Giáo). Không được lấy lời vu cáo làm chân lý khách quan của thế giới truyện.

---

## 2. GIAO THỨC TRUY VẤN & KHÓA MÃ NGUỒN (PROVENANCE PROTOCOL)

Trước khi lập kế hoạch (Plan) hoặc chấp bút (Draft) bất kỳ chương nào:

### Bước 1: Truy vấn SQLite Database Bắt Buộc
Agent phải chạy truy vấn trực tiếp vào `migration/source_corpus/01_Database/story_database.sqlite3`:
- Xác định rõ: `task_id`, `sub_id`, `name`, `describe_cleaned`, `dialog_npc_name`, `dialogues`.
- Đối soát đối thoại NPC, địa danh và sự kiện nguyên bản của Kingsoft/VNG.

### Bước 2: Khóa Nguồn trong YAML Frontmatter
Mọi tệp chương `.md` bắt buộc phải khai báo trường `provenance` hợp lệ theo hợp đồng `docs/contracts/chapter_contract.md`:
```yaml
provenance: "KT2 Engine Task [ID] (Subtask [ID]: [Tên Subtask Gốc]) | File XML [Tên File]"
```

---

## 3. CHẾ TÀI KIỂM SOÁT
- Bất kỳ chương bản thảo nào thiếu mã `provenance` hoặc trỏ về một Subtask không tồn tại trong SQLite sẽ bị **ĐÁNH TRƯỢT NGAY LẬP TỨC TẠI GATE A (MINIMAL HARD REGRESSION)** của quy trình Review và bắt buộc phải viết lại.
