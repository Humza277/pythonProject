# Super class for all passengers


class Passenger:
    def __init__(self, fname, lname, passportNumber, DoB):
        self.fname = fname
        self.lname = lname
        self.passportNumber = passportNumber
        self.DoB = DoB
