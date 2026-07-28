#    ------------<CAMBIOS SOLICITADOS>------------



# I fixed the indentation of the add_passengers and remove_passengers methods
# so they are now inside the Bus_sebas class.


class Bus_sebas:
    
    def __init__(self, max_passengers = 50):
        self.max_passengers = max_passengers 
        self.passengers = []

    def add_passangers(self, Person):

        if len(self.passengers) < self.max_passengers:
            self.passengers.append(Person) 
            print("Pasajero agregado")
        else:
            print("Bus lleno")

    def less_pasangers(self, Person):
        if Person in self.passangers:
            self.passengers.remove(Person)
            print("Pasajero bajó del bus.")
        else:
            print("Esa persona no está en el bus.")

bus = Bus_sebas()
print(bus)