# from BookingApp.bookingMain import passenger
# Import passenger from booking main

class Flight_trip:

    def __init__(self, passengers, origin,destination, duration, price):
        self.passengers = passengers
        self.origin = origin
        self.destination = destination.lower()
        self.duration = duration
        self.price = price

    def add_plane(self):
        self.plane = plane_number

    def add_origin(self, origin):
        self.origin = origin

    def add_destination(self, destination):
        self.destination = destination

    def add_passenger(self, passenger):
        self.passengers.append(passenger)

    def display_destinations(self):
        pass

    def print_info(self):
        print("Flight origin: ",self.origin,
              "\nFlight destination: ", self.destination,
              "\nPassenger Details: ", self.passengers,
              "\nFlight duration: ", self.duration,
              "\nTotal price: ", self.price)




