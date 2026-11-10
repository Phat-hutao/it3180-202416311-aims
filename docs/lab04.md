# Lab 04 – Release flow và baseline

## 1. SemVer MAJOR.MINOR.PATCH là gì?

SemVer là quy tắc đánh số phiên bản phần mềm gồm ba thành phần:

- **MAJOR:** Tăng khi có thay đổi API không tương thích với phiên bản trước.
- **MINOR:** Tăng khi bổ sung tính năng mới nhưng vẫn đảm bảo tương thích ngược.
- **PATCH:** Tăng khi sửa lỗi nhưng không làm thay đổi tính tương thích.

Đối với phiên bản `0.y.z`, API vẫn chưa được xem là ổn định.

Trong bài Lab này, chọn phiên bản `1.0.0` để đánh dấu baseline chức năng đã ổn định, không phải cứ đến Lab 04 thì bắt buộc phải sử dụng phiên bản `0.4.0`.

## 2. Phân biệt Tag, Release branch và GitHub Release

- **Tag:** Là tên tham chiếu đến một commit cụ thể trong lịch sử Git.
- **Annotated tag:** Là loại tag có thêm thông tin metadata và message, thường được sử dụng để đánh dấu các phiên bản phát hành.
- **Release branch:** Là nhánh dùng để duy trì một phiên bản phát hành, có thể tiếp tục nhận các commit sửa lỗi thông qua PR.
- **GitHub Release:** Là bản mô tả phiên bản phát hành, có thể đính kèm tài liệu và các file cần thiết, được tạo dựa trên một tag.

**Lưu ý:** Không di chuyển hoặc thay đổi tag đã công bố vì tag cần đại diện cho một mốc phiên bản cố định.

## 3. Vì sao phải chuẩn bị version, CHANGELOG và tài liệu trước khi tạo release?

Cần chuẩn bị các nội dung như version, CHANGELOG và tài liệu trên nhánh master thông qua PR trước khi tạo nhánh `release/lab04`.

Việc này giúp baseline có đầy đủ nội dung đã được kiểm tra, đảm bảo phiên bản phát hành phản ánh chính xác trạng thái của dự án tại thời điểm chốt.

## 4. Vì sao không merge release ngược về master?

- Nhánh release có thể chứa các commit cập nhật version và những thay đổi bảo trì riêng cho phiên bản đó.
- Nếu merge ngược release vào master, lịch sử phát triển có thể xuất hiện những thay đổi không cần thiết.
- Khi cần đưa một bản sửa lỗi từ release sang master, nên sử dụng `git cherry-pick -x` thông qua PR để chuyển đúng commit cần thiết và giữ lại thông tin nguồn gốc commit.

**Tóm lại:** Không merge toàn bộ release ngược về master. Chỉ chuyển những commit sửa lỗi thực sự cần thiết bằng cherry-pick.

## 5. Phân biệt `git log A..B` và `git diff A B`

- **`git log A..B`:** Liệt kê các commit có trong B nhưng không có trong A. Lệnh này dùng để xem sự khác biệt về lịch sử commit giữa hai nhánh.
- **`git diff A B`:** So sánh nội dung của hai snapshot tại A và B để hiển thị những thay đổi về file và mã nguồn.

Trong bài Lab này:

- Trước khi có hotfix, `master..release/lab04` rỗng vì release chưa có commit nào mà master không có.
- `release/lab04..master` hiển thị các commit phát triển mới có trên master nhưng chưa có trên release.

**Lưu ý:** `git log` so sánh lịch sử commit, còn `git diff` so sánh nội dung mã nguồn.

## 6. Detached HEAD là gì? Worktree là gì?

**Detached HEAD:**

- Là trạng thái khi HEAD trỏ trực tiếp đến một commit thay vì trỏ đến một nhánh.
- Có thể thực hiện checkout và kiểm tra mã nguồn tại một commit cụ thể.
- Nếu tạo commit mới trong trạng thái này mà không tạo nhánh để tham chiếu, commit có thể không còn được tham chiếu trực tiếp và có nguy cơ bị mất sau quá trình dọn dẹp của Git.

**Worktree:**

- Là tính năng cho phép tạo thêm nhiều working directory từ cùng một repository.
- Các worktree chia sẻ chung object database nhưng có working directory và trạng thái checkout riêng.
- Worktree có thể checkout một nhánh hoặc ở trạng thái detached HEAD.

Trong bài Lab này, sử dụng `git worktree --detach` tại một tag để kiểm tra baseline mà không cần thay đổi working tree chính.

## 7. Vì sao phải tạo bốn annotated tag sau khi chốt baseline?

Bốn annotated tag được tạo để đánh dấu các mốc phiên bản trong quá trình phát triển:

- `v0.1.0`
- `v0.2.0`
- `v0.3.0`
- `v1.0.0`

Các tag này giúp xác định chính xác những commit tương ứng với từng phiên bản, hỗ trợ kiểm tra và truy xuất lịch sử phát triển.

Sau khi công bố, không nên di chuyển hoặc chỉnh sửa tag vì sẽ làm mất tính nhất quán của các mốc phiên bản.

## 8. Audit worktree gồm những nội dung gì?

Audit worktree là quá trình kiểm tra baseline trong một working directory riêng biệt nhằm đảm bảo phiên bản đã phát hành hoạt động đúng.

Các nội dung kiểm tra bao gồm:

- Chạy chương trình bằng `python main.py`.
- Chạy kiểm thử bằng `unittest`.
- Kiểm tra thông tin version.
- Kiểm tra sự tồn tại và nội dung của các file cần thiết.
- Kiểm tra CHANGELOG.
- Sử dụng `git archive` để tạo bản lưu trữ mã nguồn tại baseline.

Vì các bằng chứng kiểm tra được tạo ra sau khi baseline đã được chốt nên chúng sẽ được bổ sung bằng một PR tiếp theo trước khi thực hiện hotfix.

**Lưu ý:** Không sửa tag hoặc thay đổi baseline đã công bố chỉ để đưa các log kiểm tra mới vào lịch sử của phiên bản đó.
