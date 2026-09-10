# HỢP ĐỒNG CHUYỂN THỂ NGUỒN (ADAPTATION CONTRACT)
## Dự án: ĐẠI TIỂU THUYẾT VÕ LÂM KIẾM THẾ (DU LONG GIÁC)
**Trạng thái:** ĐÃ ĐƯỢC TÁC GIẢ PHÊ DUYỆT (AUTHOR APPROVED)  
**Căn cứ nguồn gốc:** Kho dữ liệu nguyên bản Kiếm Thế 2 tại `migration/source_corpus/`  
**Ngày hiệu lực:** 07/09/2026

---

## 1. THẨM QUYỀN NGUỒN GỐC (SOURCE AUTHORITY)
1. **Kho ngữ liệu nguồn tối cao**:
   - `migration/source_corpus/01_Database/story_database.sqlite3`
   - Bảng nhiệm vụ: 465 Tasks, 657 Subtasks (XMLs nguyên bản).
   - Bảng đối thoại: 720 thoại thế giới, 30 thành thị, 4 đại quân doanh, 12 môn phái.
   - Bảng kiểm định: `provenance_manifest.json` (SHA-256 cryptographic hashes).
2. **Nguyên tắc bất di bất dịch**:
   - Kho dữ liệu SQLite là bằng chứng lịch sử (evidence), không copy bừa bãi toàn bộ hàng vạn dòng vào Story Skills.
   - Khi cần sự kiện hay câu thoại của bất kỳ NPC nào, Agent tra cứu O(1) qua SQL từ database này.

---

## 2. CHÍNH SÁCH DÒNG THỜI GIAN SONG HÀNH (PARALLEL SYNCHRONOUS TIMELINE)
Toàn bộ câu chuyện bắt đầu **cùng một thời điểm lịch sử: Mùa thu năm 1191 (Thuần Hi thập bát niên)** tại 3 địa bàn độc lập:

```
NĂM 1191 (MÙA THU) ────────────────────────────────────────────────────────► ĐÔNG 1191
[TUYẾN 1 - TIÊU PHÙNG (17t)]
Giang Tân Thôn (Việc vặt làng chài) ──► Đêm mưa vỡ đê ──► Thích khách đoạt Vô Danh Mật Tịch ─┐
                                                                                               │
[TUYẾN 2 - TĨNH XUYÊN (18t)]                                                                   ├─► GIAO CẮT TẤT YẾU
Thanh Loa Đảo (Thiên Vương Bang)   ──► Phò tá Dương Thiết Tâm ──► Tứ Diện Sở Ca / Mộc Nhất Lâu─┤   TẠI BIẾN CỐ
                                                                                               │   BA LĂNG HUYỆN
[TUYẾN 3 - HẠ NƯƠNG (16t)]                                                                     │
Điền Trì (Thúy Yên Môn)            ──► Huyết kiếp Bách Hoa Trận ──► Xuống núi tìm độc dược ───┘
```

- Không nhân vật nào vào giang hồ chậm trễ; ba tuyến vận hành song song và chỉ va vào nhau khi các luồng điều tra nhiệm vụ giao cắt tại Động Đình Hồ.

---

## 3. CHÍNH SÁCH BỘ BA NHÂN VẬT CHÍNH (CORE PROTAGONISTS CANON)

### A. TIÊU PHÙNG (17 tuổi khởi điểm) — Lăng kính Hiệp sĩ Áo vải
- **Thân thế & Địa bàn**: Giang Tân Thôn (Ba Lăng Huyện). Mồ côi sau thảm sát Ma Y Cốc (1174), được Bạch Thu Lâm (Thu Di) nuôi nấng. Huyết mạch hoàng tộc Nam Chiếu bị chàng cự tuyệt để sống đời áo vải bãi sậy.
- **Tính cách & Khẩu khí**: Hài hước, bắng nhắng, châm biếm, tự trào, tinh quái; thích uống rượu, tính tình ồn ào và hơi tự mãn kiểu thanh niên bãi sậy, hay dùng lời trêu chọc bỡn cợt để châm chọc thói đạo đức giả của bọn quan quyền và che giấu nỗi mặc cảm ăn bám mồ côi.
- **Tuyến nhiệm vụ gắn liền**: Task Arc 00 (Giang Hồ Sơ Thính) & Arc 01 (Ba Lăng Phong Vân).
- **Võ học & Triết lý**: Đoản côn gỗ nghiến, Túy Bộ bến sông; bái nhập Cái Bang học bổng pháp và *Kháng Long Hữu Hối* (phát 7 thu 3, Kinh Dịch) từ Thạch Hiên Viên.
- **Khiếm khuyết cốt tử**: Nghiện ôm hết trách nhiệm và hiểm nguy, tự làm rạn nứt kinh mạch (`Burden -> Self-erasure`).

