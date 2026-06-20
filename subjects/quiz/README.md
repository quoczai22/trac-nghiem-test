# Generic Quiz Runner

Runner này chỉ dành cho các môn local được tạo từ `admin/import-export.html`.

- Nhận môn qua query string: `index.html?subject=<subject-id>`.
- Đọc metadata từ `shared/subjects-registry.js`.
- Đọc bộ câu đã lưu local tại `quiz_subject_<subject-id>_data`.
- Tách history, timer, answers và đề random theo từng `subject-id`.

Hệ điều hành giữ runner riêng tại `subjects/he-dieu-hanh/` để không làm thay đổi luồng đang ổn định ở Phase 1.
