import pyodbc
# Creating a class with singular method
class Database:
    def __init__(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password

    # when this method, cursor is returned
    def establishing_connection(self):
        connections = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+ self.password
        #
        try:
            with pyodbc.connect(connections, timeout=5) as connection:
                print("Connection did not time out")
        except:
            print("Connection Time out")
        else:
            cursor = connection.cursor() # variable set to cursor
            return cursor # return the value of allocated position of the cursor