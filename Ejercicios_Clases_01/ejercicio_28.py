def ejercicio28():
    class Pasajeros:
        def __init__(self, nombre):
            self.nombre = nombre

        def __str__(self):
            return f"Nombre: {self.nombre}"

    class Vuelo:
        def __init__(self, num_vuelo, capacidad):
            self.num_vuelo = num_vuelo
            self.capacidad = capacidad
            self.pasajeros = []

        def reservar(self, pasajero):
            if len(self.pasajeros) < self.capacidad:
                self.pasajeros.append(pasajero)
                print(f"{pasajero.nombre} reservó en el vuelo {self.num_vuelo}.")
            else:
                print("No hay asientos disponibles.")


    bob = Pasajeros("Bob")
    Ana = Pasajeros("Ana")
    Nestor = Pasajeros("Nestor")

    vuelo1 = Vuelo("AB123", 2)

    vuelo1.reservar(bob)
    vuelo1.reservar(Ana)
    vuelo1.reservar(Nestor)

