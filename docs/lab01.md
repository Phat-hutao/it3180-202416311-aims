# Lab 01 – Trả lời câu hỏi thảo luận

## Câu hỏi nhanh: Cấu hình `--global` được lưu ở đâu? Khác gì so với `--local`?

- `--global`: Cấu hình được lưu trong file `~/.gitconfig` (đối với Windows là `C:\Users\<tên-user>\.gitconfig`). Cấu hình này được áp dụng cho tất cả repository của người dùng.
- `--local`: Cấu hình được lưu trong file `.git/config` của từng repository và chỉ có tác dụng trong repository đó.
- Khi có nhiều cấu hình trùng nhau, Git sẽ ưu tiên theo thứ tự: `system` < `global` < `local`. Có nghĩa là cấu hình ở phạm vi cụ thể hơn sẽ ghi đè cấu hình ở phạm vi chung hơn.

Có thể sử dụng lệnh `git config --list --show-origin` để kiểm tra các cấu hình và vị trí lưu của chúng.

## 1. Vì sao dùng `git mv`?

Lệnh `git mv` được sử dụng để đổi tên hoặc di chuyển file trong Git. Ưu điểm của lệnh này là vừa thực hiện việc di chuyển file, vừa tự động đưa thay đổi vào staging, không cần thực hiện thêm các lệnh khác.

Việc sử dụng `git mv` mang lại một số lợi ích:

- Khi tạo Pull Request, Git có thể nhận diện và hiển thị file được đổi tên trong mục *Files changed*, giúp người review dễ dàng theo dõi những thay đổi.
- Có thể tiếp tục xem lại lịch sử của file sau khi đổi tên bằng lệnh `git log --follow -- aims/cart.py`.

Về cơ bản, `git mv` tương đương với việc sử dụng `mv` kết hợp với `git rm` và `git add`. Tuy nhiên, sử dụng `git mv` sẽ thuận tiện hơn và hạn chế việc quên đưa file mới vào staging.

## 2. `release/lab01` có phải baseline không?

Có. Theo quy định của học phần, baseline là một phiên bản đã được thống nhất và chỉ được thay đổi khi thực hiện đúng quy trình.

Trong Lab 01, nhánh `release/lab01` được tạo từ `master` sau khi hoàn thành bài thực hành. Nhánh này được giữ nguyên để làm mốc phiên bản và sử dụng làm bản nộp bài. Nếu cần thay đổi sau đó thì phải thực hiện theo quy trình hotfix được học ở Lab 05.

Đến Lab 04, baseline sẽ được đánh dấu chính thức bằng tag annotated `v0.1.0`.

Ngoài ra, có thể sử dụng lệnh `git rev-parse origin/master origin/release/lab01` để kiểm tra mã băm của hai nhánh. Nếu hai mã băm giống nhau thì chứng tỏ `release/lab01` đang có cùng trạng thái với `master` tại thời điểm đó.

## 3. Vì sao không commit thẳng master dù làm một mình?

Mặc dù chỉ làm việc một mình, việc tuân thủ quy trình Git vẫn rất cần thiết vì những lý do sau:

- **Đảm bảo quy trình làm việc:** Nhánh `master` được xem là nhánh chính dùng để phát hành. Vì vậy, các thay đổi nên được thực hiện thông qua nhánh riêng, Pull Request, review và cuối cùng mới merge vào `master`.
- **Dễ kiểm soát thay đổi:** Sử dụng Pull Request giúp theo dõi những nội dung đã chỉnh sửa, dễ dàng kiểm tra và khôi phục khi có lỗi.
- **Làm quen với môi trường thực tế:** Trong các dự án thực tế, nhánh `master` thường được bảo vệ để tránh việc thay đổi trực tiếp. Từ Lab 02, nhánh này sẽ được bật branch protection nên việc push trực tiếp sẽ bị chặn.
- **Đáp ứng yêu cầu chấm điểm:** Rubric của bài thực hành có phần đánh giá việc tuân thủ branching policy (20%). Vì vậy, cần thực hiện đúng quy trình tạo nhánh, tạo Pull Request và merge thay vì commit trực tiếp vào `master`.
