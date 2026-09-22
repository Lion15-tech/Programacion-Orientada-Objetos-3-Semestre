class ProductoTienda:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.__precio = precio

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, nuevo_monto):
        if nuevo_monto > 0:
            self.__precio = nuevo_monto
        else:
            print("El precio debe ser un valor positivo")

    def __str__(self):
        return f"Producto: {self.nombre} | Precio: ${self.precio}"



# Código de prueba para validar tu solución:
lapiz = ProductoTienda("Lápiz 2B", 15.0)

# Probar __str__
print(lapiz)  # Debería imprimir: Producto: Lápiz 2B | Precio: $15.0

# Probar modificación correcta usando el setter
lapiz.precio = 20.0
print(lapiz)  # Debería imprimir: Producto: Lápiz 2B | Precio: $20.0

# Probar la validación del setter
lapiz.precio = -5.0  # Debería imprimir el mensaje de error y NO modificar el precio
print(lapiz)  # Debería mantener el precio en $20.0