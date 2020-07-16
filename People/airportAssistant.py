# Creates class Assistant to enter for flight_attendant list 
class Assistant:
    # username and passwords are stored within data as attributes
    @staticmethod
    def staff_or_passenger():
        user_exit = False

        while not user_exit:
            try:
                user_input = input("\nAre you a crew member or a passenger?\n\nType [C] to login as a crew member\nType [P] to login as a passenger\nYour selection:\n")
            except Exception:
                print("Invalid selection. Please type in [C] for crew member or [P] for passenger\n")
            if user_input.upper() == "P":
                print("\nDirecting you to the passenger login...\n")
                a = Assistant
                return(a.login_passenger())
                user_exit = True

            elif user_input.upper() == "C":
                print("\nDirecting you to the crew member login page...\n")
                a = Assistant
                return(a.login_crew())
                user_exit = True
            else:
                print("Invalid choice")

    # test




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

    # if correct details are entered, user can look for details within make_booking method
    def make_booking():
        pass

# Test
a = Assistant()
a.staff_or_passenger()