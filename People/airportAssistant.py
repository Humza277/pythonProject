from Destinations import databaseconnect
from Destinations.databaseconnect import Databases
from Destinations.flight_scheduling import FlightDetails
import pandas as pd
import hashlib
import os
import bcrypt


# Creates class Assistant to enter for flight_attendant list

class Assistant:
    # username and passwords are stored within data as attributes

    @staticmethod
    def staff_or_passenger():
        s_or_p = True

        while s_or_p:
            try:
                user_input = input(
                    "\nType [C] to view booking\nYour selection:\n")
            except Exception:
                print("Invalid selection. Please type in [C]\n")
            if user_input.upper() == "C":
                print("\nDirecting you to the crew member login page...\n")
                a = Assistant
                return (a.login_crew())
                s_or_p = False
            else:
                print("\nInvalid selection. Please type in [C] to login as a crew member")


    @staticmethod
    def login_crew():
        # count is set to 0
        count = 0
        # only runs code when code is < 3
        awd = b"forlorn"
        hashed = bcrypt.hashpw(awd, bcrypt.gensalt())
        print(hashed)
        while True:

            userName = input("Please input user name: \n")
            password = input("Please input password: \n")

            count += 1
            if userName == 'assistant' and bcrypt.checkpw(awd, hashed):
                print("W.I.P --- print the passenger list here")
                break

            elif count == 3:
                # after 3 attempts, statement is printed
                print("Too many tries... Exiting program")
                # 3 attempts will stop the code
                # add break and method call to creating a booking
                break
            else:
                print("Incorrect username or password, try again")

        # method Ugne when you choose a location if it is a long haul it will assign the large plane
        # if short haul assign small plane
        # allows crew members to print out passenger list

    # if correct details are entered, user can look for details within make_booking method
    @staticmethod
    def assign_plane():
        pass
        # assign a passenger to a plane if country is short assign small plane

    @staticmethod
    def make_booking():
        mb = databaseconnect.Databases()
        cursor = mb.create_cursor()

        make_booking_loop = True

        while make_booking_loop:
            try:
                passenger_ID = input("Input passenger ID:\n")
                cursor.execute("SELECT * FROM Passengers WHERE PassengersID = ?", [passenger_ID])
                row = cursor.fetchone()
                FlightDetails.choose_destination(row)
                break
                #df = pd.DataFrame(row, columns=['PassengersID', 'FirstName', 'LastName',
                                               # 'DOB', 'Booking_ID', 'Passport_Number'])

                # takes destination id
            except Exception:
                print("Invalid passenger ID,\nInput a correct Passenger ID: \n")


    @staticmethod
    def selectdest():
        pass

# if passenger_ID == "Next":
#     print("Select the destination")
#     cursor.execute("SELECT City FROM Destination")
#     drow = cursor.fetchall()
#     print(drow)
#     df['Destination'] = drow
#     print(df)


# Test
# a = Assistant()
# a.staff_or_passenger()
