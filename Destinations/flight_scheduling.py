from Destinations.citiestoDatabase import DummyCities
from BookingApp.bookingMain import Bookingapp
import secretfile
from Destinations import databaseconnect

class FlightDetails:

    # function to display all flight options
    @staticmethod
    def menu():
        print("""
        ===============================================
        | Welcome to the Dangus Flight Booking System! |
        ===============================================

        Please choose one of the following options:
        [1] To choose a destination 
        [2] To display all short haul flights
        [3] To display all long haul flights
        [4] To see your booking details 
        [5] To add a passenger to a current booking 
        [6] To exit 
        """)

    @staticmethod
    # change this method to database pull
    def list_all_destinations():
        print("Below are the following available destinations departing from London:\n")
        from Destinations.citiestoDatabase import DummyCities
        dc = DummyCities
        dc.csv_to_dataframe()

    # Function to retrieve all cities available in the database
    @staticmethod
    def choose_destination(row):
        fd1 = FlightDetails
        bm = Bookingapp
        choosing = False
        mb = databaseconnect.Databases()
        cursor = mb.create_cursor()
        while not choosing:
            try:
                #from Destinations.citiestoDatabase import DummyCities
                #dc = DummyCities
                #dc.checking_city_exists()
                cursor.execute("SELECT * FROM Destination")
                dt = cursor.fetchall()
                print(row)
                print(dt)






                user_input = input("\n\nType [M] to return to the menu\n\nYour selection: \n")
            except Exception:
                print("Invalid selection. Please type [M] to return to the menu")
            if user_input.upper() == "Y":
                return bm.userStore()
                choosing = True
            elif user_input.upper() == "M":
                print(fd1.menu())
                choosing = True
            else:
                print("Invalid selection. Please type in [Y] or [M]")

# Test
# fd1 = FlightDetails()
# fd1.menu()
# fd1.list_all_destinations()
# fd1.choose_destination()