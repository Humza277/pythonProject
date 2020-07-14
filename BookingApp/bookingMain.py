import datetime
from People import passenger
from People.passenger import Passenger


class Bookingapp(Passenger):
    def __init__(self, fname, lname, passportNumber, DoB):
        super().__init__(fname, lname, passportNumber, DoB, booking_id):
        self.booking_id = booking_id

    @classmethod
    def createUser(cls):
        return cls(
<<<<<<< HEAD
            fname = input('First Name: '),
            lname = input('Last Name: '),
            passportNumber = (input('PassportNumber: ')),
            Dob = input('Date of Birth in DD/MM/YYYY format: ')
=======
            fname=input('First Name: '),
            lname=input('Last Name: '),
            passportNumber=int(input('PassportNumber: ')),
            DoB=input('Date of Birth in DD/MM/YYYY format: ')
>>>>>>> f86f5b4cbd6423bb6527843b13a5f8ca2f768a85
        )

    @staticmethod
    def userStore():
        passengerB = {}
        for i in range(1):
            person = Bookingapp.createUser()
            passengerB[person.lname] = person.fname, person.lname, person.passportNumber, person.DoB
            print(passengerB.items())


user = Bookingapp
# user.createUser()
user.userStore()
