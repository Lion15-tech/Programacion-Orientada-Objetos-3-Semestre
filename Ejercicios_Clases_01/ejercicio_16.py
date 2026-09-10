def ejercicio16():
    class Animal:
        def hablar(self, ):
            return "sonido"

    class Perro(Animal):
        def hablar(self):
            return "Guau"
        
    class Gato(Animal):
        def hablar(self):
            return "Miau"

    husky = Perro()
    gato = Gato()

    print(f"El perro hace: {husky.hablar()}")
    print(f"El gato hace: {gato.hablar()}")