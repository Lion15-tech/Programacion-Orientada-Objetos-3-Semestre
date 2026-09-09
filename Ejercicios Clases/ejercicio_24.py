def ejercicio24():
    class Vector:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        #EL TRADUCTOR DEL SIGNO '+'
        #Se activa automáticamente al escribir 'v1 + v2'
        #'self' representa al vector de la izquierda (v1)
        #'other' representa al vector de la derecha (v2)
        def __add__(self, other):
            nuevo_vector = Vector(self.x + other.x, self.y + other.y)
            return nuevo_vector
        #¿POR QUÉ SE USA?
        # Porque en la matemática de vectores, para sumar v1 + v2, debes sumar las 'x' con las 'x' 
        # y las 'y' con las 'y'. Python por sí solo no sabe cómo sumar dos objetos que tú inventaste.
        # Si intentas hacer 'v1 + v2' sin este método, el programa fallará con un error.
        # Además, se usa para cumplir con las reglas de la POO: la suma no debe modificar los vectores 
        # originales, sino fabricar y REGRESAR UN VECTOR NUEVO con el resultado combinado.


        #"EL DISEÑADOR VISUAL"
        #Le dice a Python cómo quieres que se dibuje el vector en pantalla
        #Se activa automáticamente cuando usas un 'print()' con el objeto
        #Obligatoriamente debe devolver un texto (String)
        def __str__(self):
            return f"Vector({self.x}, {self.y})"
        #¿POR QUÉ SE USA?
        # Porque si intentas usar 'print(v1)' sin este método, Python imprimirá un texto horrible 
        # y sin sentido técnico en la pantalla (como "<__main__.Vector object at 0x7f9b10>").
        # Se usa para tomar el control total de la apariencia del objeto y "traducir" sus datos internos 
        # a un formato de texto (String) que sea limpio, elegante y exactamente el que pide el ejercicio.

    v1 = Vector(2, 3)
    v2 = Vector(4, 1)

    print(v1 + v2)