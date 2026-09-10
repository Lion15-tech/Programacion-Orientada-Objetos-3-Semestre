def ejercicio30():
    class Jugador:
        def __init__(self, nombre, salud):
            self.nombre = nombre
            self.salud = salud
            self.xp = 0
            self.nivel = 1

        def ganar_xp(self, cantidad):
            print(f"{self.nombre} ganó {cantidad} XP.")
            self.xp = self.xp + cantidad
            if self.xp >= 100:
                self.nivel += 1
                self.xp -= 100
                print(f"{self.nombre} ha subido al nivel {self.nivel}!")
                if self.xp > 0:
                    print(f"XP restante: {self.xp}")

    jugador = Jugador("Airi", 100)

    jugador.ganar_xp(60)
    jugador.ganar_xp(60)

