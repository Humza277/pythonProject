import pyodbc
from Database.database_connections import *


class Airport_Assistant_Staff:

    @staticmethod
    def flight_attendant_list():
        object = Database()
        # cursor runs all queries
        cursor = object.establishing_connection()  # cursor required to run queries in database
        # location = input("Where are you flying to?")
        query_result = "SELECT Flight_ID, Destination_ID, PassengersID FROM Airplane"
        rows = cursor.execute(query_result)
        for row in rows:
            print(row)

a = Airport_Assistant_Staff()
a.flight_attendant_list()