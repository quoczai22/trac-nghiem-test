EXPLAIN = {
    "gen_134": ("ACL trên router chặn gói theo cổng đích 23 là lọc gói (packet filtering): chỉ xét thông tin header như IP, cổng, giao thức.", {
        "A": "Circuit-level gateway giám sát bắt tay TCP của phiên, không chỉ xét cổng của từng gói.",
        "B": "Application proxy xét nội dung tầng ứng dụng, không phải ACL trên router.",
        "C": "Stateful inspection theo dõi trạng thái phiên; ACL tĩnh chặn cổng 23 không cần trạng thái.",
    }),
    "gen_135": ("Lọc gói xét IP nguồn/đích (thông tin tầng mạng) nên slide xếp nó ở tầng mạng.", {
        "B": "Tầng ứng dụng là của application proxy.",
        "C": "Slide gắn tầng giao vận (phiên TCP) với circuit-level gateway.",
        "D": "Tầng vật lý là tín hiệu, cáp; tường lửa không lọc ở đó.",
    }),
    "gen_138": ("Stateful inspection lưu bảng trạng thái phiên, nên biết gói đến có thuộc một kết nối hợp lệ đã thiết lập hay không.", {
        "A": "SIF vẫn xét cả cổng; không xét cổng là sai với mọi loại lọc gói.",
        "C": "SIF hoạt động ở tầng mạng/giao vận, không ở tầng vật lý.",
        "D": "SIF chặn được gói từ Internet không thuộc phiên nào.",
    }),
    "gen_140": ("Xác nhận phiên TCP hợp lệ (bắt tay) rồi mới chuyển tiếp là cách làm của circuit-level gateway.", {
        "B": "Stateful inspection theo dõi trạng thái từng gói trong phiên, không đứng ra xác nhận phiên rồi chuyển tiếp.",
        "C": "Lọc gói chỉ xét header từng gói, không xác nhận phiên.",
        "D": "Application proxy kiểm tra nội dung ứng dụng.",
    }),
    "gen_141": ("Circuit-level gateway giám sát quá trình bắt tay TCP giữa các gói để quyết định phiên có hợp lệ.", {
        "A": "Nội dung lệnh HTTP là việc của tường lửa tầng ứng dụng.",
        "C": "Tín hiệu vô tuyến của AP thuộc bảo mật WLAN.",
        "D": "Chữ ký virus là việc của antivirus.",
    }),
    "gen_144": ("Tường lửa tầng ứng dụng hiểu giao thức ứng dụng nên kiểm tra được nội dung và lệnh (ví dụ lệnh HTTP, FTP).", {
        "A": "Chỉ xét IP là lọc gói; tầng ứng dụng thường chậm hơn vì kiểm tra sâu.",
        "C": "Mọi tường lửa đều cần cấu hình luật.",
        "D": "Nó hoạt động ở tầng ứng dụng, không phải tầng vật lý.",
    }),
    "gen_146": ("\"Appliance\" là thiết bị chuyên dụng riêng, nên phân theo hình thức đây là tường lửa phần cứng.", {
        "B": "\"Biên\" là cách phân theo vị trí; câu hỏi nhấn vào việc dùng một appliance, tức phân theo hình thức triển khai.",
        "C": "Tường lửa nội bộ đặt giữa các vùng bên trong LAN, không ở ranh giới Internet.",
        "D": "Tường lửa máy chủ là phần mềm cài trên chính một máy.",
    }),
    "gen_147": ("Tường lửa phần cứng là thiết bị riêng đặt trên đường truyền, bảo vệ cả mạng phía sau nó.", {
        "A": "Chỉ bảo vệ máy đã cài là tường lửa phần mềm trên máy.",
        "B": "Tường lửa phần cứng lọc được theo cổng.",
        "C": "Chạy trên máy trạm là tường lửa phần mềm.",
    }),
    "gen_149": ("Luật trên chính server chỉ nhận cổng quản trị từ subnet tin cậy là tường lửa máy chủ (host-based).", {
        "A": "Tường lửa nội bộ đặt giữa các vùng mạng, không nằm trên một server.",
        "B": "Tường lửa phần cứng là thiết bị riêng, không phải luật trên server.",
        "D": "Tường lửa biên đặt ở ranh giới Internet.",
    }),
    "gen_150": ("Host-based firewall chạy trên một máy và chỉ bảo vệ chính máy đó.", {
        "A": "Bảo vệ cả LAN là tường lửa biên/phần cứng.",
        "B": "Nó không bảo vệ các thiết bị Wi-Fi khác.",
        "D": "Nó không giới hạn ở DMZ; máy nào cài thì bảo vệ máy đó.",
    }),
    "gen_152": ("Gateway kiểm tra mọi kết nối từ Internet vào văn phòng nằm ở ranh giới, tức tường lửa biên.", {
        "A": "Phần cứng là cách phân theo hình thức; tình huống nhấn vào vị trí ở ranh giới.",
        "B": "Tường lửa máy chủ chỉ bảo vệ một máy.",
        "C": "Tường lửa nội bộ đặt giữa các vùng bên trong, không phải cổng ra Internet.",
    }),
    "gen_153": ("Tường lửa biên đặt giữa mạng nội bộ và Internet để kiểm soát lưu lượng ra vào.", {
        "A": "Đặt trong từng máy là tường lửa máy chủ.",
        "B": "Tường lửa không đặt giữa CPU và bộ nhớ.",
        "D": "Tủ điện không phải vị trí mạng.",
    }),
    "gen_155": ("Chặn VLAN người dùng vào thẳng VLAN cơ sở dữ liệu là lọc giữa các vùng bên trong, tức tường lửa nội bộ.", {
        "A": "Tường lửa máy chủ nằm trên một máy, không chia VLAN.",
        "C": "Phần cứng là hình thức; tình huống nói về vị trí giữa các vùng nội bộ.",
        "D": "Tường lửa biên ở ranh giới Internet, không phải giữa hai VLAN.",
    }),
    "gen_156": ("Tường lửa giữa các vùng nội bộ chặn kẻ đã vào LAN đi tiếp sang vùng khác (di chuyển ngang).", {
        "A": "Thêm lớp kiểm tra không làm Internet nhanh hơn.",
        "B": "Nó bổ sung chứ không thay tường lửa biên.",
        "C": "Tường lửa không quyết định số IP cần cấp.",
    }),
    "gen_158": ("Chỉ một router có ACL đứng trước cả mạng nội bộ là kiến trúc screening router.", {
        "A": "Screened subnet có hai lớp lọc kẹp một DMZ.",
        "B": "Screened host có thêm bastion host phía sau router.",
        "D": "Dual-homed host là máy có hai card mạng, không phải router ACL.",
    }),
    "gen_159": ("Screening router chỉ có một lớp lọc; vượt qua nó là vào thẳng mạng nội bộ.", {
        "A": "Đây là kiến trúc đơn giản nhất, không cần nhiều máy chủ hay vùng.",
        "B": "Router lọc gói lọc được theo IP.",
        "D": "Kiến trúc này không có DMZ.",
    }),
    "gen_161": ("Máy proxy có một card mạng ra ngoài và một vào trong là dual-homed host.", {
        "B": "Screened subnet là hai lớp lọc kẹp DMZ.",
        "C": "Screened host là router lọc cộng bastion host.",
        "D": "Screening router là một router lọc gói.",
    }),
    "gen_162": ("Dual-homed host là máy có hai card mạng, một nối mạng ngoài, một nối mạng trong, và không định tuyến thẳng giữa hai bên.", {
        "A": "\"Dual\" là hai card mạng, không phải hai hệ điều hành.",
        "B": "Hai router nối tiếp gần với screened subnet.",
        "D": "Máy chủ web trong DMZ là chuyện vị trí, không phải dual-homed.",
    }),
    "gen_165": ("Screened host gồm router lọc gói ở ngoài và một bastion host bên trong làm điểm nhận kết nối.", {
        "A": "Hai router kẹp DMZ là screened subnet.",
        "B": "Một router duy nhất là screening router.",
        "C": "Một máy nhiều card nối nhiều vùng là multi-homed.",
    }),
    "gen_167": ("Web công khai đặt trong DMZ kẹp giữa hai lớp lọc là kiến trúc screened subnet.", {
        "A": "Screening router chỉ có một lớp lọc, không có DMZ.",
        "B": "Dual-homed host là một máy hai card mạng.",
        "D": "Screened host không có vùng đệm riêng giữa hai lớp lọc.",
    }),
    "gen_168": ("Hai lớp lọc của screened subnet tạo ra vùng DMZ ở giữa để đặt máy chủ công khai.", {
        "B": "VLAN quản trị không phải vùng mà kiến trúc này tạo ra.",
        "C": "Mạng không dây không liên quan kiến trúc này.",
        "D": "Vùng sao lưu không phải mục đích của kiến trúc này.",
    }),
    "gen_171": ("DMZ dành cho máy chủ phải phục vụ Internet như web, mail công khai.", {
        "A": "Cơ sở dữ liệu nhân sự là dữ liệu nhạy cảm, phải ở sâu trong mạng nội bộ.",
        "B": "Máy trạm kế toán thuộc mạng nội bộ.",
        "D": "Máy chủ quản lý tài khoản nội bộ không được mở ra Internet.",
    }),
    "gen_173": ("Máy nhảy chuyên dụng được gia cố, là điểm duy nhất cho SSH từ ngoài vào, chính là bastion host.", {
        "A": "DMZ là một vùng mạng, không phải một máy cụ thể.",
        "B": "Mạng ngoài là phía Internet không tin cậy.",
        "C": "Mạng nội bộ là vùng được bảo vệ, không phải máy trung gian.",
    }),
    "gen_174": ("Bastion host là máy được gia cố kỹ, chạy rất ít dịch vụ, vì nó đối mặt trực tiếp với tấn công từ ngoài.", {
        "A": "Router chỉ xét IP và cổng là screening router.",
        "B": "Máy trạm của quản trị viên không phải bastion host.",
        "D": "Máy lưu sao lưu không phải bastion host.",
    }),
    "gen_176": ("Máy nhân sự nằm sau các lớp kiểm soát biên là thuộc mạng nội bộ.", {
        "A": "Bastion host là máy chịu tấn công trực tiếp ở biên.",
        "C": "Mạng ngoài là phía Internet.",
        "D": "DMZ chứa máy chủ công khai, không chứa máy nhân sự.",
    }),
    "gen_177": ("Không mở máy nội bộ ra Internet để giảm bề mặt tấn công; chỉ dịch vụ công khai mới đặt ở DMZ.", {
        "B": "Internet vẫn dùng TCP bình thường.",
        "C": "Máy nội bộ vẫn có địa chỉ MAC.",
        "D": "Lý do là bảo mật, không phải tốc độ.",
    }),
    "gen_179": ("Yêu cầu từ Internet trước khi qua chính sách biên vẫn đang ở mạng ngoài.", {
        "B": "DMZ nằm sau ít nhất một lớp lọc biên.",
        "C": "Mạng nội bộ nằm sau các lớp kiểm soát.",
        "D": "Bastion host là một máy, không phải vùng mạng.",
    }),
    "gen_180": ("Lưu lượng từ Internet mặc định không tin cậy; tường lửa chỉ cho qua các luồng được phép rõ ràng.", {
        "A": "Nhà mạng không kiểm tra an ninh thay cho doanh nghiệp.",
        "C": "Cho qua hết thì ghi log cũng không ngăn được tấn công.",
        "D": "Chờ người dùng báo sự cố là đã quá muộn.",
    }),
    "gen_182": ("Luật cuối cùng chặn mọi thứ chưa khớp luật nào là default deny (từ chối mặc định).", {
        "A": "Rule order nói về thứ tự xét luật, không phải luật chặn cuối cùng.",
        "B": "Change review là duyệt thay đổi luật.",
        "D": "Least privilege nói việc mở vừa đủ, còn luật chặn mọi thứ chưa khớp có tên riêng là default deny.",
    }),
    "gen_183": ("Default deny chặn mọi luồng không khớp một luật cho phép nào.", {
        "B": "Cho qua mọi luồng không khớp luật chặn là default allow, ngược lại.",
        "C": "Luồng đã được cho phép thì vẫn đi qua.",
        "D": "Nguyên tắc áp dụng cho cả chiều vào và chiều ra.",
    }),
    "gen_186": ("Tối thiểu hóa quyền truy cập: chỉ mở đúng dịch vụ, cổng, địa chỉ IP thật sự cần.", {
        "B": "Mở mọi cổng làm tăng bề mặt tấn công.",
        "C": "Cấp quyền quản trị cho mọi người ngược với tối thiểu hóa.",
        "D": "Any-Any rồi chặn dần là mặc định cho phép.",
    }),
    "gen_189": ("Tường lửa áp dụng luật khớp đầu tiên; luật cho phép rộng ở trên đã bắt hết, nên luật chặn hẹp bên dưới không bao giờ được dùng.", {
        "A": "Tường lửa không xét độ cụ thể mà xét thứ tự trên xuống.",
        "B": "Đây là lỗi cấu hình, tường lửa không báo lỗi hay dừng.",
        "C": "Tường lửa không tự gộp luật.",
    }),
    "gen_192": ("Rà soát luật định kỳ giúp tìm luật thừa, trùng hoặc sai thứ tự.", {
        "A": "Tắt log làm mất dữ liệu để rà soát.",
        "B": "Đổi tên thiết bị không ảnh hưởng luật.",
        "C": "Thời gian hết hạn phiên không giúp tìm luật sai.",
    }),
    "gen_194": ("Kiểm soát luồng từ Internet đi vào web DMZ là lọc chiều vào (inbound filtering).", {
        "B": "Outbound là luồng từ trong đi ra.",
        "C": "East-west là luồng giữa các vùng bên trong.",
        "D": "Ghi log là chức năng ghi nhận, không phải hướng lọc.",
    }),
    "gen_195": ("Inbound filtering kiểm soát luồng từ mạng ngoài đi vào mạng nội bộ.", {
        "A": "Từ nội bộ ra Internet là outbound.",
        "B": "Giữa hai tiến trình trên một máy không qua tường lửa mạng.",
        "D": "Luồng CPU – ổ cứng không phải lưu lượng mạng.",
    }),
    "gen_197": ("Chặn máy trạm gửi SMTP thẳng ra Internet là lọc chiều ra (outbound filtering).", {
        "A": "Ghi log không chặn luồng.",
        "C": "East-west là giữa các vùng bên trong, còn đây là đi ra Internet.",
        "D": "Inbound là chiều từ ngoài vào.",
    }),
    "gen_198": ("Outbound filtering ngăn máy nhiễm mã độc đẩy dữ liệu ra ngoài hoặc liên lạc với máy điều khiển.", {
        "A": "Quét cổng từ Internet vào là việc của lọc chiều vào.",
        "B": "Gõ sai mật khẩu là chuyện xác thực.",
        "C": "Mất điện không liên quan lọc lưu lượng.",
    }),
    "gen_200": ("Chặn VLAN khách vào VLAN máy chủ là lọc giữa các vùng bên trong, tức east-west filtering.", {
        "A": "Outbound là đi ra Internet.",
        "C": "Ghi log không chặn luồng.",
        "D": "Inbound là từ Internet vào.",
    }),
    "gen_203": ("Bản ghi nguồn, đích, cổng và hành động drop là nhật ký của tường lửa (logging).", {
        "A": "Outbound là hướng lọc, không phải bản ghi.",
        "B": "Inbound là hướng lọc, không phải bản ghi.",
        "D": "East-west là hướng lọc, không phải bản ghi.",
    }),
    "gen_206": ("Chỉ máy 10.0.0.5 được vào, máy khác thì không: luật phân biệt theo người gửi, tức địa chỉ IP nguồn.", {
        "A": "IP đích là firewall, giống nhau với mọi máy gửi tới.",
        "B": "Cổng đích là cổng cấu hình, giống nhau với mọi máy.",
        "C": "Lọc gói không đọc nội dung HTTP.",
    }),
    "gen_209": ("Chỉ máy web 203.0.113.10 được nhận: luật phân biệt theo máy nhận, tức địa chỉ IP đích.", {
        "A": "Nguồn là bất kỳ máy nào trên Internet.",
        "B": "Cổng nguồn do máy khách chọn ngẫu nhiên.",
        "D": "Cờ SYN có ở mọi kết nối mới, không phân biệt máy web với máy khác.",
    }),
    "gen_212": ("Cùng máy chủ, khác dịch vụ (443 và 23): luật phân biệt bằng cổng đích.", {
        "B": "IP đích như nhau vì cùng một máy chủ.",
        "C": "Câu hỏi không phân biệt theo người gửi.",
        "D": "MAC nguồn không phân biệt dịch vụ.",
    }),
    "gen_215": ("Stateful inspection nhớ phiên do LAN khởi tạo nên tự cho gói trả lời vào và chặn kết nối do Internet khởi tạo, không cần luật chiều ngược.", {
        "A": "Lọc gói không trạng thái phải mở luật chiều ngược mới cho gói trả lời vào.",
        "B": "WAF chỉ bảo vệ ứng dụng web, không quản lý phiên duyệt web của cả LAN.",
        "D": "ACL tĩnh không biết gói nào là trả lời của phiên nào.",
    }),
    "gen_221": ("Chặn kết nối từ Internet tới cơ sở dữ liệu theo IP/cổng là việc của tường lửa mạng.", {
        "A": "NAT đổi địa chỉ, không phải công cụ đặt chính sách chặn.",
        "C": "Proxy web trung chuyển việc duyệt web của người dùng.",
        "D": "WAF bảo vệ ứng dụng web, không phải cơ sở dữ liệu.",
    }),
    "gen_224": ("Người dùng nội bộ duyệt web qua một máy trung gian là proxy web.", {
        "A": "WAF đứng trước máy chủ web để bảo vệ nó, không phục vụ người dùng duyệt web.",
        "B": "NAT chỉ đổi địa chỉ, không phải máy trung gian xử lý yêu cầu web.",
        "C": "Tường lửa mạng lọc theo luật, không trung chuyển yêu cầu.",
    }),
    "gen_227": ("Nhiều máy LAN dùng chung một IP công khai là NAT (dịch địa chỉ mạng).", {
        "A": "Tường lửa mạng lọc lưu lượng, không đổi địa chỉ.",
        "B": "Proxy web trung chuyển web, khác cơ chế dịch địa chỉ.",
        "C": "WAF bảo vệ ứng dụng web.",
    }),
    "case_21": ("Cho gói phản hồi của phiên đã thiết lập và chặn gói không thuộc phiên nào là stateful inspection.", {
        "A": "IDS thụ động chỉ cảnh báo, không chặn.",
        "B": "Chỉ xét địa chỉ đích thì không biết gói thuộc phiên nào.",
        "D": "NAT đổi địa chỉ, không phải cơ chế kiểm tra phiên.",
    }),
    "case_22": ("Kiểm tra lệnh HTTP và nội dung yêu cầu cần tường lửa tầng ứng dụng (application proxy).", {
        "A": "Router không ACL không lọc gì.",
        "B": "Circuit-level gateway chỉ xét phiên, không đọc nội dung.",
        "C": "Packet filter chỉ xét IP, cổng.",
    }),
    "case_23": ("Web công khai cần truy cập được từ Internet nhưng tách khỏi LAN chứa dữ liệu, nên đặt ở DMZ.", {
        "A": "Cùng subnet với hồ sơ thì web bị chiếm là lộ hồ sơ.",
        "B": "Mạng quản trị CSDL là vùng nhạy cảm, không được mở ra Internet.",
        "D": "VLAN người dùng không lọc là mạng nội bộ không được bảo vệ.",
    }),
    "case_24": ("Router lọc cộng một bastion host làm điểm nhận kết nối, không có vùng đệm riêng: đó là screened host.", {
        "A": "Mạng có router lọc, nên không phải mạng phẳng không tường lửa.",
        "B": "Mạng có router lọc, nên không phải dual-homed không router.",
        "D": "Screened subnet phải có vùng đệm (DMZ) giữa hai lớp lọc.",
    }),
    "case_25": ("Tường lửa dừng ở luật khớp đầu tiên; IP xấu khớp luật cho phép mọi nguồn ở trên nên được cho qua.", {
        "A": "IDS không tự xóa máy khỏi mạng.",
        "B": "Tường lửa không tự chuyển gói sang mã hóa.",
        "C": "Luật chặn phía sau không bao giờ được xét vì luật trên đã khớp.",
    }),
    "case_26": ("Mở đúng luật cụ thể (TCP 443 vào web DMZ) rồi đặt default deny ở cuối để chặn mọi thứ khác.", {
        "A": "Gộp chung một VLAN làm mất phân vùng.",
        "C": "Allow any-any ở đầu thì mọi thứ đều được qua.",
        "D": "Tắt log và mở mọi cổng ngược hẳn yêu cầu.",
    }),
    "case_27": ("Dữ liệu đi từ trong ra ngoài qua cổng lạ nên cần lọc chiều ra (outbound).", {
        "A": "RAM không ảnh hưởng luồng mạng.",
        "B": "SSID WLAN không liên quan máy trạm gửi dữ liệu ra ngoài.",
        "C": "Inbound chỉ xét luồng từ ngoài vào, bỏ qua luồng đi ra.",
    }),
    "case_28": ("SQL injection nằm trong tham số HTTP; WAF chuyên kiểm tra yêu cầu web để chặn loại tấn công này.", {
        "A": "NAT chỉ đổi địa chỉ, không đọc yêu cầu HTTP.",
        "C": "DHCP cấp địa chỉ IP.",
        "D": "Bộ khuếch đại Wi-Fi chỉ tăng sóng.",
    }),
    "case_29": ("Nhật ký quyết định lọc ghi lại IP nguồn, đích, cổng và hành động drop để điều tra.", {
        "A": "SSID không chứa thông tin luồng bị chặn.",
        "B": "Mật khẩu quản trị không phải dữ liệu điều tra và không được lưu kiểu này.",
        "D": "Ảnh chụp màn hình không ghi luồng mạng.",
    }),
    "case_30": ("Phân vùng mạng và lọc lưu lượng giữa các vùng chặn khách đi ngang tới DB.", {
        "A": "Mở DB cho mọi VLAN làm tăng rủi ro.",
        "B": "Firewall ở cổng Internet không thấy luồng khách đi tới DB bên trong.",
        "D": "Tắt xác thực DB càng nguy hiểm hơn.",
    }),
    "reviewed_atm_74": ("Firewall kiểm tra luồng theo luật cho phép/chặn tại ranh giới mạng.", {
        "A": "RADIUS là máy chủ xác thực.",
        "C": "IDS thụ động chỉ phát hiện và cảnh báo, không chặn theo luật.",
        "D": "Keylogger là mã độc ghi phím.",
    }),
    "reviewed_atm_92": ("Screened subnet tạo DMZ để web công khai tách khỏi vùng cơ sở dữ liệu.", {
        "A": "LAN phẳng để mọi máy chung một vùng.",
        "B": "Nối thẳng vào DB làm lộ DB.",
        "D": "Bỏ bộ lọc biên làm mất lớp bảo vệ.",
    }),
    "abbr_c3_016": ("DMZ là Demilitarized Zone, vùng phi quân sự, tức vùng đệm giữa Internet và mạng nội bộ.", {
        "B": "Không phải Dynamic Management Zone.",
        "C": "Không phải Direct Mail Zone.",
        "D": "Không phải Data Monitoring Zone.",
    }),
    "abbr_c3_017": ("NAT là Network Address Translation, dịch địa chỉ mạng.", {
        "A": "Không phải Node Authentication Table.",
        "B": "Không phải Network Access Token.",
        "C": "Không phải Network Alert Tracking.",
    }),
    "abbr_c3_018": ("SIF là Stateful Inspection Firewall, tường lửa kiểm tra trạng thái.", {
        "A": "Không phải Session Integrity Filter.",
        "C": "Không phải Secure Internet Firewall.",
        "D": "Không phải Static Interface Filter; SIF ngược với lọc tĩnh.",
    }),
    "abbr_c3_019": ("VPN là Virtual Private Network, mạng riêng ảo.", {
        "B": "Không phải Verified Public Network.",
        "C": "Không phải Virtual Packet Node.",
        "D": "Không phải Vendor Protected Network.",
    }),
    "abbr_c3_020": ("NGFW là Next-Generation Firewall, tường lửa thế hệ mới.", {
        "A": "Không phải Network-Grade Firewall.",
        "B": "Không phải Network Gateway Firewall.",
        "D": "Không phải New Global Filtering Wall.",
    }),
    "abbr_c3_021": ("WAF là Web Application Firewall, tường lửa ứng dụng web.", {
        "A": "Không phải Wireless Access Firewall.",
        "C": "Không phải Web Access Forwarder.",
        "D": "Không phải Wide Area Filter.",
    }),
    "abbr_c3_022": ("FWaaS là Firewall as a Service, tường lửa cung cấp dạng dịch vụ đám mây.", {
        "A": "Không phải Filtering Web as a Standard.",
        "B": "Không phải Firewall with Antivirus and Scanning.",
        "C": "Không phải Firewall Wide-area Access System.",
    }),
    "abbr_c3_023": ("SASE là Secure Access Service Edge.", {
        "B": "Không phải Software-Assisted Security Engine.",
        "C": "Không phải Secure Application Server Environment.",
        "D": "Không phải System Access and Session Encryption.",
    }),
    "abbr_c3_024": ("SSE là Security Service Edge, phần dịch vụ bảo mật của SASE.", {
        "A": "Không phải Secure Socket Encryption.",
        "B": "Không phải Session Security Engine.",
        "D": "Không phải Secure Server Exchange.",
    }),
    "abbr_c3_025": ("ZTNA là Zero Trust Network Access, truy cập mạng theo Zero Trust.", {
        "A": "Không phải Zoned Traffic Network Analyzer.",
        "C": "Chữ T là Trust, không phải Time; chữ A là Access, không phải Authentication.",
        "D": "Không phải Zone Transfer Network Address.",
    }),
    "abbr_c3_026": ("SWG là Secure Web Gateway, cổng kiểm soát truy cập web an toàn.", {
        "A": "Không phải Switched Wireless Gateway.",
        "B": "Không phải Software WAN Gateway.",
        "D": "Không phải Server Workload Guard.",
    }),
    "abbr_c3_027": ("CASB là Cloud Access Security Broker, kiểm soát việc dùng dịch vụ đám mây.", {
        "A": "Không phải Cloud Application Signature Base.",
        "B": "Không phải Content-Aware Security Backbone.",
        "C": "Không phải Central Authentication Service Broker.",
    }),
    "abbr_c3_028": ("SD-WAN là Software-Defined Wide Area Network, mạng diện rộng điều khiển bằng phần mềm.", {
        "B": "SD là Software-Defined, không phải Secure Data.",
        "C": "SD không phải Single-Domain.",
        "D": "SD không phải Switched Digital.",
    }),
    "rev_c3_029": ("Theo slide, SSE gồm SWG, CASB, ZTNA và FWaaS.", {
        "B": "DMZ, NAT, VPN, DHCP, DNS là các thành phần mạng truyền thống.",
        "C": "IDS, IPS, NIDS, HIDS là nhóm phát hiện xâm nhập ở Bài 4.",
        "D": "WEP, WPA, WPA2 là các chuẩn bảo mật Wi-Fi ở Bài 5.",
    }),
    "rev_c3_030": ("SASE = SSE (dịch vụ bảo mật) + kết nối diện rộng như SD-WAN.", {
        "A": "DMZ và proxy là kiến trúc truyền thống, không phải SASE.",
        "B": "IDS và router lọc không phải định nghĩa của SASE.",
        "C": "WAF và chữ ký virus không phải định nghĩa của SASE.",
    }),
    "rev_c3_031": ("Slide nói Zero Trust là mô hình kiến trúc (không mặc định tin ai), không phải một thiết bị cụ thể.", {
        "A": "Zero Trust ngược lại: không tin mặc định, kể cả máy trong LAN.",
        "C": "Zero Trust không phải dòng sản phẩm NGFW.",
        "D": "Zero Trust không phải giao thức mã hóa.",
    }),
    "rev_c3_032": ("WAF chuyên bảo vệ ứng dụng web: lưu lượng HTTP/HTTPS và API.", {
        "A": "Kiểm soát mọi giao thức là phạm vi của NGFW.",
        "B": "Chỉ lọc IP, cổng, giao thức là lọc gói; WAF đọc nội dung yêu cầu web.",
        "D": "WAF không thay NGFW; hai loại bổ sung cho nhau.",
    }),
    "rev_c3_033": ("East-west là lưu lượng bên trong: giữa các server, VLAN, VM.", {
        "A": "Người dùng từ xa vào VPN là luồng north-south.",
        "B": "ISP tới router biên là luồng north-south.",
        "D": "Doanh nghiệp ra Internet là north-south.",
    }),
    "rev_c3_034": ("Từ chối mặc định: luồng nào chưa được cho phép rõ ràng thì bị chặn.", {
        "A": "Cho phép mọi luồng là mặc định cho phép, ngược lại.",
        "C": "Nguyên tắc áp dụng cả hai chiều, không riêng inbound.",
        "D": "Luồng hợp lệ đã được cho phép thì vẫn đi qua.",
    }),
    "rev_c3_035": ("Slide ghi proxy firewall chấm dứt rồi tạo lại kết nối, nên tăng độ trễ.", {
        "A": "Proxy kiểm tra được nội dung ứng dụng; đó là ưu điểm của nó.",
        "B": "Hạn chế slide nêu là độ trễ, không phải theo dõi phiên.",
        "C": "Chỉ bảo vệ web và API là đặc điểm của WAF.",
    }),
    "rev_c3_141": ("Trong ma trận chính sách mẫu, Internet chỉ được vào WAF qua HTTPS/443.", {
        "A": "SMTP/25 là thư, không phải dịch vụ vào WAF.",
        "C": "FTP/21 là truyền tệp, không có trong luồng Internet vào WAF.",
        "D": "Ma trận dùng HTTPS/443, không mở HTTP/80 không mã hóa.",
    }),
    "rev_c3_142": ("Slide định nghĩa tường lửa là rào chắn giữa mạng tin cậy (nội bộ) và mạng không tin cậy (Internet).", {
        "A": "Cấp địa chỉ IP là DHCP.",
        "B": "Tường lửa phải kiểm tra gói, không chuyển tiếp mù.",
        "D": "Tường lửa không nhằm tăng tốc đường truyền.",
    }),
    "rev_c3_143": ("Slide nêu bốn chức năng: kiểm soát dịch vụ, hướng, người dùng và hành vi.", {
        "A": "Cấp IP, phân giải tên, gửi mail là DHCP, DNS, mail server.",
        "B": "Diệt virus, vá lỗi là việc của antivirus và quản lý bản vá.",
        "C": "Mã hóa ổ cứng, sao lưu là các biện pháp bảo vệ dữ liệu khác.",
    }),
    "rev_c3_144": ("Slide liệt kê Cisco ASA (cùng Checkpoint, CyberRoam) là tường lửa phần cứng.", {
        "B": "ISA Server Firewall được slide xếp vào giải pháp phần mềm.",
        "C": "Wireshark là công cụ bắt gói, không phải tường lửa.",
        "D": "IPCOP được slide xếp vào giải pháp phần mềm.",
    }),
    "rev_c3_145": ("Slide xếp Screened Host, Screened Subnet và Multi-homed Firewall vào kiến trúc kết hợp.", {
        "A": "WEP, WPA, WPA2 là chuẩn bảo mật Wi-Fi.",
        "C": "Standalone, Distributed, Hybrid là kiến trúc IDPS ở Bài 4.",
        "D": "Packet Filtering, Circuit Gateway, Application là các loại tường lửa theo cách lọc, không phải kiến trúc.",
    }),
    "rev_c3_146": ("Multi-homed firewall có nhiều cổng mạng, nối và tách nhiều vùng như LAN, DMZ, Internet.", {
        "A": "\"Multi-homed\" nghĩa là nhiều cổng, không phải một.",
        "B": "Cài trên nhiều máy trạm là tường lửa trên máy, không phải multi-homed.",
        "D": "Multi-homed nói về số cổng mạng, không phải chạy trên đám mây.",
    }),
    "rev_c3_147": ("Kiến trúc đơn lẻ: một thiết bị tường lửa duy nhất đảm nhận toàn bộ việc lọc.", {
        "B": "Kiến trúc nào cũng cần chính sách.",
        "C": "Nhiều tường lửa quản lý chung là hybrid mesh.",
        "D": "Tường lửa trong pod Kubernetes là NetworkPolicy/eBPF.",
    }),
    "rev_c3_148": ("Slide nói hybrid mesh firewall là thuật ngữ thị trường cho nền tảng quản lý thống nhất nhiều loại firewall (vật lý, ảo, đám mây).", {
        "A": "Không phải giao thức của IEEE.",
        "B": "Không phải thuật toán mã hóa.",
        "C": "\"Mesh\" ở đây không phải mạng không dây mesh.",
    }),
    "rev_c3_149": ("Slide nêu nhược điểm: phụ thuộc nhà cung cấp, và lộ tài khoản quản trị trung tâm thì ảnh hưởng toàn hệ thống.", {
        "A": "Hybrid mesh quản lý cả tường lửa phần cứng.",
        "B": "Không có yêu cầu tắt log.",
        "D": "Hybrid mesh sinh ra chính để dùng cho hybrid/multi-cloud.",
    }),
    "rev_c3_150": ("NetworkPolicy chỉ là khai báo; CNI của cụm phải hỗ trợ thì chính sách mới được thực thi.", {
        "B": "Tường lửa ngoại vi không liên quan việc NetworkPolicy có tác dụng.",
        "C": "Mỗi pod có IP riêng; NetworkPolicy không đòi chung IP.",
        "D": "Số node không quyết định NetworkPolicy có tác dụng.",
    }),
    "rev_c3_151": ("eBPF (như Cilium) chạy chương trình lọc ngay trong Linux kernel.", {
        "A": "RADIUS là máy chủ xác thực.",
        "C": "Router của ISP nằm ngoài cụm.",
        "D": "BIOS không thực thi chính sách mạng.",
    }),
    "rev_c3_152": ("TLS 1.3 và QUIC mã hóa thêm nhiều thông tin, nên thiết bị trung gian thấy ít hơn để kiểm tra.", {
        "A": "Chúng vẫn dùng cổng 443.",
        "B": "Chúng dùng trên Internet, không chỉ nội bộ.",
        "C": "Chúng vẫn chạy trên IP.",
    }),
    "rev_c3_153": ("Slide nêu giải mã TLS làm tăng tải, ảnh hưởng quyền riêng tư và có thể vi phạm yêu cầu bảo mật, nên không bật tràn lan.", {
        "A": "Giải mã nội dung không làm mất IP nguồn hay cổng đích.",
        "C": "Tường lửa giải mã được TLS (đóng vai trung gian), chỉ là có cái giá phải trả.",
        "D": "Giải mã TLS không bắt buộc tắt NAT.",
    }),
    "rev_c3_154": ("Slide đánh giá nhận định này sai: AI chỉ bổ trợ cho luật, chữ ký, sandbox và chuyên gia.", {
        "A": "AI không thay thế hoàn toàn luật và con người.",
        "B": "Không tường lửa nào chặn được mọi mối đe dọa chưa biết.",
        "C": "Bật giải mã TLS không làm AI chặn được mọi thứ.",
    }),
    "rev_c3_155": ("NGFW ở biên không chặn luồng giữa các máy chủ bên trong; máy chủ giao tiếp tự do nên kẻ tấn công vẫn di chuyển ngang được.", {
        "A": "Số địa chỉ IP không liên quan.",
        "B": "HTTPS vẫn truy cập bình thường.",
        "D": "Kết nối Internet không bị ảnh hưởng.",
    }),
}
