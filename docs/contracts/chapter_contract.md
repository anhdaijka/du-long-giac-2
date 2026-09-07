# HỢP ĐỒNG CHƯƠNG TRUYỆN (ICHAPTERCONTRACT SPECIFICATION)

> **Mục đích (LSP & ISP)**: Mọi chương trong dự án (Core Plot, Living Lore, Mystery Lore, Road Novel) đều bắt buộc phải tuân thủ và triển khai đầy đủ hợp đồng này. Không có ngoại lệ nào được miễn trừ kiểm định.

---

## 1. YAML FRONTMATTER SCHEMA
Mỗi tệp chương (`chapters/chapter_XX.md`) bắt buộc phải mở đầu bằng khối YAML chính xác:

```yaml
---
number: <int: Số thứ tự chương, vd: 1>
title: "<string: Tên chương theo phong cách cổ phong Kim Dung, vd: Rượu Nếp Giang Tân>"
pov: "<string: Tên nhân vật trung tâm góc nhìn, vd: Tiêu Phùng>"
status: "draft" | "review" | "approved"
date: "<string: Mốc thời gian bối cảnh năm 1191, vd: 1191-08-15>"
location: "<string: Địa danh chuẩn xác trong game, vd: Giang Tân Thôn>"
arc: "<string: Tên Arc tương ứng, vd: Arc 00: Tân Thủ Thôn>"
word_count: <int: Dung lượng thực tế sau khi viết, vd: 4250>
provenance: "KT2 Engine Task [ID] (Subtask [ID]: [Tên Subtask Gốc]) | File XML [Tên File]"
---
```

---

## 2. QUY CHUẨN DUNG LƯỢNG VÀNG (WORD COUNT BAND)
- **Mục tiêu chuẩn mực (Target Band)**: **4.000 – 4.800 từ**.
- **Sàn cứng (Hard Floor)**: **3.500 từ** (Bản thảo dưới 3.500 từ sẽ bị đánh trượt tại Gate E vì thiếu chiều sâu giác quan/chi tiết dân sinh).
- **Trần mềm (Soft Ceiling)**: **5.200 từ** (Nếu một phân cảnh tự nhiên vượt quá 5.200 từ, bắt buộc phải tách thành 2 chương độc lập có điểm ngắt dramatic hook tự nhiên).

---

## 3. TIÊU CHUẨN THẨM ĐỊNH BẮT BUỘC (VERIFICATION GATES)
Mỗi chương trước khi trình duyệt Tác giả phải vượt qua:
1. `npm run lint:prose` $\rightarrow$ 0 lỗi vi phạm (sạch hoàn toàn 7 nhóm sạn AI).
2. Thẩm định độc lập 5 Cổng duyệt (Gate A $\rightarrow$ Gate E) theo `.agents/rules/05-review.md`.
3. Có mã `provenance` hợp lệ trỏ về SQLite theo `.agents/rules/10-provenance-kernel.md`.
