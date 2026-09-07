class Temperatura:
    def __init__(self, celcius):
        self.celcius = celcius

    def a_fahrenheit(self):
        fahrenheit = (self.celcius * 9/5) + 32
        return (f"{fahrenheit} °F")

    def a_kelvin(self):
        kelvin = self.celcius + 273.15
        return (f"{kelvin} K")

temperatura_celcius = Temperatura(23)

print(temperatura_celcius.a_fahrenheit())

print(temperatura_celcius.a_kelvin())