class Usuario:
    def __init__(self, nombre, contraseña):
        self.nombre = nombre
        self.contraseña = contraseña

    def revisar_contraseña(self, contraseña2):
        if contraseña2 == self.contraseña:
            return ("Contraseña Correcta")
        else:
            return ("Contraseña incorrecta,")

usuario1 = Usuario("Rodrigo", 12345)

print(usuario1.revisar_contraseña(123))

print(usuario1.revisar_contraseña(12345))