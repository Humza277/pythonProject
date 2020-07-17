from Destinations.flight_scheduling import FlightDetails
from Destinations import databaseconnect
# import pandas as pd
# Display all short haul flights method
# Menu option 2

class FlightType:

    @staticmethod
    def short_haul_flights():
        # print("\nShort Haul Flights unavailable. Server is down")
        try:
            mb = databaseconnect.Databases()
            query = "SELECT * FROM Destination WHERE Flight_Type = 'Short-haul';"
            cursor = mb.create_cursor()
            rows = cursor.execute(query)
            for row in rows:
                print(row)
            # a = []
            # for row in rows:
            #     a.append(row)
            # df = pd.DataFrame()
            # # df['Short Haul Flights']
            # print(df)
        except Exception:
            print("Server is down. Please try reconnecting")
        # else:
        #     dd = FlightDetails()
        #     dd.list_all_destinations()


    @staticmethod
    def long_haul_flights():

        try:
            mb = databaseconnect.Databases()
            query = "SELECT * FROM Destination WHERE Flight_Type = 'Long-haul';"
            cursor = mb.create_cursor()
            rows = cursor.execute(query)
            for row in rows:
                print(row)
            # a = []
            # for row in rows:
            #     a.append(row)
            # df = pd.DataFrame()
            # df['Short Haul Flights']
            # print(df)
        except Exception:
            print("Server is down. Please try reconnecting")
        # else:
        #     dd = FlightDetails()
        #     dd.list_all_destinations()



# ft = FlightType()
# ft.short_haul_flights()
# ft.long_haul_flights()