
class Assistant:
    userName = "ass101"
    password = "richard"
    def login(self):
        count = 0
        while True:
            userName = input("Please input user name")
            password = input("Please input password")
            count += 1
            if count == 3:
                print("Too many tries... Exiting program")
                break
            else:
                if userName == 'ass101' and password == 'richard':
                # add break and method call to creating a booking
                    break
                else:
                    print("Incorrect username or password, try again")



    def make_booking