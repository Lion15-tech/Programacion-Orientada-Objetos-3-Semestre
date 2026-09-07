class Orden:
    def __init__(self, id_orden, costo):
        self.id_orden = id_orden
        self.costo = costo

    def costo_total(self):
        return self.costo


class Orden_descuento(Orden):
    def __init__(self, id_orden, costo):
        super().__init__(id_orden, costo)

    def costo_descuento(self):
        costo_con_descuento = self.costo
        costo_con_descuento = self.costo - (self.costo * 0.10)
        return costo_con_descuento

orden1 = Orden_descuento("ORD001", 1200)

print(f"ID Orden: {orden1.id_orden}"
    f"\nCosto Original: {orden1.costo_total()}"
    f"\nCosto con Descuento: {orden1.costo_descuento()}")