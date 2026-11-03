EXPLAIN = {
    "gen_230": ("Chỉ gửi cảnh báo mà không tự chặn là IDS (hệ thống phát hiện xâm nhập).", {
        "B": "Firewall chặn hoặc cho qua theo luật, không chỉ gửi cảnh báo.",
        "C": "IDPS gồm cả phát hiện lẫn ngăn chặn; ở đây không có chặn.",
        "D": "IPS chủ động chặn gói, trái với tình huống.",
    }),
    "gen_231": ("IDS phát hiện thì tạo cảnh báo và ghi log để quản trị viên xử lý; nó không tự can thiệp.", {
        "A": "Xóa tệp, khởi động lại máy là hành động chủ động mà IDS không làm.",
        "B": "IDS không ngắt điện máy chủ.",
        "C": "IDS không đổi mật khẩu người dùng.",
    }),
    "gen_234": ("IPS đặt trên đường truyền nên có thể chủ động chặn lưu lượng tấn công; IDS chỉ cảnh báo.", {
        "A": "Chỉ ghi log và cảnh báo là IDS.",
        "C": "IPS dùng cho mọi loại mạng, có bản riêng cho không dây là WIPS.",
        "D": "IPS cũng cần luật hoặc chữ ký để nhận ra tấn công.",
    }),
    "gen_236": ("Hệ thống vừa cảnh báo vừa chặn là IDPS (Intrusion Detection and Prevention System).", {
        "A": "Firewall lọc theo luật, không phải hệ phát hiện xâm nhập.",
        "C": "IPS nhấn vào việc chặn; tên gọi bao cả hai chức năng là IDPS.",
        "D": "IDS chỉ phát hiện, không chặn.",
    }),
    "gen_237": ("Slide nêu ba mô hình triển khai IDPS: Standalone, Distributed và Hybrid.", {
        "A": "Personal, Enterprise, Open là chế độ bảo mật Wi-Fi.",
        "B": "Packet, Circuit, Application là các loại tường lửa.",
        "C": "Boot, File, Macro là các loại virus.",
    }),
    "gen_239": ("Chặn cổng không được mở theo ACL là việc của firewall.", {
        "A": "IDS chỉ cảnh báo, không chặn theo ACL.",
        "B": "IPS chặn theo dấu hiệu tấn công, không theo ACL mở/đóng cổng.",
        "C": "IDPS phát hiện/ngăn tấn công theo dấu hiệu, không phải lọc cổng theo ACL.",
    }),
    "gen_240": ("Firewall chỉ cho qua/chặn theo luật (IP, cổng); tấn công đi qua cổng được mở vẫn lọt, nên cần IDS/IPS phân tích dấu hiệu tấn công.", {
        "A": "Firewall chặn được cổng; đó là chức năng chính của nó.",
        "C": "IDS/IPS bổ sung chứ không thay firewall.",
        "D": "Firewall dùng cho mọi loại mạng.",
    }),
    "gen_242": ("Thiết bị nhận bản sao gói từ cổng SPAN để phân tích lưu lượng mạng là NIDS.", {
        "A": "HIDS chạy trên máy, đọc sự kiện của máy, không nhận gói từ SPAN.",
        "B": "NIPS phải đặt inline; nhận bản sao thì không chặn được.",
        "D": "WIDS giám sát sóng vô tuyến, không nhận gói từ switch.",
    }),
    "gen_243": ("NIDS chỉ thấy lưu lượng đi qua chỗ đặt sensor, nên vị trí đặt quyết định tầm nhìn.", {
        "A": "Antivirus trên máy trạm không ảnh hưởng thứ NIDS nhìn thấy.",
        "B": "Mật khẩu không liên quan tầm nhìn của sensor.",
        "D": "Dung lượng ổ cứng máy chủ web không liên quan.",
    }),
    "gen_245": ("Agent cài trên server theo dõi thay đổi tệp hệ thống là HIDS.", {
        "B": "NIDS xem lưu lượng mạng, không thấy tệp trên máy.",
        "C": "WIDS giám sát mạng không dây.",
        "D": "NIPS chặn gói trên đường truyền, không theo dõi tệp.",
    }),
    "gen_246": ("HIDS chạy trên máy nên thấy tiến trình, tệp, nhật ký hệ thống; NIDS chỉ thấy gói tin.", {
        "B": "Lưu lượng lớp lõi là phạm vi của NIDS.",
        "C": "Tín hiệu vô tuyến là phạm vi của WIDS.",
        "D": "Gói qua router biên là phạm vi của NIDS.",
    }),
    "gen_248": ("Phát hiện AP lạ phát cùng SSID (evil twin/rogue AP) là việc của WIDS.", {
        "A": "NIDS xem lưu lượng có dây, không quét sóng vô tuyến.",
        "B": "NIPS chặn gói trên đường truyền có dây.",
        "D": "HIDS chỉ giám sát một máy.",
    }),
    "gen_249": ("WIDS giám sát khung và hoạt động vô tuyến của mạng không dây.", {
        "A": "Tiến trình và tệp trên máy là HIDS.",
        "B": "Cáp quang là mạng có dây, thuộc NIDS.",
        "C": "Truy vấn SQL là phạm vi của WAF hoặc giám sát CSDL.",
    }),
    "gen_251": ("Bỏ gói tấn công trước khi tới máy chủ là chặn trên đường truyền mạng, tức NIPS.", {
        "A": "NIDS chỉ cảnh báo, không bỏ gói.",
        "C": "WIDS giám sát không dây, không bỏ gói trước máy chủ.",
        "D": "HIDS chạy trên máy chủ, chỉ thấy sau khi gói đã tới.",
    }),
    "gen_252": ("NIPS phải inline để lưu lượng đi xuyên qua nó; như vậy nó mới bỏ được gói tấn công ngay.", {
        "A": "Nhận bản sao từ SPAN là cách của NIDS thụ động, không chặn được.",
        "C": "Đọc nhật ký trên máy là HIDS.",
        "D": "NIPS không phát Wi-Fi.",
    }),
    "gen_254": ("Câu hỏi nói về máy phân tích độc lập nhận bản sao lưu lượng: đó là sensor thụ động, không nằm trên đường truyền và không chặn.", {
        "A": "SPAN port là cổng trên switch làm việc sao chép; câu hỏi gọi tên máy phân tích nhận bản sao, tức sensor thụ động.",
        "B": "Sensor inline nằm trên đường truyền, không nhận bản sao.",
        "C": "Network TAP là đầu nối phần cứng trên đường cáp, không phải switch mirror.",
    }),
    "gen_255": ("Sensor thụ động nhận bản sao lưu lượng, phát cảnh báo nhưng không chặn trực tiếp.", {
        "A": "Nằm trên đường truyền và thả gói là sensor inline.",
        "B": "Cài trên từng máy để đọc tiến trình là HIDS.",
        "C": "Sensor cần lưu lượng mạng mới hoạt động.",
    }),
    "gen_257": ("Mọi gói đi qua IPS trước khi tới server nghĩa là IPS nằm trên đường truyền: sensor inline.", {
        "B": "Sensor thụ động chỉ nhận bản sao, gói không phải đi qua nó.",
        "C": "TAP chỉ sao chép lưu lượng, không để gói đi xuyên qua một IPS.",
        "D": "SPAN port là cổng sao chép trên switch.",
    }),
    "gen_258": ("Sensor inline nằm trên đường truyền; nếu nó hỏng thì đường truyền có thể bị gián đoạn.", {
        "B": "Sensor inline chặn được gói, đó là ưu điểm của nó.",
        "C": "Nhận bản sao từ SPAN là sensor thụ động.",
        "D": "Sensor inline vẫn ghi log.",
    }),
    "gen_260": ("Switch sao chép gói từ uplink sang một cổng để IDS nghe là SPAN port (port mirroring).", {
        "A": "TAP là đầu nối phần cứng trên cáp, không phải chức năng của switch.",
        "C": "Sensor thụ động là máy nhận bản sao, còn cơ chế switch sao chép gói được hỏi ở đây là SPAN.",
        "D": "Inline là nằm trên đường truyền, không phải sao chép.",
    }),
    "gen_261": ("SPAN do switch sao chép bằng tài nguyên của nó, nên khi switch quá tải có thể bỏ sót gói.", {
        "B": "SPAN chỉ gửi bản sao, IDS hỏng không làm ngắt mạng.",
        "C": "SPAN sao chép được mọi loại gói, kể cả TCP.",
        "D": "SPAN là chức năng của switch có dây.",
    }),
    "gen_263": ("Đầu nối chuyên dụng đặt trên đường cáp để đưa bản sao gói tới sensor là Network TAP.", {
        "B": "Sensor thụ động là máy nhận bản sao, không phải đầu nối.",
        "C": "SPAN là chức năng trên switch, không phải đầu nối riêng.",
        "D": "Inline là nằm trên đường truyền để chặn.",
    }),
    "gen_264": ("Network TAP sao chép lưu lượng trên đường truyền vật lý để đưa cho sensor.", {
        "A": "Chặn gói theo chữ ký là việc của IPS.",
        "B": "Cấp IP là DHCP.",
        "D": "Mã hóa giữa chi nhánh là VPN.",
    }),
    "gen_266": ("Luật cảnh báo khi thấy một chuỗi exploit cụ thể là phát hiện theo chữ ký.", {
        "A": "Phân tích hành vi xét chuỗi hành động theo thời gian.",
        "B": "Phát hiện bất thường so với baseline, không tìm chuỗi cụ thể.",
        "C": "IDS máy học chấm điểm theo mô hình, không dùng luật chuỗi cố định.",
    }),
    "gen_267": ("Chữ ký chỉ bắt được cái đã biết, nên dễ bỏ sót tấn công mới (zero-day) hoặc biến thể.", {
        "A": "Cần baseline và báo động giả nhiều là nhược điểm của phát hiện bất thường.",
        "C": "IDS dùng chữ ký vẫn ghi log.",
        "D": "Chữ ký dùng được trên mọi loại mạng.",
    }),
    "gen_269": ("Lưu lượng tăng đột biến so với lịch sử là lệch khỏi baseline, tức phát hiện bất thường.", {
        "A": "Phân tích hành vi xét chuỗi hành động của một tài khoản/tiến trình, không chỉ so lượng.",
        "B": "Không có chuỗi tấn công cụ thể nào để khớp chữ ký.",
        "C": "Tình huống chỉ so với lịch sử, không nói tới mô hình máy học.",
    }),
    "gen_270": ("Phát hiện bất thường so với hành vi bình thường, nên cần một baseline phù hợp; baseline sai thì báo nhầm nhiều.", {
        "B": "Cơ sở dữ liệu chữ ký là thứ phát hiện theo chữ ký cần.",
        "C": "Mật khẩu quản trị không quyết định chất lượng phát hiện.",
        "D": "Chuẩn Wi-Fi không liên quan.",
    }),
    "gen_272": ("Một tài khoản đăng nhập rồi đi quét hàng loạt máy là chuỗi hành động đáng ngờ của một chủ thể: phân tích hành vi.", {
        "A": "Phát hiện bất thường so lượng/chỉ số với baseline; ở đây trọng tâm là chuỗi việc tài khoản làm.",
        "B": "Không có chữ ký cụ thể nào được khớp.",
        "D": "Tình huống không nói tới mô hình máy học.",
    }),
    "gen_273": ("Behavior-based xét chuỗi hành động của tiến trình hoặc người dùng theo thời gian.", {
        "A": "Mẫu byte cố định so với chữ ký là signature-based.",
        "B": "Tên miền chỉ là một thuộc tính, không phải chuỗi hành vi.",
        "D": "Kích thước tệp đính kèm không phải hành vi.",
    }),
    "gen_275": ("Dùng mô hình chấm điểm phiên từ các đặc trưng flow là IDS máy học.", {
        "A": "Phát hiện bất thường so với baseline, không cần mô hình chấm điểm.",
        "B": "Chữ ký khớp mẫu cố định.",
        "C": "Phân tích hành vi theo dõi chuỗi hành động, không nói tới mô hình.",
    }),
    "gen_276": ("Slide nêu IDS máy học phụ thuộc dữ liệu huấn luyện và có thể bị tấn công adversarial (đánh lừa mô hình).", {
        "A": "Máy học cần dữ liệu huấn luyện.",
        "B": "Không mô hình nào chính xác 100%.",
        "D": "Virus boot không liên quan IDS máy học.",
    }),
    "gen_278": ("Có tấn công thật (đã xác nhận) và IDS báo: true positive.", {
        "A": "False positive là báo nhầm khi không có tấn công.",
        "B": "True negative là không tấn công và không báo.",
        "D": "False negative là có tấn công nhưng không báo.",
    }),
    "gen_279": ("TP: có tấn công thật và IDS cảnh báo đúng.", {
        "A": "Không có tấn công mà cảnh báo là FP.",
        "B": "Có tấn công mà bỏ sót là FN.",
        "C": "Không tấn công và không cảnh báo là TN.",
    }),
    "gen_282": ("IPS chặn theo cảnh báo của nó; báo nhầm nhiều thì chặn nhầm lưu lượng hợp lệ, gây gián đoạn nghiệp vụ.", {
        "B": "Bỏ sót tấn công là false negative.",
        "C": "FP không làm lộ khóa WLAN.",
        "D": "FP không xóa log.",
    }),
    "gen_285": ("False negative là có tấn công mà không cảnh báo, nên mọi người tưởng an toàn trong khi tấn công vẫn diễn ra.", {
        "A": "Nhiều cảnh báo giả là false positive.",
        "B": "Chặn nhầm lưu lượng hợp lệ là false positive của IPS.",
        "D": "FN không làm sensor khởi động lại.",
    }),
    "gen_287": ("Lưu lượng hợp lệ (không tấn công) và không bị cảnh báo: true negative.", {
        "B": "False negative là có tấn công mà không báo.",
        "C": "True positive là có tấn công và báo.",
        "D": "False positive là không tấn công mà báo.",
    }),
    "gen_288": ("TN: không có tấn công và IDS không cảnh báo.", {
        "A": "Có tấn công và cảnh báo là TP.",
        "B": "Không tấn công mà cảnh báo là FP.",
        "D": "Có tấn công mà bỏ sót là FN.",
    }),
    "gen_290": ("Precision = TP/(TP+FP) đo tỷ lệ cảnh báo đúng trong tổng số cảnh báo; giảm báo động giả là tăng precision.", {
        "B": "Recall đo tỷ lệ tấn công được phát hiện, không phải tỷ lệ báo giả.",
        "C": "Baseline là mức bình thường dùng để so sánh.",
        "D": "Tuning là cách tinh chỉnh luật; chỉ số được hỏi ở đây là precision.",
    }),
    "gen_291": ("Precision = TP / (TP + FP): trong các cảnh báo, bao nhiêu phần là đúng.", {
        "A": "TP/(TP+FN) là recall.",
        "B": "TN/(TN+FP) là độ đặc hiệu (specificity).",
        "D": "(TP+TN)/tổng là độ chính xác chung (accuracy).",
    }),
    "gen_293": ("Bỏ sót ít hơn nghĩa là phát hiện được nhiều tấn công thật hơn, tức recall tăng.", {
        "A": "Baseline là mức bình thường để so sánh.",
        "C": "Precision liên quan báo động giả, không phải bỏ sót.",
        "D": "Tuning là tinh chỉnh luật, không phải chỉ số đo.",
    }),
    "gen_294": ("Recall = TP / (TP + FN): trong các tấn công thật, bao nhiêu phần được phát hiện.", {
        "A": "TP/(TP+FP) là precision.",
        "B": "FP/(FP+TN) là tỷ lệ báo động giả (FPR).",
        "D": "TN/(TN+FN) không phải recall.",
    }),
    "gen_296": ("Chỉnh luật đang báo nhầm (giới hạn theo lịch backup) là tuning.", {
        "A": "Precision là chỉ số đo, không phải hành động chỉnh luật.",
        "B": "Recall là chỉ số đo.",
        "C": "Baseline là mức bình thường, không phải việc chỉnh luật.",
    }),
    "gen_299": ("Xác định mức DNS trung bình ngày làm việc là xây baseline (mức bình thường).", {
        "B": "Recall là chỉ số đo tỷ lệ phát hiện.",
        "C": "Tuning là chỉnh luật, còn đây là đo mức bình thường.",
        "D": "Precision là chỉ số đo cảnh báo đúng.",
    }),
    "gen_302": ("Một bộ IDS riêng, tự vận hành ở chi nhánh nhỏ là mô hình standalone.", {
        "B": "Distributed có nhiều sensor gửi về bộ điều khiển chung.",
        "C": "SIEM là hệ thống tương quan log, không phải mô hình IDPS.",
        "D": "Hybrid kết hợp nhiều loại sensor (như HIDS + NIDS).",
    }),
    "gen_308": ("Kết hợp HIDS (trên máy) với NIDS (mạng) và gửi về trung tâm là hybrid IDPS.", {
        "A": "Standalone là một bộ IDS riêng lẻ.",
        "B": "SIEM tương quan log, không phải mô hình triển khai IDPS.",
        "D": "Distributed nói về nhiều sensor phân tán; điểm nhấn ở đây là kết hợp hai loại HIDS và NIDS.",
    }),
    "gen_317": ("Thiết bị inline hỏng thì ngắt luồng để không cho gì đi qua mà không kiểm tra: fail-close.", {
        "A": "Fail-open là hỏng thì vẫn cho lưu lượng đi qua.",
        "B": "Prevention mode là chế độ chặn khi đang hoạt động bình thường.",
        "D": "Detection mode là chỉ quan sát, không chặn.",
    }),
    "gen_320": ("Chạy luật mới chỉ quan sát, chưa chặn là detection mode.", {
        "A": "Prevention mode là chặn thật.",
        "B": "Fail-close là cách xử lý khi thiết bị hỏng.",
        "C": "Fail-open là cách xử lý khi thiết bị hỏng.",
    }),
    "gen_323": ("Chuyển luật sang drop gói tấn công là bật prevention mode.", {
        "A": "Detection mode chỉ quan sát.",
        "B": "Fail-close là hành vi khi thiết bị hỏng.",
        "D": "Fail-open là hành vi khi thiết bị hỏng.",
    }),
    "case_31": ("Muốn quan sát báo động giả trước khi chặn thì chạy IDS hoặc chế độ detection.", {
        "B": "Fail-close là cách xử lý khi thiết bị hỏng, không phải giai đoạn quan sát.",
        "C": "Chặn ngay thì chưa kịp đánh giá báo nhầm và dễ chặn nhầm.",
        "D": "Tắt sensor thì không quan sát được gì.",
    }),
    "case_32": ("Nằm inline và bỏ gói tấn công trước khi tới server là IPS.", {
        "A": "IDS thụ động không chặn.",
        "B": "SPAN chỉ sao chép gói.",
        "C": "SIEM chỉ tương quan log.",
    }),
    "case_33": ("Thay đổi tệp hệ thống trên server chỉ thấy được từ trong máy, nên cần HIDS trên server.", {
        "A": "Router làm NAT không thấy tệp trên server.",
        "C": "AP không liên quan.",
        "D": "NIDS ở cổng nào cũng chỉ thấy gói tin, không thấy tệp.",
    }),
    "case_34": ("Bắt được mẫu đã biết nhưng bỏ sót biến thể không khớp: đó là phát hiện theo chữ ký.", {
        "A": "Phân tích nguyên nhân gốc là việc sau sự cố.",
        "B": "Baseline có thể bắt biến thể mới vì không phụ thuộc mẫu.",
        "D": "Đánh giá hành vi không dựa vào chữ ký.",
    }),
    "case_35": ("Tác vụ hợp lệ bị coi là tấn công: false positive.", {
        "A": "True negative là hợp lệ và không báo.",
        "B": "True positive là tấn công thật và báo.",
        "D": "False negative là tấn công thật mà không báo.",
    }),
    "case_36": ("Tấn công thật mà không có cảnh báo: false negative.", {
        "A": "True negative là không có tấn công.",
        "B": "True positive phải có cảnh báo.",
        "C": "False positive là cảnh báo khi không có tấn công.",
    }),
    "case_37": ("Precision = TP/(TP+FP) = 30/(30+10) = 30/40 = 75%.", {
        "A": "30% lấy nhầm TP làm phần trăm.",
        "B": "90% không khớp công thức nào với số liệu này.",
        "C": "25% là FP/(TP+FP), tức tỷ lệ cảnh báo sai.",
    }),
    "case_38": ("Recall = TP/(TP+FN) = 30/(30+20) = 30/50 = 60%.", {
        "B": "50% không khớp công thức recall.",
        "C": "40% là FN/(TP+FN), tức tỷ lệ bỏ sót.",
        "D": "80% không khớp công thức recall.",
    }),
    "case_39": ("Ưu tiên giữ dịch vụ khi IPS hỏng thì để lưu lượng tiếp tục đi qua: fail-open.", {
        "A": "Default deny là luật tường lửa, không phải chế độ khi thiết bị hỏng.",
        "B": "Cách ly mọi máy làm dừng dịch vụ.",
        "C": "Fail-close ngắt luồng, trái với ưu tiên giữ dịch vụ.",
    }),
    "case_40": ("Gom log từ nhiều nguồn về một nơi để tương quan là SIEM.", {
        "A": "BSSID là địa chỉ MAC của AP.",
        "C": "WEP là chuẩn bảo mật Wi-Fi cũ.",
        "D": "NAT là dịch địa chỉ.",
    }),
    "reviewed_atm_27": ("IPS inline nằm trên đường truyền nên chặn được gói tấn công ngay.", {
        "A": "SIEM chỉ lưu và tương quan log.",
        "B": "SPAN chỉ sao chép gói.",
        "C": "IDS thụ động chỉ cảnh báo.",
    }),
    "reviewed_atm_89": ("Phát hiện mà chưa chặn để đánh giá báo động giả: dùng IDS/detection mode.", {
        "A": "Fail-close là cách xử lý khi thiết bị hỏng.",
        "B": "Default deny là luật tường lửa.",
        "D": "Prevention là chặn thật, trái với yêu cầu.",
    }),
    "reviewed_atm_106": ("Nhiều sensor ở nhiều cơ sở cùng một bộ điều khiển là distributed IDPS.", {
        "A": "Một host đơn lẻ không quản lý nhiều cơ sở.",
        "C": "Standalone là một bộ riêng lẻ.",
        "D": "AP không phải mô hình IDS.",
    }),
    "reviewed_atm_141": ("IDS không nằm trên đường truyền nên chức năng cốt lõi là phát hiện và cảnh báo.", {
        "A": "IDS không mã hóa phiên.",
        "B": "Cấp IP là DHCP.",
        "D": "IDS không chặn lưu lượng.",
    }),
    "abbr_c4_036": ("IDS là Intrusion Detection System, hệ thống phát hiện xâm nhập.", {
        "B": "D là Detection, không phải Deterrence.",
        "C": "Không phải Integrated Data Security.",
        "D": "Không phải Internet Defense Service.",
    }),
    "abbr_c4_037": ("IPS là Intrusion Prevention System, hệ thống ngăn chặn xâm nhập.", {
        "A": "Không phải Integrated Policy Server.",
        "B": "Không phải Internet Protection Service.",
        "C": "P là Prevention (ngăn chặn), không phải Prediction (dự đoán).",
    }),
    "abbr_c4_038": ("IDPS là Intrusion Detection and Prevention System.", {
        "B": "Không phải Intrusion Data Processing Server.",
        "C": "Không phải Integrated Detection and Policy System.",
        "D": "Không phải Internet Defense and Protection Service.",
    }),
    "abbr_c4_039": ("N là Network-based (đặt trên mạng), H là Host-based (đặt trên máy).", {
        "A": "N không phải New-generation.",
        "C": "H không phải Hardware-based.",
        "D": "N không phải Node-based, H không phải Hybrid-based.",
    }),
    "abbr_c4_040": ("HIPS là Host-based Intrusion Prevention System, IPS chạy trên máy.", {
        "A": "Không phải High-speed Intrusion Protection Switch.",
        "B": "H là Host-based, không phải Hybrid.",
        "D": "Không phải Host Integrity Policy Service.",
    }),
    "abbr_c4_041": ("W trong WIDS/WIPS là Wireless, dành cho mạng không dây.", {
        "B": "W không phải Windows.",
        "C": "W không phải WAN.",
        "D": "W không phải Web.",
    }),
    "abbr_c4_042": ("NBA là Network Behavior Analysis, phân tích hành vi mạng.", {
        "A": "Không phải Network Baseline Alert.",
        "B": "Không phải Network Backup Archive.",
        "D": "Không phải Node Blocking Agent.",
    }),
    "abbr_c4_043": ("SIEM là Security Information and Event Management, quản lý thông tin và sự kiện an ninh.", {
        "A": "Không phải Secure Internet Exchange Monitor.",
        "C": "Không phải Security Incident and Exposure Matrix.",
        "D": "Không phải System Integrity and Encryption Module.",
    }),
    "abbr_c4_044": ("SOAR là Security Orchestration, Automation and Response: điều phối, tự động hóa và phản ứng.", {
        "A": "Không phải Signature Optimization and Alert Reduction.",
        "B": "Không phải Secure Online Access and Routing.",
        "C": "Không phải System Operation, Audit and Recovery.",
    }),
    "abbr_c4_045": ("SOC là Security Operations Center, trung tâm điều hành an ninh.", {
        "A": "Không phải System Optimization Console.",
        "C": "Không phải Security Ownership Certificate.",
        "D": "Không phải Secure Online Channel.",
    }),
    "abbr_c4_046": ("EDR là Endpoint Detection and Response, phát hiện và phản ứng trên thiết bị đầu cuối.", {
        "B": "Không phải Event Data Repository.",
        "C": "Không phải Encrypted Data Recovery.",
        "D": "Không phải Edge Defense Router.",
    }),
    "abbr_c4_047": ("XDR là Extended Detection and Response, mở rộng EDR ra nhiều nguồn.", {
        "A": "Không phải Extra Defense Rule.",
        "B": "Không phải External Data Replication and Recovery.",
        "D": "Không phải Cross-Domain Routing.",
    }),
    "abbr_c4_048": ("NDR là Network Detection and Response, phát hiện và phản ứng trên lưu lượng mạng.", {
        "A": "Không phải Network Domain Registry.",
        "B": "Không phải Network Defense Router.",
        "C": "Không phải Node Data Replication.",
    }),
    "abbr_c4_049": ("IOC là Indicator of Compromise, chỉ dấu cho thấy hệ thống đã bị xâm nhập (IP, tên miền, băm tệp độc...).", {
        "A": "Không phải Intrusion Origin Code.",
        "B": "Không phải Integrity of Content.",
        "D": "Không phải Index of Connections.",
    }),
    "abbr_c4_050": ("SPAN là Switched Port Analyzer, chức năng sao chép lưu lượng của switch sang một cổng.", {
        "A": "Không phải Signal Path Amplifier Network.",
        "C": "Không phải Sensor Port Allocation.",
        "D": "Không phải Secure Packet Access Node.",
    }),
    "abbr_c4_051": ("FP: lưu lượng bình thường nhưng bị cảnh báo là tấn công (báo nhầm).", {
        "B": "Tấn công thật mà không cảnh báo là FN.",
        "C": "Tấn công thật và cảnh báo đúng là TP.",
        "D": "Bình thường và không cảnh báo là TN.",
    }),
    "abbr_c4_052": ("FN: có tấn công thật nhưng không được cảnh báo (bỏ sót).", {
        "A": "Tấn công thật và cảnh báo đúng là TP.",
        "B": "Bình thường bị cảnh báo là FP.",
        "C": "Bình thường không cảnh báo là TN.",
    }),
    "rev_c4_055": ("EDR chỉ xét endpoint; XDR tương quan dữ liệu từ endpoint, mạng, cloud và danh tính.", {
        "A": "XDR không phải thiết bị inline chặn gói.",
        "C": "Chỉ một máy chủ là phạm vi hẹp hơn cả EDR.",
        "D": "Phát hiện rogue AP là WIDS.",
    }),
    "rev_c4_056": ("MITRE ATT&CK là danh mục kỹ thuật tấn công; IDPS dùng để ánh xạ cảnh báo vào kỹ thuật tương ứng.", {
        "A": "ATT&CK không phải giao thức mã hóa.",
        "B": "ATT&CK không cấp chứng nhận sản phẩm.",
        "D": "Phân giải IP sang MAC là ARP.",
    }),
}
