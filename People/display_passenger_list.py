import pandas as pd

def csv_to_dataframe():
    data = pd.read_csv('passenger_details.csv')
    df = pd.DataFrame(data, columns=['First Name', 'Last Name', 'Passport Number', 'Date of Birth', 'Booking_ID'])
    print(df)
csv_to_dataframe()

