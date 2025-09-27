#Ejercicio Extra OOP 3

class Vehicle:
    def __init__(self, brand, year):
        self._brand = brand
        self._year = year

    def get_info(self):
        return f"{self._brand} ({self._year})" #Can be overwritten by child classes


class Car(Vehicle):  # Inherits from Vehicle
    def __init__(self, brand, year, doors): 
        self._brand = brand
        self._year = year
        self.doors = doors

    def get_info(self):
        return f"{self._brand} - {self._year} - {self.doors} puertas"


class Motorcycle(Vehicle):  # Inherits from Vehicle
    def __init__(self, brand, year, type): #Calls the Vehicle constructor to set brand and year
        self._brand = brand
        self._year = year
        self.type = type

    def get_info(self):
        return f"{self._brand} - {self._year} - Tipo {self.type}"


vehicle1 = Car("Nissan", 2025, 4)
vehicle2 = Motorcycle("BMW", 2023, "Sport")

print(vehicle1.get_info())
print(vehicle2.get_info())