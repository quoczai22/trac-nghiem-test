EXPLAIN = {
    "gen_050": ("Virus gắn mã của nó vào một tệp chủ (ở đây là tệp thực thi) và lây khi tệp đó chạy.", {
        "B": "Trojan giả làm phần mềm hợp lệ và không sửa tệp khác để lây.",
        "C": "Worm tự lây qua mạng, không cần gắn vào tệp chủ.",
        "D": "Rootkit dùng để che giấu sự hiện diện của mã độc, không phải gắn mã lây vào tệp.",
    }),
    "gen_051": ("Theo slide, virus gắn vào một đối tượng chủ (tệp, cung boot, tài liệu) và lây khi chương trình chủ được chạy.", {
        "A": "Tự lây qua mạng mà không cần tệp chủ là đặc điểm của worm.",
        "B": "Ghi lại phím gõ là keylogger.",
        "C": "Virus phải sửa đối tượng chủ để gắn mã vào, nên tệp bị nhiễm có thay đổi.",
    }),
    "gen_054": ("Worm tự nhân bản và lây qua mạng mà không cần gắn vào tệp chủ; virus thì cần tệp chủ.", {
        "B": "Gắn vào tệp chủ và chờ người dùng mở là virus, ngược với worm.",
        "C": "Worm lây chủ yếu qua mạng, không chỉ qua đĩa mềm/USB.",
        "D": "Worm lây ồ ạt nên thường tiêu tốn nhiều băng thông.",
    }),
    "gen_057": ("Theo slide, Trojan không tự nhân bản như virus; nó nằm và chạy ngầm trong máy bị nhiễm để làm việc cho kẻ tấn công.", {
        "A": "Tự nhân bản và lây khắp LAN là đặc điểm của worm, không phải Trojan.",
        "C": "Trojan cố ẩn mình, không báo cho người dùng.",
        "D": "Lây trên cung boot là boot virus.",
    }),
    "gen_063": ("RAT cài phần server trên máy nạn nhân; hacker dùng phần client để kết nối và điều khiển từ xa.", {
        "B": "RAT không biến máy thành máy chủ DNS.",
        "C": "RAT mở đường vào cho hacker, ngược với tường lửa chặn kết nối.",
        "D": "Chỉ ghi phím là keylogger; RAT cho điều khiển toàn bộ máy.",
    }),
    "gen_066": ("Slide chia keylogger làm hai loại: phần cứng (thiết bị gắn giữa bàn phím và máy) và phần mềm (chương trình chạy ngầm).", {
        "B": "Boot và macro là các loại virus, không phải loại keylogger.",
        "C": "Slide không chia keylogger theo mạng và không dây.",
        "D": "Còn có keylogger phần cứng.",
    }),
    "gen_068": ("Lấy tệp cấu hình chứa mật khẩu đã lưu rồi gửi ra ngoài là việc của Trojan đánh cắp mật khẩu.", {
        "A": "RAT cho điều khiển từ xa toàn bộ máy; tình huống chỉ nói lấy mật khẩu đã lưu.",
        "B": "Backdoor là đường vào bí mật, không phải chương trình gom mật khẩu gửi đi.",
        "C": "Keylogger ghi phím gõ; ở đây mật khẩu lấy từ tệp cấu hình, không từ bàn phím.",
    }),
    "gen_069": ("Trojan ăn trộm password tìm tài khoản, mật khẩu trên máy (trình duyệt, IRC, ICQ...) rồi gửi cho kẻ tấn công.", {
        "A": "Mã hóa ổ cứng rồi đòi tiền chuộc là ransomware.",
        "B": "Làm quá tải băng thông là DoS/DDoS hoặc worm.",
        "D": "Mục tiêu là lấy thông tin, không phải phá hủy dữ liệu.",
    }),
    "gen_072": ("Backdoor (cửa hậu) là lối vào bí mật, bỏ qua xác thực thông thường, để kẻ tấn công quay lại hệ thống.", {
        "A": "Phần mềm diệt virus là công cụ bảo vệ, ngược với backdoor.",
        "B": "Bản vá lỗi dùng để sửa lỗ hổng, không phải lối vào bí mật.",
        "C": "Backdoor không phải cổng vật lý hay cổng dự phòng của router.",
    }),
    "gen_075": ("Spyware lén thu thập thông tin người dùng (thói quen duyệt web, tài khoản...) mà không xin phép.", {
        "A": "Tự nhân bản qua mạng là worm.",
        "C": "Phá cung boot là boot virus.",
        "D": "Spyware muốn máy vẫn kết nối để gửi dữ liệu đi, không chặn Internet.",
    }),
    "gen_087": ("Slide nêu Trojan thường xâm nhập qua file đính kèm email, phần mềm tải về, chat... người dùng tự mở.", {
        "A": "Bản cập nhật firmware chính hãng là nguồn tin cậy, không phải đường lây thường gặp.",
        "C": "Cáp nguồn chỉ cấp điện, không truyền dữ liệu.",
        "D": "Đèn báo trạng thái chỉ hiển thị, không truyền mã.",
    }),
    "gen_090": ("Macro virus viết bằng ngôn ngữ macro nên lây trên tài liệu Word, Excel, Access.", {
        "A": "Lây trên cung boot là boot virus.",
        "C": "Lây trên tệp .exe là file virus.",
        "D": "Registry không phải nơi macro virus lây nhiễm.",
    }),
    "gen_092": ("File lạ xuất hiện ngay sau khi cắm USB ngoài cho thấy mã độc đến từ USB.", {
        "A": "Macro độc hại đi kèm tài liệu Office được mở, không gắn với việc cắm USB.",
        "B": "Khai thác dịch vụ mạng lây qua cổng mạng, không qua USB.",
        "D": "Tệp đính kèm độc hại đến qua email.",
    }),
    "gen_093": ("Kiểm soát thiết bị ngoại vi và quét USB trước khi dùng chặn mã độc ngay từ cửa vào.", {
        "A": "USB 3.0 chỉ chép nhanh hơn, mã độc cũng chép nhanh hơn.",
        "B": "Dùng chung USB làm mã độc lây giữa nhiều máy hơn.",
        "D": "Tắt diệt virus khi cắm USB là bỏ lớp bảo vệ đúng lúc rủi ro nhất.",
    }),
    "gen_095": ("Worm dò các máy mở cùng một cổng có lỗi rồi khai thác lỗi đó để lây, tức khai thác dịch vụ mạng.", {
        "A": "Macro độc hại cần người dùng mở tài liệu Office.",
        "C": "Tệp đính kèm cần người dùng mở email; ở đây worm tự lây qua cổng.",
        "D": "USB lây qua thiết bị cắm vào, không qua cổng mạng.",
    }),
    "gen_096": ("Theo slide, Network Virus tự phát tán theo email bằng lệnh và các giao thức của mạng máy tính.", {
        "A": "Lây trên cung boot là boot virus.",
        "B": "Lây trên tập tin Word, Excel là macro virus.",
        "D": "Ghi đè mã vào tập tin chủ là cách của file virus, không phải network virus.",
    }),
    "gen_098": ("So khớp với mẫu mã độc đã lưu trong cơ sở dữ liệu là phát hiện theo chữ ký (signature).", {
        "A": "Phát hiện hành vi theo dõi việc chương trình làm khi chạy, không so mẫu đã lưu.",
        "B": "Sandbox chạy thử tệp trong môi trường cô lập.",
        "D": "Heuristic tìm đoạn mã đáng ngờ, kể cả mã độc chưa có mẫu.",
    }),
    "gen_099": ("Basic scanning tìm chữ ký (chuỗi byte đặc trưng) của virus đã biết trong tập tin.", {
        "B": "Quét đoạn mã đáng ngờ là heuristic scanning.",
        "C": "So giá trị ICV là ICV scanning.",
        "D": "Chạy trong máy ảo là phân tích sandbox.",
    }),
    "gen_101": ("Cờ cảnh báo vì cấu trúc mã bất thường (như tự giải mã) chứ không vì trùng mẫu đã biết là phát hiện heuristic.", {
        "A": "Phát hiện hành vi dựa vào việc chương trình làm khi chạy; ở đây bộ quét xét cấu trúc mã.",
        "B": "Sandbox phải chạy mẫu trong môi trường cô lập.",
        "C": "Chữ ký cần trùng mẫu đã biết; cấu trúc tự giải mã không phải một mẫu cụ thể.",
    }),
    "gen_102": ("Theo slide, heuristic scanning quét các đoạn mã đáng ngờ và hành vi của chương trình, nên bắt được cả virus chưa có chữ ký.", {
        "A": "Dựa vào chữ ký đã biết là basic scanning.",
        "C": "Giá trị ICV dùng cho ICV scanning.",
        "D": "Tên tệp và phần mở rộng rất dễ đổi, không phải cơ sở của heuristic.",
    }),
    "gen_104": ("Sửa hàng loạt tệp và liên lạc với máy lạ là những việc chương trình đang làm khi chạy, nên là phát hiện hành vi.", {
        "B": "Chữ ký so mẫu byte đã biết, không xét việc chương trình làm.",
        "C": "Heuristic xét đoạn mã đáng ngờ trong tệp; ở đây là hoạt động thực tế của ứng dụng.",
        "D": "Sandbox là chạy thử có chủ đích trong môi trường cô lập; ở đây ứng dụng chạy thật trên máy.",
    }),
    "gen_113": ("Ghi lại tiến trình, tệp và kết nối mà mẫu tạo ra khi chạy là phân tích động.", {
        "B": "Giá trị băm chỉ nhận dạng tệp, không cho biết mẫu làm gì.",
        "C": "Chỉ dấu xâm nhập (IoC) là kết quả dùng để phát hiện, không phải phương pháp quan sát mẫu.",
        "D": "Phân tích tĩnh xem mẫu mà không chạy nó.",
    }),
    "gen_116": ("Một tên miền điều khiển (C2) xuất hiện trên nhiều máy là dấu vết dùng để phát hiện xâm nhập, tức chỉ dấu xâm nhập (IoC).", {
        "A": "Giá trị băm mẫu nhận dạng tệp, không phải tên miền trong log.",
        "C": "Phân tích tĩnh là cách xem mẫu, không phải dấu vết trong log.",
        "D": "Phân tích động là chạy mẫu để quan sát.",
    }),
    "gen_128": ("Dựng lại tệp từ bản sao lưu offline sau khi bị mã hóa là khôi phục từ sao lưu.", {
        "A": "Cách ly máy nhiễm là ngắt khỏi mạng, không dựng lại dữ liệu.",
        "B": "Quarantine là cô lập tệp nghi nhiễm.",
        "C": "Phân tích nguyên nhân gốc là tìm đường xâm nhập.",
    }),
    "gen_131": ("Tìm lỗ hổng đã bị khai thác sau khi dọn mã độc là phân tích nguyên nhân gốc, để không bị nhiễm lại.", {
        "A": "Cách ly máy là bước khoanh vùng, làm trước khi dọn.",
        "B": "Quarantine chỉ cô lập tệp nghi nhiễm.",
        "D": "Khôi phục sao lưu là dựng lại dữ liệu, không tìm lỗ hổng.",
    }),
    "case_11": ("Tự dò máy khác và lây qua dịch vụ có lỗ hổng, không cần tệp chủ hay người dùng mở tệp, là worm.", {
        "B": "Virus gắn tệp cần tệp chủ và người dùng chạy tệp đó.",
        "C": "Logic bomb chỉ kích hoạt theo điều kiện, không tự lây.",
        "D": "Trojan cần người dùng tự cài và không tự nhân bản.",
    }),
    "case_12": ("Giả làm phần mềm có ích để được cài, mở đường điều khiển từ xa, không tự nhân bản: đúng đặc điểm Trojan.", {
        "B": "Virus macro lây trên tài liệu Office và tự nhân bản.",
        "C": "Worm tự nhân bản qua mạng.",
        "D": "Mã độc kích hoạt theo ngày là logic/time bomb, không nói đến việc giả phần mềm.",
    }),
    "case_13": ("Vẫn vào được dù đã đổi mật khẩu nghĩa là có lối vào bỏ qua xác thực, tức backdoor.", {
        "B": "Bản vá lỗi dùng để bịt lỗ hổng, không phải lối vào của kẻ tấn công.",
        "C": "Bản sao lưu dùng để khôi phục dữ liệu.",
        "D": "Chữ ký số xác minh nguồn gốc, không phải lối vào hệ thống.",
    }),
    "case_14": ("Tài liệu Word chỉ chạy mã sau khi bật nội dung tự động (macro) là dấu hiệu macro độc hại.", {
        "A": "WEP IV là lỗi của bảo mật Wi-Fi cũ, không liên quan tài liệu Word.",
        "B": "AES-CCMP là mã hóa của WPA2, không phải đường lây.",
        "C": "ACL sai thứ tự là lỗi cấu hình tường lửa.",
    }),
    "case_15": ("Chỉ so mẫu byte đã biết nên bỏ sót biến thể mới: đó là hạn chế của phát hiện theo chữ ký.", {
        "B": "Phân tích hành vi xét việc chương trình làm, nên có thể bắt biến thể mới.",
        "C": "Giám sát bất thường so với baseline cũng phát hiện được cái mới.",
        "D": "Sandbox quan sát mẫu khi chạy, không so mẫu byte.",
    }),
    "case_16": ("Chạy tệp trong máy ảo cô lập để ghi lại những gì nó làm là phân tích động trong sandbox.", {
        "B": "Phân tích tĩnh không chạy tệp.",
        "C": "Phần mở rộng tệp dễ giả mạo và không cho biết tệp làm gì.",
        "D": "Giá trị băm chỉ nhận dạng tệp.",
    }),
    "case_17": ("Đọc header, chuỗi và hàm nhập mà không chạy mẫu là phân tích tĩnh.", {
        "A": "Cách ly máy trạm là khoanh vùng sự cố, không phải phân tích mẫu.",
        "C": "Khôi phục sao lưu là dựng lại dữ liệu.",
        "D": "Phân tích động phải chạy mẫu.",
    }),
    "case_18": ("Worm lây qua mạng nên cách ly máy nghi nhiễm khỏi mạng là cách nhanh nhất để chặn lây ngang.", {
        "A": "Ngừng cập nhật chữ ký làm khả năng phát hiện kém đi.",
        "B": "Xóa nhật ký làm mất bằng chứng để điều tra.",
        "D": "Đổi hình nền không ảnh hưởng gì tới worm.",
    }),
    "case_19": ("SHA-256 khác nhau nghĩa là nội dung khác nhau; tên tệp giống nhau không chứng minh chúng là cùng một mẫu.", {
        "A": "SHA-256 là hàm băm một chiều, không giải ngược được.",
        "B": "Băm khác nhau thì nội dung chắc chắn khác nhau.",
        "D": "Băm khác chỉ cho biết nội dung khác, không cho biết tệp nào là ransomware.",
    }),
    "case_20": ("Không tìm và đóng đường xâm nhập thì mã độc quay lại; việc còn thiếu là phân tích nguyên nhân gốc và khắc phục đường vào.", {
        "B": "Trình phát media không liên quan việc chặn tái nhiễm.",
        "C": "Đổi tên nhật ký không khắc phục lỗ hổng.",
        "D": "Độ sáng màn hình không liên quan bảo mật.",
    }),
    "reviewed_atm_91": ("RAT (Remote Access Trojan) cho kẻ ngoài điều khiển máy nạn nhân từ xa.", {
        "A": "Keylogger chỉ ghi phím gõ, không điều khiển máy.",
        "B": "Logic bomb kích hoạt theo điều kiện để gây hại, không cho điều khiển từ xa.",
        "C": "Rootkit dùng để che giấu mã độc, không phải công cụ điều khiển từ xa.",
    }),
    "reviewed_atm_99": ("Âm thầm thu thập thói quen duyệt web rồi gửi đi là spyware (phần mềm gián điệp).", {
        "A": "Boot virus lây trên cung khởi động.",
        "B": "Ransomware mã hóa dữ liệu đòi tiền chuộc.",
        "C": "Worm tự lây qua mạng.",
    }),
    "reviewed_atm_101": ("Từ quyền thường giành được quyền quản trị là leo thang đặc quyền.", {
        "A": "Phát lại gói là gửi lại gói tin cũ.",
        "C": "Đánh cắp phiên là chiếm phiên đăng nhập của người khác, không phải tăng quyền.",
        "D": "Lọc gói là chức năng của tường lửa.",
    }),
    "reviewed_atm_107": ("Dịch vụ dừng là mất tính sẵn sàng, tệp bị lấy là mất tính bí mật; một mã độc có thể gây cả hai.", {
        "A": "Tệp bị lấy cắp nghĩa là dữ liệu đã bị ảnh hưởng.",
        "C": "Dịch vụ dừng và mất dữ liệu nghiêm trọng hơn nhiều so với chậm mạng.",
        "D": "Mất tệp và dừng dịch vụ không chỉ là chuyện tên tệp.",
    }),
    "reviewed_atm_119": ("Antivirus quét, cách ly và loại bỏ mã độc trên máy trạm.", {
        "A": "Proxy web trung chuyển truy cập web, không dọn mã độc trên máy.",
        "C": "DNS resolver phân giải tên miền.",
        "D": "Load balancer chia tải giữa các máy chủ.",
    }),
    "reviewed_atm_128": ("Nhiễm ngay sau khi mở tệp lạ từ email: đường lây là tệp đính kèm độc hại.", {
        "A": "Cập nhật hệ thống là biện pháp phòng thủ.",
        "B": "Sao lưu ngoại tuyến là biện pháp khôi phục.",
        "D": "Phân tách mạng là biện pháp hạn chế lây lan.",
    }),
    "reviewed_atm_147": ("Ghi lại phím người dùng bấm để lấy mật khẩu là keylogger.", {
        "B": "Worm tự lây qua mạng.",
        "C": "Ransomware mã hóa dữ liệu đòi tiền chuộc.",
        "D": "Adware hiện quảng cáo.",
    }),
    "abbr_c2_009": ("RAT là Remote Access Trojan, Trojan truy cập (điều khiển) từ xa.", {
        "B": "Không phải Root Access Toolkit.",
        "C": "Không phải Random Attack Tool.",
        "D": "RAT là mã độc, không phải công cụ diệt virus.",
    }),
    "rev_c2_010": ("Theo slide, RAT biến máy bị nhiễm thành server; máy hacker là client kết nối vào để điều khiển.", {
        "A": "Máy nhiễm RAT là server bị điều khiển, không phải client tự gửi thư rác.",
        "C": "RAT cho điều khiển toàn bộ máy, không chỉ chuyển tiếp web.",
        "D": "RAT không chỉ phá dữ liệu; mục đích là điều khiển từ xa.",
    }),
    "abbr_c2_011": ("ICV là Integrity Check Value, giá trị kiểm tra toàn vẹn nối vào cuối tệp sạch; tệp bị nhiễm sẽ làm ICV thay đổi.", {
        "A": "Không phải Infection Control Vector.",
        "B": "Không phải Internal Code Verifier.",
        "C": "Không phải Instant Capture of Virus.",
    }),
    "abbr_c2_012": ("HMAC là Hash-based Message Authentication Code, mã xác thực thông điệp dùng hàm băm kèm khóa bí mật.", {
        "A": "Không phải Hybrid Memory Access Control.",
        "B": "HMAC không phải trung tâm cảnh báo mã độc.",
        "D": "HMAC không phải công cụ phân tích mã độc trên máy.",
    }),
    "abbr_c2_013": ("FTP là File Transfer Protocol, giao thức truyền tệp; FTP Trojan mở dịch vụ này để người khác tải dữ liệu từ máy nạn nhân.", {
        "A": "Không phải Fast Transmission Port.",
        "B": "Không phải Forward Transfer Proxy.",
        "C": "Không phải File Tracking Program.",
    }),
    "abbr_c2_014": ("IRC là Internet Relay Chat, dịch vụ trò chuyện trực tuyến; Trojan ăn trộm mật khẩu tài khoản IRC.", {
        "A": "Không phải trung tâm ứng cứu sự cố.",
        "B": "Không phải điều khiển định tuyến.",
        "D": "Không phải bộ đệm tài nguyên.",
    }),
    "abbr_c2_015": ("API là Application Programming Interface, giao diện lập trình ứng dụng; chặn các hàm API mạng để mã độc không kết nối ra ngoài khi phân tích.", {
        "A": "Không phải Application Process Isolation Interface.",
        "C": "Không phải Automated Process Inspector.",
        "D": "Không phải Access Permission Index.",
    }),
    "rev_c2_138": ("Slide ghi Back Orifice dùng cổng 31337.", {
        "A": "443 là cổng HTTPS.",
        "B": "21 là cổng FTP, slide gắn với FTP Trojan.",
        "C": "12345 không phải cổng slide ghi cho Back Orifice.",
    }),
    "rev_c2_139": ("FTP Trojan mở dịch vụ FTP, cổng mặc định 21, để người khác tải dữ liệu từ máy nạn nhân.", {
        "A": "23 là Telnet.",
        "C": "25 là SMTP.",
        "D": "80 là HTTP.",
    }),
    "rev_c2_140": ("Slide giới thiệu TCPView và CurrPorts để xem chương trình nào đang mở cổng nào, từ đó phát hiện Trojan.", {
        "B": "Barri, Kuang là tên các Trojan trong slide, không phải công cụ xem cổng.",
        "C": "Back Orifice, NetBus là các Trojan.",
        "D": "KGB Spy, DJI RAT là các Trojan trong mục \"Một số Trojan phổ biến\".",
    }),
}
