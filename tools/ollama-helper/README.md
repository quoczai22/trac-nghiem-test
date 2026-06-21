# Ollama Helper

Helper local cho chức năng Import AI.

GitHub Pages không nên gọi Ollama trực tiếp, nên dùng helper này làm lớp trung gian.

## Cài Ollama model

```bash
ollama pull qwen2.5:7b
```

Có thể dùng model khác:

```bash
ollama pull qwen3:8b
ollama pull llama3.1:8b
```

## Chạy helper

```bash
cd tools/ollama-helper
node server.js
```

Mặc định chạy tại:

```text
http://localhost:3100
```

Sau đó mở:

```text
admin/import-export.html
```

Quy trình:

1. Phân tích file / tạo draft.
2. Nếu rule parser không tách được câu nào từ PDF/DOCX/TXT, Admin tự gửi raw text đến `POST /api/ai/parse-questions` để Ollama tách câu hỏi và gợi ý đáp án.
3. Nếu parser đã tách được câu nhưng còn thiếu đáp án, bấm AI/Ollama gợi ý đáp án thiếu.
4. Kiểm tra preview.
5. Merge draft.

AI chỉ gợi ý, không tự merge.

## API parse fallback

```http
POST /api/ai/parse-questions
Content-Type: application/json
```

```json
{
  "model": "qwen2.5:7b",
  "text": "Nội dung thô từ PDF/DOCX/TXT",
  "subject": "Hệ điều hành",
  "chapter": "Chương 1"
}
```

API chỉ trả những câu có đủ bốn lựa chọn A/B/C/D. Kết quả vẫn là draft để người dùng xem trước rồi mới Merge.
