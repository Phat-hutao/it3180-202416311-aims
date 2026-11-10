# Merge base là gì? Vì sao master/release/* phải dùng revert?

## 1. Merge base là gì?

Merge base là tổ tiên chung tốt nhất của hai commit hoặc hai nhánh. Trong trường hợp phân nhánh thông thường, đây là commit chung gần nhất trước khi hai nhánh tách ra.

Git sử dụng merge base làm mốc để xác định những thay đổi của từng nhánh khi thực hiện merge.

**Tóm lại:** Merge base là điểm chung trong lịch sử Git, giúp Git xác định sự khác biệt giữa hai nhánh để hợp nhất mã nguồn chính xác.

## 2. Vì sao master và release/* phải dùng revert?

- **Đây là các nhánh dùng chung:** Master và release/* chứa lịch sử commit mà nhiều thành viên trong nhóm cùng sử dụng.
- **Revert giữ nguyên lịch sử:** Lệnh `git revert` tạo một commit mới để đảo ngược thay đổi của commit trước đó, không xóa hay viết lại lịch sử cũ. Điều này giúp dễ dàng truy vết nguyên nhân hoàn tác.
- **Reset có thể làm thay đổi lịch sử:** Lệnh `git reset` có thể di chuyển vị trí HEAD và đầu nhánh về commit trước đó. Nếu ép cập nhật remote, lịch sử mà những thành viên khác đang sử dụng có thể bị ảnh hưởng.

**Tóm lại:** Trên các nhánh dùng chung như master và release/*, nên sử dụng `git revert` để hoàn tác thay đổi mà vẫn giữ nguyên lịch sử commit, đảm bảo an toàn và dễ truy vết.
