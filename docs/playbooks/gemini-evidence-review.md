> Current temporal/creative authority: migration/restructure_2026_09/temporal-continuity-contract.md and migration/restructure_2026_09/temporal-character-framework.md (D-064/R-90 and D-065/R-91). Read both before chapter operations. Framework direction is not evidence for an in-world claim.

# Gemini — kiểm chứng bản thảo theo nguồn

Áp dụng cho continuity restructure_2026_09. Mọi đường dẫn dưới đây tính từ repository root.
D-063/R-89 ghi việc Tác giả cho phép bổ sung workflow và skills; không phải phê duyệt bất kỳ fact/scene/prose mới.

## Authority và phạm vi

Đầu lượt đọc AGENTS.md, author/session-state.md, story.md, các quyết định liên quan trong author/decision-log.md và migration/restructure_2026_09/author-decisions.md; sau đó đọc router và index trong cùng thư mục migration. Chỉ tải profile/state/style liên quan chapter; state không hiện hữu hoặc chưa được duyệt phải ghi UNKNOWN.
Khi `canon-registry/` có row liên quan, dùng nó như locator và mở raw receipt/decision trước khi kết luận. Registry rỗng hoặc thiếu row không chứng minh absence; `AUTHOR_DIRECTION` và open slot không là fact row.
Các hướng dẫn cũ trong docs/WORKFLOW.md, .agents/rules/05-review.md và templates/review-report.md không được tái áp đặt exact date, tự split a/b/c, quota hài hoặc closed-world cấm mọi Bridge đã duyệt trái quyết định restructure. Tái dùng định dạng verifier, nhưng giữ nguyên các khoảng mở của author.
Nếu có xung đột authority thực sự chưa được quyết, trình hai bằng chứng cho Tác giả; không tự chọn nguồn thắng.

Preflight/source research/review được làm ngay theo yêu cầu. Lệnh write không tự gỡ freeze scene/prose: tìm đúng quyết định mở cổng cho chapter; nếu thiếu, làm phần preflight hữu ích và báo chính xác cổng còn thiếu. Review một bản thảo chưa được duyệt vẫn được phép.
Wording, cảm giác và micro-action không tạo durable state không cần receipt. Một động tác hàm ý có võ học, chữa khỏi, có vật phẩm, ở một địa điểm mới hoặc biết bí mật vẫn là claim bền vững.

## Gói làm việc tối thiểu

Ưu tiên artifact chapter hiện hữu được người dùng chỉ định. Nếu chưa có, dùng research/chapter-work/V1-CH-001/ (thay bằng key thật từ allocation; Quyển I dùng 3 chữ số, II–V dùng 2).
Trong đó chỉ tạo file khi cần: preflight.md; evidence.json; claims.json; review.md; revised.md. Prose mới, khi được phép, có thể lưu draft.md. Không chuyển bản viết vào canon tự động.
Một claim ledger đủ cho chương; review ghi claim bỏ sót và verdict trong review.md trước khi sửa ledger. Không ghi đè bản tác giả để làm khớp nguồn.

Receipt đầy đủ cho mỗi durable claim gồm: proposition; game fact/historical fact/game alt-history/report/inference/Bridge; subject, predicate, negation, certainty; source file/table/field/ID; query và bind hoặc đường dẫn chính xác tới query đã lưu; trích xuất nguyên văn; speaker/recipient; branch/flag; knowledge receiver; decision ID và scope nếu có.
Đọc toàn subtask liên quan gồm describe, steps và dialogues, không chỉ excerpt thuận lợi. Nếu cần mở rộng, truy family/condition liên quan có mục tiêu. Không dùng một báo cáo NPC như xác nhận narrator.

## Review nguồn độc lập với lời tự giải thích của writer

