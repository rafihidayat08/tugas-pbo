class BankAccount:
    def __init__(self, no, saldo):
        # Validasi saldo
        if saldo < 0:
            raise ValueError("Saldo tidak boleh negatif")

        self.no = no
        self.saldo = saldo

budi = BankAccount("123456789", 1000)
print(f"Akun sukses dibuat -> No: {budi.no}, Saldo: {budi.saldo}")

try:
    eko = BankAccount("987654321", -500)
except ValueError as e:
    print(f"Gagal membuat akun -> Error: {e}")