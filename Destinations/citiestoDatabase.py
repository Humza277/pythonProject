import pyodbc
import pandas as pd
import os
from Destinations.databaseconnect import Databases

"""
CSV files to import 
List of destinations (dangus airline)
List of short haul flights (SELECT cities where flight type = short haul)
List of long haul flights (SELECT cities where flight type = long haul)
List of cheapest flights (import from destinations.py, import flight budget method)
Databases to display = list of cities
Passenger details (passengerlist.csv)

"""
# d = Databases()

class DummyCities(Databases):

    # Importing csv
    def csv_to_dataframe():
        data = pd.read_csv('mock_cities.csv')
        df = pd.DataFrame(data, columns=['country', 'city', 'country_code'])
        print(df)

#
# dc = DummyCities
# dc.csv_to_dataframe()