> Current temporal/creative authority: migration/restructure_2026_09/temporal-continuity-contract.md and temporal-character-framework.md (D-064/R-90 and D-065/R-91). Read both before chapter operations. Framework direction is not source receipt or prose authorization.

# Series Chapter Allocation Index — Quyển I–V

Trạng thái: `AUTHOR-DEFAULTED PLANNING / D61-R87 / GEMINI ROUTER INDEX / NOT SOURCE / NOT CANON / NOT SCENE PLAN / NOT PROSE`.

## Mục đích

Đây là điểm vào duy nhất để Gemini định tuyến **140 chapter-function** đã phân cho năm quyển. File này không thay thế SQLite, source packet, provenance ledger hoặc quyết định của Tác giả. Nó chỉ cho biết phải mở artifact nào và dừng ở đâu.

Quy tắc dùng:

1. Chọn đúng quyển và chapter trong `chapter-sequence.md`.
2. Đọc row cùng khóa trong `provenance-ledger.tsv`.
3. Mở packet và đúng `tasks[task_id=...].subtasks[sub_id=...]`; chỉ proposition thật sự xuất hiện trong receipt mới được mang nhãn game fact.
4. Giữ riêng `GAME FACT`, `HISTORICAL FACT`, `GAME ALT-HISTORY`, `SOURCE REPORT` và `NOVELIZATION BRIDGE`.
5. POV là aperture tiểu thuyết, không đồng nhất nhân vật với avatar đã làm nhiệm vụ trong game.
6. Nếu implementation cần một durable fact, chronology, branch, relationship change hoặc Bridge chưa có receipt/decision thì hard-stop hỏi Tác giả. Wording, gesture, vi động tác và cảm giác không làm đổi durable state thuộc quyền thi hành văn chương.

## Toàn cảnh allocation đã kiểm

| Quyển | Chương | Tĩnh Xuyên | Tiêu Phùng | Hạ Nương | Source scope | Receipt |
| --- | ---: | ---: | ---: | ---: | --- | ---: |
| I | 25 | 8 | 11 | 6 | Arc 00, 01, 06 | 45 lượt / 36 locator duy nhất |
| II | 24 | 7 | 9 | 8 | Arc 04, 05, 07; 1 Bridge chức năng | 31 lượt / 30 locator + 1 decision-only row |
| III | 28 | 14 | 8 | 6 | Arc 08; lát cắt Phục Ngưu–quân doanh Arc 09 | 43 lượt / 43 locator |
| IV | 28 | 10 | 10 | 8 | cụm Đại Lý cuối Arc 09; Arc 10 chọn lọc | 33 lượt / 33 locator |
| V | 35 | 13 | 12 | 10 | Arc 11, 12; insert T4/S36–S37 từ Arc 00 | 41 lượt / 41 locator |
| **Tổng** | **140** | **52** | **50** | **38** | 11 packet Arc được dùng trực tiếp | **193 lượt / 183 locator duy nhất + 1 decision-only row** |

`V2-CH-21` ghi POV là `Tiêu Phùng — limited convergence`; phép đếm chuẩn hóa nó về Tiêu Phùng. Đây là lý do bộ đếm máy phải nhận prefix, không coi nó là POV thứ tư.

## Router theo quyển

| Quyển | Điểm vào chapter | Ledger bắt buộc | Source-window hỗ trợ | Vai trò và handoff ra |
| --- | --- | --- | --- | --- |
| I | [chapter-sequence.md](chapter-plan-volume-i/chapter-sequence.md) | [provenance-ledger.tsv](chapter-plan-volume-i/provenance-ledger.tsv) | [coverage ledger](writer-preflight-volume-i/volume-i-coverage-ledger.md) | Dựng ba tuyến riêng và dư chấn Bách Hoa; chỉ hội tụ gián tiếp, không cho trio gặp sớm. |
| II | [chapter-sequence.md](chapter-plan-volume-ii/chapter-sequence.md) | [provenance-ledger.tsv](chapter-plan-volume-ii/provenance-ledger.tsv) | [expanded source windows](writer-preflight-volume-ii/volume-ii-expanded-source-windows.md) | Living wulin, family-task qua report/memory/lore và first physical convergence hữu hạn; kết ở áp lực dựng quân doanh. |
| III | [chapter-sequence.md](chapter-plan-volume-iii/chapter-sequence.md) | [provenance-ledger.tsv](chapter-plan-volume-iii/provenance-ledger.tsv) | [expanded source windows](writer-preflight-volume-iii/volume-iii-expanded-source-windows.md) | Quân–chính, dân lực và giá xã hội của đại cục; chỉ dùng lát cắt quân doanh Arc 09. |
| IV | [chapter-sequence.md](chapter-plan-volume-iv/chapter-sequence.md) | [provenance-ledger.tsv](chapter-plan-volume-iv/provenance-ledger.tsv) | [expanded source windows](writer-preflight-volume-iv/volume-iv-expanded-source-windows.md) | Đại Lý, bí mật thứ hai và tình báo phương Bắc; kết bằng hậu quả ở phân đà phía Bắc. |
| V | [chapter-sequence.md](chapter-plan-volume-v/chapter-sequence.md) | [provenance-ledger.tsv](chapter-plan-volume-v/provenance-ledger.tsv) | [expanded source windows](writer-preflight-volume-v/volume-v-expanded-source-windows.md) | Huy động, Linh Bích, Huyễn Cảnh, di sản và lựa chọn đạo đức; kết cục trước mắt khép nhưng Du Long không bị giải kín. |

## Integrity của nguồn và ranh giới quyển

