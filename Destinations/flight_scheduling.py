import pandas as pd
import numpy as np
import itertools as it
from BookingApp.bookingMain import Bookingapp
import secretfile
# import database

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
        [6] To book a flight
        [7] To exit 
        """)

    # Function to retrieve all cities available in the database
    @staticmethod
    def choose_destination():
        fd1 = FlightDetails()
        print("Below are the following available destinations departing from London:\n")
        from Destinations.citiestoDatabase import DummyCities
        dc = DummyCities
        dc.csv_to_dataframe()
        # ba = Bookingapp
        # ba.userStore()
        choosing = False
        while not choosing:
            try:
                user_input = input("\n\nTo make a booking type [Y] to return to the menu type [M]\n\nYour selection: \n")
            except Exception:
                print("Invalid selection. Please type in [Y] or [M]")
            if user_input.upper() == "Y":
                return fd1.display_destination()
                choosing = True
            elif user_input.upper() == "M":
                print(fd1.menu())
                choosing = True
            else:
                print("Invalid selection. Please type in [Y] or [M]")

    @staticmethod
    def display_destination():
        # from BookingApp.bookingMain import Bookingapp
        fd1 = FlightDetails()
        # continue_program = True
        # while continue_program:
        # try:
            # passenger_choice = input("Please type in the destintion you would like to travel to: \n")
            from Destinations.citiestoDatabase import DummyCities
            dc = DummyCities
            dc.csv_to_dataframe()
            dc.checking_city_exists()
        # except ValueError:
        #     print(
        #         "Sorry! We currently do not fly to your chosen destination. Please select a valid city. Below is a list of available cities")
        #     print("To exit type E")

        # query_result = "SELECT City FROM Destination} "
        # rows = cursor.execute(query_result)

        if passenger_choice.capitalize() == "Paris": # country 1
            print("You are going to Paris!")
            from BookingApp.bookingMain import Bookingapp

            after_booking = input("\nType in [M] to return to the Menu or [E] to Exit your booking\nYour selection:\n")
            if after_booking == "M":
                return fd1.menu(), fd1.display_destination()
            if after_booking == "E":
                print("""
                    ==================================================
                    | Thank you for choosing Dangus Airline! GoodBye!|
                    ==================================================
                    """)
            elif passenger_choice.upper() == "M":  # to return to menu
                print(fd1.menu())
                print(fd1.display_destination())
            # print(fd1.choose_destination())
        elif passenger_choice.upper() == "E":  # exit program
            continue_program = False
            print("""
            ==================================================
            | Thank you for choosing Dangus Airline! GoodBye!|
            ==================================================
            """)
        elif passenger_choice == 7:
            continue_program = False
            print("""
            ==================================================
            | Thank you for choosing Dangus Airline! GoodBye!|
            ==================================================
            """)
        else:
            print("Sorry! We currently do not fly to your chosen destination. Please select a valid city: \n")
            # call choose destination method again to display a list of all available cities
            # sql_command = "SELECT cities from cities_list"
            # cursor = connection.cursor()
            # rows = cursor.execute(sql_command)
            # for row in rows:
            #     print(row)




# Test
fd1 = FlightDetails()
fd1.menu()
fd1.display_destination()
fd1.choose_destination()