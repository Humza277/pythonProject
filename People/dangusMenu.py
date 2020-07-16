class DangusMenu:

        @staticmethod
        def firstMenu():
            s_or_p = True

            while s_or_p:
                try:
                    print("""
                        ==============================================
                        | Welcome to the Dangus Airline login system!|
                        ==============================================
                            """)
                    user_input = input(""
                                       "\n\nType in one of the options below"
                                       "\n----------------------------------"
                                       "\nType [C] to login as a crew member"
                                       "\nType [P] to login as a passenger"
                                       "\nType [A] to login as an airport assistant"
                                       "\nYour selection:\n")
                except Exception:
                    print("Invalid selection. Please type in [C] for crew member, [P] for passenger [A] for airport assistant\n")
                if user_input.upper() == "A":
                    print("\nDirecting you to the Airport Assistant Page")
                elif user_input.upper() == "P":
                    print("\nDirecting you to the passenger login page...\n")
                    # a = Assistant
                    # return(a.login_passenger())
                    s_or_p = False

                elif user_input.upper() == "C":
                    print("\nDirecting you to the crew member login page...\n")
                    # a = Assistant
                    # return(a.login_crew())
                    s_or_p = False
                else:
                    print("\nInvalid selection. Please type in [C] for crew member, [P] for passenger, [A] for airport assistant")

dm = DangusMenu()
dm.firstMenu()