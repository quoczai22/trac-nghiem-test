# AI Import Workflow

Mục tiêu: import được nhiều loại tài liệu, kể cả tài liệu không có bảng đáp án rõ ràng.

## Luồng xử lý

```text
File PDF/DOCX/TXT/JSON/JS
    ↓
Rule-based parser
    ↓
Nếu nhận diện được đáp án: giữ lại
Nếu thiếu đáp án: đưa vào draft thiếu đáp án
    ↓
Ollama local gợi ý đáp án thiếu
    ↓
Preview + confidence
    ↓
Người dùng kiểm tra
    ↓
Merge vào bộ import
```

## Quy tắc an toàn

- Không Replace toàn bộ.
- Không tự merge kết quả AI.
- AI chỉ gợi ý đáp án.
- Câu thiếu đáp án sẽ không được merge nếu người dùng không xác nhận.
- Bộ đề gốc `questions.js` không bị sửa trực tiếp.

## DOCX có đáp án in đậm

Trang admin dùng `JSZip` để đọc trực tiếp `word/document.xml`.
Nếu một lựa chọn A/B/C/D có chữ in đậm thì hệ thống gán đáp án theo lựa chọn đó.

## Ollama

Chạy helper:

```bash
cd tools/ollama-helper
node server.js
```

Khuyên dùng:

```bash
ollama pull qwen2.5:7b
```
