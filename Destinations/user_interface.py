from Destinations.flight_scheduling import FlightDetails
from Destinations.long_shorthaul import FlightType
from People.airportAssistant import Assistant
# from BookingApp.check_booking import CheckingPassenger

class User_interaction:

        @staticmethod
        def user_interface():

            user_exit = False
            while not user_exit:
                fd1 = FlightDetails()
                fd1.menu()
                try:
                    user_input = int(input("\nYour selection: \n"))
                except Exception:
                    print("Invalid selection. Please try again.")
                if user_input == 1:
                    fd1 = FlightDetails()
                    fd1.choose_destination()
                    # user_exit = True
                elif user_input == 2:
                    dd = FlightType()
                    print(dd.short_haul_flights())
                elif user_input == 3:
                    dd = FlightType()
                    print(dd.long_haul_flights())
                elif user_input == 4:
                    print("""
                        ==============================================
                        | Welcome to the Dangus Airline login system!|
                        ==============================================
                            """)
                    a = Assistant()
                    a.staff_or_passenger()

                elif user_input == 5:
            #         print("""
            #             ==============================================
            #             | Welcome to the Dangus Airline login system!|
            #             ==============================================
            # """)
            #         print("Work in progress")
                    b = Assistant()
                    b.make_booking()
                elif user_input == 6:
                    print("To book flight")
                    fd1.choose_destination()  # call create user method from booking main
                elif user_input == 7:
                    print("""
            ==================================================
            | Thank you for visiting! I hope to see you again |
            ==================================================
            """)
                    user_exit = True
                else:
                    print("Invalid selection. Please try again.")




# # Test
# ui = User_interaction()
# ui.user_interface()

