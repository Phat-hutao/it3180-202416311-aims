# Lab 05 – Thảo luận: Ưu, nhược điểm của upstream first so với release first? Nếu quên lan truyền bản sửa sang release/lab05, lệnh nào ở Phần F sẽ phát hiện?

## 1. Upstream first so với release first

**Upstream first:** Là cách sửa lỗi trên dòng phát triển chính (master) trước, sau đó đưa bản sửa về các nhánh release có liên quan.

- **Ưu điểm:** Dòng phát triển chính nhận được bản sửa sớm, giảm nguy cơ quên cập nhật các nhánh khác.
- **Nhược điểm:** Bản sửa có thể cần điều chỉnh khi đưa về các phiên bản cũ do sự khác biệt về mã nguồn.

**Release first:** Là cách sửa lỗi trực tiếp trên nhánh release đang gặp vấn đề, sau đó chủ động đưa bản sửa sang master và các nhánh release khác có liên quan.

- **Ưu điểm:** Phù hợp khi cần vá lỗi khẩn cấp trên phiên bản đã phát hành.
- **Nhược điểm:** Phải chủ động lan truyền bản sửa sang các nhánh khác, nếu không có thể xảy ra tình trạng các phiên bản không đồng nhất.

## 2. Nếu quên sửa release/lab05, phát hiện bằng cách nào?

Có thể kiểm tra bằng cách chạy thử hành vi tìm kiếm trên các phiên bản khác nhau:

- `v1.0.1`
- `v1.1.0`
- `master`

Trong repository này, mốc hoàn chỉnh cuối cùng được sử dụng là `v1.1.1` (giải thích ở mục 4).

Nếu phiên bản Lab 05 vẫn tìm kiếm từ khóa "lion" và trả về 0 kết quả thì bản sửa lỗi chưa được đưa vào phiên bản đó.

Ngoài ra, có thể kiểm tra lịch sử commit cherry-pick để xác nhận bản sửa đã được lan truyền hay chưa.

**Lưu ý:** Không nên chỉ dựa vào `git tag --contains` vì cherry-pick tạo ra commit mới với SHA khác, dù nội dung thay đổi có thể giống commit gốc.

## 3. Vì sao phải tách commit sửa lỗi và nâng phiên bản?

Cần tách riêng commit sửa lỗi và commit nâng phiên bản để dễ dàng quản lý và lựa chọn những thay đổi cần đưa sang các nhánh release khác.

Cụ thể:

- Commit sửa lỗi và regression test có thể được cherry-pick sang các nhánh phiên bản khác.
- Commit nâng version chỉ áp dụng cho dòng phiên bản tương ứng.
- Tránh trường hợp khi chuyển bản sửa lỗi sang nhánh khác lại vô tình làm thay đổi số phiên bản của nhánh đó.

**Tóm lại:** Tách commit giúp việc cherry-pick chính xác hơn, tránh đưa những thay đổi không cần thiết sang các dòng phiên bản khác.

## 4. Mốc phát hành cuối cùng của bài nộp

Tag `v1.1.0` đã được đẩy lên trước khi hoàn tất bản sửa lỗi và vẫn khai báo phiên bản `1.0.0`.

Vì vậy, không xóa hoặc di chuyển tag đã công bố. Bản hoàn chỉnh được sử dụng là `v1.1.1` trên nhánh `release/lab05`.

Đây là sự thay đổi mốc định danh so với ví dụ `v1.1.0` trong slide nhằm giữ nguyên lịch sử đã công bố.

Hai commit cherry-pick từ commit sửa lỗi gốc `eaab7f90b030d1bbdffd8b9db1cdbdf271b48554` được giữ nguyên:

- `a988eae`: Đưa vào master thông qua PR #20.
- `2497553`: Đưa vào release/lab05 thông qua PR #21.

## 5. Kiểm toán và tiêu chí nghiệm thu

Bảng kết quả kiểm tra các dòng phiên bản:

| Dòng phiên bản | Version trong mã | Kết quả tìm "lion" | Số test |
|---|---|---|---|
| v1.0.0 (đối chứng cũ) | 1.0.0 | 0 | 4 |
| v1.0.1 / release/lab04 | 1.0.1 | 1 | 5 |
| v1.1.1 / release/lab05 | 1.1.1 | 1 | 8 |
| master | 1.1.1 | 1 | 8 |

Các lệnh kiểm toán sau khi tạo tag phát hành:

```bash
git diff --stat v1.0.0 v1.0.1

git log --all --oneline --grep="cherry picked from commit eaab7f90b030d1bbdffd8b9db1cdbdf271b48554"

git cherry -v origin/master origin/release/lab04

git rev-parse 'v1.0.1^{commit}' origin/release/lab04

git rev-parse 'v1.1.1^{commit}' origin/release/lab05
```

Kết quả kiểm toán cho thấy:

- Chênh lệch giữa `v1.0.0` và `v1.0.1` chỉ bao gồm các file `aims/search.py`, `tests/test_search.py`, `aims/__init__.py` và `CHANGELOG.md`.
- Hai cặp SHA cuối phải có giá trị bằng nhau để xác nhận tag và nhánh tương ứng trỏ đến cùng một commit.
- `git tag --contains` chỉ kiểm tra quan hệ tổ tiên giữa tag và commit, không thay thế việc kiểm tra hành vi khi bản sửa được cherry-pick sang commit có SHA khác.

**Tóm lại:** Cần kết hợp kiểm tra lịch sử commit, SHA, nội dung thay đổi và kết quả chạy chương trình để đảm bảo bản sửa đã được đưa vào đúng các dòng phiên bản.

## 6. CI mở rộng

Workflow `.github/workflows/ci.yml` được cấu hình để chạy kiểm thử tự động bằng `unittest` với Python 3.12.

- Job `test` được sử dụng làm required status check trên nhánh master.
- Mọi PR cần vượt qua kiểm thử CI trước khi được phép merge.
- PR thử nghiệm `bugfix/lab05-ci-demo` cố ý tạo lỗi bằng cách cho hàm `total_cost` trả về 0 để chứng minh CI có thể phát hiện lỗi.
- Sau khi kiểm tra, cần đóng PR thử nghiệm này và không merge mã nguồn bị lỗi.

**Lưu ý:** Đây là bài thực hiện cá nhân. Mọi thay đổi trên master và release/lab05 đều phải thông qua Pull Request (PR). Không tự tạo approval bằng chính tài khoản của tác giả PR.
