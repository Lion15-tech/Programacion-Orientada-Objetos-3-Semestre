def ejercicio5():
    class Producto:
        def __init__(self, nombre, precio, cantidad):
            self.nombre = nombre
            self.precio = precio
            self.cantidad = cantidad

        def valor_total(self):
            valor_total = self.precio * self.cantidad
            return valor_total

    laptop = Producto("Asus Tuf Gaming A16", 19000, 4)

    print(f"Producto: {laptop.nombre} | Valor Total: {laptop.valor_total()}")