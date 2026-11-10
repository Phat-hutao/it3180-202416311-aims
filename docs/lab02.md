# Lab 02 – Trả lời câu hỏi thảo luận

## 1. Vì sao phải đồng bộ master trước khi gửi PR?

- **PR sạch, dễ review:** Nếu nhánh được tạo từ phiên bản main cũ, tab *Files changed* có thể hiển thị lẫn cả những thay đổi người khác đã merge, khiến reviewer khó phân biệt đâu là thay đổi của mình.
- **Phát hiện xung đột sớm:** Sử dụng `git merge origin/main` để chủ động giải quyết conflict ngay trên máy cá nhân, thay vì đợi đến khi PR báo lỗi "This branch has conflicts".
- **Kiểm thử tích hợp:** Sau khi merge main vào nhánh cá nhân, cần chạy chương trình hoặc unit test để kiểm tra xem tính năng của mình có hoạt động với mã nguồn mới nhất hay không.
- **Lịch sử Git rõ ràng:** Đồng bộ đúng cách giúp lịch sử commit dễ theo dõi, tránh tạo ra quá nhiều merge không cần thiết khiến `git log --graph` khó đọc.

**Tóm lại:** Cần đồng bộ main trước khi gửi PR để phát hiện lỗi, xử lý xung đột và đảm bảo mã nguồn của mình tương thích với phiên bản mới nhất.

## 2. Khi nào KHÔNG được rebase?

- **Nhánh đã chia sẻ với người khác:** Rebase làm thay đổi SHA của commit, khiến lịch sử giữa các thành viên không còn đồng nhất. Vì vậy, không nên rebase các commit đã được push và sử dụng chung.
- **Nhánh đang có PR được review:** Rebase có thể làm thay đổi lịch sử commit, gây khó khăn trong việc theo dõi những thay đổi đã được review và phê duyệt.
- **Trường hợp bắt buộc phải rebase nhánh đã push:** Nên sử dụng `git push --force-with-lease` thay vì `git push --force` để hạn chế ghi đè lên thay đổi của người khác.
- **Trên nhánh main và release:** Không nên rebase vì đây là những nhánh dùng chung. Khi cần hoàn tác thay đổi trên các nhánh này, nên sử dụng `git revert`.

**Tóm lại:** Chỉ nên rebase trên nhánh cá nhân và các commit chưa được chia sẻ. Tránh viết lại lịch sử của những nhánh dùng chung.

## 3. `feature/*` khác `topic/*` ở đâu?

| Tiêu chí | `feature/*` | `topic/*` |
|---|---|---|
| Nội dung | Phát triển tính năng sản phẩm, thay đổi hành vi mà người dùng có thể nhìn thấy. | Các công việc kỹ thuật, tài liệu hoặc cấu hình phục vụ dự án. |
| Ví dụ | `feature/cart-print`, `feature/search-by-title` | `topic/pr-template`, `topic/use-case-diagram` |
| Ý nghĩa commit | Thường sử dụng tiền tố `feat:` | Thường sử dụng `docs:`, `chore:`, `ci:`... |
| Vòng đời | Thường gắn với Issue hoặc đề xuất tính năng. | Phục vụ các công việc phụ trợ, không trực tiếp thay đổi hành vi chương trình. |

**Điểm giống nhau:** Cả hai đều là nhánh ngắn hạn, được tạo từ `main` và tích hợp trở lại `main` thông qua Pull Request (PR).

**Điểm khác nhau:** `feature/*` tập trung vào việc phát triển tính năng sản phẩm, còn `topic/*` tập trung vào các công việc kỹ thuật, tài liệu và quy trình của dự án.
