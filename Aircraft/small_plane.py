# importing planes file
from Aircraft.planes import Planes

# creating a subclass for small aircraft
class SmallPlane(Planes):
    # initialising the class using instance attributes
    def __init__(self, name, number_of_seats, fuel_capacity, flight_type):
        super().__init__(name, number_of_seats, fuel_capacity)
        # adding flight type attribute
        self.flight_type = flight_type

# creating an object
sp_1 = SmallPlane("E195", 120, "16,213 Litres", "Short haul")

print(sp_1.flight_type)

