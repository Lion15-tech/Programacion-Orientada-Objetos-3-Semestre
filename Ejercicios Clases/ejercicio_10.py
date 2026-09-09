def ejercicio10():
    class Libreta:
        def __init__(self, notas):
            self.notas = notas
            self.notas = []

        def agregar_nota(self, nota):
            self.notas.append(nota)

        def ver_notas(self):
            return enumerate(self.notas, 1)

    agenda = Libreta([])

    agenda.agregar_nota("Comprar víveres")
    agenda.agregar_nota("Leer un libro")
    agenda.agregar_nota("Llamar al médico")

    for nota in agenda.ver_notas():
        print(nota)