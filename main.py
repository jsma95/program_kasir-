# === main.py ===
# DIP - Menggunakan dependency abstraction (Cart, Inventory, TransactionManager)
# Tidak membuat logika baru; hanya mengatur interaksi antar komponen

from cart import Cart
from inventory import Inventory
from transaction_manager import TransactionManager
from product import ProductSearch

def menu():
    inventory = Inventory()
    transaction_manager = TransactionManager()

    while True:
        print("\n=== Menu Kasir ===")
        print("1. Tambah Barang")
        print("2. Lihat Barang Tersedia")
        print("3. Belanja Pelanggan")
        print("4. Lihat Semua Transaksi")
        print("5. Pencarian Produk")
        print("6. Keluar")

        choice = input("Pilih menu (1-5): ")

        if choice == "1":
            name = input("Nama barang: ")
            try:
                price = float(input("Harga barang: "))
                inventory.add_product(name, price)
                print(f"✔ Barang '{name}' ditambahkan.")
            except ValueError:
                print("⚠️ Harga tidak valid.")

        elif choice == "2":
            inventory.show_products()

        elif choice == "3":
            cart = Cart()
            while True:
                inventory.show_products()
                name = input("Masukkan nama barang yang ingin dibeli (atau 'selesai'): ")
                if name.lower() == "selesai":
                    break

                product = inventory.get_product(name)
                if not product:
                    print("⚠️ Barang tidak ditemukan.")
                    continue

                try:
                    jumlah = int(input("Jumlah barang: "))
                    for _ in range(jumlah):
                        cart.add_product(product)
                    print(f"✔ {jumlah} x {product.name} ditambahkan ke keranjang.")
                except ValueError:
                    print("⚠️ Jumlah tidak valid.")

            cart.print_receipt()
            transaction_manager.add_transaction(cart)

        elif choice == "4":
            transaction_manager.show_transactions()

        elif choice == "5":
            keyword = input("Nama barang: ")
            results = ProductSearch.search(inventory.products, keyword)
            if results:
                print("\n=== Hasil Pencarian ===")
                for p in results:
                    print(f"- {p.name}: Rp {p.price:.2f}")
            else:
                print("⚠️ Tidak ada barang yang cocok.")
        elif choice == "6":
            print("Terima kasih telah menggunakan sistem kasir.")
            break

        else:
            print("⚠️ Pilihan tidak valid. Silakan pilih 1–5.")

if __name__ == "__main__":
    menu()
