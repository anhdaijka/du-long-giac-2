# Spec continuity-detail — Quyển I

Trạng thái: `AUTHOR-APPROVED PLANNING / CDQ-01–05 / NOT CANON / NOT A CHAPTER PLAN`.

Spec này cụ thể hóa ranh giới continuity giữa ba route Quyển I sau V1PQ-01–04, BFCQ-01–04 và CDQ-01–05. Ngày 2026-09-09, Tác giả phê duyệt toàn bộ năm CDQ theo đề xuất. Spec khóa điều gì **phải đúng** trước khi lập chương, nhưng không đặt số chương, scene order, ngày tháng, thời lượng hành trình, lời thoại hay văn xuôi. Các ô vẫn được ghi là chưa chọn tiếp tục là `OPEN SLOT`; không agent nào được tự điền chúng chỉ để làm continuity trông kín hơn.

## 1. Goal, scope và out of scope

### Goal

- Cho ba tuyến Tiêu Phùng, Tĩnh Xuyên và Hạ Nương có thể vận hành song song mà không chia lại một player-avatar cho cả ba.
- Bảo toàn tri thức hạn chế, agency của NPC/tổ chức và các cạnh nguồn đã chứng minh.
- Đặt contract rõ ràng cho bốn khoảng BFCQ còn mở trước khi bước sang chapter planning.
- Khóa tuyệt đối hạt nhân canon Tĩnh Xuyên–Ân Đồng mà không kéo route này vào Quyển I sớm hoặc bịa chi tiết thay thế.

### In scope

- Partial order giữa các checkpoint Quyển I.
- Actor/state/knowledge handoff ở Cái Bang và Bách Hoa.
- Trạng thái tài liệu của hai lá thư và thông cáo T12/S92.
- Ranh giới custody Du Long Giác.
- Future-continuity invariant Tĩnh Xuyên–Ân Đồng.
- Open questions cần Tác giả chốt hoặc cho phép giữ mở trước chapter planning.

### Out of scope

- Số/tên chương, beat sheet, scene card, POV scene, thoại và prose.
- Ngày lịch sử, thời lượng di chuyển, bản đồ hành trình chi tiết.
- Lời giải Huyền Nguyệt, custody thật hoặc công năng khách quan của Du Long Giác.
- Nội dung route bible Quyển II–V, trừ invariant bảo toàn tương lai đã được Tác giả tái xác nhận.
- Satellite POV, Legendary Shadow, nhân vật mới, kết quả y khoa và từng đòn chiến đấu.

## 2. Authority và provenance

SQLite: `story_database.sqlite3`, SHA-256 `b5c30040c9449f2223cf40bfec9866216423a60a82e2333b5cedb4fb5261bdb0`.

| Cụm | Query nguyên văn / bind | Kết quả trích xuất lưu tại |
| --- | --- | --- |
| T1, T2, T4 | `SELECT task_id, task_id_hex, name, describe_cleaned, category, category_desc, order_type, repeat, task_type_code, file_path FROM tasks WHERE task_id = ?` với bind `(1)`, `(2)`, `(4)`; cùng ba query chuẩn packet bên dưới | [arc_00.json](evidence/source-packets/arc_00.json), `tasks[task_id=1]`, `tasks[task_id=2]`, `tasks[task_id=4]` |
| T12 | Cùng query task, bind `(12)`; cùng query chuẩn packet | [arc_01.json](evidence/source-packets/arc_01.json), `tasks[task_id=12]` |
| T157 | Cùng query task, bind `(157)`; cùng query chuẩn packet | [arc_06.json](evidence/source-packets/arc_06.json), `tasks[task_id=157]` |

Các query chuẩn packet:

```sql
SELECT sub_id, sub_id_hex, task_id, name, describe_cleaned, file_path, dialog_npc_id, dialog_npc_name FROM subtasks WHERE task_id = ? ORDER BY sub_id;
SELECT id, sub_id, step_index, instruction, target_function, target_params FROM steps WHERE sub_id = ? ORDER BY step_index, id;
SELECT id, sub_id, phase, cleaned_text FROM dialogues WHERE sub_id = ? ORDER BY id;
```