### B. TĨNH XUYÊN (20 tuổi khởi điểm) — Lăng kính Kỷ luật Sa trường
- **Thân thế & Địa bàn**: Thanh Loa Đảo (Thiên Vương Bang). Con trai dũng tướng Tĩnh Hùng hy sinh năm 1181; 10 năm phụng dưỡng người mẹ mù Diệp Mẫu.
- **Tuyến nhiệm vụ gắn liền**:
  - Task `0000000000000001` (*Tứ Diện Sở Ca*): Được Tân Bang chủ Dương Thiết Tâm cất nhắc làm tướng tiên phong hộ tống Hàn Thác Trụ và giải vây Đại Mãnh Chủy.
  - Task `0000000000000005` (Subtask 27–38): Mang thân phận gián điệp **Mộc Nhất Lâu** thâm nhập Ngũ Độc Giáo.
- **Bi kịch cốt tử**: Ân Đồng trao trọn tình yêu cho Mộc Nhất Lâu; nhưng vì bí mật quân cơ đại cục, Tĩnh Xuyên buộc phải hạ sát nàng (Subtask 37 kịch bản gốc: *"Ân Đồng đã chết dưới tay người mình yêu... nàng nói cho dù huynh không ra tay, muội cũng không bao giờ tiết lộ bí mật này"*). Kỷ vật túi thổ cẩm uyên ương cài trước ngực là bản án lương tâm theo chàng suốt đời.
- **Võ học & Triết lý**: Dương Gia Thương Pháp & Bôn Lôi Toàn Long Thương.
- **Khiếm khuyết cốt tử**: Lấy danh nghĩa đại cục để độc đoán phán xét và áp đặt (`Accountability -> Decision entitlement`).

### C. HẠ NƯƠNG (16 tuổi khởi điểm) — Lăng kính Y đạo Thực chứng
- **Thân thế & Địa bàn**: Điền Trì (Thúy Yên Môn). Con gái y quán Đại Lý, nữ đệ tử y quán Thúy Yên dưới thời Chưởng môn Doãn Hàm Yên / Doãn Tiêu Vũ.
- **Tuyến nhiệm vụ gắn liền**: Task `000000000000000C` (*Huyết Quang Tai*): Trực tiếp đối mặt với cảnh hoang tàn của Huyết kiếp Bách Hoa Trận, cứu thương cho hơn 100 sư tỷ muội thương vong sau khi thích khách đột nhập cướp Du Long Giác.
- **Võ học & Triết lý**: Băng Tâm Kiếm Pháp đưa giải phẫu huyệt vị vào thực chiến; Băng Phách Hàn Châm (nhất châm định sinh tử).
- **Khiếm khuyết cốt tử**: Lòng trắc ẩn cứu chữa biến thành ham muốn kiểm soát đối phương (`Care -> Control`).

---

## 4. MA TRẬN CHUYỂN ĐỔI CƠ CHẾ GAME SANG TIỂU THUYẾT (MECHANIC TRANSLATION)

| Cơ chế Game | Chuyển đổi sang Tiểu thuyết |
| :--- | :--- |
| **Đánh N con quái** | Nén thành 1 trận đấu kịch chiến sinh tử, phục kích địa hình hiểm, hoặc một trận đấu trí võ học. |
| **Thu thập N vật phẩm** | Chuyển thành quá trình trinh sát, giải mã dấu vết hiện trường, tìm kiếm manh mối độc dược, phẫu thuật dã chiến. |
| **Cửa ải cấp độ (Level gate)** | Chuyển thành thời gian bế quan dưỡng thương, tu luyện nội công, thay đổi theo mùa, hoặc chờ đợi thời cơ chính trị. |
| **Xa phu / Dịch chuyển bản đồ** | Miêu tả hành trình cưỡi ngựa, chèo thuyền vượt sóng Động Đình, phong thổ sơn thủy giang hồ chân thực. |
| **Nhiệm vụ lặp lại (Daily / Grind)** | Loại bỏ hoàn toàn; chỉ giữ lại những sự kiện có tác động nhân quả tới cốt truyện và biến đổi tâm lý nhân vật. |

---

## 5. PHÂN ĐỊNH 3 NHÃN ĐỘ TIN CẬY (FIDELITY CLASSES)

1. **`DIRECT CANON`**:
   - Các dữ kiện có nguồn gốc 100% trong database Kiếm Thế 2 (Dương Thiết Tâm nhận chức bang chủ, Huyết kiếp Bách Hoa Trận, mật lệnh Mộc Nhất Lâu và cái chết của Ân Đồng trong Subtask 37, Bạch Thu Lâm lãnh đạo nghĩa quân).
2. **`SOURCE-SUPPORTED INFERENCE`**:
   - Suy luận logic từ chuỗi nhiệm vụ và bối cảnh lịch sử Nam Tống - Kim (khoảng cách phi ngựa giữa Ba Lăng và Lâm An, âm mưu của Hàn Thác Trụ, mâu thuẫn giữa Tống triều và Ngũ Độc Giáo).
3. **`NOVELIZATION BRIDGE`**:
   - Các tình tiết nối văn học: độc thoại nội tâm, chi tiết miêu tả thế võ, những cuộc cọ xát đối thoại giữa Tiêu Phùng - Tĩnh Xuyên - Hạ Nương. **Bắt buộc phải được Tác giả phê duyệt trước khi ghi nhận vào Canon tiểu thuyết.**
