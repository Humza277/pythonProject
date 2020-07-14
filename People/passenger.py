# Super class for all passengers

class Passenger:
    def __init__(self, fname, lname, passportNumber, age):
        self.fname = fname
        self.lname = lname
        self.passportNumber = passportNumber
        self.age = age
