import numpy as np
import pandas as pd
from database_connections import *
from BookingApp.bookingMain import *


# database_OOP parent class
class Airport_queries:
    def __init__(self):
        pass

    def passenger_info(self):
        object = Bookingapp.userStore()  # object of Database_OOP class
        # cursor runs all queries
        cursor = object.establishing_connection()  # cursor required to run queries in databse
        # code
        query_result = f"insert into user_name(First_Name,Last_Name,Passport_Number,Date_of_Birth) values " \
                       f"({fname}, {lname},{passportNumber},{Dob})"
        rows = cursor.execute(query_result)
        for row in rows:
            print(row)

    def send_to_database(self):
        df = pd.read_csv('passengerlist.csv')
        first_column = df.columns[0]
        df = df.drop([first_column], axis=1)
        df.to_csv('passengerdatabaselist.csv', index=False)

        data = pd.read_csv('passengerdatabaselist.csv')
        pdl = pd.DataFrame(data, columns=['First_Name', 'Last_Name', 'Passport_Number', 'Date_of_Birth', 'Passenger_ID'])

        # d = Database()
        # cursor = d.create_cursor()
        # for row in pdl.intertuples():
        #     cursor.execute('''
        #     INSERT INTO dangus_db.dbo.Passenger (Passenger_ID, First_Name, Last_Name, Date_of_Birth, Passport_Number)
        #     VALUES (?,?,?,?,?)
        #     ''',
        #                    row.Passenger_ID,
        #                    row.First_Name,
        #                    row.Last_Name,
        #                    row.Date_of_Birth,
        #                    row.Passport_Number,
        #                    )
        # d.connections.commit()

        # filename = "passengerlist.csv"
        # opening the file with w+ mode truncates the file
        # f = open(filename, "a+") # opening the file with w+ mode truncates the file
        # f.close()
        # data = pd.read_csv('passengerlist.csv')
        # df = pd.DataFrame(data, columns=['Passenger_ID', 'First_Name',
        #                                  'Last_Name', ' Date_Of_Birth', 'Passport_Number'])
        #
        # pass


u = Airport_queries()
u.send_to_database()
