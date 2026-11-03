# An toàn mạng máy tính

Ngân hàng 316 câu chọn lọc theo đề cương học phần 2022 và slide Bài 1–6. Đây không phải đề thi chính thức.

- Số câu theo chương 1–6: 28, 67, 63, 63, 66, 29.
- 30 câu được biên tập lại từ ngân hàng công khai tại `https://pttp-huitquiz.site/`; 286 câu được biên soạn theo đề cương và slide.
- Các câu cùng `family` là biến thể của một khái niệm. Bộ chọn đề ngẫu nhiên lấy tối đa một biến thể từ mỗi `family` khi đề có tối đa 100 câu.
- Bỏ các biến thể định nghĩa trùng với câu tình huống và các ví dụ trùng trực tiếp với câu vận dụng. Bộ còn 220 nhóm `family`; 96 nhóm có hai góc hỏi khác nhau. Câu vận dụng cùng khái niệm được gắn chung `family` để một đề không lấy cả hai.
- 60 câu tình huống vận dụng được biên tập riêng từ đề cương/slide.
- Đề mặc định 50 câu và 50 phút, chia theo chương 5/10/10/10/10/5; trong đó 24 câu được lấy từ nhóm tình huống vận dụng.
- Đây là mục tiêu cân bằng cách luyện, không phải ước tính xác suất trúng đề thi thật.

`questions.js` là dữ liệu tĩnh để GitHub Pages dùng trực tiếp. Có thể tạo lại từ JSON nguồn bằng:

```text
python tools/convert_atm_bank.py path/to/an_toan_mang_chon_loc.json
```

Hai tệp Scribd Summary người dùng cung cấp trước đó không có toàn văn câu hỏi/đáp án, nên ngân hàng này chưa thể được đối chiếu trực tiếp với chúng. Các mục pháp luật và phiên bản tiêu chuẩn ở Chương 6 được trình bày theo đề cương 2022, không dùng làm tài liệu pháp lý hiện hành.