1. Đọc bản manuscript HIỆN TẠI tuần tự L1 đến EOF. Đọc từng đoạn vừa đủ, không dùng rg hay summary thay toàn văn. Ghi coverage không hở, mỗi range tối đa 120 dòng kèm nhận xét thật. Nếu chưa đọc hết: INCOMPLETE, nêu đoạn chưa đọc.
2. Tự trích claim từ văn bản trước khi đọc verdict/self-check của writer. Bao gồm quan hệ, động cơ được narrator xác nhận, sở hữu, hành động, hậu quả, tình trạng thương tật, võ học, thời gian, tri thức, lời hứa và các tiền giả định. “Lại sử dụng thanh kiếm của cha” chứa cả sở hữu, phả hệ và tiền sử sử dụng.
3. Đối soát hai chiều: mọi claim trong prose phải có căn cứ; mọi requirement của chapter phải được thực hiện hoặc ghi thiếu. Claim có ledger nhưng prose không sử dụng không được tính là đã kiểm toàn chương.
4. Mở lại raw source và quyết định của author cho từng claim. Trích cả span bản thảo và span nguồn. Tên nhân vật đúng, locator tồn tại và excerpt khớp chưa chứng minh quan hệ/diễn biến là đúng.
5. Kiểm độc lập POV đã nhận tin bằng kênh nào, khi nào; source/reader biết không đồng nghĩa POV biết. Đối chiếu chương trước đã được author chấp nhận, state liên quan và handoff quyển. Không coi draft trước là canon.
6. Đối chiếu mọi WG trong index VÀ writer boundary của chapter VÀ open slots liên quan. WG không phải danh sách đóng; medical/combat/relationship/identity chưa có căn cứ vẫn phải phát hiện.
7. Review craft riêng: causal progression, agency người ngoài trio, living wulin, khẩu khí, nhịp và chức năng kết chương. Fact đúng không đồng nghĩa truyện hay; không chế lỗi để đủ quota. Tastes là recommendation, không phải canon conflict.

Ưu tiên review trong một conversation Gemini mới để giảm ảnh hưởng lập luận của writer; người dùng mở thủ công và đưa key, manuscript path, preflight path. Cùng model vẫn dùng được. Nếu cùng conversation, ghi SAME-CONTEXT SELF-REVIEW; không tự nhận là independent review. Không tự gọi API, tiêu quota thêm hoặc tạo task.

## Verdict cho từng claim

| Verdict | Ý nghĩa và xử lý |
| --- | --- |
| SUPPORTED | Đúng proposition, scope, condition và certainty; vẫn chưa là novel canon nếu chưa được author chọn. |
| ATTRIBUTED_ONLY | Nguồn chỉ xác nhận ai nói/tin điều đó; prose chỉ được giữ đúng attribution và kênh tiếp nhận. |
| APPROVED_BRIDGE | Quyết định author thật, đúng phạm vi; không gọi là game fact. |
| OVERSTATED | Nguồn hẹp hơn prose; chặn PASS tới khi giảm claim hoặc author quyết. |
| UNSUPPORTED | Chưa có evidence cho claim; chặn PASS, không kết luận nguồn chứng minh claim sai. |
| CONTRADICTED | Có evidence/decision xung đột trực tiếp; ghi cả hai, chặn PASS. |
| UNCHECKED | Thiếu quyền đọc, nguồn, thời gian kiểm hoặc context; INCOMPLETE, không PASS. |

Bảng audit trong review.md phải có claim ID, manuscript Lx-Ly + quote, proposition, source path/field/node + quote, decision, verdict, lý do entailment và intervention. Bắt cả câu thoại tạo lời hứa/sự kiện/tri thức mới; không chặn một nhân vật nói sai nếu sai lầm đó được phép và không bị narrator xác nhận.
Tĩnh Xuyên/Mộc Nhất Lâu tự tay giết Ân Đồng và chịu trách nhiệm là invariant tuyệt đối; không sửa thành bẫy, tai nạn hoặc người khác giết. Placement/hung khí chưa chọn vẫn giữ mở.

## Kiểm máy hiện có

