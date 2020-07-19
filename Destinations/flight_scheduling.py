import csv

from Destinations.databaseconnect import Databases
from Destinations.citiestoDatabase import DummyCities
from BookingApp.bookingMain import Bookingapp
import secretfile
from Destinations import databaseconnect
import pandas as pd


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
    def list_all_destinations():
        pass

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
                # from Destinations.citiestoDatabase import DummyCities
                # dc = DummyCities
                # dc.checking_city_exists()
                cursor.execute("SELECT * FROM Destination")
                dt = cursor.fetchall()
                for dt in dt:
                    print(dt)
                das = input("Please enter a DestinationID:\n")

                cursor.execute("SELECT d.Destination_ID, d.Country, d.City, d.Flight_Price, "
                               "d.Flight_Type, a.Flight_Number "
                               "FROM Destination d JOIN Airplane a on a.Destination_ID = d.Destination_ID "
                               "WHERE d.Destination_ID = ?", [das])

                dest = cursor.fetchone()
                dest_l = list(dest)
                row_l = list(row)
                print(dest_l)
                print(row_l)


                query = f"""
                INSERT INTO Booking_Details(Booking_ID, Flight_Number, PassengersID, Destination_ID, Flight_Price)
                    Values('{row_l[4]}' , '{dest_l[5]}', '{row_l[0]}', '{dest_l[0]}', '{dest_l[3]}')"""
                cursor.execute(query)
                cursor.commit()


                cursor.execute('SELECT * FROM Booking_Details')
                rob = cursor.fetchall()
                print(rob)

                #
                # FlightDetails.sql_to_csv(dest)
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

    @staticmethod
    def sql_to_csv(dest):
        with open("dest+flightnumb.csv", 'a+') as dest1:
            dest1.write(dest)

# Test
# fd1 = FlightDetails()
# fd1.menu()
# fd1.list_all_destinations()
# fd1.choose_destination()
