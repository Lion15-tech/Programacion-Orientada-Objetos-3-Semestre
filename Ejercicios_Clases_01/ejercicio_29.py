def ejercicio29():
    class Animal:
        def comer(self):
            return "El animal está comiendo"

    class Leon(Animal):
        def comer(self):
            return "El león come carne"

    class Elefante(Animal):
        def comer(self):
            return "El elefante come hierba"

    class Loro(Animal):
        def comer(self):
            return "El loro come semillas"

    class Zoo:
        def __init__(self):
            self.animales = []

        def agregar_animal(self, animal):
            self.animales.append(animal)

        def alimentar_animales(self):
            for animal in self.animales:
                print(animal.comer())

    leon = Leon()
    elefante = Elefante()
    loro = Loro()

    zoo = Zoo()

    zoo.agregar_animal(leon)
    zoo.agregar_animal(elefante)
    zoo.agregar_animal(loro)

    zoo.alimentar_animales()