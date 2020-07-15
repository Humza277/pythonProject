import pandas as pd
import numpy as np
import itertools as it


# import database

class FlightDetails:

    # function to display all flight options
    @staticmethod
    def menu():
        return ("""
        ===============================================
        | Welcome to the Dangus Flight Booking System! |
        ===============================================

        Please choose one of the following options:
        [1] To choose a destination 
        [2] To display all short haul flights, retrieve data from database)
        [3] To find the longest flight OR (display all long haul flights, retrieve data from database) 
        [4] To see your booking (insert booking ID, validate it against database to retrieve booking) 
        [5] To add a passenger to a current booking 
        [6] To book a flight (passenger details, import create user from booking main, ) 
        [7] To exit 
        """)

    # Function to retrieve all cities available in the database
    @staticmethod
    def choose_destination():
        fd1 = FlightDetails()
        print("Below are the following available destinations departing from London:\n")
        # print(fd1.display_destination())
        # sql_command = "SELECT cities from cities_list"
        # cursor = connection.cursor()
        # rows = cursor.execute(sql_command)
        # for row in rows:
        #     print(row)
        #     print("Type E in the keyboard to exit")
        #     print("Type M in the keyboard to return to the menu")

    # retrieve data from the database, list of destination
    # if chosen destination not in database, raise Error, display flight destination options
    # SELECT cities from cities_list
    # display available destinations for passengers to view

    @staticmethod
    def display_destination():
        # from BookingApp.bookingMain import Bookingapp
        fd1 = FlightDetails()
        continue_program = True

        while continue_program:
            try:
                passenger_choice = input("Please type in your chosen destination: \n")
            except ValueError:
                print(
                    "Sorry! We currently do not fly to your chosen destination. Please select a valid city. Below is a list of available cities")
                print(row)
                print("To exit type E")

            if passenger_choice.capitalize() == "Paris":  # country 1
                print("You are going to Paris!")
                from BookingApp.bookingMain import Bookingapp
                print(Bookingapp.userStore())
                print(
                    "Thank you for booking with Dangus Airline!\nTo see the menu options again type in [M]\nTo see exit your booking type in [E]")

            elif passenger_choice.capitalize() == "Madrid":  # country 2
                print("You are going to Madrid!")
                from BookingApp.bookingMain import Bookingapp
                print(Bookingapp.userStore())
                print(
                    "Thank you for booking with Dangus Airline!\nTo see the menu options again type in [M]\nTo see exit your booking type in [E]")

            elif passenger_choice.capitalize() == "Berlin":  # country 3
                print("You are going to Berlin!")
                from BookingApp.bookingMain import Bookingapp
                print(Bookingapp.userStore())
                print(
                    "Thank you for booking with Dangus Airline!\nTo see the menu options again type in [M]\nTo see exit your booking type in [E]")

            elif passenger_choice.capitalize() == "TelAviv":  # country 4
                print("You are going to Tel Aviv!")
                from BookingApp.bookingMain import Bookingapp
                print(Bookingapp.userStore())
                print(
                    "Thank you for booking with Dangus Airline!\nTo see the menu options again type in [M]\nTo see exit your booking type in [E]")

            elif passenger_choice.capitalize() == "Amsterdam":  # country 5
                print("You are going to Amsterdam! \n")
                from BookingApp.bookingMain import Bookingapp
                print(Bookingapp.userStore())
                print(
                    "Thank you for booking with Dangus Airline!\nTo see the menu options again type in [M]\nTo see exit your booking type in [E]")

            elif passenger_choice.capitalize() == "Sydney":  # country 6
                print("You are going to Sydney! \n")
                from BookingApp.bookingMain import Bookingapp
                print(Bookingapp.userStore())
                print(
                    "Thank you for booking with Dangus Airline!\nTo see the menu options again type in [M]\nTo see exit your booking type in [E]")

            elif passenger_choice.capitalize() == "Vilnius":  # country 7
                print("You are going to Vilnius! Please enter your passenger details to confirm booking: \n")
                from BookingApp.bookingMain import Bookingapp
                print(Bookingapp.userStore())
                print(
                    "Thank you for booking with Dangus Airline!\nTo see the menu options again type in [M]\nTo see exit your booking type in [E]")

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
# fd1 = FlightDetails()
# fd1.menu()
# fd1.choose_destination()
# fd1.display_destination()