import Database.database_connections


class Airport_Assistant_Staff:

    @staticmethod
    def flight_attendant_list():
        object = Database()
        # cursor runs all queries
        cursor = object.establishing_connection()  # cursor required to run queries in database
        location = input("Where are you flying to?")
        query_result = f"SELECT First_Name, Last_Name, Passport_Number FROM Passenger WHERE Destination {location} "
        rows = cursor.execute(query_result)
        for row in rows:
            print(row)

a = Airport_Assistant_Staff()
a.flight_attendant_list()