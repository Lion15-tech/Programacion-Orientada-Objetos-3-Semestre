def ejercicio6():
    class CuentaBanco:
        def __init__(self, saldo):
            self.saldo = saldo

        def depositar(self, monto):
            self.saldo = self.saldo + monto

        def retiro(self, monto):
            if self.saldo >= monto:
                self.saldo = self.saldo - monto
            else:
                print("Fondos insuficientes")

    cuenta1 = CuentaBanco(1000)
    print(f"Saldo: {cuenta1.saldo}")

    cuenta1.depositar(500)
    print(f"Saldo: {cuenta1.saldo}")

    cuenta1.retiro(200)
    print(f"Saldo: {cuenta1.saldo}")

    cuenta1.retiro(2000)
    print(f"Saldo: {cuenta1.saldo}")

