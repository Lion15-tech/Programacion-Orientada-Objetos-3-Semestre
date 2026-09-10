def ejercicio23():
    class Animal: 
        pass

    class Perro(Animal):
        pass

    d = Perro()

    print(f"d es una instacia de Perro? {isinstance(d, Perro)}")
    print(f"d es una instacia de Animal? {isinstance(d, Animal)}")

    print(f"Perro es una subclase de Animal? {issubclass(Perro, Animal)}")
    print(f"Animal es una subclase de Perro? {issubclass(Animal, Perro)}")