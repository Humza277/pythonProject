# Display all short haul flights method
# Menu option 2

class FlightType:

    @staticmethod
    def short_haul_flights():
        sql_command = "SELECT cities FROM destination(table) WHERE flight_type == shorthaul"
        cursor = connection.cursor()
        rows = cursor.execute(sql_command)
        Cities = []
        for row in rows:
            Cities.append(row)

        # instantiate flight details class, call display
        dd = FlightDetails()
        dd.display_destination()

    @staticmethod
    def long_haul_flights():
        sql_command = "SELECT cities FROM destination(table) WHERE flight_type == longhaul"
        cursor = connection.cursor()
        rows = cursor.execute(sql_command)
        Cities = []
        for row in rows:
            Cities.append(row)

        # instantiate flight details class, call display
        dd = FlightDetails()
        dd.display_destination()