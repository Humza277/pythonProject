# open source module to implement Open Data Base Connectivity
import pyodbc
# Creating a class with singular method


class Database:
    # Database information is stored 
    server = 'databases2.spartaglobal.academy'  
    database = 'dangus_db'
    username = 'SA'
    password = 'Passw0rd2018'

    # when this method, cursor is returned
    def establishing_connection(self):
        connections = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+ self.password
        # tries to connect to server
        try:
            # If there is connectivity within 5 seconds, "Connection did not time out" is printed 
            with pyodbc.connect(connections, timeout=10) as connection:
                print("Connection did not time out")
        # otherwise the error is raised, thus printing "Conection Time out
        except:
            print("Connection Time out")
        self.connection = connection
        return self.connection

    # method to create cursor 
    def create_cursor(self):
        cursor = self.connection.cursor()  # variable set to cursor
        print("cursor has been established")
        return cursor  # return the value of allocated position of the cursor


    # use the dangus_db database
    def use_database(self):
        self.establishing_connection()
        self.create_cursor()
        d = Database()
        d.create_cursor().execute("use dangus_db")
        print("Connection to dangus_db database successful")

# Test
d = Database()
d.establishing_connection()
# d.use_database()