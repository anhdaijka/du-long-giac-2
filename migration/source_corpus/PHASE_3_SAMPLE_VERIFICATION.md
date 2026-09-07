# BÁO CÁO MẪU KIỂM CHỨNG GIAI ĐOẠN 3: LUA SCRIPTS & NPC THẾ GIỚI (STRICT PROVENANCE)

> Đối chiếu trực tiếp dữ liệu trích xuất từ các file LUA và bảng cấu hình `dialognpc.txt`.

## 1. Mẫu Đối Thoại NPC Thế Giới (Ambient NPCs)

### [Vân Trung Trấn] Lớp NPC: `bingqipulaoban` (Record #1)
- **Nguồn**: `Kiếm Thế 2\Server\Docker_KT2\Kiemthe2-server\gameserver\setting\npc\dialognpc.txt` (Map ID: 1)
- **Lời thoại**: Hi hi! Có vũ khí của ta trong tay, muốn trở thành đệ nhất võ lâm cao thủ dễ như trở bàn tay. Khách quan hãy mua 1 cái đi, sau đó đến chỗ Tạ Hiền mua chiếc phi phong, chắc chắn sẽ rất oai!
- **Các lựa chọn tương tác**: "Vũ Khí","Dialog:OpenShop",388,1, "Khoáng thạch","Dialog:OpenShop",16,1, "Không mua nữa"

---

### [Long Môn Trấn] Lớp NPC: `bingqipulaoban` (Record #2)
- **Nguồn**: `Kiếm Thế 2\Server\Docker_KT2\Kiemthe2-server\gameserver\setting\npc\dialognpc.txt` (Map ID: 2)
- **Lời thoại**: Hi hi! Có vũ khí của ta trong tay, muốn trở thành đệ nhất võ lâm cao thủ dễ như trở bàn tay. Khách quan hãy mua 1 cái đi, sau đó đến chỗ Tạ Hiền mua chiếc phi phong, chắc chắn sẽ rất oai!
- **Các lựa chọn tương tác**: "Vũ Khí","Dialog:OpenShop",388,1, "Khoáng thạch","Dialog:OpenShop",16,1, "Không mua nữa"

---

### [Vĩnh Lạc Trấn] Lớp NPC: `bingqipulaoban` (Record #3)
- **Nguồn**: `Kiếm Thế 2\Server\Docker_KT2\Kiemthe2-server\gameserver\setting\npc\dialognpc.txt` (Map ID: 3)
- **Lời thoại**: Hi hi! Có vũ khí của ta trong tay, muốn trở thành đệ nhất võ lâm cao thủ dễ như trở bàn tay. Khách quan hãy mua 1 cái đi, sau đó đến chỗ Tạ Hiền mua chiếc phi phong, chắc chắn sẽ rất oai!
- **Các lựa chọn tương tác**: "Vũ Khí","Dialog:OpenShop",388,1, "Khoáng thạch","Dialog:OpenShop",16,1, "Không mua nữa"

---

### [Đạo Hương Thôn] Lớp NPC: `bingqipulaoban` (Record #4)
- **Nguồn**: `Kiếm Thế 2\Server\Docker_KT2\Kiemthe2-server\gameserver\setting\npc\dialognpc.txt` (Map ID: 4)
- **Lời thoại**: Hi hi! Có vũ khí của ta trong tay, muốn trở thành đệ nhất võ lâm cao thủ dễ như trở bàn tay. Khách quan hãy mua 1 cái đi, sau đó đến chỗ Tạ Hiền mua chiếc phi phong, chắc chắn sẽ rất oai!
- **Các lựa chọn tương tác**: "Vũ Khí","Dialog:OpenShop",388,1, "Khoáng thạch","Dialog:OpenShop",16,1, "Không mua nữa"

---

### [Giang Tân Thôn] Lớp NPC: `bingqipulaoban` (Record #5)
- **Nguồn**: `Kiếm Thế 2\Server\Docker_KT2\Kiemthe2-server\gameserver\setting\npc\dialognpc.txt` (Map ID: 5)
- **Lời thoại**: Hi hi! Có vũ khí của ta trong tay, muốn trở thành đệ nhất võ lâm cao thủ dễ như trở bàn tay. Khách quan hãy mua 1 cái đi, sau đó đến chỗ Tạ Hiền mua chiếc phi phong, chắc chắn sẽ rất oai!
- **Các lựa chọn tương tác**: "Vũ Khí","Dialog:OpenShop",388,1, "Khoáng thạch","Dialog:OpenShop",16,1, "Không mua nữa"

---

## 2. Mẫu Kịch Bản 4 Đại Chiến Trường Quân Doanh

### Chiến trường: Hậu Sơn Phục Ngưu Sơn
- **Phân đoạn**: `doorsill` (Đối thoại kịch bản) | **Nguồn**: `Kiếm Thế 2\Server\Docker_KT2\Kiemthe2-server\gameserver\script\task\armycamp\90_100\npc\caikuangqu\doorsill.lua`
- **Nội dung**: Thuyền sửa xong rồi, có thể đi thuyền tiến về Loạn Thạch Than.

