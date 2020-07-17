# parent class for all planes

# initializing the class by considering parameters name, number of seats, fuel capacity.
class Planes:
    def __init__(self, name, number_of_seats, fuel_capacity):
        self.name = name
        self.number_of_seats = number_of_seats
        self.fuel_capacity = fuel_capacity

