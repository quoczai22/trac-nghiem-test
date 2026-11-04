# An toàn mạng máy tính

Ngân hàng 414 câu theo đề cương học phần 2022 và slide Bài 1–6 (cả bản cũ lẫn bản cập nhật). Đây không phải đề thi chính thức.

- Số câu theo chương 1–6: 40, 52, 81, 81, 98, 62.
- 30 câu được biên tập lại từ ngân hàng công khai tại `https://pttp-huitquiz.site/`; các câu còn lại được biên soạn theo đề cương và slide.
- Các câu cùng `family` là biến thể của một khái niệm. Bộ chọn đề ngẫu nhiên lấy tối đa một biến thể từ mỗi `family` khi đề có tối đa 100 câu. Bộ hiện có 311 nhóm `family`.
- 57 câu tình huống vận dụng (`application`) được biên tập riêng từ đề cương/slide.
- 75 câu chữ viết tắt (`acronym`) phủ cả 6 chương, ví dụ CIA, RAT, ICV, NGFW, SASE, ZTNA, SIEM, EDR, SAE, PMF, OWE, TOE, EAL, PCI DSS, FIPS.
- 45 câu về chuẩn (`standard`): IEEE 802.11i/802.11w/802.11ax/802.11be, 802.1X/EAP/RADIUS ở Chương 5; ISO/IEC 27001/27002 qua các phiên bản 2005/2013/2022, 27005, 27701, 42001, 15408, 13335, PCI DSS, FIPS 140-2/140-3, NIST CSF 2.0 và luật Việt Nam ở Chương 6.
- 9 câu về số cổng, chỉ lấy cổng slide nêu trong nội dung: 21 (FTP Trojan), 25, 80, 443, 31337 (Back Orifice), cùng Port scan và `netstat -ano`. Bảng 70 cổng Trojan không được đưa vào.
- 14 câu tường lửa cho các phần Bài 3 trước đó chưa có câu: chức năng, sản phẩm, kiến trúc đơn lẻ/kết hợp, multi-homed, hybrid mesh, NetworkPolicy/eBPF, lưu lượng mã hóa, AI/ML.
- Đã bỏ 37 câu dư thừa: mã độc slide không dạy (rootkit, ransomware, botnet, logic bomb, cryptojacking, fileless), nhãn không có trong slide (Rule order, Change review, ACL) và câu hỏi lặp lại đúng một ý của câu khác. Danh sách nằm trong `REMOVE_IDS`.
- Chương 3 đã bỏ thêm 24 câu: câu tình huống có đáp án là nhãn slide không dùng ("Mạng ngoài", "Mạng nội bộ", "Logging firewall", "Network firewall", "Proxy web", "Tường lửa máy chủ", ACL) và câu hỏi lại đúng ý của câu khác. Thêm 12 câu về nguyên tắc và quy trình thiết kế tường lửa trong slide Bài 3 bản cập nhật (`tools/atm_design_c3.py`).
- Các câu phân biệt (`distinction`) được viết lại thành câu hỏi thẳng, mỗi câu một ý cụ thể, bám slide khi slide có nội dung (`tools/atm_direct.py`).
- Mỗi câu có lời giải thích vì sao đáp án đúng (`explanation`) và vì sao từng đáp án sai là sai (`optionNotes`), viết trong `tools/atm_explain_c1.py`…`atm_explain_c6.py`. Sau khi nộp bài, câu đúng chỉ hiện lý do đúng; câu sai hiện thêm lý do đáp án đã chọn sai.
- Đề mặc định 50 câu và 50 phút, chia theo chương 5/10/10/10/10/5; trong đó 14 câu vận dụng và 10 câu chữ viết tắt.
- Đây là mục tiêu cân bằng cách luyện, không phải ước tính xác suất trúng đề thi thật.

Đề cương 2022 nêu ISO/IEC 27001/27002:2005, ISO/IEC 13335 và FIPS 140-2, còn slide Bài 6 bản cập nhật dùng 27001/27002:2022, FIPS 140-3 và luật 2025. Câu hỏi luôn ghi rõ phiên bản hoặc nguồn ("theo slide cập nhật") để không có hai đáp án cùng đúng.

`questions.js` là dữ liệu tĩnh để GitHub Pages dùng trực tiếp. Có thể tạo lại từ JSON nguồn bằng lệnh dưới; lệnh này tự gộp phần bổ sung trong `tools/atm_supplement.py` và bỏ các câu được liệt kê trong `REMOVE_IDS`:

```text
python tools/convert_atm_bank.py path/to/an_toan_mang_chon_loc.json
```

Hai tệp Scribd Summary người dùng cung cấp trước đó không có toàn văn câu hỏi/đáp án, nên ngân hàng này chưa thể được đối chiếu trực tiếp với chúng. Các mục pháp luật ở Chương 6 lấy theo slide bài giảng, không dùng làm tài liệu pháp lý.
