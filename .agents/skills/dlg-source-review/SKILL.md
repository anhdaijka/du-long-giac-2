---
name: dlg-source-review
description: Review toàn văn và fact của bản thảo Du Long Giác bằng đối chiếu nguồn độc lập với ledger writer.
---

# dlg-source-review

Mọi path bên dưới tính từ repository root du-long-giac-2.
Bắt buộc đọc docs/playbooks/gemini-evidence-review.md trước khi thực hiện. Đây là contract chung cho authority, receipts, author gates, output paths và kiểm chứng; chỉ load resources liên quan chapter.

1. Đọc hướng dẫn chung đầy đủ và prompts/roles/reviewer.md; dùng quy trình review nguồn trong hướng dẫn chung.
2. Review được phép dù prose chưa được duyệt. Xác định current manuscript path và chapter key; thiếu manuscript thì yêu cầu đúng file, không review theo summary.
3. Đọc L1–EOF rồi tự inventory durable claims trước khi xem verdict writer. Kiểm hai chiều prose→receipt và requirement→prose; bắt claim không có ledger.
4. Mở lại nguồn/decisions cho mỗi claim, rà conditions/negation/certainty/receiver, source conflicts và toàn bộ knowledge/state liên quan. Đọc steps/dialogues, không chỉ title/excerpt.
5. Lưu source-grounded audit và craft findings riêng trong review.md, dùng format tương thích review-guard của hướng dẫn chung. Không sửa manuscript/source/canon.
6. Chạy claim-guard cho evidence/claims JSON của review và review-guard với paths thật. Ghi limitation từng tool và INCOMPLETE nếu thiếu coverage.
7. Không cần cố tìm lỗi. Semantic PASS chỉ khi evidence thực sự đủ; machine PASS và reviewer APPROVED không có nghĩa tác giả phê duyệt.

