# === cart.py ===
# SRP - Bertugas menangani keranjang belanja
# OCP - Mendukung extensibility (produk diskon, promo dll)
# LSP - Mengikuti kontrak dari interface (Payable dan PrintableReceipt)

from interfaces import Payable, PrintableReceipt
from product import Product, DiscountedProduct

class Cart(Payable, PrintableReceipt):
    def __init__(self):
        self.items = []

    def add_product(self, product: Product):
        self.items.append(product)

    def calculate_total(self):  # ISP & LSP - Implementasi kontrak Payable
        total = 0
        for product in self.items:
            if isinstance(product, DiscountedProduct):
                total += product.get_discounted_price()
            else:
                total += product.price
        return total

    def print_receipt(self):  # ISP & LSP - Implementasi kontrak PrintableReceipt
        print("\n=== Receipt ===")
        for item in self.items:
            if isinstance(item, DiscountedProduct):
                print(f"{item.name}: {item.get_discounted_price():.2f} (after {int(item.discount * 100)}% discount)")
            else:
                print(f"{item.name}: {item.price:.2f}")
        print(f"Total: {self.calculate_total():.2f}\n")
