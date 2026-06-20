# GitHub Pages Deploy

Nguồn hiện tại đã có:

```text
index.html
stylesmain.css
subjects/he-dieu-hanh/index.html
subjects/he-dieu-hanh/app.js
subjects/he-dieu-hanh/questions.js
subjects/he-dieu-hanh/styles.css
admin/import-export.html
admin/admin.css
admin/admin.js
```

## Nếu GitHub Pages đang bật theo branch

Chỉ cần:

```bash
git add .
git commit -m "Update quiz website"
git push
```

## Nếu dùng GitHub Actions

1. Vào repo -> Settings -> Pages.
2. Source chọn **GitHub Actions**.
3. Push lên `main`.
4. Workflow `.github/workflows/deploy-pages.yml` sẽ tự deploy.

Web:

```text
https://quoczai22.github.io/trac-nghiem-test/
```
