def ejercicio11():
    class Maquina_de_Cafe:
        def __init__(self, agua, cafe, leche):
            self.agua = agua
            self.cafe = cafe
            self.leche = leche

        def hacer_latte(self):
            agua_requerida = 200
            cafe_requerido = 20
            leche_requerida = 150

            if agua_requerida <= self.agua and cafe_requerido <= self.cafe and leche_requerida <= self.leche:
                print(f"Preparado! Tienes todos los ingredientes. \n"
                    f"Ingredientes restantes: agua: {self.agua - agua_requerida} | "
                    f"cafe: {self.cafe - cafe_requerido} | leche: {self.leche - leche_requerida}")
                self.agua = self.agua - agua_requerida
                self.cafe = self.cafe - cafe_requerido
                self.leche = self.leche - leche_requerida
            else:
                print("No tienes los ingredientes suficientes")


    taza = Maquina_de_Cafe(300, 100, 200)
    taza.hacer_latte()

    taza.hacer_latte()
