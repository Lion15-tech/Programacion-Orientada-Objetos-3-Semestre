def ejercicio22():
    class Perro:
        pass

    class Gato:
        pass

    class Vehiculo:
        pass

    #Estos primero los creamos así nomás porque no deja ponerlos 
    #en una lista o diccionario
    d = Perro()
    c = Gato()
    v = Vehiculo()

    #Creamos un diccionario donde venga su nombre (la letra) y 
    #luego le asignamos el hijo que creamos arriba
    cosas = {"d":d, "c":c, "v":v}

    #revisa el nombre y luego el hijo del diccionario gracias al .items() 
    for nombre, objeto in cosas.items():
                                    #type(objeto) devuelve 
                                    #<class '__main__.[aqí va el nombre de la clase]'>
        print(f"{nombre} es de tipo {type(objeto).__name__}")
                                    #Por eso ocupamos .__name__ que sirve
                                    #para que python nos "revele" el nombre que
                                    #le asigna a cada cosa, en este caso a la clase
                                    #del objeto