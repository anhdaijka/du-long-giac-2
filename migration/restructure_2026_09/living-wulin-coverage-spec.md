# Spec đề xuất — Living Wulin & toàn cảnh sự kiện game

Trạng thái: `AUTHOR APPROVED — LWCQ-01–04 / IMPLEMENTATION AUTHORIZED`.

Tác giả đã trả lời “theo đề xuất” cho cả LWCQ-01–04. Quyền này mở bảng bao phủ sơ bộ rồi pilot Quyển I theo RABQ đã duyệt; nhân vật huyền thoại mới và Bridge bền vững vẫn được trình riêng.

## 1. Restate Brief

Tiểu thuyết cần giữ ba nhân vật chính làm trục cảm xúc nhưng không được tạo ảo giác rằng toàn bộ thiên hạ chỉ vận hành khi họ xuất hiện. Độc giả phải nhận biết các biến cố chính trị, môn phái, truyền thừa, địa phương và lịch sử võ lâm nằm ngoài tầm tham dự trực tiếp của Tiêu Phùng, Tĩnh Xuyên và Hạ Nương.

Mục tiêu không phải biến 465 task thành 465 cảnh. Mục tiêu là **100% source content được phân loại**, mọi event-family có quyết định sử dụng hoặc loại bỏ có lý do, và mọi biến cố quan trọng có dấu chân đủ để độc giả hiểu nó đã xảy ra, ai trả giá và nó đổi thế giới thế nào.

## 2. Kết luận thiết kế

**Có, cần thêm một phương án bên cạnh ba Route Arc Bible.**

Kiến trúc nên có hai trục giao nhau bằng `event_family_id`:

1. **Character Spine:** ba Route Arc Bible giữ lựa chọn, biến đổi và hậu quả riêng của ba POV chính.
2. **World Spine:** một World Event Coverage Ledger theo dõi toàn bộ task/event-family và cách mỗi sự kiện đi vào nhận thức độc giả.

Nhờ vậy, “ai thực hiện nhiệm vụ” và “độc giả biết sự kiện” trở thành hai câu hỏi khác nhau. Bộ ba không cần có mặt tại triều đình, mọi môn phái hay mọi truyền thừa để thế giới ấy hiện hữu.

## 3. Các kênh đưa sự kiện đến độc giả

Mỗi event-family chọn một kênh chính và tối đa các kênh phụ có chức năng rõ:

| Mã | Kênh | Khi dùng |
| --- | --- | --- |
| `DIRECT_TRIO` | Một POV chính trực tiếp trải qua | Sự kiện buộc nhân vật chính lựa chọn hoặc đổi trạng thái bền vững |
| `SATELLITE_POV` | Interlude giới hạn qua nhân vật phụ | Sự kiện quan trọng nhưng không ai trong bộ ba có thể hiện diện hợp lý |
| `WITNESS_RELAY` | Nhân chứng, sứ giả, thương nhân, binh sĩ, đệ tử kể lại | Cần truyền kinh nghiệm người thật và giữ độ lệch nhận thức |
| `DOCUMENT_TRACE` | Thư, mật báo, cáo thị, gia phả, quân báo, y án | Chính trị/tình báo cần provenance hoặc nhiều bản kể đối nghịch |
| `AFTERMATH` | Bộ ba đi qua hậu quả thay vì sự kiện gốc | Cần cho thấy giá người, tổn thất, thay đổi địa phương hay tổ chức |
| `LIVING_LORE` | Phong tục, quán rượu, truyền khẩu, nghề nghiệp, vật dụng | Task nhỏ có giá trị làm dày thế giới nhưng không đủ sức thành plot |
| `LEGENDARY_ECHO` | Di vật, chiêu thức, môn quy, bia ký và lời kể mâu thuẫn | Nhân vật quá khứ tác động hiện tại dù không xuất hiện |
| `EXCLUDE_GAMEPLAY` | Loại khỏi truyện, giữ lý do | Loop, daily, level variant, tutorial hoặc nội dung làm loãng tiểu thuyết |

Không dùng relay như đoạn thuyết minh tiện lợi. Một kênh chỉ hợp lệ khi nó làm thay đổi quyết định, quan hệ, rủi ro hoặc cách hiểu của ít nhất một nhân vật đang sống.

## 4. Dấu chân ba tầng của biến cố lớn

Event-family cấp cao nên có đủ ba tầng, dù không cần cảnh trực tiếp:

