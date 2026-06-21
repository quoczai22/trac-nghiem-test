# Trắc nghiệm Test

Web trắc nghiệm local/publish cho ngân hàng câu hỏi.

GitHub Pages:https://quoczai22.github.io/trac-nghiem-test/

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


## AI Import Workflow

Đã thêm workflow import an toàn:

```text
Phân tích file -> tạo draft -> Ollama gợi ý đáp án thiếu -> preview -> merge
```

File liên quan:

```text
admin/import-export.html
admin/admin.js
tools/ollama-helper/server.js
docs/AI_IMPORT_WORKFLOW.md
```

Lưu ý: AI chỉ gợi ý đáp án, không tự merge và không replace bộ đề gốc.

## Mở AI Import một chạm trên Windows

Nhấp đúp [Chay-AI-Import.cmd](./Chay-AI-Import.cmd). Script sẽ kiểm tra helper có hỗ trợ AI parse fallback,
thay helper cũ ở cổng `3100` nếu cần, rồi mở trang Admin. Ollama (`http://localhost:11434`) vẫn cần được cài và chạy trên máy.
