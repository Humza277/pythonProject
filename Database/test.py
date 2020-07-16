from database_connections import Database

class Airport_Assistant_Staff:

    @staticmethod
    def flight_attendant_list():
        object = Database()
        # cursor runs all queries
        cursor = object.establishing_connection()  # cursor required to run queries in database
        passenger_choice = input("Please type in your choice: \n")
        if passenger_choice.capitalize() in rows:
            print("success")
        else:
            print("oh hell no")


a = Airport_Assistant_Staff()
a.flight_attendant_list()