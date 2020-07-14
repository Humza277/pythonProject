import pyodbc
import pandas as pd
import os

# Importing csv
data = pd.read_csv('cities_list.csv')
df = pd.DataFrame(data, columns=['country','geonameid','name','subcountry'])

print(df)

# connecting to SQL server
server = os.environ.get('db_server')
database = os.environ.get('dangus_db')
username = os.environ.get('db_username')
password = os.environ.get('db_password')

cnxn = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password
connection = pyodbc.connect(cnxn, timeout=5)

# creating a table
cursor.execute('CREATE TABLE cities_list (Country varchar(50), Geonameid int, Name varchar(50), City varchar(50)')

# inserting dataframe to table
for row in df.itertuples():
    cursor.execute('''
                INSERT INTO TestDB.dbo.cities_list (Country, Geoname, Name, City)
                VALUES (?,?,?)
                ''',
                row.Country,
                row.Geoname,
                row.Name,
                row.City
                )
conn.commit()

# Perform a test on azure data studio using dangus_db database