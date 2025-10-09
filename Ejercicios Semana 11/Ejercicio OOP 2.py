#Ejercicio OOP #2

class Passenger:
    def __init__(self, name): #Constructor
        self.name = name #Saves passenger's name


class Bus:
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers #Bus max capacity
        self.current_passengers = [] #List of current passengers


    def add_passenger(self, passenger):
        if len(self.current_passengers) < self.max_passengers: #Checks if there are available sits
            self.current_passengers.append(passenger) #Adds the passenger to the list
            print(f'{passenger.name} abordó.')
            return True
        else:
            print("El bus está lleno.")
            return False


    def dropoff_passenger(self):
        if self.current_passengers: #Checks if there are passengers in the bus
            passenger = self.current_passengers.pop() #Removes the last passenger who boarded
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