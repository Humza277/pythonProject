import datetime
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
            float(input('Date of Birth in DD/MM/YYYY format: '))
        )

    def calculateAge(self):
        try:
            today = datetime.date.today()
        except ValueError:
            print("Incorrect Format")
        else:
            age = today - self.DoB
            return age


user = Bookingapp
user.createUser()