1. **Tiền chấn:** dấu hiệu, lời đồn, giá hàng, điều quân, người mất tích hoặc môn quy thay đổi.
2. **Nhân chứng:** một góc nhìn trực tiếp, tài liệu hoặc lời kể có giới hạn và độ tin cậy xác định.
3. **Dư chấn:** thương vong, dòng người, tranh chấp kế vị, biến đổi địa bàn hoặc lựa chọn mới của bộ ba.

Cấu trúc này giúp độc giả hiểu toàn bộ causal footprint mà không biến nhân vật chính thành avatar làm mọi quest.

## 5. Tầng nhân vật

| Tầng | Vai trò | Quyền POV |
| --- | --- | --- |
| `S — CORE TRIO` | Tiêu Phùng, Tĩnh Xuyên, Hạ Nương | POV chính xuyên series |
| `A — SATELLITE` | Nhân vật source có stake riêng và hậu quả bền vững | Được interlude giới hạn khi qua đủ tiêu chí |
| `B — RELAY` | Sứ giả, quân sĩ, đệ tử, thương nhân, y giả, dân địa phương | Truyền dấu vết; thường không mở POV độc lập |
| `C — LOCAL` | Nhân vật một sự kiện hoặc sinh hoạt | Làm living lore; không kéo thành tuyến nếu không có causal return |
| `L — LEGENDARY SHADOW` | Nhân vật quá khứ vắng mặt nhưng để lại truyền thừa và tranh luận | Hiện qua dấu tích và lời kể bất toàn, không dùng POV toàn tri |

Ưu tiên NPC/lore đã có trong game. Nhân vật mới chỉ được tạo khi source có khoảng trống chức năng thật sự và phải đi qua `BRIDGE-CANDIDATE`.

## 6. Chính sách Satellite POV

Một interlude nhân vật phụ chỉ được dùng khi đồng thời thỏa các điều kiện:

- biến cố không thể truyền đạt trung thực chỉ bằng aftermath hoặc thư tín;
- nhân vật phụ có mong muốn, lựa chọn và cái giá riêng, không phải camera biết tuốt;
- cảnh cung cấp thông tin/cảm xúc mà ba POV chính không thể sở hữu hợp lý;
- cảnh để lại causal return trong thế giới hoặc route chính;
- kiến thức của POV không vượt quá điều nhân vật thực sự có thể biết;
- provenance của event và mọi bridge đều được ghi rõ.

Không khóa quota chương interlude. Chất lượng và chức năng quyết định số lượng, không phải tỷ lệ cơ học.

## 7. “Bóng huyền thoại” thay vì sao chép nhân vật có sẵn

Có thể tạo một hoặc vài nhân vật mang **chức năng kiến trúc** tương tự mẫu “cao thủ vắng mặt nhưng bóng phủ lên nhiều thế hệ”, nhưng không sao chép Độc Cô Cầu Bại, tiểu sử, võ công hay giọng văn của Kim Dung.

Một `LEGENDARY SHADOW` hợp lệ phải:

- mọc từ hạt giống game: tên NPC, binh khí, Tàng Kiếm, môn quy, bia ký, ký ức hoặc mâu thuẫn truyền thừa;
- được biết qua nhiều nguồn không hoàn toàn thống nhất;
- tác động đến ít nhất hai tổ chức/thế hệ bằng hậu quả cụ thể;
- biểu hiện một câu hỏi tư tưởng, không chỉ “võ công mạnh nhất”;
- không xuất hiện để cứu cao trào, giải Du Long Giác hoặc trao sức mạnh miễn phí;
- có proposal riêng và cần Tác giả duyệt trước khi trở thành planning authority.

Task 197–202 là vùng nguồn đáng khảo sát cho chức năng này: Task 197 nói Long Ngũ kể về mười hai chưởng môn dựng Tàng Kiếm Sơn Trang và thờ các anh hùng; Tasks 198–202 tiếp tục các nhánh Ma Nữ, Long Thương, Cửu Tuyệt, Tôn Sư và Chuyện Cũ Giang Hồ. Đây mới là **hạt giống khảo sát**, chưa chứng minh một nhân vật huyền thoại duy nhất.

## 8. Áp dụng sơ bộ vào các cụm nguồn hiện có

### Gia Vương–Triệu Khoách và chính trị triều đình

