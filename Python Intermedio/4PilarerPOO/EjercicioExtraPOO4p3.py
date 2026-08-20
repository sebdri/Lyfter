class Vehicle:
    def __init__(self, _brand, _year):
        self._brand = _brand
        self._year = _year

    def get_info(self):
        return f"{self._brand} ({self._year})"


class Car(Vehicle):
    def __init__(self, _brand, _year, doors):
        super().__init__(_brand, _year)
        self.doors = doors

    def get_info(self):
        base = super().get_info()
        return base + f" - {self.doors} puertas"


class Motorcycle(Vehicle):
    def __init__(self, _brand, _year, _type):
        super().__init__(_brand, _year)
        self._type = _type

    def get_info(self):
        base = super().get_info()
        return base + f" - Tipo: {self._type[0]}"


# Prueba
vehicle1 = Car("Toyota", 2020, 4)
vehicle2 = Motorcycle("Yamaha", 2022, "Deportiva")

print(vehicle1.get_info())  # Toyota (2020) - 4 puertas
print(vehicle2.get_info())  # Yamaha (2022) - Tipo: D