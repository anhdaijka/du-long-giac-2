---
name: dlg-source-preflight
description: Dựng preflight một chương với claim receipt và kiểm nguồn trước khi viết.
---

# dlg-source-preflight

Mọi path bên dưới tính từ repository root du-long-giac-2.
Bắt buộc đọc docs/playbooks/gemini-evidence-review.md trước khi thực hiện. Đây là contract chung cho authority, receipts, author gates, output paths và kiểm chứng; chỉ load resources liên quan chapter.

1. Đọc hướng dẫn chung, router, index rồi sequence/ledger/packet đúng chapter. Giải key từ allocation, không đoán số.
2. Đọc author decisions/profile/state liên quan và toàn subtask gồm steps/dialogues. Receipt phải kèm raw excerpt và query/binds; tách game/report/history/Bridge và knowledge receiver.
3. Tạo preflight + evidence/claims JSON theo schema hiện có trong gói chapter. Query bổ sung chỉ read-only, theo đúng source identity; không suy từ clue hoặc Task ID.
4. Chạy claim-guard với paths cụ thể. Missing/overclaim phải ghi unresolved, không tự nhận READY vì JSON hợp lệ.
5. Đầu ra PREFLIGHT READY hoặc câu hỏi canon cần thiết, kèm open slots. Không yêu cầu duyệt lại các lựa chọn planning đã chốt. Không tạo scene/prose từ lệnh preflight.

