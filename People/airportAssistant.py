from Destinations import databaseconnect
from Destinations.databaseconnect import Databases

# Creates class Assistant to enter for flight_attendant list

class Assistant:
    # username and passwords are stored within data as attributes
    @staticmethod
    def staff_or_passenger():
        s_or_p = True

        while s_or_p:
            try:
                user_input = input("\nAre you a crew member or a passenger?\n\nType [C] to login as a crew member\nType [P] to login as a passenger\nYour selection:\n")
            except Exception:
                print("Invalid selection. Please type in [C] for crew member or [P] for passenger\n")
            if user_input.upper() == "P":
                print("\nDirecting you to the passenger login page...\n")
                a = Assistant
                return(a.login_passenger())
                s_or_p = False

            elif user_input.upper() == "C":
                print("\nDirecting you to the crew member login page...\n")
                a = Assistant
                return(a.login_crew())
                s_or_p = False
            else:
                print("\nInvalid selection. Please type in [C] for crew member or [P] for passenger")


    @staticmethod
    def login_passenger():
        # count is set to 0 
        count = 0
        # only runs code when code is < 3 
        while True:

            userName = input("Please input user name: \n")
            password = input("Please input password: \n")

            count += 1
            if count == 3:
                # after 3 attempts, statement is printed
                print("Too many tries... Exiting program")
                # 3 attempts will stop the code 
                break
            else:
                
                if userName == 'ass101' and password == 'richard':
                # add break and method call to creating a booking
                    break
                else:
                    print("Incorrect username or password, try again")

    def login_crew():
        print("Work in progress..... logging in as a crew member")
        # method
        # allows crew members to print out passenger list

    # if correct details are entered, user can look for details within make_booking method

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
                print(row)
            except Exception:
                print("Invalid passenger ID,\nInput a correct Passenger ID: \n")
                continue
            else:
                print("")
# Test
# a = Assistant()
# a.staff_or_passenger()