def ejercicio15():
    class Vehiculo:
        def __init__(self, nombre, max_speed, tarifa_mantenimiento):
            self.nombre = nombre
            self.max_speed = max_speed
            self.tarifa_mantenimiento = tarifa_mantenimiento

        def total_tarifa(self):
            print(f"La tarifa de mantenimiento es de: {self.tarifa_mantenimiento}")

    class Taxi(Vehiculo):
        def __init__(self, nombre, max_speed, tarifa_mantenimiento):
            super().__init__(nombre, max_speed, tarifa_mantenimiento)
            self.tarifa_mantenimiento = self.tarifa_mantenimiento + self.tarifa_mantenimiento * 0.10

        def total_tarifa(self):
            return super().total_tarifa()

    taxi = Taxi("Taxi", 120, 500)
    vehiculo = Vehiculo("Tesla", 250, 100)

    vehiculo.total_tarifa()
    taxi.total_tarifa()