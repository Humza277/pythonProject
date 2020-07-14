import datetime
import csv
from People.passenger import Passenger


class Bookingapp(Passenger):
    booking_ID = 12345

    def __init__(self, fname, lname, passportNumber, DoB, booking_ID):
        super().__init__(fname, lname, passportNumber, DoB)
        self.booking_ID = booking_ID
        self.booking_ID = Bookingapp.booking_ID

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
        csv_columns =["First name", "Last Name", "Passport Number", "Date of Birth", "ID"]
        for i in range(2):
            person = Bookingapp.createUser()
            Bookingapp.booking_ID += 1
            # need to change passport number to ID
            passengerB[Bookingapp.booking_ID] = person.fname, person.lname, person.passportNumber, \
                                                person.DoB, Bookingapp.booking_ID
            for k, v in passengerB.items():
                print(f"Passenger details - ID:{k} : {v}")

        with open("passengerlist.csv", "w+") as passdata:
            for key in passengerB.keys():
                passdata.write("%s,%s\n"%(key, passengerB[key]))

        # with open("passengerlist.csv", "w+") as passdata:
        #     writer = csv.DictWriter(passdata, fieldnames=csv_columns)
        #     writer.writeheader()
        #     for data in passengerB:
        #         writer.writerow(data)


# file.write()
# print("Passenger file has been created")
# CSV = "\n".join(str([k + ',' + ','.join(v) for k, v in passengerB.items()]))

user = Bookingapp
# user.createUser()
user.userStore()
