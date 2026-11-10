
class DigitalVideoDisc:
    """Một đĩa DVD bán trong cửa hàng AIMS."""

    def __init__(self, title: str, category: str = "", cost: float = 0.0):
        self.title = title
        self.category = category
        self.cost = cost

    def __str__(self):
        return f"DVD - {self.title} - {self.category} - {self.cost} $"
