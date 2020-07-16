import pyodbc
import pandas as pd
import os
from Destinations.databaseconnect import Databases


class DummyCities(Databases):

    # Importing csv
    def csv_to_dataframe():
        data = pd.read_csv('mock_cities.csv')
        df = pd.DataFrame(data, columns=['country', 'city', 'country_code'])
        print(df)


    def checking_city_exists():
        data = pd.read_csv('mock_cities.csv')
        df = pd.DataFrame(data, columns=['country', 'city', 'country_code'])
        while True:
            user_input = input("\nSelect your destination:\n")
            if df['city'].str.contains(user_input).any():
                print(f"Yay we fly to {user_input}")
                break
            else:
                print(f"Sorry we don't fly to {user_input} yet")






#Test
dc = DummyCities
# dc.csv_to_dataframe()
dc.checking_city_exists()