import pyodbc
# Creating a class with singular method
class Database:
    server = 'databases2.spartaglobal.academy'  #
    database = ''
    username = 'SA'
    password = 'Passw0rd2018'

    # when this method, cursor is returned
    def establishing_connection(self):
        connections = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+ self.password
        #
        try:
            with pyodbc.connect(connections, timeout=5) as connection:
                print("Connection did not time out")
        except:
            print("Connection Time out")


    def create_cursor(self):
        cursor = self.connections.cursor()  # variable set to cursor
        print("cursor has been established")
        return cursor  # return the value of allocated position of the cursor


