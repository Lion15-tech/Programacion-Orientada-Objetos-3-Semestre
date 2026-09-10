def ejercicio27():
    # ANALOGÍA: Esta clase es como los planos de una máquina exprimidora.
    # No es la máquina real todavía, sino las instrucciones de cómo funciona.
    class Multiplicador:
        # "LA CONFIGURACIÓN"
        # Aquí es cuando compras la máquina.
        # Le instalas el filtro (por ejemplo, "Modo: Multiplicar por 3").
        # La máquina ahora tiene "memoria" y recuerda su configuración.
        def __init__(self, factor):
            self.factor = factor

        # "EL BOTÓN ROJO DE ACTIVACIÓN"
        # Este método es el botón físico. Cuando lo presionas 
        # (usando paréntesis), la máquina se activa, revisa qué
        # configuración tenía guardada y hace el trabajo.
        def __call__(self, valor):
            return self.factor * valor

        
    # Compramos una máquina y la configuramos permanentemente en "Modo 3"
    triple = Multiplicador(3)

    # Compramos OTRA máquina y la configuramos permanentemente en "Modo 5"
    quintuple = Multiplicador(5)

    # La máquina recuerda en que modo esta e imprime el resultado correspondiente
    print(triple(10))
    print(quintuple(7))