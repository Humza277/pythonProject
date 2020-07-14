from database_connections import *
from BookingApp import bookingMain


# database_OOP parent class
class Airport_queries:

    def All_products(self):
        booking = Bookingapp.createUser()
        object = Database()  # object of Database_OOP class
        # cursor runs all queries
        cursor = object.establishing_connection()  # cursor required to run queries in databse
        query_result = f"insert into user_name(First_Name,Last_Name,Passport_Number,Date_of_Birth) values " \
                       f"({fname}, {lname},{passportNumber},{Dob})"
        rows = cursor.execute(query_result)
        for row in rows:
            print(row)
