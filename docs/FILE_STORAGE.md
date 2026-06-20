# Lưu PDF/DOCX ở đâu?

Hiện tại dùng GitHub Pages nên tài liệu public có thể lưu ở:

```text
assets/docs/
```

Ví dụ:

```text
assets/docs/he-dieu-hanh.pdf
assets/docs/ngan-hang-cau-hoi.docx
```

Link trong HTML:

```html
<a href="./assets/docs/he-dieu-hanh.pdf">Tải PDF</a>
```

Không nên lưu file riêng tư trong repo public.
Sau này nếu có backend/cloud thì chuyển sang storage riêng.
