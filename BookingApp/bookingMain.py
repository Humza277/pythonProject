from People import passenger
from People.passenger import Passenger


class Bookingapp(Passenger):
    def __init__(self, fname, lname, passportNumber, DoB):
        super().__init__(fname, lname, passportNumber, DoB)

    @classmethod
    def createUser(cls):
        return cls(
            input('First Name: '),
            input('Last Name: '),
            int(input('PassportNumber: ')),
            float(input('Date of Birth: '))
        )


user = Bookingapp
user.createUser()
