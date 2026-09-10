---
name: dlg-source-revision
description: Sửa bản thảo Du Long Giác theo findings đã xác minh và kiểm lại nguồn, continuity.
---

# dlg-source-revision

Mọi path bên dưới tính từ repository root du-long-giac-2.
Bắt buộc đọc docs/playbooks/gemini-evidence-review.md trước khi thực hiện. Đây là contract chung cho authority, receipts, author gates, output paths và kiểm chứng; chỉ load resources liên quan chapter.

1. Đọc hướng dẫn chung cùng current manuscript, review, preflight, source receipts và author instructions mới nhất.
2. Kiểm finding có đúng dòng hiện tại và có evidence trước khi sửa. Không phục hồi bản agent cũ lên văn tác giả. Nếu review cũ lệch manuscript, review lại đoạn liên quan trước.
3. Sửa cục bộ những lỗi được yêu cầu; mặc định tạo revised.md để tác giả đối chiếu. Sửa trực tiếp khi tác giả đã yêu cầu rõ. Không rewrite cả chương cho lỗi một đoạn.
4. Canon/Bridge conflict không có quyết định thì hỏi kèm hai nguồn; vẫn sửa findings độc lập. Không tự đổi outcome, knowledge hoặc lấp open slot.
5. Đọc lại toàn văn sau sửa, rà claim mới và dependency, làm mới coverage/line spans và run guards như hướng dẫn chung.
6. Giao bản sửa, resolved/unresolved findings và checks. Không tự promote canon, ghi approval hay commit.

