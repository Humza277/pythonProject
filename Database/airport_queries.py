from database_connections import *
# from BookingApp.bookingMain import *
import pandas as pd

# database_OOP parent class
def passenger_info(self):
    self.passenger_data = pd.read_csv(r'C:\Users\marcu\PycharmProjects\pythonProject\BookingApp.csv')
    df = pd.DataFrame(data, columns=['First_Name', 'Last_Name', 'Passport_Number', 'Date_of_Birth'])
    print(df)
    
# class Airport_queries(bookingMain, passenger_data):
#     def __init__(self, passenger_data):
#         self.passenger_data = passenger_data



    # def All_products(self):
    #     object = Bookingapp.createUser()  # object of Database_OOP class
    #     # cursor runs all queries
    #     cursor = object.establishing_connection()  # cursor required to run queries in databse
    #     # code
    #     query_result = f"insert into user_name(First_Name,Last_Name,Passport_Number,Date_of_Birth) values " \
    #                    f"({fname}, {lname},{passportNumber},{Dob})"
    #     rows = cursor.execute(query_result)
    #     for row in rows:
    #         print(row)