Dùng schema templates/evidence-packet.json và templates/claim-ledger.json khi xuất JSON. Không truyền bảng Markdown vào claim-guard.
Schema legacy không có SOURCE_REPORT: encode proposition “NPC A nói P” là DIRECT_SOURCE và ghi attribution ở reasoning; không encode P là truth. Bridge dùng NOVELIZATION_BRIDGE/ADAPTATION_DECISION + decision_ref/scope trong reasoning hoặc trường bổ sung. promotion=author_approval_required là trạng thái canon; approval planning không tự là canon approval. Không tạo dòng author approval giả để qua regex.
Claim UNSUPPORTED/UNCHECKED dùng UNRESOLVED, promotion=blocked, durability=ephemeral để biểu thị chưa được nhận làm truth; ghi intended_durability=durable và verdict riêng. Nếu cả evidence list rỗng, structural PASS không có nghĩa đã kiểm source.

Chạy với path thật, từ root, trên PowerShell:
```powershell
$env:PYTHONUTF8='1'
$env:PYTHONIOENCODING='utf-8'
python scripts/claim-guard.py --chapter V1-CH-001 --evidence research/chapter-work/V1-CH-001/evidence.json --claims research/chapter-work/V1-CH-001/claims.json --db migration/source_corpus/01_Database/story_database.sqlite3
python scripts/review-guard.py --chapter-number V1-CH-001 --chapter research/chapter-work/V1-CH-001/draft.md --review research/chapter-work/V1-CH-001/review.md
```
Xác minh DB/path tồn tại trước chạy; dùng DB identity của packet, không ngầm chọn database khác.
claim-guard kiểm locator/excerpt/structure; review-guard kiểm khai báo coverage và trích đoạn. Không công cụ nào chứng minh Gemini đã hiểu đúng nghĩa hoặc rà hết claim.
Báo tên check, exit status và phạm vi; không dùng execution:check/file_nonempty hay “no files found” thay review.

## Định dạng review và điều kiện hoàn tất

Review có: current manuscript path, chapter key, context mode, authority đọc, audit claim, requirement/continuity gaps, findings và checks.
Tái dùng headings máy đọc:
- `## Full-Read Coverage` với `L1-L120` và các range thật cho đến EOF.
- `### Gate A:` provenance/canon/knowledge; B: causality; C: agency/state; D: voice; E: density/function. Mỗi gate **PASS**/**FAIL**; phần chưa kiểm ghi FAIL + INCOMPLETE, không bịa lỗi.
- Ít nhất bốn evidence spans cho full chapter, mỗi span có **Vị trí**: `Lx-Ly` và **Trích đoạn**: nguyên văn đúng range. Không bịa thương tật nếu chương không có.
- Findings: severity, location, problem, evidence, why it matters, smallest intervention, needs_author.
- Cuối báo `SEMANTIC_REVIEW: PASS | REVISE_REQUIRED | INCOMPLETE` và `AUTHOR_ACCEPTANCE: PENDING`.

Nếu dùng parser legacy, **APPROVED** chỉ là recommendation của reviewer khi mọi gate pass; ghi ngay rằng không phải author approval. Còn blocker/unchecked dùng **REVISE_REQUIRED**. Không được xóa blocker khỏi báo cáo để qua verifier.
Chỉ đạt semantic PASS khi đã đọc hết, kiểm đủ claim và requirement, không còn unsupported/overstated/contradicted/unchecked hoặc authority gap. Một tuyên bố self-check không thay bằng chứng.

## Sửa và kiểm lại

Khi người dùng yêu cầu sửa, sửa đúng findings trong phạm vi được phép. Ưu tiên bản revised.md nếu tác giả chưa yêu cầu sửa trực tiếp manuscript. Xóa/hạ certainty một claim do agent bịa khi được yêu cầu sửa lỗi; không thay nó bằng một lore mới.
Nếu sửa buộc chọn canon/Bridge chưa quyết: hỏi một câu có evidence, vẫn xử lý findings độc lập.
Sau sửa, đọc toàn văn mới, kiểm lại claim ở vùng sửa và các dependency bị ảnh hưởng, làm mới line spans/coverage. Ghi finding resolved hoặc còn mở; không giữ PASS cũ cho nội dung đã đổi.
