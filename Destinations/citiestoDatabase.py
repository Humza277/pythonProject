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
        pass
#
# dc = DummyCities
# dc.csv_to_dataframe()