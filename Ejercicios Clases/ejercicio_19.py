def ejercicio19():
    class Media:
        def __init__(self, nombre, precio):
            self.nombre = nombre
            self.precio = precio
        
        def descripcion(self):
            raise NotImplementedError("Cada subclase debería tenerlo hecho")


    class Libro(Media):
        def __init__(self, nombre, precio, autor):
            super().__init__(nombre, precio)
            self.autor = autor

        def descripcion(self):
            return (f"Libro: {self.nombre} | Precio: {self.precio} | Autor {self.autor}") 


    class Revista(Media):
        def __init__(self, nombre, precio, publicacion):
            super().__init__(nombre, precio)
            self.publicacion = publicacion

        def descripcion(self):
            return (f"Revista: {self.nombre} | Precio: {self.precio} | Publicación: {self.publicacion}")


    class DVD(Media):
        def __init__(self, nombre, precio, duracion):
            super().__init__(nombre, precio)
            self.duracion = duracion

        def descripcion(self):
            return (f"Nombre: {self.nombre} | Precio: {self.precio} | Duración: {self.duracion}")


    libro = Libro("Clean Code", 499, "Robert C. Martin")
    revista = Revista("Wired", 150, "Monthly")
    dvd = DVD("Inception", 299, 148)

    print(libro.descripcion())
    print(revista.descripcion())
    print(dvd.descripcion())
