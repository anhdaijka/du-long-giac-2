# Antigravity — lệnh cho Du Long Giác

Mở đúng repository du-long-giac-2 trong Antigravity rồi dùng:

| Lệnh | Ví dụ | Kết quả |
| --- | --- | --- |
| /dlg-preflight | `/dlg-preflight Quyển I chương 01` | Preflight + receipt/claim cho chương hiện tại; câu hỏi nếu cần canon/Bridge chưa quyết. |
| /dlg-write | `/dlg-write V1-CH-001 theo preflight đã duyệt` | NON-CANON DRAFT khi có quyền scene/prose; nếu chưa có thì báo gate thật. |
| /dlg-review | `/dlg-review V1-CH-001 manuscript: <path thật>` | Đọc toàn văn, tìm claim, đối chiếu source và review craft; không sửa prose. |
| /dlg-revise | `/dlg-revise V1-CH-001 theo review: <path thật>` | Sửa cục bộ findings, kiểm lại claim và continuity, giữ văn tác giả. |

Skills tương ứng: dlg-source-preflight, dlg-source-writer, dlg-source-review, dlg-source-revision trong `.agents/skills/`. Workflow wrappers nằm ở `.agents/workflows/`; logic chung ở [contract review nguồn](playbooks/gemini-evidence-review.md). Skill descriptions giữ phạm vi riêng theo skill-creator; không tải toàn corpus hoặc nhân bản hướng dẫn vào mỗi lệnh.

Ưu tiên mở conversation Gemini mới cho `/dlg-review`, cung cấp chapter key, manuscript path, preflight path; reviewer tự đọc nguồn. Nếu review trong cùng conversation, báo SAME-CONTEXT SELF-REVIEW. Không bắt buộc nhà cung cấp/model khác.

Nếu menu slash chưa xuất hiện, mở conversation mới/kiểm tra Customizations của workspace. Có thể yêu cầu trực tiếp: “Đọc .agents/skills/dlg-source-review/SKILL.md và review file …”. Không cần cài package hay API key riêng. Chưa xác minh menu/lượt chạy Gemini trong Antigravity của Tác giả.

Đường dẫn theo [Google Skills](https://antigravity.google/docs/skills/) và [Google workflow migration](https://antigravity.google/docs/migration/workflows-to-skills): `.agents/skills/` và `.agents/workflows/`. Tài liệu Google hiện thông báo chuyển workflow sang skills; wrappers chỉ gọi skills để giữ một nơi bảo trì logic. Nếu phiên bản cũ chỉ nhận `.agent/workflows/`, xác nhận phiên bản trước khi thêm lớp tương thích; không nhân đôi file tự động.

Các kiểm tra máy tái dùng claim-guard (locator/excerpt/schema) và review-guard (coverage/span). Chúng không chứng minh mọi claim được Gemini tìm đủ hoặc hiểu đúng. Không thể cam kết zero hallucination; cần kiểm hành vi trên chương thật.

Bootstrap được chỉnh để giữ bốn project skills, và .gitignore cho phép Git quản lý chúng. Không chạy bootstrap để cài bộ workflow này.
