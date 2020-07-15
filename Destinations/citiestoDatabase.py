import pyodbc
import pandas as pd
import os
import Destinations.databaseconnect

"""
CSV files to import 
List of destinations (dangus airline)
List of short haul flights
List of long haul flights
List of cheapest flights (import from destinations.py, import flight budget method)

Passenger details (passengerlist.csv)

"""

# Importing csv
data = pd.read_csv('cities_list.csv')
df = pd.DataFrame(data, columns=['country','geonameid','name','subcountry'])

print(df)

# # creating a table
# cursor.execute('CREATE TABLE cities_list (Country varchar(50), Geonameid int, Name varchar(50), City varchar(50)')
#
# # inserting dataframe to table
# for row in df.itertuples():
#     cursor.execute('''
#                 INSERT INTO TestDB.dbo.cities_list (Country, Geoname, Name, City)
#                 VALUES (?,?,?)
#                 ''',
#                 row.Country,
#                 row.Geoname,
#                 row.Name,
#                 row.City
#                 )
# conn.commit()

# Perform a test on azure data studio using dangus_db database