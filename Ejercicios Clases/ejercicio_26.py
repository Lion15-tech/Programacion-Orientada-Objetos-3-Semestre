class Cuenta_Banco:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial

    #"LA VENTANA"
    #Se activa AUTOMÁTICAMENTE cuando alguien escribe 'cuenta.balance' (sin paréntesis)
    #Solo sirve para "asomarse" a ver el valor de la "caja fuerte" (o sea __saldo)
    @property 
    def saldo(self):
        return self.__saldo

    #"EL GUARDIA" 
    #Se activa AUTOMÁTICAMENTE cuando alguien usa un signo igual '=' (ej: cuenta.balance = 500)
    #Su único trabajo es revisar el 'nuevo_monto' antes de dejarlo entrar a la "caja fuerte"
    @saldo.setter
    def saldo(self, nuevo_monto):
        if nuevo_monto >= 0:
            self.__saldo = nuevo_monto
        else:
            print("Error, el monto no debería ser negativo")

    #Un método normal. 
    #Al usar 'self.saldo = ...', activa al GUARDIA (setter) de arriba
    #pasándole el resultado de la suma para que él lo valide.
    def depositar(self, monto):
        self.saldo = self.__saldo + monto
        return self.saldo
    
cuenta = Cuenta_Banco(1000)

print(f"Saldo: {cuenta.saldo}")
print(f"Saldo: {cuenta.depositar(500)}") 
cuenta.saldo = -200 

