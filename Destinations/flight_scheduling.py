import pandas as pd
import numpy as np
import itertools as it


class FlightDetails:

    # function to display all flight options

    def menu():
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

    menu()

    def choose_destination():
        pass


    def user_interface():

        user_exit = False
        while not user_exit:
            print(FlightDetails.menu())
            try:
                user_input = int(input("\nYour selection: \n"))
            except ValueError:
                print("Invalid selection. Please try again.")
            except Exception:
                print("Invalid selection. Please try again.")
                if user_input == 7:
                    print("""
        ==================================================
        | Thank you for visiting! I hope to see you again |
        ==================================================
        """)




