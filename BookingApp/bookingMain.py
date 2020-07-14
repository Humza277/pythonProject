import datetime
from People import passenger
from People.passenger import Passenger


# class Resource(object):
#     class_counter = 0
#
#     def __init__(self, name, position, type, active):
#         self.name = name
#         self.position = position
#         self.type = type
#         self.active = active
#         self.id = Resource.class_counter
#         Resource.class_counter += 1


class Bookingapp(Passenger):
    booking_ID = 12345

    def __init__(self, fname, lname, passportNumber, DoB, booking_ID):
        super().__init__(fname, lname, passportNumber, DoB)
        self.booking_ID = booking_ID
        self.booking_ID = Bookingapp.booking_ID
        Bookingapp.booking_ID += 1

    @classmethod
    def createUser(cls):
        return cls(
            fname=input('First Name: '),
            lname=input('Last Name: '),
            passportNumber=int(input('PassportNumber: ')),
            DoB=input('Date of Birth in DD/MM/YYYY format: '),
            booking_ID=Bookingapp.booking_ID
        )

    # def createID(self, booking_ID):
    #     self.booking_ID = booking_ID
    #     if createUser = True

    @staticmethod
    def userStore():
        passengerB = {}
        for i in range(2):
            person = Bookingapp.createUser()
            # need to change passport number to ID
            passengerB[person.passportNumber] = person.fname, person.lname, person.passportNumber, \
                                                person.DoB, Bookingapp.booking_ID
            for k, v in passengerB.items():
                print(f"Passenger details - ID:{k} : {v}")


user = Bookingapp
# user.createUser()
user.userStore()
