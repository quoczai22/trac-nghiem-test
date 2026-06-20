// Demo data only. This bank exists to validate the multi-subject flow.
window.__QUIZ_DATA__ = {
  title: "Ngân hàng trắc nghiệm Cơ sở dữ liệu - Demo",
  count: 24,
  sourceCounts: { demo: 24 },
  questions: [
    { chapter: 1, question: "Cơ sở dữ liệu là gì?", options: { A: "Tập hợp dữ liệu có tổ chức", B: "Một hệ điều hành", C: "Một ngôn ngữ lập trình", D: "Một thiết bị lưu trữ" }, answer: "A" },
    { chapter: 1, question: "Hệ quản trị cơ sở dữ liệu (DBMS) có vai trò chính là:", options: { A: "Quản lý, lưu trữ và truy vấn dữ liệu", B: "Thay thế RAM", C: "Biên dịch mã C", D: "Lập lịch CPU" }, answer: "A" },
    { chapter: 1, question: "Trong mô hình quan hệ, một bảng còn được gọi là:", options: { A: "Relation", B: "Thread", C: "Segment", D: "Frame" }, answer: "A" },
    { chapter: 1, question: "Một hàng trong bảng quan hệ được gọi là:", options: { A: "Tuple/bản ghi", B: "Attribute", C: "Schema", D: "Index" }, answer: "A" },
    { chapter: 1, question: "Một cột trong bảng quan hệ được gọi là:", options: { A: "Attribute/thuộc tính", B: "Tuple", C: "Transaction", D: "View" }, answer: "A" },
    { chapter: 1, question: "Khóa chính (primary key) phải có tính chất:", options: { A: "Duy nhất và không NULL", B: "Có thể trùng", C: "Luôn là số", D: "Luôn gồm hai cột" }, answer: "A" },
    { chapter: 1, question: "Khóa ngoại (foreign key) dùng để:", options: { A: "Liên kết dữ liệu giữa các bảng", B: "Tăng RAM", C: "Mã hóa password", D: "Sắp xếp kết quả" }, answer: "A" },
    { chapter: 1, question: "Schema mô tả:", options: { A: "Cấu trúc của cơ sở dữ liệu", B: "Một bản ghi cụ thể", C: "Kết quả của SELECT", D: "Tên người dùng" }, answer: "A" },

    { chapter: 2, question: "Câu lệnh SQL dùng để lấy dữ liệu là:", options: { A: "SELECT", B: "INSERT", C: "DELETE", D: "DROP" }, answer: "A" },
    { chapter: 2, question: "Mệnh đề WHERE trong SQL dùng để:", options: { A: "Lọc các dòng theo điều kiện", B: "Đổi tên bảng", C: "Tạo khóa chính", D: "Xóa database" }, answer: "A" },
    { chapter: 2, question: "Mệnh đề ORDER BY dùng để:", options: { A: "Sắp xếp kết quả truy vấn", B: "Gộp nhóm", C: "Thêm dữ liệu", D: "Tạo bảng" }, answer: "A" },
    { chapter: 2, question: "Câu lệnh INSERT dùng để:", options: { A: "Thêm bản ghi mới", B: "Sửa bản ghi", C: "Xóa bản ghi", D: "Cấp quyền" }, answer: "A" },
    { chapter: 2, question: "Câu lệnh UPDATE dùng để:", options: { A: "Cập nhật dữ liệu đã có", B: "Tạo database", C: "Đọc toàn bộ bảng", D: "Tạo index" }, answer: "A" },
    { chapter: 2, question: "INNER JOIN trả về:", options: { A: "Các dòng có dữ liệu khớp ở cả hai bảng", B: "Toàn bộ dòng bảng trái", C: "Toàn bộ dòng bảng phải", D: "Các dòng không khớp" }, answer: "A" },
    { chapter: 2, question: "GROUP BY thường đi cùng mục đích:", options: { A: "Gom nhóm để tính tổng hợp", B: "Tạo khóa ngoại", C: "Xóa cột", D: "Đổi kiểu dữ liệu" }, answer: "A" },
    { chapter: 2, question: "HAVING khác WHERE ở điểm:", options: { A: "HAVING lọc nhóm sau GROUP BY", B: "HAVING chỉ dùng để sắp xếp", C: "WHERE chỉ dùng cho INSERT", D: "Hai mệnh đề hoàn toàn giống nhau" }, answer: "A" },

    { chapter: 3, question: "Chuẩn hóa dữ liệu chủ yếu nhằm:", options: { A: "Giảm dư thừa và bất thường dữ liệu", B: "Tăng số cột vô hạn", C: "Thay thế backup", D: "Loại bỏ SQL" }, answer: "A" },
    { chapter: 3, question: "Dạng chuẩn 1NF yêu cầu:", options: { A: "Mỗi ô chứa giá trị nguyên tử", B: "Không cần khóa chính", C: "Mọi bảng chỉ một cột", D: "Không có khóa ngoại" }, answer: "A" },
    { chapter: 3, question: "ACID là các tính chất của:", options: { A: "Transaction", B: "Primary key", C: "ERD", D: "Index" }, answer: "A" },
    { chapter: 3, question: "Tính Atomicity trong ACID nghĩa là:", options: { A: "Hoàn thành toàn bộ hoặc không thực hiện gì", B: "Luôn chạy song song", C: "Dữ liệu luôn công khai", D: "Chỉ đọc dữ liệu" }, answer: "A" },
    { chapter: 3, question: "COMMIT có tác dụng:", options: { A: "Xác nhận vĩnh viễn transaction", B: "Hoàn tác transaction", C: "Tạo bảng", D: "Khóa database" }, answer: "A" },
    { chapter: 3, question: "ROLLBACK có tác dụng:", options: { A: "Hoàn tác các thay đổi chưa COMMIT", B: "Tăng tốc truy vấn", C: "Tạo primary key", D: "Xóa toàn bộ database" }, answer: "A" },
    { chapter: 3, question: "Index thường được tạo để:", options: { A: "Tăng tốc truy vấn phù hợp", B: "Tăng số bản ghi", C: "Thay thế khóa chính", D: "Xóa dữ liệu trùng" }, answer: "A" },
    { chapter: 3, question: "Ràng buộc NOT NULL đảm bảo rằng:", options: { A: "Cột không nhận giá trị NULL", B: "Cột luôn duy nhất", C: "Bảng không có khóa ngoại", D: "Dữ liệu tự sắp xếp" }, answer: "A" }
  ]
};
