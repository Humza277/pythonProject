from database_connections import *
from BookingApp import bookingMain
import panda as pd

# database_OOP parent class
class Airport_queries:
    # static method in python, static includes the whole method. self is part of the instance,
    # methods are at a class level once static methods assigned
    # no static variables but are class variables, doesn't remember it's state level
    def All_products(self):
        object = Database()  # object of Database_OOP class
        # cursor runs all queries
        cursor = object.establishing_connection()  # cursor required to run queries in databse
        query_result = f"insert into user_name(First_Name,Last_Name) values ('pyodbc', 'awesome library')"
        rows = cursor.execute(query_result)
        for row in rows:
            print(row)

        cursor.execute()
        cnxn.commit()