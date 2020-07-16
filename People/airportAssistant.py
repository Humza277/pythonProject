# Creates class Assistant to enter for flight_attendant list 
class Assistant:
    # username and passwords are stored within data as attributes
    userName = "assistant1"
    password = "wolo101"
    def login(self):
        # count is set to 0 
        count = 0
        # only runs code when code is < 3 
        while True:
<<<<<<< HEAD
            # asks for username 
            userName = input("Please input user name")
            # asks for password
            password = input("Please input password")
            # after each failed iteration, count is increased by one 
=======
            userName = input("Please input user name: \n")
            password = input("Please input password: \n")
>>>>>>> 05d98bc1ad383a09a561a861859b60f3d657c542
            count += 1
            if count == 3:
                # after 3 attempts, statement is printed
                print("Too many tries... Exiting program")
                # 3 attempts will stop the code 
                break
            else:
                
                if userName == 'assistant1' and password == 'wolo101':
                # add break and method call to creating a booking
                    break
                else:
                    print("Incorrect username or password, try again")

<<<<<<< HEAD
    # if correct details are entered, user can look for details within make_booking method
    def make_booking
=======


    def make_booking():
        pass
>>>>>>> 05d98bc1ad383a09a561a861859b60f3d657c542
