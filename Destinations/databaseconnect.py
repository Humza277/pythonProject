import pyodbc
import os
import secretfile
import sys

class Databases:
    server = secretfile.server
    database = secretfile.database
    username = secretfile.username
    password = secretfile.password

    def __init__(self):


        try:
            self.connections = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.server +
                                              ';DATABASE=' + self.database + ';UID=' + self.username +
                                              ';PWD=' + self.password)
            print("""
                    ==========================================================
                    | Connection Established! Welcome to the Dangus Database |
                    ==========================================================
            """)
            # self.cursor = self.connections.cursor()
        except Exception:
            print("Did not connect")

    def create_cursor(self):
        self.cursor = self.connections.cursor()
        return self.cursor
    print("Cursor established")

    # def use_database(self):
    #     self.create_cursor()
    #     self.cursor.execute("USE dangus_db")


# test
d = Databases()
d.create_cursor()




