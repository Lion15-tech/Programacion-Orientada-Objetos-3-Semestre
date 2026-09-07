class Vehiculo:
    def __init__(self, nombre, max_speed,):
        self.nombre = nombre
        self.max_speed = max_speed

    def capacidad_asientos(self, capacidad):
        print(f"La capacidad de asientos de {self.nombre} es de: {capacidad}")

class Bus(Vehiculo):
    def capacidad_asientos(self, capacidad):
        super().capacidad_asientos(capacidad)

bus1 = Bus("Bus escolar", 120)
vehiculo = Vehiculo("Tesla", 250)

vehiculo.capacidad_asientos(5)
bus1.capacidad_asientos(50)