Packet lưu query, bind và toàn bộ result rows. Locator như `T4/S36/E172` trỏ Task 4, subtask 36 và step id 172, không phải chapter/beat number.

Nhãn dùng trong spec:

- `GAME FACT`: proposition có trong SQLite, giữ đúng speaker/document scope.
- `AUTHOR-APPROVED NOVELIZATION BRIDGE`: phép tuyến tính hóa/phân vai đã được Tác giả duyệt.
- `PROTECTED CANON INVARIANT`: quyết định tác giả bắt buộc bảo toàn xuyên các phase, nhưng không vì thế trở thành game fact.
- `OPEN SLOT`: chưa được chọn; không được lấp bằng suy luận hoặc prose convenience.

## 3. Invariant bắt buộc

| ID | Invariant | Kiểm soát thất bại |
| --- | --- | --- |
| CDI-01 | Mọi claim phải giữ nhãn `GAME FACT`, `HISTORICAL FACT`, `AUTHOR-APPROVED NOVELIZATION BRIDGE` hoặc `OPEN SLOT` đúng provenance. | Không nâng lời đồn, thông cáo, nhan đề task hoặc Foundation thành sự thật khách quan. |
| CDI-02 | `PHYSICAL_CONVERGENCE_VOLUME_I = NONE`. Ba POV không gặp trực tiếp, không cứu nhau, không cùng trú quán/thuyền và không thành đội trong Quyển I. | Cùng địa danh/tổ chức không chứng minh cùng thời điểm. |
| CDI-03 | Tĩnh Xuyên mang thư rồi rời cửa sổ Cái Bang; Tiêu Phùng tới bằng PB-02 ở cửa sổ khác. | Không chia ký ức của một avatar cho hai người và không để họ chạm mặt vì tiện handoff. |
| CDI-04 | Lục Trầm Châu đấu Thôi Xuất Trần; Tiêu Phùng không nhận chiến công, võ học hoặc vị thế từ trận ấy. | Không biến living wulin thành sân khấu nâng cấp protagonist. |
| CDI-05 | Hạ Nương cứu/chuyển chữa; không lấy, giao, xác nhận custody hoặc giải công năng Du Long Giác. | Không dùng POV y thuật làm người kể toàn tri cho artifact. |
| CDI-06 | Thông cáo “bị cướp” là nước cờ thông tin có chủ ý theo dialogue nguồn, không phải bằng chứng custody khách quan. | Mọi người chỉ biết bản thông cáo đã thật sự tới kênh của họ. |
| CDI-07 | Canon Tĩnh Xuyên–Ân Đồng là bất khả thay thế, bất khả giảm nhẹ và bất khả chuyển trách nhiệm. | Xem contract riêng ở mục 8; không dùng nạn nhân thay thế trong Quyển I. |

## 4. Partial order Quyển I

Đây là đồ thị trước–sau tối thiểu, không phải lịch hoặc scene order.

### Lane Tiêu Phùng

1. `TP-A`: mạng việc quê T157/S306–S321 tạo nghĩa vụ cộng đồng.
2. `TP-B`: T157/S320/E1432 cho Thu Di nhận chìa khóa, cử người cứu Giới Sơn Tông và dẫn về S312.
3. `TP-C`: tuyến Bạch Cương/sấm thi đi tới cổng xuất hành T157/S323.
4. `TP-D`: PB-02 đưa Tiêu Phùng tới môi trường Cái Bang qua La Tuấn; chi tiết hành trình còn mở.
5. `TP-E`: chàng có thể chứng kiến hậu quả luật bang/T2/S13 và nhận phần việc phù hợp; Lục giữ trận Thôi.
6. `TP-F`: sau khi thông cáo T12/S92 đã tới Thạch Hiên Viên, phần công khai có thể tới Tiêu Phùng qua La Phong hoặc Cầu Chỉ Thủy.

Required edges: `TP-A → TP-B → TP-C → TP-D`; `TP-D → TP-E`. Không có source edge đủ để đặt `TP-E` trước/sau lane Hạ Nương. `TP-F` chỉ bắt buộc sau việc Thạch nhận thông cáo, không bắt buộc sau trận Thôi nếu chưa có chronology.

