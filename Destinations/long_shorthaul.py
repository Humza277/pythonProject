# from Destinations import databaseconnect
# import pandas as pd
# Display all short haul flights method
# Menu option 2

class FlightType:

    @staticmethod
    def short_haul_flights():
        print("\nShort Haul Flights unavailable. Server is down")
        # try:
        #     mb = databaseconnect.Databases()
        #     query = "SELECT cities FROM Destination WHERE flight_type = short_haul"
        #     cursor = mb.create_cursor()
        #     rows = cursor.execute(query)
        #     a = []
        #     for row in rows:
        #         a.append(row)
        #     df = pd.DataFrame()
        #     # df['Short Haul Flights']
        #     print(df)
        # except Exception:
        #     print("Server is down. Please try reconnecting")
        # else:
        #     dd = FlightDetails()
        #     dd.display_destination()


    @staticmethod
    def long_haul_flights():
        print("\nLong Haul Flights unavailable. Server is down")
        # try:
        #     mb = databaseconnect.Databases()
        #     query = "SELECT cities FROM Destination WHERE flight_type = long_haul"
        #     cursor = mb.create_cursor()
        #     rows = cursor.execute(query)
        #     a = []
        #     for row in rows:
        #         a.append(row)
        #     df = pd.DataFrame()
        #     # df['Short Haul Flights']
        #     print(df)
        # except Exception:
        #     print("Server is down. Please try reconnecting")
        # else:
        #     dd = FlightDetails()
        #     dd.display_destination()



ft = FlightType()
ft.short_haul_flights()