- **Phân đoạn**: `doorsill` (Đối thoại kịch bản) | **Nguồn**: `Kiếm Thế 2\Server\Docker_KT2\Kiemthe2-server\gameserver\script\task\armycamp\90_100\npc\caikuangqu\doorsill.lua`
- **Nội dung**: Con thuyền này hư nhiều quá, cần dùng ba dây thừng và ba tấm gỗ gia cố lại mới sử dụng được.

---

### Chiến trường: Bách Man Sơn
- **Phân đoạn**: `guwang` (Đối thoại kịch bản) | **Nguồn**: `Kiếm Thế 2\Server\Docker_KT2\Kiemthe2-server\gameserver\script\task\armycamp\100_110\npc\guwang.lua`
- **Nội dung**: Vào bây giờ không?

- **Phân đoạn**: `guwang` (Thông cáo cốt truyện) | **Nguồn**: `Kiếm Thế 2\Server\Docker_KT2\Kiemthe2-server\gameserver\script\task\armycamp\100_110\npc\guwang.lua`
- **Nội dung**: Chỉ có đội ngũ ở

---

### Chiến trường: Hải Lăng Vương Mộ
- **Phân đoạn**: `ercengnpc` (Đối thoại kịch bản) | **Nguồn**: `Kiếm Thế 2\Server\Docker_KT2\Kiemthe2-server\gameserver\script\task\armycamp\110_120\npc\ercengnpc.lua`
- **Nội dung**: Có muốn vào?

- **Phân đoạn**: `ercengnpc` (Đối thoại kịch bản) | **Nguồn**: `Kiếm Thế 2\Server\Docker_KT2\Kiemthe2-server\gameserver\script\task\armycamp\110_120\npc\ercengnpc.lua`
- **Nội dung**: Có muốn vào?

---

### Chiến trường: Ngạc Luân Hà Nguyên
- **Phân đoạn**: `altar` (Đối thoại kịch bản) | **Nguồn**: `Kiếm Thế 2\Server\Docker_KT2\Kiemthe2-server\gameserver\script\task\armycamp\elunheyuan\npc\altar.lua`
- **Nội dung**: Các ngươi quá nóng vội, hãy hoàn thành mọi khiêu chiến rồi hãy đến tìm ta.

- **Phân đoạn**: `animalmanager` (Đối thoại kịch bản) | **Nguồn**: `Kiếm Thế 2\Server\Docker_KT2\Kiemthe2-server\gameserver\script\task\armycamp\elunheyuan\npc\animalmanager.lua`
- **Nội dung**: Hãy đi bắt ngựa, xong rồi trở lại gặp ta.

---

## 3. Mẫu Truyện Ngắn Nghĩa Quân Bao Vạn Đồng

### [Bao Vạn Đồng] Truyện #1 (Nghĩa quân / Tình báo chiến sự)
- **Nguồn**: `Kiếm Thế 2\Server\Docker_KT2\Kiemthe2-server\gameserver\script\task\linktask\text.lua` (Mã: 10000)
- **Nguyên văn**: Gần đây cao thủ Cái Bang Ảnh Xã tử thương nặng nề ở Kim quốc. Bạch thủ lĩnh và Bang chủ Cái Bang Thạch Hiên Viên vốn có thâm giao, nàng tập trung một nhóm cao thủ, chuẩn bị đến Trung Nguyên giải cứu những cao thủ Ảnh Xã còn lại. Hiện tại vẫn còn thiếu <Item>, ngươi có thể tìm giúp?

---

### [Bao Vạn Đồng] Truyện #2 (Nghĩa quân / Tình báo chiến sự)
- **Nguồn**: `Kiếm Thế 2\Server\Docker_KT2\Kiemthe2-server\gameserver\script\task\linktask\text.lua` (Mã: 10000)
- **Nguyên văn**: Bạch thủ lĩnh cho rằng, bọn Thát Đát có ý đồ tiêu diệt Tây Hạ và Kim quốc, như vậy Đại Tống ta sẽ lâm nguy. Hiện nay ta biết rất ít về bọn Thát Đát, vì vậy ngươi hãy đi tìm <Item>, nghe nói chúng được làm bởi thợ của bộ lạc Mông Cổ.

---

### [Bao Vạn Đồng] Truyện #3 (Nghĩa quân / Tình báo chiến sự)
- **Nguồn**: `Kiếm Thế 2\Server\Docker_KT2\Kiemthe2-server\gameserver\script\task\linktask\text.lua` (Mã: 10000)
- **Nguyên văn**: Hôm qua nhận được tin, toán quân yểm trợ của Nhậm Tiếu Thiên đã tập kích Từ Châu. Nơi đó đất đai màu mỡ, là nơi binh gia tranh giành. Nếu họ trụ được đến cuối thu thì không lo thiếu lương thảo cho năm tới, nhưng Nhậm Tiếu Thiên còn thiếu <Item>, ngươi có thể tìm giúp?

---

