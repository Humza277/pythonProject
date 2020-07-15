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


# Importing csv
def csv_to_dataframe():
    data = pd.read_csv('cities_list.csv')
    df = pd.DataFrame(data, columns=['country', 'geonameid', 'name', 'subcountry'])
    print(df)
csv_to_dataframe()

def create_table():
    d = Databases()
    cursor = d.establish_cursor()
    cursor.execute('CREATE TABLE cities_list (Country varchar(50), Geonameid int, Name varchar(50), City varchar(50)')

# def insert_df_to_table():
#     d = Databases()
#     data = pd.read_csv('cities_list.csv')
#     df = pd.DataFrame(data, columns=['country', 'geonameid', 'name', 'subcountry'])
#     for row in df.itertuples():
#         cursor = d.establish_cursor()
#         cursor.execute("""
#                         INSERT INTO TestDB.dbo.cities_list (Country, Geonameid, Name, City)
#                         VALUES (?,?,?)
#                         """,
#                         row.country,
#                         row.geonameid,
#                         row.name,
#                         row.subcountry
#                         )
#         d.establish_cursor().commit()
#         print("Data Frame to SQL successfully exported")
# insert_df_to_table()

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