### Lane Tĩnh Xuyên

1. `TX-A`: T1/S1–S2 đặt chính danh, vu cáo Cầu Chỉ Thủy và tin Du Long từ Thành Đô.
2. `TX-B`: T1/S3–S7 đặt tranh luận cứu Hàn Thác Trụ, hộ tống, phòng thủ và kỹ nghệ tập thể.
3. `TX-C`: T1/S8/E37 giao hai thư; T1/S8/E41 đưa người mang thư tới La Phong.
4. `TX-D`: Tĩnh Xuyên giao thư vào đầu mối Cái Bang rồi rời cửa sổ hiện diện theo PB-01/BFCQ-03.

Required edges: `TX-A → TX-B → TX-C → TX-D`. `TX-D` phải hoàn tất trước cửa sổ Cái Bang trực tiếp của Tiêu Phùng. Đích đi tiếp, đường đi, thời lượng và việc có quay lại Thanh Loa hay không đều là `OPEN SLOT`.

### Lane Cái Bang/Lục Trầm Châu

1. `CB-A`: Cái Bang tiếp nhận và tự quyết định phản ứng với thư T1/T2.
2. `CB-B`: T2/S10/E50 xác nhận trong lời avatar rằng võ nghệ Lục Trầm Châu rất cao.
3. `CB-C`: Lục sống qua vụ Tô Hữu Tưởng nhờ một hành động Cái Bang ngoài màn.
4. `CB-D`: T2/S12/E60 cho Lục theo Thạch và chuyển thẳng tới S13.
5. `CB-E`: Lục đấu Thôi Xuất Trần tại T2/S13; chi tiết giao đấu chưa được thiết kế.

Required edges: `CB-B → CB-C → CB-D → CB-E`. Actor/cách thức ở `CB-C` là `OPEN SLOT`; không được lược bỏ trạng thái sống cần thiết chỉ vì sự kiện ở ngoài màn.

### Lane Hạ Nương/Thúy Yên

1. `HN-A`: T12/S85–S86 đặt tìm ngọc, la bàn và mâu thuẫn custody ban đầu.
2. `HN-B`: T12/S87–S90 nối báo động, tập kích, cứu nạn, trận phòng thủ và trợ chiến ngoài trio.
3. `HN-C`: T12/S91 đặt tù binh tự tử, Tam Muội trọng thương và yêu cầu chuyển tới Đại Lý.
4. `HN-D`: T12/S92 đặt hậu quả, tái thiết và quyết định công bố “bị cướp” để thăm dò/huy động.
5. `HN-E`: T12/S92/E516 cho sứ giả Doãn Hàm Yên báo Thạch Hiên Viên; đây là đầu vào của `TP-F`.

Required edges: `HN-A → HN-B → HN-C → HN-D → HN-E`. Không có cạnh nguồn xác định `HN-E` trước/sau `CB-E`.

## 5. Continuity knots và handoff contract

