def ejercicio4():
    class Estudiante:
        def __init__(self, nombre, notas):
            self.nombre = nombre
            self.notas = notas

        def promedio(self):
            promedio = sum(self.notas) / len(self.notas)
            return promedio

    estudiante1 = Estudiante("Rodrigo", [10, 8, 9, 8.7, 9.5])

    print(f"Estudiante: {estudiante1.nombre} | Promedio: {estudiante1.promedio()}")
