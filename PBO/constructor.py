class BankAccount:
    no = ""
    saldo = 0

    def __init__(self, no, saldo):
        #validasi saldo
        if saldo < 0:
            raise ValueError("Saldo tidak boleh negatif")

        self.no = no
        self.saldo = saldo

budi = BankAccount("123456789", 1000) #sukses
eko = BankAccount("987654321", -500) #error
