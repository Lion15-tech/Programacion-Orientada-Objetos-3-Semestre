class Rectangulo:
    def __init__(self, altura, ancho):
        self.altura = altura
        self.ancho = ancho

    def area(self):
        area = self.altura * self.ancho 
        return area

    def perimetro(self):
        perimetro = 2 * (self.altura + self.ancho)
        return perimetro

figura = Rectangulo(10, 4)

print(f"Area: {figura.area()}")
print(f"Perimetro: {figura.perimetro()}")