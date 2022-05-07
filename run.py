import gspread
from google.oauth2.service_account import Credentials
import os
import platform
import random
from datetime import datetime

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('The-Boutique-Hotel')


class Customer:
    """
    Create instance of Customer
    """
    num_of_customer = 0

    def __init__(self):
        self.customer_name = None
        self.customer_address = None
        self.customer_checkin_date = None
        self.customer_checkout_date = None
        Customer.num_of_customer += 1
        self.total_customers = Customer.num_of_customer
        



def Main_menu():
    """
    Management system home page
    """
    print("\nWelcome to The Boutique Hotel\n")

    print("1. Enter/Manage Customer Data")
    print("2. Enter/Manage Room")
    print("3. Display Total Cost")
    print("4. EXIT")

def main():
    """
    Function when main menu option selected
    """
    while True:
        Main_menu()
        if (choice ==1 ):
            print("Customer")
        if (choice == 2):
            print("Room Price")
        if (choice == 3):
            print(" Total cost")
        if (choice == 4):
            quit()
        if (choice > 4):
            print("Please select a valid choice")

main()

