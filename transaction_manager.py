# === transaction_manager.py ===
# SRP - Bertugas menyimpan dan menampilkan transaksi

class TransactionManager:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, cart):
        self.transactions.append(cart)

    def show_transactions(self):
        if not self.transactions:
            print("⚠️ Belum ada transaksi.")
        else:
            print("\n=== Riwayat Transaksi ===")
            for i, cart in enumerate(self.transactions, start=1):
                print(f"\nTransaksi #{i}")
                cart.print_receipt()
