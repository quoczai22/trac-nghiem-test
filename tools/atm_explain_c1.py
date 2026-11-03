EXPLAIN = {
    "gen_003": ("Bí mật (Confidentiality) là chỉ người được cấp quyền mới đọc được thông tin; người khác không xem được nội dung.", {
        "A": "Không bị sửa đổi trái phép là tính toàn vẹn (Integrity), không phải bí mật.",
        "B": "Luôn sẵn sàng khi cần là tính sẵn sàng (Availability).",
        "C": "Xác minh danh tính là xác thực (Authentication), không thuộc ba chữ của CIA.",
    }),
    "gen_006": ("Giá trị băm thay đổi khi dữ liệu bị sửa dù chỉ một bit, nên so sánh băm phát hiện được dữ liệu mất toàn vẹn.", {
        "A": "Mã hóa che nội dung, tức bảo vệ tính bí mật; nó không tự báo khi dữ liệu bị sửa.",
        "B": "Sao lưu giúp khôi phục sau sự cố, chủ yếu phục vụ tính sẵn sàng, không phát hiện sửa đổi.",
        "D": "Băng thông chỉ ảnh hưởng tốc độ và tính sẵn sàng, không liên quan việc dữ liệu bị sửa.",
    }),
    "gen_009": ("DoS/DDoS làm dịch vụ quá tải để người dùng hợp lệ không truy cập được, tức tấn công vào tính sẵn sàng.", {
        "B": "DoS không đọc trộm dữ liệu, nên không vi phạm trực tiếp tính bí mật.",
        "C": "DoS không sửa dữ liệu, nên không vi phạm trực tiếp tính toàn vẹn.",
        "D": "Chống chối bỏ liên quan việc chứng minh ai đã gửi/thực hiện; DoS không đụng tới điều này.",
    }),
    "gen_011": ("Chứng minh người đăng nhập đúng là chủ tài khoản chính là xác thực (authentication).", {
        "A": "Sẵn sàng là dịch vụ hoạt động khi cần, không phải kiểm tra danh tính.",
        "C": "Bí mật là giữ nội dung không bị đọc trộm, không phải xác minh người dùng.",
        "D": "Toàn vẹn là dữ liệu không bị sửa trái phép, không phải xác minh người dùng.",
    }),
    "gen_012": ("Xác thực trả lời câu hỏi \"anh có đúng là người/thiết bị anh nhận không\", ví dụ qua mật khẩu, mã OTP, chứng thư.", {
        "A": "Cấp quyền sau khi đăng nhập là phân quyền (authorization), diễn ra sau xác thực.",
        "C": "Mã hóa dữ liệu bảo vệ tính bí mật, không xác minh danh tính.",
        "D": "Ghi nhật ký là kiểm toán (accounting/audit), không phải xác thực.",
    }),
    "gen_014": ("Chỉ bắt gói để đọc mà không sửa hay chen vào là nghe lén (eavesdropping/sniffing).", {
        "A": "Người đứng giữa chen vào giữa hai bên và có thể sửa thông điệp; ở đây kẻ lạ chỉ đọc.",
        "C": "Mạo danh là giả làm nguồn hợp lệ; tình huống không có việc giả danh.",
        "D": "Phát lại là gửi lại gói cũ; tình huống chỉ có đọc gói.",
    }),
    "gen_015": ("Mã hóa kênh truyền (TLS, VPN) làm gói bắt được chỉ là dữ liệu mã hóa, kẻ nghe lén không đọc được.", {
        "A": "Ổ cứng và RAM chỉ tăng hiệu năng máy chủ, không che dữ liệu trên đường truyền.",
        "B": "Đổi tên máy không làm thay đổi việc gói tin truyền ở dạng rõ.",
        "C": "Tắt tường lửa làm hệ thống kém an toàn hơn, không giảm nghe lén.",
    }),
    "gen_017": ("Gói tin ghi địa chỉ nguồn của máy khác là giả mạo nguồn, tức mạo danh (spoofing).", {
        "A": "Người đứng giữa chen vào chuyển tiếp/sửa thông điệp; ở đây chỉ là sửa địa chỉ nguồn.",
        "C": "Phát lại là gửi lại gói hợp lệ cũ, không phải ghi sai địa chỉ nguồn.",
        "D": "Nghe lén chỉ đọc gói tin, không tạo gói giả.",
    }),
    "gen_018": ("Spoofing là giả làm một nguồn hợp lệ, ví dụ dùng IP hoặc MAC của máy khác để được tin cậy.", {
        "A": "Làm quá tải bằng nhiều máy là DDoS.",
        "B": "Đọc trộm gói mà không sửa là nghe lén.",
        "C": "Thử lần lượt mật khẩu là tấn công vét cạn (brute force).",
    }),
    "gen_020": ("Ghi lại một yêu cầu xác thực hợp lệ rồi gửi lại là tấn công phát lại (replay).", {
        "A": "Mạo danh là giả địa chỉ/danh tính nguồn, không nhất thiết dùng lại gói cũ.",
        "C": "Nghe lén chỉ đọc gói, không gửi lại.",
        "D": "Người đứng giữa chuyển tiếp và có thể sửa thông điệp theo thời gian thực, không phải lặp gói cũ.",
    }),
    "gen_023": ("Đứng giữa khách và máy chủ, chuyển tiếp rồi sửa thông điệp là tấn công người đứng giữa (MITM).", {
        "A": "Mạo danh chỉ giả danh tính nguồn; ở đây kẻ tấn công còn chen vào giữa và sửa nội dung.",
        "B": "Phát lại gửi lại gói cũ nguyên vẹn, không sửa nội dung trên đường đi.",
        "D": "Nghe lén chỉ đọc, không chuyển tiếp hay sửa thông điệp.",
    }),
    "gen_026": ("Chỉ một máy gửi dồn dập yêu cầu làm dịch vụ quá tải là DoS (một nguồn).", {
        "B": "Phishing lừa người dùng bằng email/trang giả, không làm quá tải máy chủ.",
        "C": "Tràn bộ đệm là ghi dữ liệu vượt vùng nhớ trong chương trình, không phải gửi dồn yêu cầu.",
        "D": "DDoS cần nhiều nguồn phối hợp; ở đây chỉ có một máy.",
    }),
    "gen_035": ("Email giả ngân hàng dẫn tới trang đăng nhập nhái để lấy tài khoản là lừa đảo phishing.", {
        "A": "DDoS làm quá tải dịch vụ từ nhiều nguồn, không dùng email giả.",
        "C": "DoS làm quá tải dịch vụ, không lừa người dùng nhập thông tin.",
        "D": "Tràn bộ đệm là lỗi bộ nhớ chương trình, không phải lừa đảo qua email.",
    }),
    "gen_044": ("Mật khẩu (thứ biết) cộng mã từ thiết bị (thứ có) là hai yếu tố khác loại, tức xác thực đa yếu tố (MFA).", {
        "B": "Đặc quyền tối thiểu là chỉ cấp quyền vừa đủ cho công việc, không nói về cách đăng nhập.",
        "C": "Phòng thủ nhiều lớp là xếp nhiều lớp bảo vệ khác nhau (firewall, IDS, vá lỗi...) cho cả hệ thống, không phải hai yếu tố trong một lần đăng nhập.",
        "D": "Quản lý bản vá là cập nhật bản sửa lỗi phần mềm.",
    }),
    "gen_047": ("Đánh giá tương thích rồi cài bản sửa lỗi là quy trình quản lý bản vá.", {
        "A": "Đặc quyền tối thiểu là giới hạn quyền của tài khoản, không phải cài bản sửa lỗi.",
        "B": "Xác thực đa yếu tố là đăng nhập bằng nhiều yếu tố.",
        "C": "Phòng thủ nhiều lớp là kết hợp nhiều biện pháp; việc cài bản vá chỉ là một biện pháp cụ thể.",
    }),
    "case_01": ("Người lạ xem được hồ sơ nhưng không sửa, không xóa: dữ liệu bị lộ, tức tính bí mật bị xâm phạm.", {
        "A": "Hệ thống vẫn hoạt động, nên tính sẵn sàng không bị ảnh hưởng.",
        "C": "Dữ liệu không bị sửa, nên tính toàn vẹn còn nguyên.",
        "D": "Không chối bỏ liên quan chứng minh hành động của một bên, không phải việc lộ dữ liệu.",
    }),
    "case_02": ("Số tiền giao dịch bị đổi là dữ liệu bị sửa trái phép, tức tính toàn vẹn bị phá vỡ.", {
        "B": "Dịch vụ vẫn hoạt động bình thường, nên tính sẵn sàng không bị ảnh hưởng.",
        "C": "Vấn đề là dữ liệu bị sửa chứ không phải bị đọc trộm.",
        "D": "Tình huống không nói về việc giả danh người dùng mà về nội dung bị thay đổi.",
    }),
    "case_03": ("Cổng không truy cập được do quá tải là mất tính sẵn sàng; dữ liệu chưa bị đọc hay sửa.", {
        "A": "Dữ liệu chưa bị sửa, nên toàn vẹn chưa bị ảnh hưởng.",
        "B": "Không chối bỏ không liên quan việc dịch vụ ngừng phục vụ.",
        "C": "Dữ liệu chưa bị đọc trộm, nên bí mật chưa bị ảnh hưởng.",
    }),
    "case_04": ("Điểm khác cốt lõi của DDoS là lưu lượng đến từ nhiều nguồn phối hợp (thường là botnet), còn DoS chỉ từ một nguồn.", {
        "A": "Cả DoS và DDoS đều có thể nhắm vào bất kỳ dịch vụ nào, không riêng máy chủ web.",
        "B": "Cả hai đều không cần mật khẩu quản trị; chúng chỉ làm quá tải dịch vụ.",
        "C": "Cả hai tấn công tính sẵn sàng và thường không sửa dữ liệu.",
    }),
    "case_05": ("Nonce hoặc mã giao dịch dùng một lần giúp máy chủ nhận ra yêu cầu đã dùng rồi và từ chối bản gửi lại.", {
        "A": "Mã hóa không ngăn phát lại: kẻ tấn công gửi lại nguyên gói mã hóa vẫn hợp lệ.",
        "C": "Băng thông không giúp phân biệt yêu cầu mới với yêu cầu cũ.",
        "D": "Đổi cổng không làm yêu cầu cũ mất hiệu lực.",
    }),
    "case_06": ("Kiểm tra chứng thư máy chủ và dùng kênh mã hóa hợp lệ (TLS) làm kẻ đứng giữa không đọc và không sửa được dữ liệu mà không bị phát hiện.", {
        "A": "Chặn tệp đính kèm không ngăn việc đọc/sửa phản hồi trên đường truyền.",
        "C": "Sao lưu chỉ giúp khôi phục, không bảo vệ dữ liệu đang truyền.",
        "D": "Mật khẩu dài chống đoán mật khẩu, không chống chen vào kênh truyền.",
    }),
    "case_07": ("Tài khoản chỉ cần xem thì chỉ nên có quyền xem: đó là nguyên tắc đặc quyền tối thiểu.", {
        "A": "Chia sẻ tài khoản chung làm mất trách nhiệm từng người, ngược với yêu cầu bảo mật.",
        "B": "Bỏ ghi nhật ký làm khó điều tra sự cố, không giải quyết việc thừa quyền.",
        "C": "Mặc định cho phép mở rộng quyền thay vì thu hẹp.",
    }),
    "case_08": ("Kết hợp firewall, giám sát xâm nhập và vá lỗi là nhiều lớp bảo vệ chồng lên nhau, tức phòng thủ nhiều lớp (defense in depth).", {
        "B": "Tắt toàn bộ dịch vụ làm mất tính sẵn sàng, không phải cách bảo vệ.",
        "C": "Tình huống dùng nhiều lớp kỹ thuật, không chỉ tầng vật lý.",
        "D": "Tình huống cho thấy một lớp (firewall) là chưa đủ.",
    }),
    "case_09": ("Mật khẩu là yếu tố \"biết\", điện thoại nhận mã là yếu tố \"sở hữu\"; hai loại khác nhau nên là đa yếu tố.", {
        "A": "Mã gửi qua điện thoại là yếu tố sở hữu, không phải sinh trắc học.",
        "C": "MFA vẫn là xác minh danh tính, chỉ chặt hơn.",
        "D": "Hai mật khẩu đều là yếu tố \"biết\", nên chỉ là một loại yếu tố.",
    }),
    "case_10": ("Chép dữ liệu dài vào vùng nhớ cố định mà không kiểm tra độ dài sẽ ghi đè vùng nhớ kế bên, tức tràn bộ đệm.", {
        "A": "Giả mạo SSID là tấn công mạng không dây, không liên quan lỗi xử lý đầu vào.",
        "C": "DDoS là làm quá tải từ nhiều nguồn, không phải lỗi chép dữ liệu.",
        "D": "Phát lại là gửi lại gói cũ, không phải lỗi bộ nhớ.",
    }),
    "reviewed_atm_9": ("Hàng nghìn máy nhiễm (botnet) cùng gửi yêu cầu là tấn công từ nhiều nguồn, tức DDoS.", {
        "A": "MITM chen vào giữa để đọc/sửa thông điệp, không làm cạn tài nguyên.",
        "B": "DoS một nguồn chỉ có một máy tấn công; ở đây có hàng nghìn máy.",
        "D": "Phishing lừa người dùng qua email/trang giả.",
    }),
    "reviewed_atm_28": ("Điểm bị sửa trái phép là dữ liệu mất toàn vẹn; hệ thống vẫn chạy nên không phải mất sẵn sàng.", {
        "A": "Hệ thống vẫn truy cập bình thường, nên tính sẵn sàng còn nguyên.",
        "C": "Vấn đề là dữ liệu bị sửa, không phải bị đọc trộm.",
        "D": "Xác thực không phải một chữ trong CIA, và câu hỏi nói về dữ liệu bị sửa.",
    }),
    "abbr_c1_001": ("CIA là ba mục tiêu cốt lõi: Confidentiality (bí mật), Integrity (toàn vẹn), Availability (sẵn sàng).", {
        "B": "C không phải Cryptography và A không phải Authorization.",
        "C": "I là Integrity chứ không phải Identity, A là Availability chứ không phải Accountability.",
        "D": "Cả ba chữ đều sai: đúng là Confidentiality, Integrity, Availability.",
    }),
    "abbr_c1_002": ("DoS là Denial of Service, tấn công từ chối dịch vụ.", {
        "A": "Disk Operating System là hệ điều hành MS-DOS, không phải tấn công.",
        "C": "Không có thuật ngữ Domain of Security cho DoS.",
        "D": "Data over Socket không phải nghĩa của DoS.",
    }),
    "abbr_c1_003": ("DDoS là Distributed Denial of Service; Distributed nghĩa là tấn công phân tán từ nhiều nguồn.", {
        "A": "D không phải Duplicate; DDoS không phải lặp một gói tin.",
        "B": "D không phải Dynamic; DDoS không định nghĩa bằng việc đổi địa chỉ đích.",
        "D": "D không phải Direct; điểm chính là nhiều nguồn, không phải đánh thẳng một cổng.",
    }),
    "abbr_c1_004": ("ARP (Address Resolution Protocol) tìm địa chỉ MAC ứng với một địa chỉ IP trong mạng LAN; ARP spoofing gửi trả lời ARP giả để chiếm vị trí máy khác.", {
        "A": "Cấp phát IP động là DHCP.",
        "B": "Định tuyến giữa các mạng con là việc của router và giao thức định tuyến.",
        "C": "Phân giải tên miền sang IP là DNS.",
    }),
    "abbr_c1_005": ("SYN là gói đầu tiên của bắt tay ba bước TCP (SYN, SYN-ACK, ACK); SYN flood gửi rất nhiều SYN để làm đầy hàng đợi kết nối.", {
        "A": "Truy vấn tên miền qua UDP là DNS, không phải SYN.",
        "B": "Kiểm tra kết nối bằng ICMP là ping (Echo Request).",
        "D": "Kết thúc phiên TCP dùng FIN, không phải SYN.",
    }),
    "abbr_c1_006": ("ICMP là Internet Control Message Protocol, giao thức gửi thông báo điều khiển/lỗi, ví dụ ping.", {
        "B": "Không phải Internal Control Mapping Protocol.",
        "C": "Chữ C là Control, không phải Cache.",
        "D": "Chữ M là Message, không phải Management; cũng không có chữ Connection.",
    }),
    "abbr_c1_007": ("MAC trong địa chỉ MAC là Media Access Control, địa chỉ phần cứng của card mạng.", {
        "A": "Không phải Machine Address Code.",
        "B": "Không phải Main Access Channel.",
        "C": "Message Authentication Code cũng viết tắt MAC nhưng là mã xác thực thông điệp trong mật mã, không phải địa chỉ card mạng.",
    }),
    "abbr_c1_008": ("MITM là Man-in-the-Middle, kẻ tấn công đứng giữa hai bên để đọc hoặc sửa thông điệp.", {
        "A": "Chữ M thứ hai là Middle, không phải Memory.",
        "C": "MITM không phải tên một công cụ giám sát lưu lượng.",
        "D": "Middle chứ không phải Mail.",
    }),
    "rev_c1_133": ("SMTP gửi email dùng cổng TCP 25, nên lọc tcp.port == 25 để bắt gói email.", {
        "B": "Cổng 21 là FTP (truyền tệp).",
        "C": "Cổng 443 là HTTPS.",
        "D": "Cổng 80 là HTTP.",
    }),
    "rev_c1_134": ("HTTP mặc định dùng cổng TCP 80.", {
        "A": "Cổng 21 là FTP.",
        "B": "Cổng 25 là SMTP.",
        "C": "Cổng 443 là HTTPS (HTTP có mã hóa TLS).",
    }),
    "rev_c1_135": ("HTTPS (HTTP qua TLS) mặc định dùng cổng TCP 443.", {
        "A": "Cổng 80 là HTTP không mã hóa.",
        "C": "Cổng 25 là SMTP.",
        "D": "8080 là cổng HTTP thay thế hay dùng cho proxy/web thử nghiệm, không phải cổng mặc định của HTTPS.",
    }),
    "rev_c1_136": ("Port scan gửi gói thử tới các cổng để biết cổng TCP/UDP nào đang mở, tức dịch vụ nào đang chạy.", {
        "A": "Port scan không mã hóa dữ liệu.",
        "B": "Port scan chỉ dò, không đổi cấu hình dịch vụ.",
        "D": "Chặn cổng là việc của tường lửa; port scan chỉ phát hiện.",
    }),
    "rev_c1_137": ("netstat -ano liệt kê mọi kết nối và cổng đang nghe (-a), dạng số (-n), kèm PID tiến trình (-o).", {
        "A": "ipconfig /all hiện cấu hình card mạng (IP, MAC, DNS), không liệt kê cổng.",
        "B": "tracert dò đường đi qua các router tới đích.",
        "D": "ping -t gửi ping liên tục để kiểm tra kết nối.",
    }),
}
