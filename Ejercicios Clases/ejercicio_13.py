def ejercicio13():
    class Vehiculo:
        def __init__(self, nombre, max_speed,):
            self.nombre = nombre
            self.max_speed = max_speed

        def display(self):
            print(f"Nombe: {self.nombre} | Max speed: {self.max_speed}")


    class Bus(Vehiculo):
        pass

    bus1 = Bus("Bus escolar", 120)

    bus1.display()