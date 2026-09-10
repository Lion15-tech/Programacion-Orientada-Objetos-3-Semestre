def ejercicio21():
    class Vehiculo:
        def __init__(self, nombre, max_speed):
            self.nombre = nombre
            self.max_speed = max_speed

        def descripcion(self):
            print(f"La velocidad máxima de {self.nombre} es de: {self.max_speed} km/h")


    class Moto(Vehiculo):
        def __init__(self, nombre):
            super().__init__(nombre, 120)


    class Camion(Vehiculo):
        def __init__(self, nombre):
            super().__init__(nombre, 90)


    class Bus(Vehiculo):
        def __init__(self, nombre):
            super().__init__(nombre, 100)


    moto = Moto("Bike")
    camion = Camion("Truck")
    autobus = Bus("Bus")

    moto.descripcion()
    camion.descripcion()
    autobus.descripcion()