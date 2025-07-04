# === product.py ===
# SRP - Kelas ini hanya bertanggung jawab sebagai representasi data produk

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class DiscountedProduct(Product):  # SRP - Produk dengan diskon
    def __init__(self, name, price, discount):
        self.name = name
        self.price = price
        self.discount = discount

    def get_discounted_price(self):
        return self.price * (1 - self.discount)

class ProductSearch:
    @staticmethod
    def search(products_dict, keyword):
        keyword = keyword.lower().strip()
        return [
            product
            for name, product in products_dict.items()
            if keyword in name.lower()
        ]
