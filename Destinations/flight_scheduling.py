
import pandas as pd
import numpy as np
import itertools as it
# import database

class FlightDetails:

    # function to display all flight options
    @staticmethod
    def menu():
        fd1 = FlightDetails()
        print("""
        ===============================================
        | Welcome to the Dangus Flight Booking System! |
        ===============================================
        
        Please choose one of the following options:
        1. To choose a destination
        2. To find the cheapest flight (display all short haul flights, retrieve data from database)
        3. To find the longest flight (display all long haul flights, retrieve data from database)
        4. To see your booking (insert booking ID, validate it against database to retrieve booking) 
        5. 
        6. To book a flight (passenger details, import create user from booking main, )
        7. To exit
        """)




    # menu()
    @staticmethod
    def choose_destination():
        fd1 = FlightDetails()
        print(f"Below are the following available destinations departing from London:\n{fd1.display_destination()}")
        # print(fd1.display_destination())


    # retrieve data from the database, list of destination
    # if chosen destination not in database, raise Error, display flight destination options
    # SELECT cities from cities_list

    # display available destinations for passengers to view
    @staticmethod
    def display_destination():
        # from BookingApp.bookingMain import Bookingapp
        fd1 = FlightDetails()

        close_program = True

        # sql_command = "SELECT cities from cities_list"
        # cursor = connection.cursor()
        # rows = cursor.execute(sql_command)
        # for row in rows:
        #     print(row)
        #     print("Type E in the keyboard to exit")
        #     print("Type M in the keyboard to return to the menu")
        while close_program:
            try:
                passenger_choice = input("Please type in the destination you would like to travel to: \n")
            except ValueError:
                print("Sorry! We currently do not fly to your chosen destination. Please select a valid city. Below is a list of available cities")
                print(row)
                print("To exit type E")
            if passenger_choice.capitalize() == "Paris": # country 1
                print("Something")
            elif passenger_choice.capitalize() == "Madrid": # country 2
                print("Something")
            elif passenger_choice.capitalize() == "Berlin": # country 3
                print("Something")
            elif passenger_choice.capitalize() == "Tel Aviv": # country 5
                print("Something")
            elif passenger_choice.capitalize() == "Vilnius":
                print("You are going to Vilnius! Please enter your passenger details to confirm booking: \n")
                from BookingApp.bookingMain import Bookingapp
                # print(Bookingapp.createUser())
                print(Bookingapp.userStore())
                print("Thank you for booking with Dangus Airline!\nTo see the menu options again type in [M]\nTo see exit your booking type in [E]")
            elif passenger_choice.upper() == "M": # to return to menu
                print(fd1.menu())
            elif passenger_choice.upper() == "E":
                print("""
                ==================================================
                | Thank you for choosing Dangus Airline! GoodBye!|
                ==================================================
                """)
                close_program = False
            else:
                print("Sorry! We currently do not fly to your chosen destination. Please select a valid city")






    def passenger_budget():
        pass
    # require passenger input (int) for budget
    # if budget < min(pricelist)
    # raise error no flights available
    # if budget > min(pricelist)
    # retrieve list of available destinations
    # if passenger choose destination
    # call usercreate method
    # if passenger does not want to book, display menu
    # else: exit program


    @staticmethod
    def user_interface():
        fd1 = FlightDetails()
        user_exit = False
        while not user_exit:
            print(FlightDetails.menu())
            try:
                user_input = int(input("\nYour selection: \n"))
            except ValueError:
                print("Invalid selection. Please try again.")
            except Exception:
                print("Invalid selection. Please try again.")
            if user_input == 1:
                print(fd1.choose_destination())
            elif user_input == 2:
                print("Work in progress.... finding cheapest flight")
            elif user_input == 3:
                print("Work in progress...finding shortest flight")
            elif user_input == 4:
                print("Work in progress... finding booking")
            elif user_input == 5:
                print("work in progress...")
            elif user_input == 6:
                print("To book flight")
                fd1.choose_destination() # callcreate user method from booking main
            elif user_input == 7:
                print("""
        ==================================================
        | Thank you for visiting! I hope to see you again |
        ==================================================
        """)
                user_exit = True
            else:
                print("Invalid selection. Please try again.")



f = FlightDetails()
# f.menu()
f.user_interface()