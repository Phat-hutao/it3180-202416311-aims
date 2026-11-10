
MAX_NUMBERS_ORDERED = 20


class Cart:
    """Giỏ hàng chứa tối đa MAX_NUMBERS_ORDERED đĩa DVD."""

    def __init__(self):
        self.items = []

    def add_dvd(self, dvd) -> bool:
        """Thêm một DVD vào giỏ; trả về False nếu giỏ đã đầy."""
        if len(self.items) >= MAX_NUMBERS_ORDERED:
            return False
        self.items.append(dvd)
        print("Đã thêm đĩa vào giỏ hàng")
        return True

    def print_cart(self):
        """In chi tiết các đĩa trong giỏ; thông báo nếu giỏ trống."""
        if not self.items:
            print("The cart is empty")
            return
        print(f"=== Giỏ hàng ({len(self.items)} đĩa) ===")
        for index, dvd in enumerate(self.items, start=1):
            print(f"{index}. {dvd}")

    def sort_by_title(self):
        """Sắp xếp đĩa trong giỏ theo tiêu đề (A → Z)."""
        self.items.sort(key=lambda dvd: dvd.title)
        return self.items

    def sort_by_cost(self):
        """Sắp xếp đĩa trong giỏ theo giá tăng dần."""
        self.items.sort(key=lambda dvd: dvd.cost)
        return self.items

    def total_cost_with_discount(self, percent: float) -> float:
        """Tổng tiền sau khi giảm giá percent %."""
        if not 0 <= percent <= 100:
            raise ValueError("percent must be between 0 and 100")
        return round(self.total_cost() * (100 - percent) / 100, 2)

    def total_cost(self) -> float:
        """Tổng tiền của các DVD trong giỏ."""
        return round(sum(dvd.cost for dvd in self.items), 2)
