def ejercicio2():
    class Vehiculo:
        def __init__(self, nombre, max_speed, kilometraje):
            self.nombre = nombre
            self.max_speed = max_speed
            self.kilometraje = kilometraje

    vehiculo1 = Vehiculo("Tesla", 250, 18)

    print(f"Nombe: {vehiculo1.nombre} | Max speed: {vehiculo1.max_speed} | Kilometraje: {vehiculo1.kilometraje}")

