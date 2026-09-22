class CuentaDigital:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self.puntos = 0
    
    def depositar(self, monto):
        if monto > 0:
            self.saldo = self.saldo + monto
            bloques_deposito = monto // 100
            if bloques_deposito > 0:
                self.puntos = self.puntos + (bloques_deposito * 5)
        else:
            print("El monto a depositar debe ser mayor a cero")

    def retirar(self, monto):
        if monto > 0 and monto <= self.saldo:
            self.saldo = self.saldo - monto
        else:
            print("No es posible retirar el monto solicitado")

    def mostrar_resumen(self):
        print(f"Titular: {self.titular} \n"
            f"Saldo: {self.saldo} \n"
            f"Puntos: {self.puntos}")


# Código de prueba:
cuenta = CuentaDigital("Carlos", 500)
cuenta.mostrar_resumen()
print()
cuenta.depositar(200) # Debería sumar 200 al saldo y agregar 10 puntos
cuenta.mostrar_resumen()
print()
cuenta.retirar(100)   # Debería restar 100 del saldo
cuenta.mostrar_resumen()