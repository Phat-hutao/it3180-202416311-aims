
"""Tim kiem DVD trong cua hang."""


def search_by_category(items, category: str):
    """Tra ve danh sach cac DVD thuoc mot the loai (khong phan biet hoa/thuong)."""
    return [dvd for dvd in items if dvd.category.lower() == category.lower()]


def search_by_title(items, keyword: str):
    """Tra ve danh sach cac DVD co tieu de chua keyword (khong phan biet hoa/thuong)."""
    return [dvd for dvd in items if keyword.lower() in dvd.title.lower()]