| Knot | State phải có trước | State được phép có sau | `OPEN SLOT` phải giữ | Không được làm |
| --- | --- | --- | --- | --- |
| CDK-01 — giao thư | Tĩnh Xuyên đang giữ hai thư; người nhận là đầu mối Cái Bang có nguồn. | Cái Bang có thư và tự quyết; Tĩnh Xuyên đã rời cửa sổ. | Đích đi tiếp, thời gian, phương tiện chặng sau. | Để Tĩnh Xuyên ở lại rèn luyện; cho Tiêu Phùng nhớ hành trình của chàng. |
| CDK-02 — Lục sống tới lôi đài | Lục bị đặt vào nguy cơ Tô Hữu Tưởng; source avatar từng giải quyết. | Lục sống, tự chọn theo Thạch và đủ hiện diện ở S13. | CDQ-01: không nêu người cứu trong Quyển I; cách cứu/chi phí không được thiết kế nếu không mở lại scope. | Gọi hành động Cái Bang ngoài màn là game fact; trao cả cứu Lục lẫn trận Thôi cho nhân vật mới/toàn năng. |
| CDK-03 — trận Thôi | Lục đã theo Thạch; lôi đài phục vụ xử lý bang quy. | Quyết định tổ chức được thực thi; Tiêu Phùng không nhận công. | Nhịp trận, thương tích, ai tận mắt thấy, aftermath cá nhân của Lục. | Biến thành thử thách nhập môn hoặc màn học tuyệt kỹ cho Tiêu Phùng. |
| CDK-04 — thông cáo | Nội bộ Thúy Yên đã chọn tung tin “bị cướp” như một nước cờ. | Thạch nhận bản công khai; Tiêu Phùng có thể nhận một phần công khai khi có chức năng. | La Phong hay Cầu Chỉ Thủy relay; hình thức, câu chữ, độ trễ. | Tạo sứ giả mới; cho relay biết/khẳng định custody thật; buộc Tĩnh Xuyên nhận cùng tin. |
| CDK-05 — cứu/chuyển chữa | Có người bị thương và tổ chức đang chiến đấu/tái thiết. | Hạ Nương chọn chăm sóc/chuyển Tam Muội; tổ chức giữ agency chiến đấu và quản trị. | Kết quả y khoa, người đồng hành, chi tiết hành trình Đại Lý. | Để Hạ Nương lấy/giao ngọc, giải trận hoặc chữa khỏi tức thì. |
| CDK-06 — Du Long custody | T12/S86/E483, T12/S86/E484 và T12/S87 không tạo một chuỗi custody nhất quán. | Trạng thái cuối Quyển I vẫn là `OBJECTIVE_CUSTODY = UNRESOLVED`. | Người giữ thật, nơi cất, thời điểm chuyển tay. | Lấy thông cáo công khai làm ledger vật sở hữu hoặc bí mật sửa source contradiction. |

## 6. Knowledge ledger tối thiểu

| Checkpoint | Độc giả | Tiêu Phùng | Tĩnh Xuyên | Hạ Nương | NPC/tổ chức |
| --- | --- | --- | --- | --- | --- |
| Sau CDK-01 | Biết Tĩnh Xuyên đã giao thư và rời đi. | Không biết tiền sử/hộ tống của người mang thư nếu không có relay hợp lệ. | Không biết mọi quyết định Cái Bang sau khi rời. | Không liên quan. | Thạch/Cầu có nội dung thư trong phạm vi source; phân đà tự hành động. |
| Sau CDK-03 | Biết Lục là người đấu và Cái Bang có đời sống pháp độ riêng. | Chỉ biết điều chứng kiến/được kể; không sở hữu chiến công. | Không mặc nhiên biết kết quả lôi đài. | Không mặc nhiên biết. | Thạch, Lục và người hiện diện biết theo đúng cảnh tương lai. |
| Sau CDK-04 | Có thể nhận ra bản công khai khác custody khách quan vì đã theo lane Hạ Nương. | Chỉ biết phần công khai được La/Cầu relay; không biết ai giữ ngọc. | Không cần nhận thông cáo trong Quyển I. | Biết những gì tận mắt thấy và việc tổ chức chọn công bố; không biết phản ứng riêng ở Cái Bang. | Thạch nhận thông cáo; La/Cầu chỉ chuyển phần được cấp. |
| Kết Quyển I | Biết ba tuyến đã chịu tác động của cùng một trường lực chính trị–giang hồ. | Không biết hai POV còn lại là ai. | Không biết hai POV còn lại là ai. | Không biết hai POV còn lại là ai. | Các tổ chức giữ mục tiêu, nguồn lực và tri thức riêng. |

Quy tắc: `READER_KNOWLEDGE ≠ CHARACTER_KNOWLEDGE`. Không dùng hồi tưởng, lời đồn vô chủ hoặc người kể toàn tri để vượt ledger.

## 7. State ledger bắt buộc trước chapter planning

