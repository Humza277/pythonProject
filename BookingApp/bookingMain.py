import datetime
from People import passenger
from People.passenger import Passenger


class Bookingapp(Passenger):
    def __init__(self, fname, lname, passportNumber, DoB):
        super().__init__(fname, lname, passportNumber, DoB)

    @classmethod
    def createUser(cls):
        return cls(
            fname=input('First Name: '),
            lname=input('Last Name: '),
            passportNumber=int(input('PassportNumber: ')),
            DoB=input('Date of Birth in DD/MM/YYYY format: ')
        )

    @staticmethod
    def userStore():
        passengerB = {}
        for i in range(1):
            person = Bookingapp.createUser()
            passengerB[person.lname] = person
            print(passengerB.items())


user = Bookingapp
user.createUser()
