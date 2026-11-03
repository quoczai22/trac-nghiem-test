# An toàn mạng máy tính

Ngân hàng 440 câu theo đề cương học phần 2022 và slide Bài 1–6 (cả bản cũ lẫn bản cập nhật). Đây không phải đề thi chính thức.

- Số câu theo chương 1–6: 36, 74, 83, 84, 99, 64.
- 30 câu được biên tập lại từ ngân hàng công khai tại `https://pttp-huitquiz.site/`; các câu còn lại được biên soạn theo đề cương và slide.
- Các câu cùng `family` là biến thể của một khái niệm. Bộ chọn đề ngẫu nhiên lấy tối đa một biến thể từ mỗi `family` khi đề có tối đa 100 câu. Bộ hiện có 310 nhóm `family`.
- 60 câu tình huống vận dụng (`application`) được biên tập riêng từ đề cương/slide.
- 75 câu chữ viết tắt (`acronym`) phủ cả 6 chương, ví dụ CIA, RAT, ICV, NGFW, SASE, ZTNA, SIEM, EDR, SAE, PMF, OWE, TOE, EAL, PCI DSS, FIPS.
- 45 câu về chuẩn (`standard`): IEEE 802.11i/802.11w/802.11ax/802.11be, 802.1X/EAP/RADIUS ở Chương 5; ISO/IEC 27001/27002 qua các phiên bản 2005/2013/2022, 27005, 27701, 42001, 15408, 13335, PCI DSS, FIPS 140-2/140-3, NIST CSF 2.0 và luật Việt Nam ở Chương 6.
- 90 câu phân biệt (`distinction`) được viết lại thành câu hỏi thẳng, mỗi câu một ý cụ thể, bám slide khi slide có nội dung (`tools/atm_direct.py`).
- Đề mặc định 50 câu và 50 phút, chia theo chương 5/10/10/10/10/5; trong đó 14 câu vận dụng và 10 câu chữ viết tắt.
- Đây là mục tiêu cân bằng cách luyện, không phải ước tính xác suất trúng đề thi thật.

Đề cương 2022 nêu ISO/IEC 27001/27002:2005, ISO/IEC 13335 và FIPS 140-2, còn slide Bài 6 bản cập nhật dùng 27001/27002:2022, FIPS 140-3 và luật 2025. Câu hỏi luôn ghi rõ phiên bản hoặc nguồn ("theo slide cập nhật") để không có hai đáp án cùng đúng.

`questions.js` là dữ liệu tĩnh để GitHub Pages dùng trực tiếp. Có thể tạo lại từ JSON nguồn bằng lệnh dưới; lệnh này tự gộp phần bổ sung trong `tools/atm_supplement.py` và bỏ các câu được liệt kê trong `REMOVE_IDS`:

```text
python tools/convert_atm_bank.py path/to/an_toan_mang_chon_loc.json
```

Hai tệp Scribd Summary người dùng cung cấp trước đó không có toàn văn câu hỏi/đáp án, nên ngân hàng này chưa thể được đối chiếu trực tiếp với chúng. Các mục pháp luật ở Chương 6 lấy theo slide bài giảng, không dùng làm tài liệu pháp lý.
