EXPLAIN = {
    "gen_326": ("Tên Wi-Fi hiện trong danh sách mạng là SSID, tên logic của WLAN.", {
        "A": "BSSID là địa chỉ MAC của từng AP/radio, không phải tên mạng người dùng chọn.",
        "B": "Access Point là thiết bị phát sóng, không phải tên mạng.",
        "C": "Station là thiết bị của người dùng (laptop, điện thoại).",
    }),
    "gen_327": ("SSID chỉ là một cái tên ai cũng đặt được, nên kẻ tấn công có thể dựng AP giả cùng tên (Evil Twin).", {
        "A": "SSID được phát công khai trong beacon, không được mã hóa.",
        "B": "Một SSID dùng được cho nhiều AP và nhiều lần.",
        "C": "SSID không chứa mật khẩu.",
    }),
    "gen_330": ("BSSID là MAC của từng AP/radio, nên phân biệt được các AP dù cùng SSID.", {
        "A": "Phân biệt người dùng là việc của xác thực (802.1X/RADIUS).",
        "B": "Kiểu mã hóa không xác định bằng BSSID.",
        "C": "Băng tần không xác định bằng BSSID.",
    }),
    "gen_332": ("Thiết bị nhận kết nối vô tuyến và nối vào LAN có dây là Access Point.", {
        "A": "Station là chính chiếc laptop, không phải thiết bị nối vào LAN.",
        "B": "BSSID là địa chỉ của AP, không phải thiết bị.",
        "D": "SSID là tên mạng.",
    }),
    "gen_333": ("AP là điểm kết nối giữa các máy không dây và mạng có dây.", {
        "B": "Máy khách không dây là station (STA).",
        "C": "Máy chủ xác thực là RADIUS.",
        "D": "Phát nhiễu chặn sóng là jamming, không phải vai trò của AP.",
    }),
    "gen_335": ("Điện thoại là thiết bị đầu cuối không dây gửi khung tới AP, tức station.", {
        "A": "SSID là tên mạng.",
        "C": "AP là đầu nhận, còn điện thoại là station.",
        "D": "BSSID là địa chỉ của AP.",
    }),
    "gen_336": ("STA là thiết bị đầu cuối có card không dây như laptop, điện thoại.", {
        "A": "Thiết bị phát sóng nối vào mạng có dây là AP.",
        "B": "Cấp IP là DHCP.",
        "C": "Quản lý nhiều AP là bộ điều khiển WLAN (controller).",
    }),
    "gen_338": ("Nghe kênh, thấy bận thì hoãn truyền để tránh xung đột là CSMA/CA.", {
        "A": "RTS/CTS là trao đổi khung xin/cho phép gửi trước khi truyền.",
        "B": "Beacon là khung AP quảng bá thông tin mạng.",
        "C": "Association là bước ghép nối với AP.",
    }),
    "gen_339": ("WLAN dùng CSMA/CA (tránh xung đột) vì máy không dây không vừa phát vừa nghe để phát hiện xung đột được.", {
        "A": "CSMA/CD (phát hiện xung đột) dùng cho Ethernet có dây.",
        "B": "Token Ring là mạng vòng có dây kiểu cũ.",
        "C": "TDMA chia khe thời gian, dùng ở mạng di động, không phải WLAN.",
    }),
    "gen_341": ("Hai máy không nghe thấy nhau (trạm ẩn) trao đổi khung RTS/CTS với AP trước khi gửi dữ liệu.", {
        "A": "Association là ghép nối với AP.",
        "B": "CSMA/CA thuần chỉ nghe kênh, không giải quyết được trạm ẩn.",
        "C": "Beacon là khung quảng bá của AP.",
    }),
    "gen_342": ("RTS/CTS hữu ích khi xung đột do trạm ẩn (hidden node) đáng kể.", {
        "A": "RTS/CTS không chống nghe lén.",
        "B": "RTS/CTS không mã hóa dữ liệu.",
        "C": "RTS/CTS không ẩn SSID.",
    }),
    "gen_344": ("Máy quét thấy mạng nhờ khung AP phát định kỳ: beacon frame.", {
        "B": "Association là bước kết nối sau khi đã thấy mạng.",
        "C": "RTS/CTS dùng để điều phối truyền dữ liệu.",
        "D": "CSMA/CA là cơ chế truy nhập kênh.",
    }),
    "gen_345": ("AP định kỳ phát beacon để quảng bá thông tin mạng như SSID.", {
        "A": "Beacon không mã hóa dữ liệu.",
        "B": "Xác thực với RADIUS là 802.1X/EAP.",
        "D": "Ngắt kết nối dùng khung deauthentication.",
    }),
    "gen_347": ("Ghép nối logic giữa máy trạm và AP sau khi chọn mạng là association.", {
        "A": "CSMA/CA là cơ chế truy nhập kênh.",
        "C": "Beacon là khung quảng bá của AP.",
        "D": "RTS/CTS điều phối việc gửi dữ liệu.",
    }),
    "gen_348": ("STA dò tìm mạng trước, rồi xác thực với AP, cuối cùng mới kết hợp (association).", {
        "A": "Phải thấy mạng trước khi kết hợp.",
        "B": "Phải dò tìm mạng trước khi xác thực.",
        "C": "Mã hóa diễn ra sau khi đã kết nối, không phải bước đầu tiên.",
    }),
    "gen_350": ("AP cá nhân cắm vào LAN công ty mà không được phê duyệt là rogue AP.", {
        "B": "Evil Twin là AP giả cùng tên mạng để dụ người dùng.",
        "C": "Deauth spoofing là gửi khung ngắt kết nối giả.",
        "D": "Jamming là phát nhiễu.",
    }),
    "gen_351": ("Rogue AP là AP gắn vào mạng mà không được quản trị phê duyệt.", {
        "A": "AP chính thức được quản lý thì không phải rogue.",
        "B": "Ẩn SSID không làm AP thành rogue.",
        "C": "Dùng WPA3 không liên quan việc AP có được phê duyệt.",
    }),
    "gen_354": ("Evil Twin dựng AP giả cùng tên mạng để người dùng kết nối nhầm vào.", {
        "A": "Phát nhiễu là jamming.",
        "B": "Dò PIN WPS là tấn công WPS.",
        "C": "Bẻ WEP bằng IV lặp là tấn công WEP.",
    }),
    "gen_356": ("Phát nhiễu cùng băng tần làm thiết bị mất kết nối là jamming.", {
        "B": "Evil Twin là AP giả, không phát nhiễu.",
        "C": "Deauth spoofing dùng khung quản lý giả, không phải nhiễu.",
        "D": "Rogue AP là AP không được phê duyệt.",
    }),
    "gen_357": ("Jamming phát nhiễu vô tuyến để làm gián đoạn kênh truyền.", {
        "A": "Dựng AP giả cùng SSID là Evil Twin.",
        "B": "Bẻ WEP bằng IV lặp là tấn công WEP.",
        "D": "Dò mật khẩu bằng từ điển là tấn công từ điển.",
    }),
    "gen_359": ("Khung quản lý giả làm STA bị ngắt khỏi AP là deauthentication spoofing.", {
        "A": "Jamming dùng nhiễu, không dùng khung giả.",
        "B": "Rogue AP là AP không được phê duyệt.",
        "D": "Evil Twin là AP giả cùng tên.",
    }),
    "gen_360": ("Khung deauthentication giả làm máy khách bị ngắt kết nối khỏi AP.", {
        "B": "Tấn công này không đổi mật khẩu.",
        "C": "Nó không làm hỏng phần cứng AP.",
        "D": "Nó không làm mã hóa mạnh hơn.",
    }),
    "gen_362": ("Thu khung phát trên Wi-Fi mở để xem nội dung là nghe lén WLAN.", {
        "A": "Tấn công từ điển là dò mật khẩu.",
        "B": "Truy cập trái phép là vào mạng khi không được phép; ở đây chỉ thu khung.",
        "C": "Tấn công WPS PIN là dò mã PIN.",
    }),
    "gen_363": ("Sóng radio lan ra không gian, ai trong vùng phủ cũng thu được mà không cần cắm dây.", {
        "A": "WLAN vẫn dùng IP và áp dụng được tường lửa.",
        "B": "Tốc độ không quyết định việc bị nghe lén.",
        "D": "AP có địa chỉ MAC (chính là BSSID).",
    }),
    "gen_365": ("Đoán PSK yếu từ danh sách từ thông dụng là tấn công từ điển mật khẩu.", {
        "A": "Tấn công WPS PIN dò mã PIN 8 chữ số, không dùng từ điển.",
        "B": "Nghe lén chỉ thu khung.",
        "C": "Truy cập trái phép là hậu quả sau khi có mật khẩu, không phải cách đoán.",
    }),
    "gen_366": ("Mật khẩu dài, ngẫu nhiên không có trong từ điển nên tấn công từ điển khó thành công.", {
        "A": "Đổi SSID không làm mật khẩu khó đoán hơn.",
        "B": "Giảm công suất phát không bảo vệ mật khẩu.",
        "D": "Bật WPS thêm một điểm yếu khác.",
    }),
    "gen_368": ("Router mở WPS PIN để kẻ gần đó thử nhiều tổ hợp là tấn công WPS PIN.", {
        "A": "Truy cập trái phép là kết quả, không phải tên kỹ thuật tấn công.",
        "C": "Tấn công từ điển nhắm vào mật khẩu PSK, không vào mã PIN.",
        "D": "Nghe lén chỉ thu khung.",
    }),
    "gen_369": ("Tắt WPS khi không dùng thì không còn mã PIN để dò.", {
        "B": "Bật WPS cho mọi thiết bị làm rủi ro tăng.",
        "C": "Đổi SSID không ảnh hưởng tới WPS.",
        "D": "Mạng mở kém an toàn hơn.",
    }),
    "gen_371": ("Người ngoài dùng mật khẩu chung để vào LAN nội bộ là truy cập trái phép WLAN.", {
        "A": "Nghe lén chỉ thu khung, không vào mạng.",
        "C": "Họ đã biết mật khẩu, không cần dò PIN.",
        "D": "Họ được biết mật khẩu, không phải đoán bằng từ điển.",
    }),
    "gen_372": ("802.1X với RADIUS cho mỗi người một tài khoản riêng; mật khẩu chung không còn, và thu hồi được từng người.", {
        "A": "SSID ẩn vẫn bị lộ khi quét, và không ngăn người biết mật khẩu.",
        "B": "Tên thiết bị đổi được dễ dàng.",
        "C": "Tăng công suất phát làm sóng lan xa hơn.",
    }),
    "gen_375": ("Slide coi WEP là kiến thức legacy, không dùng cho thiết kế mới vì đã bị bẻ.", {
        "A": "WEP không còn là tiêu chuẩn hiện hành.",
        "B": "WEP không an toàn, kể cả cho mạng khách.",
        "D": "Wi-Fi 6/7 dùng WPA3, không dùng WEP.",
    }),
    "gen_377": ("Lớp trung gian giữa WEP và WPA2 (AES-CCMP) là WPA, dùng TKIP.", {
        "A": "WPA2 chính là thế hệ dùng AES-CCMP.",
        "B": "WEP là thế hệ trước, không phải lớp trung gian.",
        "D": "Mạng mở không có bảo vệ.",
    }),
    "gen_378": ("WPA ra đời để thay WEP, dùng TKIP đổi khóa theo gói nhằm tăng bảo mật.", {
        "A": "WPA ra trước WPA3 nhiều năm.",
        "C": "WPA mã hóa dữ liệu, không mã hóa SSID.",
        "D": "WPA không liên quan tốc độ Wi-Fi 6.",
    }),
    "gen_380": ("Chế độ Enterprise với 802.1X là WPA2-Enterprise.", {
        "A": "WPA là thế hệ cũ dùng TKIP; câu hỏi nhắm tới WPA2 trong slide.",
        "B": "Mạng mở không có xác thực.",
        "C": "WEP không có chế độ Enterprise với 802.1X.",
    }),
    "gen_381": ("Theo slide, WPA2 chuẩn hóa năm 2004 và dùng AES-CCMP.", {
        "A": "1997 là năm 802.11 gốc; RC4 là của WEP.",
        "C": "2018 và SAE là của WPA3.",
        "D": "2003 và TKIP là của WPA.",
    }),
    "gen_383": ("Kết nối SSID mà không cần khóa là mạng WLAN mở.", {
        "A": "WEP cần khóa.",
        "B": "WPA2 cần khóa hoặc tài khoản.",
        "D": "WPA cần khóa.",
    }),
    "gen_384": ("Mạng mở không mã hóa ở tầng WLAN, nên dữ liệu dễ bị nghe lén.", {
        "A": "Mạng mở vẫn vào được Internet.",
        "B": "Máy không tự chuyển sang WPA3.",
        "D": "Mạng mở vẫn phát SSID.",
    }),
    "gen_386": ("Khóa dòng kèm IV ngắn là đặc điểm của RC4 trong WEP.", {
        "B": "IV chỉ là một thành phần; thuật toán khóa dòng được hỏi là RC4.",
        "C": "AES-CCMP là mã hóa khối, không phải khóa dòng.",
        "D": "TKIP là giao thức quản lý khóa bọc quanh RC4.",
    }),
    "gen_387": ("RC4 là mã hóa dòng (stream cipher).", {
        "B": "AES-CCM là mã hóa khối, dùng ở WPA2.",
        "C": "RC4 không phải hàm băm.",
        "D": "SAE là giao thức trao đổi khóa của WPA3.",
    }),
    "gen_389": ("Trộn khóa theo từng gói để nâng cấp từ WEP trên thiết bị cũ là TKIP.", {
        "A": "AES-CCMP cần phần cứng mới hơn, không phải nâng cấp cho thiết bị WEP.",
        "B": "RC4 là thuật toán cũ của WEP.",
        "C": "IV là vector khởi tạo, không phải cơ chế nâng cấp.",
    }),
    "gen_390": ("TKIP đổi khóa theo từng gói thay cho một khóa tĩnh như WEP.", {
        "A": "Chuyển sang AES-CCMP là WPA2, không phải TKIP.",
        "B": "TKIP vẫn mã hóa.",
        "D": "TKIP không bắt buộc RADIUS.",
    }),
    "gen_392": ("Chọn WPA2 với CCMP là dùng AES-CCMP.", {
        "A": "TKIP là thứ bị thay thế trong tình huống.",
        "C": "RC4 là thuật toán của WEP.",
        "D": "IV là thành phần của WEP.",
    }),
    "gen_395": ("Giá trị 24 bit bị dùng lại trong WEP là IV (vector khởi tạo).", {
        "A": "AES-CCMP không có điểm yếu này.",
        "C": "TKIP ra đời để khắc phục điểm yếu này.",
        "D": "RC4 là thuật toán; giá trị 24 bit bị lặp là IV.",
    }),
    "gen_398": ("Một mật khẩu chung cho mọi khách là WPA2-Personal (PSK).", {
        "B": "RADIUS là máy chủ xác thực từng người.",
        "C": "802.1X là xác thực từng người, không dùng mật khẩu chung.",
        "D": "Enterprise dùng tài khoản riêng.",
    }),
    "gen_401": ("Tài khoản riêng từng sinh viên qua RADIUS là WPA2-Enterprise.", {
        "A": "Personal dùng mật khẩu chung.",
        "B": "802.1X chỉ là cơ chế kiểm soát cổng bên trong; cấu hình WLAN được gọi là WPA2-Enterprise.",
        "C": "RADIUS chỉ là máy chủ xác thực, không phải tên chế độ bảo mật.",
    }),
    "gen_404": ("Máy chủ AAA nhận yêu cầu xác thực từ AP là RADIUS.", {
        "B": "WPA2-Enterprise là tên chế độ, còn server AAA là RADIUS.",
        "C": "Personal không có server AAA.",
        "D": "802.1X là cơ chế kiểm soát cổng, không phải máy chủ.",
    }),
    "gen_407": ("Phải xong EAP mới được vào mạng là kiểm soát truy cập theo cổng 802.1X.", {
        "A": "Personal không dùng EAP.",
        "B": "Enterprise là tên chế độ; cơ chế chặn cổng tới khi xong EAP là 802.1X.",
        "D": "RADIUS là máy chủ xác thực phía sau.",
    }),
    "gen_410": ("Khách chỉ ra Internet mà không vào server nội bộ là phân tách mạng khách.", {
        "A": "Quản lý AP tập trung là cấu hình AP từ một nơi.",
        "C": "Giám sát WLAN là phát hiện bất thường.",
        "D": "Phân tách IoT dành cho thiết bị IoT, không phải khách.",
    }),
    "gen_413": ("Camera (IoT) chỉ được tới máy ghi hình là phân tách mạng IoT.", {
        "A": "Giám sát WLAN là phát hiện bất thường.",
        "B": "Quản lý AP tập trung là cấu hình AP.",
        "C": "Mạng khách dành cho người dùng khách, không phải camera.",
    }),
    "gen_416": ("Đẩy chính sách SSID đồng bộ cho nhiều tòa nhà là quản lý AP tập trung.", {
        "A": "Phân tách IoT là tách vùng mạng cho thiết bị IoT.",
        "B": "Phân tách mạng khách là tách vùng cho khách.",
        "C": "Giám sát WLAN là phát hiện bất thường.",
    }),
    "gen_419": ("Cảnh báo khi có SSID giả gần khuôn viên là giám sát WLAN.", {
        "A": "Quản lý tập trung là cấu hình AP.",
        "B": "Phân tách mạng khách là tách vùng.",
        "C": "Phân tách IoT là tách vùng.",
    }),
    "case_41": ("BSSID là địa chỉ riêng của từng AP/radio, nên phân biệt được hai AP cùng SSID.", {
        "A": "SSID giống nhau nên không phân biệt được.",
        "C": "Tên VLAN không nhận dạng AP.",
        "D": "Địa chỉ website không liên quan AP.",
    }),
    "case_42": ("AP giả cùng tên Wi-Fi để dụ kết nối là Evil Twin.", {
        "A": "Worm qua SMB lây qua chia sẻ tệp.",
        "B": "Tràn bộ đệm là lỗi chương trình.",
        "D": "Jamming là phát nhiễu.",
    }),
    "case_43": ("Nhiễu sóng khiến thiết bị không duy trì được kết nối: WLAN mất tính sẵn sàng.", {
        "A": "Chứng thư web không liên quan nhiễu sóng.",
        "B": "Tệp Word không bị sửa.",
        "C": "Bản sao lưu không bị lộ.",
    }),
    "case_44": ("Điểm yếu lịch sử của WEP là IV ngắn (24 bit) bị tái sử dụng với RC4.", {
        "A": "WEP không dùng chứng thư máy chủ.",
        "B": "Chặn khung quản lý giả là PMF, không có trong WEP.",
        "C": "SAE là của WPA3.",
    }),
    "case_45": ("WPA2-Enterprise với 802.1X và RADIUS cấp tài khoản riêng, khóa được từng người mà không đổi mật khẩu chung.", {
        "B": "WEP một khóa chung, lại không an toàn.",
        "C": "Mạng mở không có xác thực.",
        "D": "PSK chung phải đổi cho mọi người khi thu hồi.",
    }),
    "case_46": ("WPA3-Personal thay PSK cũ bằng SAE, chống đoán mật khẩu ngoại tuyến.", {
        "B": "TKIP là của WPA.",
        "C": "WEP là chuẩn cũ.",
        "D": "RC4 là thuật toán của WEP.",
    }),
    "case_47": ("PMF (Protected Management Frames) bảo vệ khung quản lý, chống deauthentication giả.", {
        "B": "WEP IV là điểm yếu cũ, không bảo vệ gì.",
        "C": "NAT là dịch địa chỉ.",
        "D": "DHCP cấp địa chỉ IP.",
    }),
    "case_48": ("OWE (Enhanced Open) mã hóa liên kết cho từng thiết bị trên mạng mở mà không cần mật khẩu.", {
        "B": "WPS PIN là cơ chế cài đặt dễ bị dò.",
        "C": "TKIP cần mật khẩu.",
        "D": "WEP cần khóa chung.",
    }),
    "case_49": ("SSID chỉ là tên, AP giả đặt được trùng tên, nên SSID giống không chứng minh AP là thật.", {
        "A": "Nhiều AP (kể cả AP giả) có thể cùng SSID.",
        "B": "WPA2 bảo vệ liên kết Wi-Fi, không xác minh trang web.",
        "D": "BSSID được phát công khai, quan sát được.",
    }),
    "case_50": ("VLAN khách riêng cộng luật lọc giữa các vùng chặn khách tới máy chủ nội bộ.", {
        "B": "Bỏ kiểm soát làm khách vào được mọi nơi.",
        "C": "Cùng VLAN với DB là mở đường tới DB.",
        "D": "Đổi tên SSID không đổi quyền truy cập.",
    }),
    "reviewed_atm_42": ("WEP dùng RC4 với IV ngắn và không nên triển khai mới.", {
        "A": "WPA dùng TKIP để khắc phục WEP.",
        "B": "802.1X là cơ chế xác thực, không phải giao thức mã hóa.",
        "D": "WPA2 dùng AES-CCMP.",
    }),
    "reviewed_atm_93": ("HTTPS hợp lệ mã hóa đầu cuối tới website, nên nội dung vẫn an toàn dù Wi-Fi không mã hóa.", {
        "A": "Bỏ kiểm tra chứng thư mở đường cho MITM.",
        "C": "Chia sẻ tệp trên mạng công cộng làm lộ dữ liệu.",
        "D": "Tắt cập nhật trình duyệt giữ lại lỗ hổng.",
    }),
    "reviewed_atm_104": ("WPA2 gắn với AES-CCMP thay cho WEP/RC4.", {
        "A": "WPA dùng TKIP, vẫn dựa trên RC4.",
        "B": "Mạng mở không mã hóa.",
        "D": "WEP chính là thứ bị thay thế.",
    }),
    "reviewed_atm_124": ("Tách VLAN khách và lọc truy cập giữa các vùng.", {
        "A": "Dùng chung VLAN nội bộ làm khách thấy máy chủ.",
        "B": "Mở mọi cổng làm tăng rủi ro.",
        "C": "Tắt log không ngăn truy cập.",
    }),
    "abbr_c5_057": ("WLAN là Wireless Local Area Network, mạng cục bộ không dây.", {
        "A": "Không phải Wireless Link Access Node.",
        "B": "W là Wireless, không phải Wide.",
        "D": "W là Wireless, không phải Wired.",
    }),
    "abbr_c5_058": ("SSID là Service Set Identifier, tên logic của WLAN.", {
        "B": "Không phải Secure Station ID.",
        "C": "Chỉ số tín hiệu là RSSI.",
        "D": "Không phải Shared Secret ID.",
    }),
    "abbr_c5_059": ("BSSID nhận dạng một BSS/radio cụ thể (thường là MAC của AP).", {
        "A": "Xác thực người dùng là RADIUS.",
        "B": "Ẩn tên mạng là tắt phát SSID.",
        "C": "Mã hóa khung là WPA2/WPA3.",
    }),
    "abbr_c5_060": ("STA là Station (thiết bị đầu cuối), AP là Access Point (điểm truy cập).", {
        "A": "Không phải Standard Antenna và Access Port.",
        "C": "AP không phải Authentication Proxy server.",
        "D": "Không phải Static Address và Access Protocol.",
    }),
    "abbr_c5_061": ("WEP là Wired Equivalent Privacy, mục tiêu riêng tư tương đương mạng có dây.", {
        "A": "Không phải Wireless Enhanced Privacy.",
        "B": "Tên hay bị nhầm là Wireless Encryption Protocol, nhưng tên đúng là Wired Equivalent Privacy.",
        "D": "Không phải Wi-Fi Encrypted Password.",
    }),
    "abbr_c5_062": ("IV là Initialization Vector, vector khởi tạo 24 bit ghép với khóa WEP.", {
        "B": "Không phải Identity Validation.",
        "C": "Không phải Integrity Value (đó là ICV).",
        "D": "Không phải Internal Verification.",
    }),
    "abbr_c5_063": ("WPA là Wi-Fi Protected Access.", {
        "A": "W là Wi-Fi, không phải Wired.",
        "C": "Không phải Wi-Fi Password Authentication.",
        "D": "Không phải Wireless Privacy Algorithm.",
    }),
    "abbr_c5_064": ("TKIP là Temporal Key Integrity Protocol, dùng khóa tạm thời đổi theo gói.", {
        "A": "Không phải Transport Key Interchange Protocol.",
        "B": "Không phải Trusted Key Infrastructure Protocol.",
        "C": "Không phải Timed Key Initialization Process.",
    }),
    "abbr_c5_065": ("CCMP là Counter Mode with CBC-MAC Protocol.", {
        "A": "Không phải Cipher Chain Management Protocol.",
        "B": "Không phải Central Certificate Management Protocol.",
        "D": "Không phải Combined Cipher and MAC Process.",
    }),
    "abbr_c5_066": ("PSK là Pre-Shared Key, khóa chia sẻ trước dùng chung.", {
        "A": "Không phải Private Session Key.",
        "B": "Không phải Public Signing Key.",
        "C": "Không phải Protected Station Key.",
    }),
    "abbr_c5_067": ("SAE là Simultaneous Authentication of Equals, xác thực đồng thời giữa hai bên ngang hàng.", {
        "B": "Không phải Secure AES Encryption.",
        "C": "Không phải Shared Access Exchange.",
        "D": "Không phải Station Authentication and Encryption.",
    }),
    "abbr_c5_068": ("PMF là Protected Management Frames, bảo vệ khung quản lý.", {
        "A": "Không phải Protected Media Format.",
        "C": "Không phải Primary MAC Filter.",
        "D": "Không phải Pre-shared Master Frame.",
    }),
    "abbr_c5_069": ("OWE là Opportunistic Wireless Encryption, mã hóa cơ hội cho mạng mở.", {
        "A": "Không phải Optional WPA Encryption.",
        "B": "Không phải Offline Wi-Fi Enrollment.",
        "C": "Không phải Open Wireless Exchange.",
    }),
    "abbr_c5_070": ("EAP là Extensible Authentication Protocol, khung xác thực mở rộng.", {
        "B": "Không phải Encrypted Access Protocol.",
        "C": "Không phải External AP Protocol.",
        "D": "Không phải Enterprise Authorization Policy.",
    }),
    "abbr_c5_071": ("RADIUS là Remote Authentication Dial-In User Service.", {
        "A": "Không phải Radio Access Domain Identity Service.",
        "C": "Không phải Remote Access Directory Integration Unit.",
        "D": "Không phải Routing Authentication and Data Integrity Service.",
    }),
    "abbr_c5_072": ("AAA là Authentication (xác thực), Authorization (phân quyền), Accounting (ghi nhận).", {
        "A": "Association, ACK là khái niệm WLAN, không phải AAA.",
        "B": "Không phải Access, Audit, Alert.",
        "D": "Availability, Anonymity không thuộc AAA.",
    }),
    "abbr_c5_073": ("WPS là Wi-Fi Protected Setup, cơ chế cài đặt nhanh bằng nút/PIN.", {
        "A": "Không phải Wi-Fi Privacy Service.",
        "C": "Không phải WPA Pre-Shared.",
        "D": "Không phải Wireless Password Storage.",
    }),
    "abbr_c5_074": ("NAC là Network Access Control, kiểm soát truy cập mạng.", {
        "A": "Không phải Network Authentication Certificate.",
        "B": "Không phải Network Alert Console.",
        "D": "Không phải Node Address Cache.",
    }),
    "abbr_c5_075": ("PMK là Pairwise Master Key, khóa chủ dùng để sinh khóa phiên trong 4-Way Handshake.", {
        "B": "P là Pairwise, không phải Public.",
        "C": "Không phải Protected Management Key.",
        "D": "Không phải Primary MAC Key.",
    }),
    "abbr_c5_076": ("GTK (Group Temporal Key) là khóa nhóm cho broadcast/multicast, được AP gửi trong 4-Way Handshake.", {
        "A": "PSK là mật khẩu chung để sinh PMK, không phải khóa nhóm.",
        "B": "PTK là khóa riêng cho từng cặp STA–AP (unicast).",
        "C": "PMK là khóa chủ, không dùng trực tiếp cho broadcast.",
    }),
    "abbr_c5_077": ("CSMA/CA là Carrier Sense Multiple Access with Collision Avoidance (tránh xung đột).", {
        "A": "CA là Collision Avoidance, không phải Authentication.",
        "C": "Không phải Channel Security Management with Certificate Authority.",
        "D": "Không phải Carrier Signal Modulation with Channel Allocation.",
    }),
    "std_c5_078": ("IEEE 802.11i quy định các giao thức bảo mật WLAN (nền tảng của WPA2).", {
        "A": "802.3 là Ethernet có dây.",
        "B": "802.11ac là chuẩn tốc độ (Wi-Fi 5).",
        "D": "802.11n là chuẩn tốc độ (Wi-Fi 4).",
    }),
    "std_c5_079": ("PMF được chuẩn hóa trong IEEE 802.11w.", {
        "A": "802.11be là Wi-Fi 7.",
        "B": "802.11g là chuẩn tốc độ cũ 54 Mbps.",
        "C": "802.1Q là chuẩn VLAN.",
    }),
    "std_c5_080": ("Wi-Fi 6 là IEEE 802.11ax.", {
        "B": "802.11ac là Wi-Fi 5.",
        "C": "802.11be là Wi-Fi 7.",
        "D": "802.11n là Wi-Fi 4.",
    }),
    "std_c5_081": ("Wi-Fi 7 là IEEE 802.11be.", {
        "A": "802.11ac là Wi-Fi 5.",
        "C": "802.11i là chuẩn bảo mật.",
        "D": "802.11ax là Wi-Fi 6.",
    }),
    "std_c5_082": ("Slide nói Wi-Fi 7 chủ yếu cải tiến PHY/MAC (tốc độ, độ trễ), không tự làm mạng an toàn hơn.", {
        "B": "Không chuẩn nào chống được mọi kiểu gây nhiễu.",
        "C": "Wi-Fi 7 vẫn dùng WPA3.",
        "D": "Vẫn cần 802.1X và PMF.",
    }),
    "std_c5_083": ("Chuẩn IEEE 802.11 gốc ban hành năm 1997.", {
        "A": "2004 là năm WPA2 (802.11i).",
        "B": "1999 là năm 802.11a/b, không phải bản gốc.",
        "D": "2009 là năm 802.11n.",
    }),
    "std_c5_084": ("WPA2 dùng AES-CCMP.", {
        "A": "TKIP là của WPA.",
        "B": "SAE và OWE là của WPA3/Enhanced Open.",
        "C": "RC4 + IV 24 bit là WEP.",
    }),
    "std_c5_085": ("Slide nêu PMF là bắt buộc trong chứng nhận WPA3.", {
        "A": "WPA3 không dùng khóa WEP.",
        "B": "WPS PIN không bắt buộc và nên tắt.",
        "C": "TKIP không có trong WPA3.",
    }),
    "std_c5_086": ("Khóa WEP dài 40 hoặc 104 bit, ghép với IV 24 bit (thành 64/128 bit).", {
        "A": "56 bit là độ dài khóa DES.",
        "C": "192 bit kèm PMK không phải WEP.",
        "D": "128/256 bit kèm nonce không phải WEP.",
    }),
    "std_c5_087": ("802.1X kiểm soát truy cập theo cổng, EAP là khung xác thực, RADIUS cung cấp dịch vụ AAA.", {
        "A": "802.1X không phải dịch vụ AAA, EAP không phải thuật toán mã hóa.",
        "B": "EAP không mã hóa, RADIUS không định tuyến.",
        "D": "Không cái nào trong ba là mã hóa khung, hàm băm hay chữ ký số.",
    }),
    "std_c5_088": ("802.1X là cơ chế kiểm soát truy cập theo cổng (port-based).", {
        "B": "Chuẩn tốc độ Wi-Fi 6 là 802.11ax.",
        "C": "Cấp IP động là DHCP.",
        "D": "802.1X không mã hóa khung.",
    }),
    "std_c5_089": ("KRACK khai thác lỗi cài lại khóa (key reinstallation) trong 4-Way Handshake.", {
        "A": "Dò PIN WPS là tấn công khác.",
        "C": "KRACK không phá AES.",
        "D": "Beacon không mã hóa là bình thường, không phải điểm KRACK khai thác.",
    }),
}