Không có locator `T/S` nào được dùng ở hai quyển khác nhau; cũng không có Task ID nào bị chia ngầm qua hai quyển. Ranh giới Arc 09 giữ đúng: quân doanh ở Quyển III, Đại Lý ở Quyển IV. Insert T4/S36–S37 tại Quyển V được ghi rõ là protected-canon insert, không phải source chronology tự suy ra từ số Task.

Các handoff chỉ là **relative planning order**:

- I → II: dư chấn Bách Hoa chuyển thành áp lực công cộng/living-wulin và hội tụ hữu hạn; chưa khóa relay, lịch đi hoặc địa điểm gặp.
- II → III: `T225/S400` được đọc thành hai mặt của cùng một transition ở cuối Quyển II; Quyển III mở bằng thiết chế quân doanh từ T228 trở đi. Không suy chronology chỉ từ Task ID.
- III → IV: giá dân lực/quân doanh trao áp lực sang mạng Đại Lý–địa chính trị; không kéo Task 303+ hoặc Đại Lý ngược về Quyển III.
- IV → V: thương tích và tình báo phương Bắc trao áp lực sang chính trị–huy động–chiến dịch; ngày, hành trình và khoảng cách vẫn mở.

## Locator được tái dùng có chủ ý trong cùng quyển

Đây là reuse của **cùng bằng chứng cho các chức năng/aftershock khác nhau**, không phải quyền kể source event hai lần:

| Quyển | Locator | Chapter dùng | Guard |
| --- | --- | --- | --- |
| I | T157/S310 | 07, 20 | Ch20 chỉ causal return; không tạo biến cố thứ hai. |
| I | T157/S320 | 09, 10 | Hai row dùng các node khác nhau trong cùng subtask. |
| I | T157/S323 | 17, 20 | Ch20 chỉ nối áp lực/handoff. |
| I | T2/S9 | 18, 20 | Không replay encounter. |
| I | T2/S13 | 21, 25 | Ch25 chỉ nhận dư chấn/relay. |
| I | T2/S14 | 22, 25 | Ch25 không tái tạo toàn bộ sự kiện. |
| I | T12/S91 | 19, 23 | Ch23 dùng aftermath, không coi là lần xảy ra mới. |
| I | T12/S92 | 23, 24, 25 | Public notice/aftermath được truyền qua nhiều lens; không nhân bản sự kiện. |
| II | T225/S400 | 23, 24 | Hai subset chiến lược và vật chất của **một** transition; tuyệt đối không kể thành hai nhiệm vụ. |

## Writer hard-stop registry

Chỉ hard-stop khi chi tiết đang viết bắt buộc phải biến một khoảng mở thành durable state:

| Gate | Phạm vi | Điều phải hỏi Tác giả trước khi khóa |
| --- | --- | --- |
| WG-01 | toàn series | Mâu thuẫn SQLite/Foundation, branch loại trừ nhau, fact không có proposition-level receipt, hoặc muốn nâng source report/game-alt-history thành sự thật khách quan. |
| WG-02 | toàn series | Exact date, travel duration/route, địa điểm bền vững hoặc causal order vượt partial order hiện có. |
| WG-03 | Quyển I–V | Cơ chế, quyền sở hữu/custody, chân tướng cuối hoặc công năng bền vững của Du Long Giác. |
| WG-04 | V2-CH-21 | Người gọi ba POV, venue, dialogue, combat, custody, outcome và thay đổi quan hệ bền vững của first convergence. Row này chỉ có R-67 + R-74, không có SQLite receipt. |
| WG-05 | Quyển IV | Muốn hòa giải T330 với T352, giải “bí mật thứ hai”, hoặc biến testimony/game-alt-history Đại Lý thành history/canon profile. |
| WG-06 | V5-CH-20 | Placement của bi kịch Tĩnh Xuyên–Ân Đồng. Killer, outcome và trách nhiệm của Tĩnh đã khóa tuyệt đối; hung khí, ngày và route logistics vẫn mở. |
| WG-07 | V5-CH-27–28 | Loại corroboration độc lập ngoài Huyễn Cảnh cho thân thế Minh Dương–Tố Trinh–Nhạc gia. T400/T457 không đủ để tự giải gate. |
| WG-08 | V5-CH-32–35 | Custody/end-state, bí mật quân bị, cơ chế chữa trị hoặc closure hậu truyện vượt trạng thái “sóng gió tạm lắng”. |

Không hỏi Tác giả để duyệt lại count, POV aperture, tên làm việc hoặc chapter function đã ghi. Nếu một gate chưa cần cho đoạn đang viết, giữ khoảng mở và tiếp tục.

## Kết quả kiểm tất định

- 140 row sequence và 140 row ledger; từng quyển khớp 25/24/28/28/35.
- POV chuẩn hóa khớp 52 Tĩnh / 50 Tiêu / 38 Hạ.
- 193 lượt locator đều resolve vào packet được khai báo; 183 locator `T/S` duy nhất.
- 0 exact locator dùng xuyên quyển; 0 Task ID dùng xuyên quyển.
- 9 locator reuse nội quyển đã được liệt kê và có guard.
- `V2-CH-21` là row duy nhất decision-only; không được dùng làm chứng cứ cho game fact.

## Boundary

Index này không tạo scene, beat, dialogue, prose, chronology, canon, source claim mới hoặc chapter brief mới. Foundation claim audit toàn repository vẫn là công việc riêng chưa hoàn tất.

[Gemini Chapter Workflow Router](gemini-chapter-workflow-router.md) hiện là contract thi hành toàn series: nó đọc index này, tự dựng preflight cục bộ theo chapter đang viết và chỉ phát câu hỏi khi chạm `WG-*`; không sinh sẵn 140 packet hoặc scene plan.
