def ejercicio12():
    class Vehiculo:
        color = "Blanco"

        def __init__(self, nombre, max_speed,):
            self.nombre = nombre
            self.max_speed = max_speed


    vehiculo = Vehiculo("Tesla", 250)
    vehiculo2 = Vehiculo("BMW", 200)

    print(f"Nombe: {vehiculo.nombre} | Max speed: {vehiculo.max_speed} | Color: {vehiculo.color}")
    print(f"Nombe: {vehiculo2.nombre} | Max speed: {vehiculo2.max_speed} | Color: {vehiculo2.color}")

    Vehiculo.color = "Rojo"

    print(f"Nombe: {vehiculo.nombre} | Max speed: {vehiculo.max_speed} | Color: {vehiculo.color}")
    print(f"Nombe: {vehiculo2.nombre} | Max speed: {vehiculo2.max_speed} | Color: {vehiculo2.color}")