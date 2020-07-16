# Creates class Assistant to enter for flight_attendant list 
class Assistant:
    # username and passwords are stored within data as attributes
    userName = 'bob'
    passWord = 123
    def login(self):
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
                
                if userName == 'bob' and password == 123:
                # add break and method call to creating a booking
                    break
                else:
                    print("Incorrect username or password, try again")


    # if correct details are entered, user can look for details within make_booking method
    def make_booking():
        pass



