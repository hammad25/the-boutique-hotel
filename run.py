import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('The-Boutique-Hotel')


def Main_menu():
    """
    Management system home page
    """
    print("\nWelcome to The Boutique Hotel\n")

    print("1. Enter/Manage Customer Data")
    print("2. Enter/Manage Room Price")
    print("3. Display Total Cost")
    print("4. EXIT")






def main():
    """
    Create a new booking 
    """
    Main_menu()
    


main()