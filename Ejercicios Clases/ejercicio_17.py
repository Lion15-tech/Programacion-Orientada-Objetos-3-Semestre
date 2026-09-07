class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre

    def calcular_pago(self):
        '''Esta linea de código me la dio la IA para saber que así
        se puede evitar que el código falle si en una subclase no 
        se define la forma de pago'''

        #Si fuera pass podría ocurrir algún error
        raise NotImplementedError("Las subclases deben implementar este método")

        '''Normalmente, Python lanza errores cuando algo sale mal sin que tú lo planees
        Pero con raise, tú te vuelves el jefe y le dices a Python: 
        ¡Alto! Si alguien llega a esta línea de código, detén el programa inmediatamente
        y lanza este error'''

class Empleado_tiempo_completo(Empleado):
    def __init__(self, nombre, salario_anual):
        super().__init__(nombre)
        self.salario_anual = salario_anual

    def calcular_pago(self):
        return self.salario_anual / 12


class Empleado_medio_tiempo(Empleado):
    def __init__(self, nombre, pago_hrs, hrs_trabajadas):
        super().__init__(nombre)
        self.pago_hrs = pago_hrs
        self.hrs_trabajadas = hrs_trabajadas

    def calcular_pago(self):
        return self.hrs_trabajadas * self.pago_hrs


alice = Empleado_tiempo_completo("Alice0",60000)
bob = Empleado_medio_tiempo("Bob", 500, 20)

print(f"{alice.nombre} gana {alice.calcular_pago()}")
print(f"{bob.nombre} gana {bob.calcular_pago()}")