# === interfaces.py ===
# ISP - Memisahkan kontrak (interface) berdasarkan tanggung jawab

from abc import ABC, abstractmethod

class Payable(ABC):  # Interface untuk perhitungan total
    @abstractmethod
    def calculate_total(self):
        pass

class PrintableReceipt(ABC):  # Interface untuk pencetakan struk
    @abstractmethod
    def print_receipt(self):
        pass