| State key | Giá trị được phép chốt ở cuối spec | Giá trị cấm tự chốt |
| --- | --- | --- |
| `TX_LETTER_HANDOFF` | `DELIVERED_TO_CAI_BANG / TX_EXITED_WINDOW` | ngày, giờ, chặng sau |
| `TP_CAI_BANG_ENTRY` | `APPROVED_VIA_LA_TUAN / DETAILS_OPEN` | bến, thư giới thiệu, lịch đi |
| `LUC_RESCUE` | `CAI_BANG_OFFSCREEN_ACTION / NO_NAMED_RESCUER_IN_VOLUME_I` | tên cứu tinh, kỹ thuật, thương tích |
| `THOI_BOUT_ACTOR` | `LUC_TRAM_CHAU` | Tiêu Phùng hoặc nhân vật mới |
| `PUBLIC_NOTICE_RECIPIENT` | `THACH_HIEN_VIEN` | mặc định toàn giang hồ đã biết |
| `TP_NOTICE_RELAY` | `FUNCTIONAL_RULE / LA_FOR_FIELD_TASK / CAU_FOR_POLITICAL_JUDGMENT / SCENE_CHOICE_UNSELECTED` | người thứ ba mới hoặc cả hai cùng relay |
| `TX_NOTICE_RELAY` | `NOT_REQUIRED_IN_VOLUME_I` | tự thêm bản tin để đối xứng ba POV |
| `DU_LONG_OBJECTIVE_CUSTODY` | `UNRESOLVED` | bất kỳ holder/location cụ thể nào |
| `HA_NUONG_ARTIFACT_ROLE` | `NO_RETRIEVE_NO_DELIVER_NO_VERIFY_NO_MECHANISM` | quyền xác nhận sự thật artifact |
| `HUYEN_NGUYET_MECHANISM` | `DEFERRED` | giải pháp quang học/cơ khí/huyền huyễn |

## 8. Protected canon invariant — Tĩnh Xuyên và Ân Đồng

### 8.1 GAME FACT của route nam

- T4/S28–S32 xây sự tin cậy qua cứu nạn, dược thảo, tình ý của Ân Đồng và sự bối rối/tự vấn của avatar.
- T4/S33 cho Điệp Phiêu Phiêu nói đã biết tình cảm Ân Đồng dành cho avatar và biết avatar chưa đáp lại tình cảm ấy.
- T4/S36/E171 cho Ân Đồng đi tìm để tiễn và phát hiện thân phận gián điệp.
- T4/S36/E172 ghi nàng nói yêu người mang route, Cơ Chú thúc ép giết để giữ kế hoạch, và step kết bằng lời Ân Đồng rằng dù sống nàng cũng không tiết lộ.
- T4/S36/E173 cho người mang route trở lại với Cơ Chú sau hành động; T4/S37 xác nhận Ân Đồng đã chết dưới tay người mình yêu và người ấy biết nàng sẽ không tiết lộ.

### 8.2 PROTECTED CANON INVARIANT

Theo quyết định tác giả D-004, R-14 và xác nhận mới ngày 2026-09-09 (SQLite hiện hành đặt route nam ở **Task 4**, dù dòng lịch sử D-004 từng ghi Task 5):

1. Tĩnh Xuyên nhận route nam và dùng thân phận **Mộc Nhất Lâu**.
2. Quan hệ Tĩnh Xuyên–Ân Đồng phải được phát triển như một quan hệ người thật có thời gian, tin cậy và tình cảm; Ân Đồng không chỉ là “nạn nhân để tạo tâm ma”.
3. Ân Đồng yêu Tĩnh Xuyên/Mộc Nhất Lâu; mức và cách Tĩnh Xuyên đáp lại phải tôn trọng route nhưng chưa bị spec Quyển I định lượng thành lời hứa hay hôn ước.
4. Khi bí mật bại lộ, **Tĩnh Xuyên tự tay hạ sát Ân Đồng** vì chọn đại cục/kế hoạch. Không tai nạn, không bẫy chông, không người thứ ba ra tay, không giả chết để miễn trách nhiệm.
5. Sau đó Tĩnh Xuyên biết rằng Ân Đồng dù sống cũng sẽ không tiết lộ bí mật. Nhận thức đến sau quyết định không thể hoàn tác là phần bắt buộc của bản án lương tâm.
6. Chiến công, tha Điệp Phiêu Phiêu, sự chuộc lỗi hay bất kỳ hậu quả sau này không được xóa, san sẻ hoặc hợp lý hóa trách nhiệm trực tiếp của Tĩnh Xuyên.

