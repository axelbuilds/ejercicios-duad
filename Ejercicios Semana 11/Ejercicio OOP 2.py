#Ejercicio OOP #2

class Passenger:
    def __init__(self, name):
        self.name = name


class Bus:
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.current_passengers = []


    def add_passenger(self, passenger):
        if len(self.current_passengers) < self.max_passengers:
            self.current_passengers.append(passenger)
            print(f'{passenger.name} abordó.')
            return True
        else:
            print("El bus está lleno.")
            return False


    def dropoff_passenger(self):
        if self.current_passengers:
            passenger = self.current_passengers.pop()
            print(f'{passenger.name} bajó del bus.')
            return True
        else:
            print("No hay pasajeros para bajar")
            return False


    def __repr__(self):
        passenger_names = ", ".join(p.name for p in self.current_passengers) or "Ninguno"
        return f"Bus(Capacidad Maxima = {self.max_passengers}, Pasajeros = [{passenger_names}])"


bus = Bus(2)
p1 = Passenger("Axel")
p2 = Passenger("Test")

bus.add_passenger(p1)
bus.add_passenger(p2)

print(bus)
bus.dropoff_passenger()
print(bus)