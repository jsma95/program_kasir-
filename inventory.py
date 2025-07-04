# === inventory.py ===
# SRP - Bertugas menyimpan dan menampilkan daftar produk yang tersedia

from product import Product

class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, name, price):
        self.products[name] = Product(name, price)

    def show_products(self):
        if not self.products:
            print("⚠️ Tidak ada produk yang tersedia.")
        else:
            print("\n=== Daftar Barang Tersedia ===")
            for name, product in self.products.items():
                print(f"- {name}: Rp {product.price:.2f}")

    def get_product(self, name):
        return self.products.get(name)
