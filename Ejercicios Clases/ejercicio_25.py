def ejercicio25():
    class Carrito:
        def __init__(self):
            self.items = []

        def agregar_items(self, item):
            self.items.append(item)

        #EL CONTADOR
        #Se activa AUTOMÁTICAMENTE cuando afuera escribes 'len(articulos)'
        # 'self' representa a este carrito en específico
        def __len__(self):
            return len(self.items)
        #¿POR QUÉ SE USA?
        # Porque por defecto Python NO SABE medir objetos que tú inventas. Si intentas hacer 
        # len(articulos) sin este método, Python se rompe y te da un error.
        # Al usar '__len__', obligas a que tu objeto se comporte exactamente igual que una 
        # lista o un texto nativo de Python, permitiendo usar la función len() normal.

    articulos = Carrito()

    articulos.agregar_items("manzana")
    articulos.agregar_items("banana")
    articulos.agregar_items("mango")


    print(f"El número de articulos en el carrito es: {len(articulos)}")