Tasks 231–242 chứa Gia Vương/Ninh Tông, Chu Hy, Triệu Nhữ Nhu, Hàn Thác Trụ và Khánh Nguyên. Không nên biến thành chuỗi việc vặt của bộ ba. Hướng phù hợp là `SATELLITE_POV + DOCUMENT_TRACE + AFTERMATH`: một người trong bộ máy hoặc nhân chứng có stake riêng, các mật báo/chiếu biểu có giới hạn, rồi hậu quả rơi xuống quân doanh và dân gian. Tất cả nhân vật lịch sử vẫn phải tách `GAME FACT/GAME ALT-HISTORY` khỏi `HISTORICAL FACT`.

### Nội bộ các môn phái

Tasks 203–214 và các family 383–441 là route song song/gameplay scaffolding. Ledger phải phân loại đủ cả family, nhưng tiểu thuyết chỉ chọn các representative có xung đột tổ chức thật. Dùng source NPC làm `SATELLITE` hoặc `RELAY`; bộ ba chỉ tham gia nhánh thuộc quyền sở hữu route đã duyệt.

### Chuyện Cũ Thần Châu/Tàng Kiếm

Task 197 phù hợp với `WITNESS_RELAY + LEGENDARY_ECHO`: lời Long Ngũ là một nguồn kể, Tàng Kiếm/di vật là dấu tích kiểm chứng, còn Tasks 198–202 có thể cho các cách hiểu cạnh tranh. Không dùng một đoạn hồi cố toàn tri để tuyên bố mọi truyền thuyết đều đúng.

### Truyện địa phương và task lặp

Các vignette có thể trở thành `LIVING_LORE`, `AFTERMATH` hoặc một local return; repeat/daily/level variants được gom thành event-family, không tái diễn như nhiều biến cố. Nội dung không đủ giá trị vẫn được ghi `EXCLUDE_GAMEPLAY` kèm lý do, nên không “biến mất” khỏi quá trình chuyển thể.

## 9. Những phẩm chất nên học ở tầm vóc tiểu thuyết võ hiệp lớn

Học nguyên lý, không bắt chước câu chữ hay sao chép nhân vật:

- thế giới có lịch sử và vận động độc lập với nhân vật chính;
- nhân vật phụ có ham muốn, sai lầm, lòng trung thành và kết cục của riêng họ;
- đại sự lịch sử đi vào truyện qua số phận cá nhân, không qua bài giảng;
- võ học mang tiểu sử, triết lý và cái giá đạo đức của người sử dụng;
- tin đồn và tri thức bất đối xứng tạo giang hồ nhiều tầng sự thật;
- địa lý, ẩm thực, nghề nghiệp, phong tục và tiếng nói địa phương tạo cảm giác “đất có người sống”;
- hài–bi, tình–nghĩa, gia–quốc và cá nhân–đại cục va vào nhau bằng lựa chọn;
- nhân vật/sự kiện đã gieo cần có causal return, không chỉ cameo để khoe kho dữ liệu.

## 10. Các đề xuất đã được duyệt — Living Wulin Coverage Gate

### LWCQ-01 — kiến trúc hai trục

**Đề xuất:** duyệt `Character Spine + World Spine`; “tận dụng toàn bộ source” được hiểu là 100% task/event-family có disposition, không phải 100% được dựng thành cảnh.

### LWCQ-02 — Satellite POV

**Đề xuất:** cho phép interlude giới hạn từ nhân vật phụ, ưu tiên NPC game, theo sáu tiêu chí ở mục 6; không khóa quota cứng.

### LWCQ-03 — Legendary Shadow

**Đề xuất:** cho phép đề xuất nhân vật huyền thoại nguyên bản mọc từ hạt giống game, nhưng mỗi nhân vật phải có hồ sơ provenance và cổng duyệt riêng; mặc định hiện diện qua dấu tích, không làm POV toàn tri hay deus ex machina.

### LWCQ-04 — thứ tự triển khai

**Đề xuất:** trước pilot Route Bible Quyển I, dựng một World Event Coverage Ledger sơ bộ cho đủ 465 task, gom các variant thành event-family và gán coverage tier/kênh. Sau đó pilot Quyển I đọc ledger này làm đầu vào; các quyển sau tiếp tục tinh chỉnh, không cần khóa scene sớm.

## 11. Approval Gate

LWCQ-01–04 đã được duyệt. Triển khai World Event Coverage Ledger sơ bộ cho đủ task trước, rồi pilot Route Bible Quyển I. Satellite POV cụ thể phải thỏa mục 6; Legendary Shadow có thể được đề xuất nhưng chưa được canon hóa nếu thiếu phê duyệt hồ sơ riêng.
