# An toàn mạng máy tính

Ngân hàng 500 câu luyện tập theo đề cương học phần 2022 và slide Bài 1–6. Đây không phải đề thi chính thức.

- Chương 1 và 6: mỗi chương 50 câu.
- Chương 2–5: mỗi chương 100 câu.
- 30 câu được biên tập lại từ ngân hàng công khai tại `https://pttp-huitquiz.site/`; 470 câu được biên soạn theo đề cương và slide.
- Các câu cùng `family` là biến thể của một khái niệm. Bộ chọn đề ngẫu nhiên lấy tối đa một biến thể từ mỗi `family` khi đề có tối đa 100 câu.
- 60 câu tình huống vận dụng được biên tập riêng từ đề cương/slide, thay cho 60 biến thể lặp. Bộ dữ liệu nay có 248 nhóm `family`.
- Đề mặc định 50 câu và 50 phút, chia theo chương 5/10/10/10/10/5; trong đó 24 câu được lấy từ nhóm tình huống vận dụng.
- Đây là mục tiêu cân bằng cách luyện, không phải ước tính xác suất trúng đề thi thật.

`questions.js` là dữ liệu tĩnh để GitHub Pages dùng trực tiếp. Có thể tạo lại từ JSON nguồn bằng:

```text
python tools/convert_atm_bank.py path/to/an_toan_mang_500_cau.json
```

Hai tệp Scribd Summary người dùng cung cấp trước đó không có toàn văn câu hỏi/đáp án, nên ngân hàng này chưa thể được đối chiếu trực tiếp với chúng. Các mục pháp luật và phiên bản tiêu chuẩn ở Chương 6 được trình bày theo đề cương 2022, không dùng làm tài liệu pháp lý hiện hành.
