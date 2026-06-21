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
2. Nếu còn câu thiếu đáp án, bấm AI/Ollama gợi ý đáp án thiếu.
3. Kiểm tra preview.
4. Merge draft.

AI chỉ gợi ý, không tự merge.