### 8.3 Boundary đối với Quyển I

- Route T4/S28–S37 **không được chuyển vào Quyển I** chỉ để foreshadow sớm; volume architecture hiện đặt nó vào phase sau khi condition/chronology được tái dựng.
- Quyển I chỉ được gieo flaw “quân lệnh/đại cục có thể khiến chàng tự trao quyền phán quyết”. Không dựng một nữ nhân thay thế, một lần “giết nhầm” rehearsal hoặc lời tiên tri gọi thẳng tên Ân Đồng.
- Không cho Tĩnh Xuyên quen, gặp, nhớ hoặc mang di vật của Ân Đồng trước khi route Mộc Nhất Lâu thật sự bắt đầu.
- Chính xác quyển nào, thời gian nào, vũ khí nào và di vật nào vẫn phải qua phase riêng. SQLite T4/S36 nói “kiếm ta đã nhuốm máu Ân Đồng”, trong khi Foundation hiện có hình tượng trường thương/mũi thương; **kết quả và chủ thể gây chết đã khóa, hung khí chưa được tự chọn**.

## 9. Acceptance criteria cho spec

Spec chỉ sẵn sàng trình duyệt khi:

1. Mọi locator trỏ đúng task/subtask/step trong packet.
2. Bốn lane có required edges nhưng không có ngày/thời lượng giả.
3. `PHYSICAL_CONVERGENCE_VOLUME_I = NONE` còn nguyên.
4. Mọi knot ghi đủ before-state, after-state, open slot và forbidden move.
5. Knowledge ledger không chuyển tri thức độc giả thành tri thức trio.
6. Custody cuối Quyển I vẫn `UNRESOLVED`; Huyền Nguyệt vẫn `DEFERRED`.
7. Tĩnh Xuyên–Ân Đồng giữ đủ chủ thể, tình cảm, hành động không thể hoàn tác, lời xác nhận sau đó và trách nhiệm dài hạn.
8. Không có chapter count, scene allocation, prose, nhân vật mới, Legendary Shadow hoặc nội dung Quyển II–V được mở.

## 10. Kết quả CDQ-01–05 — APPROVED 2026-09-09

| ID | Quyết định đã duyệt | Hệ quả ràng buộc |
| --- | --- | --- |
| CDQ-01 | Việc cứu Lục là **institutional off-screen action không nêu tên người cứu** trong toàn Quyển I; chỉ mở lại nếu một scene tương lai thật sự cần actor. | Không bịa thêm anh hùng phụ; không thiết kế người/cách cứu ở chapter architecture Quyển I. |
| CDQ-02 | Relay theo **functional rule**: dùng La Phong nếu tin gắn với nhiệm vụ hiện trường; dùng Cầu Chỉ Thủy nếu tin gắn với phán đoán bang vụ/chính trị. Chưa chọn trước khi có chapter function. | Chapter architecture phải nêu chức năng trước khi chọn một trong hai; không dùng cả hai chỉ để lặp tin. |
| CDQ-03 | State/partial order ở mục 4–7 là rào chronology duy nhất của Quyển I; ngày, độ trễ và đường đi chỉ mở sau historical/travel audit. | Chapter architecture được phép sắp nhịp tương đối, không được ghi lịch tuyệt đối giả. |
| CDQ-04 | `DU_LONG_OBJECTIVE_CUSTODY = UNRESOLVED` cả trong ledger hậu trường Quyển I, không chỉ trong tri thức nhân vật. | Không agent nào được bí mật chọn holder rồi viết quanh lựa chọn chưa duyệt. |
| CDQ-05 | Khóa **Tĩnh Xuyên là người tự tay hạ sát Ân Đồng** nhưng hoãn chọn kiếm hay thương đến phase route Mộc Nhất Lâu. | Canon quan hệ và trách nhiệm được bảo toàn; hung khí vẫn là protected unknown. |

Phê duyệt CDQ-01–05 làm spec này thành planning authority cho bước **đề xuất chapter architecture Quyển I**. Nó không tự duyệt chapter plan, scene, prose, chronology tuyệt đối, hung khí Ân Đồng, route Quyển IV hay canon promotion.
