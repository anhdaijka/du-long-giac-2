# Ghi chú biên tập — bảng bao phủ sơ bộ

`PRELIMINARY EDITORIAL CANDIDATES / NOT CANON`.

## Độ phủ và bằng chứng

465/465 là độ phủ hàng task; 390 nhóm lưu trữ giữ mọi member và query/result. 27 nhóm nhiều task gồm nhánh giới tính, cổng xuất hành, các chế độ lặp và 12 bộ tuyến môn phái. Nhóm môn phái chứa nhiều giai đoạn khác nhau; không được gọi là một event được lặp lại.

Mỗi dòng ledger trỏ packet, JSON pointer, task và subtask. Packet lưu query template, bind và kết quả nguyên văn cả steps/dialogues. `build_world_coverage.py --check` tái chạy toàn bộ query read-only rồi so kết quả, nên bắt được packet bị sửa, thiếu task hoặc stale source. Việc phân loại là first-pass từ survey/metadata, chưa phải kiểm chứng ngữ nghĩa sâu cho 465 task.

Các task B/C đang được giữ làm kho ứng viên. Chưa chọn đưa một nhiệm vụ thành cảnh không có nghĩa bị bác bỏ. Một task A cũng có thể được kể qua nhiều người ngoài trio. Không khóa số lượng scene từ thống kê này.

## Ba vùng cần ưu tiên

### Triều chính/Gia Vương

Nguồn: `source-graph.md` PM-02 và packet `arc_08.json`, task 232–242 (query `task` bind từng ID, rồi `subtasks/steps/dialogues` theo ID trả về).

Đề xuất giữ các nhân vật trong triều và bang phái làm người thực hiện sự kiện. Văn kiện/nhân chứng đưa phần công khai đến độc giả; satellite chỉ mở khi có sự lựa chọn riêng đáng kể. Ai biết âm mưu, biết lúc nào và có nói thật không phải được đọc theo từng lời. Không gán toàn bộ cho Tĩnh Xuyên chỉ vì chàng có tuyến tình báo.

Chuỗi chính trị còn rải ngoài 232–242: Task 13, 106–109, 117, 128, 156 cần đọc liên hệ với Gia Vương và hậu quả kế vị; đây là danh sách khảo sát, chưa là một chronology hợp nhất. Kênh đầu tiên trong ledger có thể thay đổi sau khi đọc sâu. Tên lịch sử trong game chưa là historical fact.

### Chuyện Cũ Thần Châu/Tàng Kiếm

Nguồn: packet `arc_07.json`, task 197–202; Task 197/sub360 `describe_cleaned` đặt lời kể trong sự truyền đạt của Long Ngũ, chỉ dẫn đến Kiếm Nô. Sáu task giữ sáu family riêng vì chung bối cảnh chưa chứng minh cùng một biến cố.

Đề xuất bảo toàn các chuyện đời và danh tiếng có sẵn trước khi sáng tạo huyền thoại mới. Hình thức LEGENDARY_ECHO chỉ là kênh kể; không chứng minh mọi điều được kể là thật. Chưa tạo nhân vật hợp nhất Ma Nữ–Long Thương–Cửu Tuyệt–Tôn Sư.

### Nội bộ môn phái và lao động

Family EF-SECT-01 đến EF-SECT-12 gom theo tên phái ghi trực tiếp ở source title, không theo vị trí mảng: thứ tự các phái ở nhóm kỹ năng 110 khác nhóm cấp 20/30/40. Phải giữ từng giai đoạn, cổng vào, người giao và outcome riêng.

Task 192 (`arc_07.json`, task.describe_cleaned) nói tới sản xuất tơ và thêu thùa tái thiết Thúy Yên. Đây là ví dụ repeat=1 vẫn có giá trị xã hội. Truyện có thể cho đệ tử và người thợ tự tổ chức công việc; Hạ Nương tiếp xúc với hậu quả và sự giới hạn nguồn lực. Trước khi thành cảnh, phải định người làm, thời điểm và giá trị nghề nghiệp từ evidence.

## Giới hạn của pilot Quyển I

Task 1/sub8/step41 dẫn trực tiếp tới La Phong; Task 2/sub9/steps43–44 giả định cùng avatar từng ở Thiên Vương và mang hai lá thư. Step43 còn nói thư yêu cầu người đưa thư lưu lại Cái Bang rèn luyện. PB-01 đã được duyệt qua V1PQ-01 ngày 2026-09-09: Tĩnh Xuyên mang thư, bỏ riêng điều khoản lưu lại trong chuyển thể; Tiêu Phùng đến qua đầu mối khác. Source không đổi; chi tiết chuyển tin/hành trình chưa chọn. Không thể đổi tên avatar hàng loạt.

Task 2/sub13 yêu cầu avatar hạ Thôi Xuất Trần; subs15–24 chứa huấn luyện Ảnh Xã và các bước phát triển sau đó. Tiêu Phùng đầu truyện không tự được thừa hưởng năng lực này. PB-03 đã được duyệt hướng chuyển vai trận đấu nhưng chưa chọn người thay; phần sau vẫn deferred, không xóa khỏi ledger.

Task 12/sub90 tự nêu phu phụ Đường Nhất Trần đến hỗ trợ. Đó là chỗ nguồn đã cho cao thủ có vai trò độc lập; phân phần cứu người cho Hạ Nương không nên khiến nàng chiếm toàn bộ chiến công. Việc đổi người thực hiện một đòn cụ thể vẫn cần Bridge.

Task 157/sub320/step1432 dẫn về sub312 (hex138); sub309 dẫn chuyện Hứa Sĩ Vĩ. Thứ tự số subtask không phải thứ tự kể. Sub320 mô tả nguy cơ thủy lưu khác sắc thái lời Thu Di trong step1432: phải giữ nguy cơ và lời báo, chưa tự khóa thôn đã bị ngập hoặc số nạn nhân.

## Công việc nguồn còn mở

- Đọc sâu mỗi family trước khi chọn scene/representative; đối chiếu điều kiện XML khi packet chỉ lưu lời dẫn.
- Task 288 thiếu subtask; chưa được thêm sự kiện hoàn thành.
- Kiểm kê các bảng nguồn ngoài tasks là công việc riêng trong chiến lược tận dụng tài nguyên game; đợt này không tuyên bố hoàn tất.
- Các Foundation khác vẫn còn cần audit claim toàn repository; bảng này không thay thế audit đó.
