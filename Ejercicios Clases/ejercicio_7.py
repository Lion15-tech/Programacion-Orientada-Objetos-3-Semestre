class Luz:
    def __init__(self, esta_encendida):
        self.esta_encendida = esta_encendida

    def encender(self):
        self.esta_encendida = True

    def apagar(self):
        self.esta_encendida = False

    def status(self):
        if self.esta_encendida == True:
            return ("La luz esta encendida")
        else:
            return ("La luz esta apagada")


lampara = Luz(False)
print(f"Estatus: {lampara.status()}")

lampara.encender()
print(f"Estatus: {lampara.status()}")

lampara.apagar()
print(f"Estatus: {lampara.status()}")
