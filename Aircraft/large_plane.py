# importing planes file
from Aircraft.planes import Planes

# creating a subclass for large aircraft
class LargePlane(Planes):
    # initialising the class using instance attributes
    def __init__(self, name, number_of_seats, fuel_capacity, flight_type):
        super().__init__(name, number_of_seats, fuel_capacity)
        # adding flight type attribute
        self.flight_type = flight_type

# creating an object
lp_1 = LargePlane("A380", 538, "320,000 Litres", "Long haul")

print(lp_1.flight_type)
