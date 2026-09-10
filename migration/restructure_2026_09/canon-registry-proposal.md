# Đề xuất Canon Registry tối thiểu

Trạng thái: `AUTHOR-DEFAULTED PLANNING / D-066 / NOT A REGISTRY / NOT CANON`. Đây là proposal thực hiện SQ-05/D-065: registry tăng dần, không chép lại corpus và không biến direction thành in-world fact.

## Mục tiêu

Cho Gemini một nơi tra cứu ngắn, có provenance, về state bền vững **đã được nhận**; vẫn bắt buộc mở source packet khi cần entailment. Registry không là database nguồn thứ hai, không thay chapter receipt và không cố tổng hợp toàn bộ canon/backstory ngay từ đầu.

## Authority và lớp dữ liệu

| Lớp | Có vào registry? | Điều kiện |
| --- | --- | --- |
| `GAME_FACT` | Có, theo proposition hẹp. | SQLite query/bind/result/excerpt, subject/predicate/certainty và branch/speaker scope. |
| `HISTORICAL_FACT` | Có. | Nguồn sử độc lập và provenance, không chỉ game row. |
| `APPROVED_BRIDGE` | Có. | Decision ID, scope, source ceiling và author approval thật. |
| `CANON_STATE` | Có. | Canon diff được Tác giả duyệt, state transition xác định. |
| `AUTHOR_DIRECTION` | Không. | D-065 framework là read-only constraint, không phải in-world assertion. |
| `SOURCE_REPORT` / `GAME_ALT_HISTORY` | Có dạng attributed assertion khi cần continuity. | Registry ghi ai nói/tin gì, không ghi proposition là objective truth. |
| `OPEN_SLOT` / `UNRESOLVED` | Không như fact row. | Chỉ index gate/open-slot ID trong `registry-open-slots.md`. |
| draft, inference chưa duyệt, locator, title task, memory | Không. | Giữ ở packet/research hoặc bỏ. |

## File layout đề xuất

```text
canon-registry/
  README.md                     # authority, query discipline, lifecycle
  registry-index.tsv            # one row per accepted proposition/state
  registry-open-slots.md        # only IDs, scope, hard-stop and decision link
  entities/                     # only when an accepted state needs a compact profile
  changes/                      # author-approved canon diff receipts, append-only
```

`canon-registry/` chưa được tạo trong D-066. Không tạo trước folders rỗng hoặc placeholder fact rows.

## Schema cho `registry-index.tsv`

| Field | Bắt buộc | Ý nghĩa |
| --- | --- | --- |
| `registry_id` | Có | ID ổn định, ví dụ `CF-TP-001`, không dùng Task ID. |
| `proposition` | Có | Một mệnh đề hẹp, không tóm tắt lore. |
| `subject` / `predicate` / `object_or_value` | Có | Claim atom để review được entailment. |
| `classification` | Có | Một lớp được phép trong bảng authority. |
| `certainty` | Có | `OBJECTIVE`, `ATTRIBUTED`, `APPROVED_BRIDGE`, `STATE`, không suy diễn. |
| `source_receipt` | Có khi có source | Packet + query/bind/result container/excerpt; không chỉ T/S. |
| `decision_ref` | Có khi Bridge/state | D/R và scope thật. |
| `branch_scope` / `knowledge_scope` | Có khi relevant | Nhánh, speaker/receiver hoặc `N/A` có lý do. |
| `effective_from` | Có | `SOURCE`, approved decision hoặc accepted chapter-state; không dùng ngày lịch. |
| `status` | Có | `ACTIVE`, `SUPERSEDED`, `RETRACTED`; không xóa history. |
| `supersedes` | Có | ID cũ hoặc `NONE`. |
| `notes` | Có | Giới hạn đọc: không phải source proof, relation open, v.v. |

Không có field “canon by summary”, “assumed timeline” hay “writer convenience”. Một row không trộn game fact và Bridge; nếu cùng proposition có hai lớp, lập hai row liên kết rõ.

## Open-slot index

`registry-open-slots.md` chỉ dùng dạng:

| Open-slot ID | Câu hỏi bị giữ mở | Authority | Gemini action |
| --- | --- | --- | --- |
| `OS-DLG-01` | Objective custody/cơ chế Du Long Giác | D-064/D-065 + relevant WG | Không chọn; hỏi khi chapter thật sự cần. |

Không ghi candidate answer, probability hay “best guess”. Các open slot đang có trong continuity detail, allocation WG/PF và framework chỉ được link, không copy lại thành truth.

## Lifecycle một claim

```text
source packet / author decision
        ↓
chapter-local receipt và review
        ↓
author-approved canon diff (nếu có durable state)
        ↓
append registry row + change receipt
        ↓
preflight/review đọc registry như locator, rồi mở raw evidence khi claim được dùng
```

Một `APPROVED_BRIDGE` phục vụ planning có thể vào registry chỉ nếu author decision nói rõ nó là state bền vững; nếu chỉ mở planning/preflight thì vẫn nằm ở decision/packet, không được promote.

## Gemini workflow sau khi registry tồn tại

1. Đọc index/router/framework trước, rồi query `registry-index.tsv` hẹp theo chapter need.
2. Mở row và raw source/decision của mọi claim định đưa vào prose; registry chỉ rút ngắn tìm kiếm.
3. Nếu không có row, Gemini không suy “không tồn tại”; quay lại packet/author decision hoặc ghi UNKNOWN.
4. Nếu cần state mới, tạo receipt/proposal hoặc canon diff theo gate; không tự append registry.
5. Reviewer inventory claim từ manuscript độc lập; registry row không thay semantic entailment check.

## CRQ — quyết định cần khi bắt đầu implementation

Không cần chốt ngay để giữ D-066 là planning. Khi tạo registry thật, Tác giả sẽ chỉ cần duyệt ba điểm sau:

| ID | Đề xuất |
| --- | --- |
| CRQ-01 | Khởi tạo registry rỗng, sau đó seed chỉ các accepted durable propositions thật sự cần cho chapter preflight đầu tiên. |
| CRQ-02 | Dùng TSV + Markdown change receipts trong Git; không thêm database/dependency mới. |
| CRQ-03 | Canon diff author-approved là write gate duy nhất cho `CANON_STATE`; game fact/approved Bridge có thể được đăng ký theo receipt nhưng không đổi state. |

## Out of scope

Không tạo registry files, seed facts, audit toàn Foundation, history/travel corpus, profile đầy đủ, scene, prose hay canon diff. D-066 không mở các cổng này.
