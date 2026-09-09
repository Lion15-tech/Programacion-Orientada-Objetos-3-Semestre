import math

def ejercicio18(): 
    class Figura:
        def __init__(self, nombre):
            self.nombre = nombre

        def area(self):
            raise NotImplementedError("No se definió en las subclases")


    class Circulo(Figura):
        def __init__(self, nombre, radio):
            super().__init__(nombre)
            self.radio = radio

        def area(self):
            return math.pi * (self.radio)**2

    class Cuadrado(Figura):
        def __init__(self, nombre, lado):
            super().__init__(nombre)
            self.lado = lado

        def area(self):
            return self.lado ** 2

    class Triangulo(Figura):
        def __init__(self, nombre, base, altura):
            super().__init__(nombre)
            self.base = base
            self.altura = altura

        def area(self):
            return (self.base * self.altura) / 2


    circulo = Circulo("CIRCULO", 7)
    cuadrado = Cuadrado("CUADRADO",4)
    triangulo = Triangulo("TRIANGULO", 6, 8)

    print(f"El area de {circulo.nombre} es: {circulo.area()}")
    print(f"El area de {cuadrado.nombre} es: {cuadrado.area()}")
    print(f"El area de {triangulo.nombre} es: {triangulo.area()}")

