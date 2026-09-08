# Đề Xuất Canon Diff: Chương [XX] — [Tiêu Đề Chương]

> **Cơ quan quản lý**: Novel OS State Ledger  
> **Trạng thái**: Chờ Tác giả xem xét và phê chuẩn trước khi commit vào Sổ cái trạng thái bền vững (Cổng Dừng 3).
>
> **Path coverage**: mọi file bền vững thực sự sẽ sửa dưới `characters/`, `worldbuilding/`, hoặc `plot/` phải xuất hiện bằng **đúng repository-relative path** ở ít nhất một `Index:`/section trong Canon Diff này. Không cần lập thêm một sổ danh sách trùng lặp; chỉ cần giữ các `Index:` bên dưới chính xác và bổ sung section cho bất kỳ durable file nào ngoài mẫu.

---

## 1. Tóm Tắt Biến Chuyển Cốt Truyện & Nhân Vật (Narrative Summary)
* **POV**: [Tên nhân vật chính, tuổi, địa bàn]
* **Mốc thời gian**: [YYYY-MM-DD (Thời điểm trong ngày)]
* **Địa điểm**: [Vị trí cụ thể diễn ra biến cố]
* **Biến chuyển cốt lõi**: [Tóm tắt 3-5 gạch đầu dòng các sự kiện bước ngoặt]

---

## 2. Đề Xuất Cập Nhật Sổ Cái Thương Tật (`worldbuilding/medical/injuries_ledger.md`)
*(Ghi nhận mã thương tật mới hoặc cập nhật tiến trình điều trị của các nhân vật tham chiến theo chuẩn L1 - L5)*

```diff
Index: worldbuilding/medical/injuries_ledger.md
===================================================================
--- worldbuilding/medical/injuries_ledger.md
+++ worldbuilding/medical/injuries_ledger.md
@@ -...,... +...,... @@
```

---

## 3. Đề Xuất Cập Nhật Hồ Sơ Nhân Vật Chính & Bản Lề (Protagonists & Anchors)
*(Cập nhật thể trạng, trang bị, tri thức mới vào Section 6/7 Sổ Cái Trạng Thái Bền Vững)*

```diff
Index: characters/[tên_nhân_vật].md
===================================================================
--- characters/[tên_nhân_vật].md
+++ characters/[tên_nhân_vật].md
@@ -...,... +...,... @@
```

---

## 4. Đề Xuất Bổ Sung & Đồng Bộ Danh Bạ Nhân Vật Phụ (`characters/supporting_cast.md`)
*(BẮT BUỘC: Liệt kê tất cả nhân vật Tier B / Tier C mới xuất hiện, hoặc cập nhật trạng thái/thương tật/lần xuất hiện gần nhất của NPC cũ)*

```diff
Index: characters/supporting_cast.md
===================================================================
--- characters/supporting_cast.md
+++ characters/supporting_cast.md
@@ -...,... +...,... @@
```

---

## 5. Đề Xuất Cập Nhật Sổ Cái Bảo Vật & Cơ Quan (`worldbuilding/artifacts/artifacts_ledger.md`)
*(Ghi nhận vị trí, chủ sở hữu, biến đổi vật lý của bảo vật/cơ quan/vật phẩm bền vững)*

```diff
Index: worldbuilding/artifacts/artifacts_ledger.md
===================================================================
--- worldbuilding/artifacts/artifacts_ledger.md
+++ worldbuilding/artifacts/artifacts_ledger.md
@@ -...,... +...,... @@
```

---

## 6. Đề Xuất Cập Nhật Ma Trận Quan Hệ Phe Phái (`worldbuilding/factions/relationships_matrix.md`)
*(Ghi nhận quan hệ ngoại giao, thù địch, biến động thế lực)*

```diff
Index: worldbuilding/factions/relationships_matrix.md
===================================================================
--- worldbuilding/factions/relationships_matrix.md
+++ worldbuilding/factions/relationships_matrix.md
@@ -...,... +...,... @@
```

---

## 7. Đề Xuất Cập Nhật Bảng Theo Dõi Lời Hứa Cốt Truyện (`plot/promises_tracker.md`)
*(Kích hoạt lời hứa mới, nâng cấp lời hứa đang mở, hoặc nghiệm thu payoff)*

```diff
Index: plot/promises_tracker.md
===================================================================
--- plot/promises_tracker.md
+++ plot/promises_tracker.md
@@ -...,... +...,... @@
```

---

## 8. Đề Xuất Cập Nhật Biên Niên Sử & Outline Deck (`plot/timeline.md` & `plot/volume_01_deck.md`)
*(Ghi nhận mốc sự kiện chính xác và đánh dấu trạng thái canon hóa chương)*

```diff
Index: plot/timeline.md
===================================================================
--- plot/timeline.md
+++ plot/timeline.md
@@ -...,... +...,... @@
```

---

## 9. Quyết Định & Chỉ Thị Của Tác Giả (Cổng Dừng Cứng 3)

- [ ] Phê chuẩn toàn văn Đề xuất Canon Diff Chương [XX].
- *(Agent TUYỆT ĐỐI KHÔNG tự ý chỉnh sửa các file sổ cái bền vững trong `characters/`, `worldbuilding/`, `plot/` cho đến khi Tác giả phê chuẩn Diff này!)*
