EXPLAIN = {
    "gen_431": ("Xác định tài sản quan trọng nhất (CSDL điểm thi) để ưu tiên bảo vệ là việc của đánh giá rủi ro.", {
        "A": "ISMS là cả hệ thống quản lý; tình huống chỉ là một bước bên trong nó.",
        "C": "27001 là tiêu chuẩn yêu cầu cho ISMS, không phải hoạt động ưu tiên tài sản.",
        "D": "27002 là danh mục biện pháp kiểm soát, không phải hoạt động đánh giá.",
    }),
    "gen_434": ("Common Criteria chính là ISO/IEC 15408, chuẩn đánh giá sản phẩm CNTT.", {
        "A": "13335 là hướng dẫn quản lý an ninh CNTT, không phải Common Criteria.",
        "B": "EAL là cấp bảo đảm, kết quả của đánh giá, không phải tên chuẩn.",
        "C": "TOE là đối tượng được đánh giá, không phải tên chuẩn.",
    }),
    "gen_440": ("Cấp bảo đảm ghi sau khi thẩm định theo Common Criteria là EAL (Evaluation Assurance Level).", {
        "A": "15408 là tên chuẩn, còn cấp ghi trong báo cáo là EAL.",
        "B": "13335 không cấp mức bảo đảm cho thiết bị.",
        "D": "TOE là đối tượng được đánh giá, không phải cấp bảo đảm.",
    }),
    "gen_443": ("Chứng nhận chỉ gắn với đúng phiên bản thiết bị được đánh giá, tức TOE (Target of Evaluation).", {
        "A": "EAL là mức bảo đảm, không xác định phạm vi phiên bản.",
        "B": "13335 không liên quan chứng nhận sản phẩm.",
        "C": "15408 là chuẩn; phần xác định đúng thứ được đánh giá là TOE.",
    }),
    "gen_452": ("HSM giữ khóa và thực hiện phép ký là một mô-đun mật mã.", {
        "A": "PCI DSS là chuẩn cho môi trường dữ liệu thẻ, không phải thiết bị.",
        "C": "Dữ liệu chủ thẻ là thông tin thẻ của khách hàng.",
        "D": "FIPS 140-2 là chuẩn đánh giá mô-đun mật mã, còn HSM là chính mô-đun đó.",
    }),
    "gen_455": ("Số thẻ thanh toán của khách là dữ liệu chủ thẻ (cardholder data).", {
        "A": "FIPS 140-2 là chuẩn mô-đun mật mã.",
        "C": "Mô-đun mật mã là thiết bị/phần mềm mã hóa.",
        "D": "PCI DSS là chuẩn bảo vệ dữ liệu này, không phải tên của dữ liệu.",
    }),
    "gen_461": ("Họ tên và thông tin liên hệ là thông tin cá nhân, nên áp dụng nội dung bảo vệ thông tin cá nhân.", {
        "A": "Luật ATTT mạng 2015 là cả bộ luật; nội dung cụ thể áp dụng ở đây là bảo vệ thông tin cá nhân.",
        "B": "Tình huống không nói về thư rác.",
        "C": "Tình huống không có sự cố cần ứng cứu.",
    }),
    "gen_464": ("Email quảng cáo trái phép hàng loạt thuộc nội dung phòng chống thư rác.", {
        "B": "Luật là cả bộ; nội dung cụ thể là phòng chống thư rác.",
        "C": "Thư rác không phải sự cố cần ứng cứu.",
        "D": "Tình huống không nói về xử lý thông tin cá nhân.",
    }),
    "gen_467": ("Cô lập máy bị xâm nhập rồi khôi phục dịch vụ là ứng cứu sự cố ATTT.", {
        "A": "Tình huống không nói về thông tin cá nhân.",
        "B": "Luật là cả bộ; hoạt động cụ thể là ứng cứu sự cố.",
        "D": "Tình huống không liên quan thư rác.",
    }),
    "case_51": ("ISO/IEC 27001:2005 nêu yêu cầu cho ISMS và là tiêu chuẩn dùng để đánh giá chứng nhận.", {
        "A": "15408 đánh giá sản phẩm, không chứng nhận ISMS.",
        "B": "27002 chỉ hướng dẫn biện pháp, không dùng để chứng nhận.",
        "D": "FIPS 140-2 đánh giá mô-đun mật mã.",
    }),
    "case_52": ("ISO/IEC 27002:2005 là bộ hướng dẫn biện pháp kiểm soát, không dùng để chứng nhận ISMS.", {
        "B": "PCI DSS dành riêng cho dữ liệu thẻ.",
        "C": "FIPS 140-2 dành cho mô-đun mật mã.",
        "D": "27001 là tiêu chuẩn chứng nhận ISMS, trái với yêu cầu.",
    }),
    "case_53": ("Đánh giá mức bảo đảm an ninh của chính một sản phẩm dùng ISO/IEC 15408 (Common Criteria).", {
        "A": "PCI DSS là chuẩn môi trường thẻ.",
        "B": "27002 hướng dẫn biện pháp cho tổ chức.",
        "C": "27001 chứng nhận ISMS của tổ chức, không phải sản phẩm.",
    }),
    "case_54": ("Slide mô tả ISO/IEC 13335 là hướng dẫn quản lý an ninh CNTT, tập trung vào quản lý rủi ro và lập kế hoạch bảo mật tổng thể.", {
        "B": "PCI DSS dành cho dữ liệu thẻ.",
        "C": "FIPS 140-2 kiểm định mô-đun mật mã, câu hỏi đã loại trừ.",
        "D": "15408 đánh giá sản phẩm.",
    }),
    "case_55": ("Môi trường xử lý dữ liệu thẻ thanh toán áp dụng PCI DSS.", {
        "A": "FIPS 140-2 chỉ cho mô-đun mật mã.",
        "C": "13335 là hướng dẫn quản lý chung, không riêng cho thẻ.",
        "D": "15408 đánh giá sản phẩm.",
    }),
    "case_56": ("Đánh giá mô-đun mật mã dùng FIPS 140-2.", {
        "A": "27001 chứng nhận ISMS của tổ chức.",
        "C": "PCI DSS cho môi trường thẻ thanh toán.",
        "D": "27002 hướng dẫn biện pháp cho tổ chức.",
    }),
    "case_57": ("27001 là yêu cầu để chứng nhận ISMS; 27002 là hướng dẫn chi tiết các biện pháp kiểm soát.", {
        "B": "Cả hai dành cho tổ chức, không chỉ mô-đun mật mã.",
        "C": "Chuẩn riêng cho thẻ là PCI DSS.",
        "D": "Đảo ngược vai trò: 27001 mới là chuẩn chứng nhận.",
    }),
    "case_58": ("27001 yêu cầu xác định phạm vi ISMS và đánh giá rủi ro trước, rồi mới chọn biện pháp kiểm soát như firewall.", {
        "A": "Băng thông không phải bước của ISMS.",
        "B": "ISMS cần tài liệu hóa chính sách, không bỏ.",
        "C": "Cấp quyền quản trị cho mọi người trái nguyên tắc bảo mật.",
    }),
    "case_59": ("Security Target (ST) là tài liệu mô tả mục tiêu bảo mật cụ thể của sản phẩm được đánh giá.", {
        "A": "Đó là tên đầy đủ của PCI DSS.",
        "B": "Đó là tên đầy đủ của IPS.",
        "D": "Đó là tên đầy đủ của SSID.",
    }),
    "case_60": ("Thu thập thông tin cá nhân thì phải bảo vệ nó trong cả quá trình xử lý, không chỉ chống virus.", {
        "A": "SSID không liên quan dữ liệu cá nhân.",
        "C": "Tắt log làm khó chứng minh tuân thủ.",
        "D": "Mở thêm cổng làm tăng rủi ro.",
    }),
    "std_c6_090": ("ISO/IEC 27002:2005 có 11 lĩnh vực, 39 mục tiêu, 133 biện pháp.", {
        "B": "4 nhóm, 93 biện pháp, 5 thuộc tính là bản 2022.",
        "C": "6 chức năng, 22 nhóm, 106 tiểu mục là NIST CSF 2.0.",
        "D": "14 lĩnh vực, 35 mục tiêu, 114 biện pháp là bản 2013.",
    }),
    "std_c6_091": ("ISO/IEC 27002:2013 có 14 lĩnh vực, 35 mục tiêu, 114 biện pháp.", {
        "A": "4 nhóm, 93 biện pháp là bản 2022.",
        "B": "6 chức năng, 22 nhóm, 106 tiểu mục là NIST CSF 2.0.",
        "C": "11 lĩnh vực, 133 biện pháp là bản 2005.",
    }),
    "std_c6_092": ("ISO/IEC 27002:2022 có 4 nhóm, 93 biện pháp, 5 thuộc tính.", {
        "A": "11 lĩnh vực, 133 biện pháp là bản 2005.",
        "B": "6 chức năng, 22 nhóm, 106 tiểu mục là NIST CSF 2.0.",
        "D": "14 lĩnh vực, 114 biện pháp là bản 2013.",
    }),
    "std_c6_093": ("114 biện pháp trong Phụ lục A là của ISO/IEC 27001:2013.", {
        "A": "Bản 2022 có 93 biện pháp.",
        "C": "Bản 2005 có 133 biện pháp.",
        "D": "27002:2022 cũng là 93 biện pháp, và 27002 không có \"Phụ lục A\".",
    }),
    "std_c6_094": ("Bốn nhóm của 27002:2022 là Tổ chức, Con người, Vật lý, Công nghệ.", {
        "A": "Nhận diện, Bảo vệ, Phát hiện, Ứng phó là các chức năng của NIST CSF.",
        "B": "Không phải cách chia nhóm của bản 2022.",
        "D": "Kế hoạch – Thực hiện – Kiểm tra – Hành động là chu trình PDCA.",
    }),
    "abbr_c6_095": ("ISMS là Information Security Management System, hệ thống quản lý an toàn thông tin.", {
        "B": "Không phải Information Systems Management Service.",
        "C": "Không phải Internet Security Monitoring Service.",
        "D": "Không phải Integrated Security Module Standard.",
    }),
    "std_c6_096": ("ISO/IEC 27001 là tiêu chuẩn dùng để cấp chứng nhận ISMS.", {
        "A": "27005 hướng dẫn quản lý rủi ro.",
        "B": "NIST CSF là khung tự nguyện, không cấp chứng nhận.",
        "C": "27002 hướng dẫn biện pháp, không chứng nhận.",
    }),
    "std_c6_097": ("SoA (Statement of Applicability) là tuyên bố áp dụng: biện pháp nào trong Phụ lục A được dùng và vì sao.", {
        "A": "SoA không phải hợp đồng cloud.",
        "B": "Danh mục tài sản là một tài liệu khác.",
        "C": "Báo cáo kiểm thử xâm nhập không phải SoA.",
    }),
    "std_c6_098": ("PDCA là Plan – Do – Check – Act.", {
        "A": "Không phải Prepare – Deploy – Correct – Assess.",
        "B": "Không phải Policy – Design – Control – Audit.",
        "D": "Không phải Protect – Detect – Contain – Analyze.",
    }),
    "std_c6_099": ("Điều 9 \"Đánh giá kết quả\" (giám sát, đánh giá nội bộ, xem xét lãnh đạo) thuộc pha CHECK.", {
        "A": "PLAN ứng với Điều 4–7 (bối cảnh, lãnh đạo, hoạch định, hỗ trợ).",
        "C": "DO ứng với Điều 8 (vận hành).",
        "D": "ACT ứng với Điều 10 (cải tiến).",
    }),
    "std_c6_100": ("Chứng chỉ 27001 có hiệu lực 3 năm, với đánh giá giám sát hằng năm.", {
        "B": "Chứng chỉ không vĩnh viễn; hết 3 năm phải tái chứng nhận.",
        "C": "Không phải 5 năm.",
        "D": "Không phải 1 năm, và vẫn cần giám sát.",
    }),
    "std_c6_101": ("Slide cập nhật ghi ISO/IEC 13335 đã bị thu hồi; phần quản lý rủi ro được kế thừa trong 27005.", {
        "A": "Chuẩn chứng nhận ISMS hiện nay vẫn là 27001.",
        "B": "Chuẩn thẻ thanh toán là PCI DSS.",
        "D": "Chuẩn mô-đun mật mã của NIST là FIPS 140.",
    }),
    "std_c6_102": ("ISO/IEC 27005 hướng dẫn quản lý rủi ro an toàn thông tin.", {
        "A": "Đánh giá mô-đun mật mã là FIPS 140.",
        "C": "Bảo vệ dữ liệu cá nhân là 27701 (và 27018 cho cloud).",
        "D": "Yêu cầu chứng nhận ISMS là 27001.",
    }),
    "std_c6_103": ("27005 có bốn cách xử lý rủi ro: giảm thiểu, tránh, chia sẻ (chuyển giao), chấp nhận.", {
        "A": "Đó là các biện pháp kỹ thuật, không phải phương án xử lý rủi ro.",
        "B": "Đó là các giai đoạn xử lý sự cố.",
        "C": "Đó là chu trình PDCA.",
    }),
    "std_c6_104": ("ISO/IEC 15408 còn gọi là Common Criteria.", {
        "B": "Cybersecurity Framework là NIST CSF.",
        "C": "Code of Practice là tên gọi của 27002.",
        "D": "Data Security Standard là phần DSS trong PCI DSS.",
    }),
    "abbr_c6_105": ("TOE là Target of Evaluation, đối tượng (sản phẩm/phiên bản) được đánh giá.", {
        "A": "Không phải Test of Encryption.",
        "B": "Không phải Trust of Entity.",
        "C": "Không phải Type of Exposure.",
    }),
    "std_c6_106": ("PP (Protection Profile) là yêu cầu chung cho một loại sản phẩm; ST (Security Target) là tuyên bố của một sản phẩm cụ thể.", {
        "A": "PP không phải hồ sơ thanh toán.",
        "C": "PP không phải chính sách mật khẩu.",
        "D": "Đảo ngược vai trò của PP và ST.",
    }),
    "abbr_c6_107": ("EAL là Evaluation Assurance Level, cấp bảo đảm đánh giá (EAL1–EAL7).", {
        "B": "Không phải Encryption Algorithm Level.",
        "C": "Không phải Enterprise Access Layer.",
        "D": "Không phải Event Alert Log.",
    }),
    "std_c6_108": ("EAL7 là cao nhất, ứng với xác minh thiết kế hình thức.", {
        "A": "EAL1 là thấp nhất (kiểm thử chức năng).",
        "B": "EAL5 là thiết kế bán hình thức.",
        "D": "EAL4 là thiết kế, kiểm thử và rà soát có phương pháp.",
    }),
    "std_c6_109": ("EAL4+ chỉ bảo đảm đánh giá đã thực hiện ở mức đó; nó không có nghĩa sản phẩm hết lỗ hổng.", {
        "A": "Có quy trình khắc phục lỗ hổng là điều chứng nhận có thể bao gồm.",
        "C": "Chức năng đúng như ST là điều chứng nhận khẳng định.",
        "D": "Rà soát thiết kế và quy trình phát triển là một phần của EAL4.",
    }),
    "abbr_c6_110": ("PCI DSS là Payment Card Industry Data Security Standard.", {
        "A": "Không phải Payment Control Interface Digital Signature Standard.",
        "B": "Không phải Public Cloud Infrastructure Data Security Suite.",
        "C": "Không phải Personal Credit Information Data Safety System.",
    }),
    "std_c6_111": ("PCI DSS do PCI SSC ban hành, với các hãng thẻ như Visa, MasterCard tham gia.", {
        "B": "Bộ Công an không ban hành PCI DSS.",
        "C": "ISO/IEC ban hành dòng 27000, không phải PCI DSS.",
        "D": "NIST ban hành FIPS và CSF.",
    }),
    "std_c6_112": ("Slide ghi PCI DSS v4.0.1 có 12 yêu cầu, nhóm thành 6 mục tiêu.", {
        "A": "6 chức năng, 106 tiểu mục là NIST CSF 2.0.",
        "B": "11 lĩnh vực, 133 biện pháp là 27002:2005.",
        "D": "Có 7 mức EAL là của Common Criteria.",
    }),
    "std_c6_113": ("Cửa hàng không còn tự nhập/lưu dữ liệu thẻ thì ít hệ thống chạm vào dữ liệu thẻ hơn, nên phạm vi PCI DSS thu hẹp.", {
        "A": "CVV2 không bao giờ được lưu sau ủy quyền.",
        "B": "Vẫn còn nghĩa vụ, chỉ là phạm vi nhỏ hơn.",
        "C": "PCI DSS và ISO 27001 là hai chứng nhận độc lập.",
    }),
    "abbr_c6_114": ("FIPS là Federal Information Processing Standards, tiêu chuẩn xử lý thông tin liên bang Hoa Kỳ.", {
        "B": "Không phải Federal Internet Privacy System.",
        "C": "Không phải Formal Integrity Protection Specification.",
        "D": "Không phải Framework for Information Protection Security.",
    }),
    "std_c6_115": ("FIPS 140-2 quy định yêu cầu cho mô-đun mật mã bảo vệ thông tin nhạy cảm chưa phân loại (SBU).", {
        "A": "Ứng dụng xử lý thẻ thuộc PCI.",
        "B": "Hệ thống quản lý ATTT là ISO 27001.",
        "D": "Ứng cứu sự cố không phải phạm vi của FIPS 140-2.",
    }),
    "abbr_c6_116": ("SBU là Sensitive but Unclassified, thông tin nhạy cảm nhưng không thuộc diện mật.", {
        "A": "Không phải Standard Baseline Usage.",
        "C": "Không phải Secure Business Unit.",
        "D": "Không phải Signed Binary Update.",
    }),
    "std_c6_117": ("Theo slide cập nhật, FIPS 140-3 (2019) thay thế FIPS 140-2.", {
        "A": "FIPS 140-1 là bản trước 140-2.",
        "B": "FIPS 197 là chuẩn thuật toán AES.",
        "D": "FIPS 186 là chuẩn chữ ký số.",
    }),
    "std_c6_118": ("Mức 3 của FIPS 140 là mức thấp nhất yêu cầu phát hiện can thiệp vật lý và xóa khóa khi mở vỏ.", {
        "A": "Mức 1 không yêu cầu bảo vệ vật lý.",
        "B": "Mức 2 chỉ yêu cầu dấu hiệu niêm phong (tamper-evident).",
        "C": "Mức 4 cũng có yêu cầu này nhưng không phải mức thấp nhất.",
    }),
    "abbr_c6_119": ("HSM là Hardware Security Module, mô-đun phần cứng giữ khóa và ký.", {
        "A": "Không phải Host Security Monitor.",
        "C": "Không phải Hybrid Storage Manager.",
        "D": "Không phải Hash Signing Method.",
    }),
    "std_c6_120": ("ISO/IEC 27701 mở rộng 27001 cho quản lý quyền riêng tư (PIMS).", {
        "B": "Common Criteria là ISO/IEC 15408.",
        "C": "Quản lý AI là ISO/IEC 42001.",
        "D": "Quản lý rủi ro là ISO/IEC 27005.",
    }),
    "std_c6_121": ("ISO/IEC 42001:2023 là chuẩn chứng nhận hệ thống quản lý AI (AIMS).", {
        "A": "Hướng dẫn biện pháp là 27002.",
        "B": "Đánh giá mô-đun mật mã là FIPS 140.",
        "D": "Khung của NIST là CSF.",
    }),
    "abbr_c6_122": ("PII là Personally Identifiable Information, thông tin định danh cá nhân.", {
        "A": "Không phải Protected Integrity Index.",
        "B": "Không phải Public Information Interface.",
        "C": "Không phải Private Internet Infrastructure.",
    }),
    "abbr_c6_123": ("DLP là Data Leakage Prevention, ngăn rò rỉ dữ liệu.", {
        "A": "Không phải nền tảng log.",
        "C": "Không phải bảo vệ bản quyền.",
        "D": "Không phải giao thức liên kết dữ liệu.",
    }),
    "abbr_c6_124": ("CSF là Cybersecurity Framework, khung an ninh mạng của NIST.", {
        "B": "Không phải Common Security Format.",
        "C": "Không phải Certified Security Function.",
        "D": "Không phải Cloud Security Foundation.",
    }),
    "std_c6_125": ("NIST CSF 2.0 thêm chức năng mới GOVERN (quản trị), thành 6 chức năng.", {
        "A": "IDENTIFY đã có từ bản 1.x.",
        "B": "RECOVER đã có từ bản 1.x.",
        "C": "DETECT đã có từ bản 1.x.",
    }),
    "std_c6_126": ("NIST CSF 2.0 là khung tự nguyện, không có chứng nhận như ISO 27001.", {
        "B": "CSF là khung của Hoa Kỳ, không phải luật Việt Nam.",
        "C": "Cấp chứng chỉ sau đánh giá độc lập là đặc điểm của ISO 27001.",
        "D": "Chỉ cho dữ liệu thẻ là PCI DSS.",
    }),
    "std_c6_127": ("Luật An toàn thông tin mạng là Luật số 86/2015/QH13.", {
        "A": "91/2025/QH15 là Luật Bảo vệ dữ liệu cá nhân.",
        "B": "24/2018/QH14 là Luật An ninh mạng 2018.",
        "D": "116/2025/QH15 là Luật An ninh mạng 2025.",
    }),
    "std_c6_128": ("Luật 86/2015/QH13 có hiệu lực từ 01/7/2016.", {
        "A": "19/11/2015 là ngày Quốc hội thông qua luật, không phải ngày hiệu lực.",
        "C": "01/7/2026 là ngày hiệu lực của Luật An ninh mạng 2025.",
        "D": "01/01/2019 là ngày hiệu lực của Luật An ninh mạng 2018.",
    }),
    "std_c6_129": ("Theo slide cập nhật, Luật Bảo vệ dữ liệu cá nhân là 91/2025/QH15.", {
        "A": "116/2025/QH15 là Luật An ninh mạng 2025.",
        "B": "24/2018/QH14 là Luật An ninh mạng 2018.",
        "D": "86/2015/QH13 là Luật An toàn thông tin mạng.",
    }),
    "std_c6_130": ("Luật ATTT mạng 2015 phân loại hệ thống thông tin theo 5 cấp độ.", {
        "A": "Không phải 4 cấp.",
        "C": "Không phải 3 cấp.",
        "D": "7 cấp là số mức EAL của Common Criteria.",
    }),
    "std_c6_131": ("Slide ghi thời hạn thông báo vi phạm dữ liệu cá nhân là 72 giờ.", {
        "B": "Không phải 48 giờ.",
        "C": "Không phải 24 giờ.",
        "D": "Không phải 7 ngày.",
    }),
    "std_c6_132": ("Slide nêu Luật An ninh mạng 2025 hợp nhất và thay thế Luật ATTT mạng 2015 và Luật ANM 2018.", {
        "A": "Theo slide, Nghị định 13/2023 được thay bằng NĐ 356 đi kèm Luật BVDLCN, không phải bởi Luật ANM 2025.",
        "B": "Luật này không thay Luật Giao dịch điện tử.",
        "C": "Luật này không thay Bộ luật Hình sự.",
    }),
}
