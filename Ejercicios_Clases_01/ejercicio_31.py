def ejercicio31():
    import random
    import time

    class Cancion:
        def __init__(self, titulo, artista):
            self.titulo = titulo
            self.artista = artista

        def __str__(self):
            return f"{self.titulo} - {self.artista}"

    class Playlist:
        def __init__(self, nombre):
            self.nombre = nombre
            self.canciones = []

        def agregar_cancion(self, cancion):
            self.canciones.append(cancion)

        def eliminar_cancion(self, cancion):
            if cancion in self.canciones:
                self.canciones.remove(cancion)
            else:
                print("La canción no está en la playlist.")

        def aleatorio(self):
            random.shuffle(self.canciones)

        def mostrar_playlist(self):
            print(f"Playlist: {self.nombre}")
            for cancion in self.canciones:
                print(cancion)
                time.sleep(1)  # Pausa de 1 segundo entre canciones

    playlist = Playlist("Playlist de Ejemplo")

    cancion1 = Cancion("Life will change", "Lyn")
    cancion2 = Cancion("Usseewa", "Ado")
    cancion3 = Cancion("Idol", "Yoasobi")

    playlist.agregar_cancion(cancion1)
    playlist.agregar_cancion(cancion2)
    playlist.agregar_cancion(cancion3)

    playlist.mostrar_playlist()

    playlist.aleatorio()
    playlist.mostrar_playlist()

    playlist.eliminar_cancion(cancion2)
    playlist.mostrar_playlist()