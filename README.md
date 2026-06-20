# Trắc nghiệm Test

Web trắc nghiệm local/publish cho ngân hàng câu hỏi.

GitHub Pages:

```text
https://quoczai22.github.io/trac-nghiem-test/
```

## Cấu trúc hiện tại

```text
index.html
stylesmain.css
subjects/he-dieu-hanh/
admin/import-export.html
admin/admin.css
admin/admin.js
.github/workflows/deploy-pages.yml
docs/
demo/
assets/docs/
```

## Chức năng đã gộp đúng

- Trang chủ chọn môn.
- Môn Hệ điều hành đang có sẵn.
- Admin import/export local.
- Import nhiều file PDF/DOCX/TXT/JSON/JS.
- Import có lựa chọn Tất cả/Tổng ôn/Không chọn chương cho file tổng ôn.
- Import chỉ thêm vào bộ đề đang có, không thay toàn bộ.
- Export theo 3 nguồn:
  - Chỉ bộ đề mặc định.
  - Chỉ các file đã import.
  - Gộp mặc định + tất cả file đã import.
- Export `questions.js`.
- Export `questions.json`.
- Export Word `.doc`.
- Export PDF bằng cửa sổ in, chọn `Save as PDF`.
- CI/CD GitHub Pages bằng GitHub Actions.
- Tài liệu PDF/DOCX public để trong `assets/docs/`.
- Backend/cloud/database để trong `demo/future-cloud-backend/` cho hè nghiên cứu sau.

## Push lên GitHub

```bash
git add .
git commit -m "Update import export and GitHub Pages deploy"
git push
```

Nếu GitHub Pages dùng GitHub Actions, workflow sẽ tự deploy.
