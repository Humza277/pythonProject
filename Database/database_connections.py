import pyodbc

class database_OOP:
    # passing connection parameters
    def __init__(self,server,database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
   # establishing connection
    def establish_connection(self):
        connectionString = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.server + ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password
        try:
            with pyodbc.connect(connectionString, timeout=5) as connection:
                print("Connection did not time out")
        except:
            print("Connection Timed Out")
        else:
            return connection # connection obj created and returned
    # creating cursor
    def create_cursor(self, connection):
        return connection.cursor()

