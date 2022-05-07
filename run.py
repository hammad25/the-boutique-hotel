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

    def Set_customer_date(self):
        self.customer_name = input("Enter Customer Name=")
        self.customer_address = input("Enter Customer Address=")
        self.customer_checkin_date = input("Enter Customer CheckInDate=")
        self.customer_checkout_date = input("Enter Customer CheckOutDate=")

    def Total_num_of_customers(self):
        """
        Method to print total number of customers
        """
        print("Total Number Of Customers= "+str(self.total_customers))
    
    def Get_customer_data(self):
        print("Customer Name="+self.customer_name)
        print("Customer Address="+self.customer_address)
        print("Customer CheckInDate="+self.customer_checkin_date)
        print("Customer CheckOutDate="+self.customer_checkout_date)

def Main_menu():
    """
    Management system home page
    """
    print("\nWelcome to The Boutique Hotel\n")

    print("1. Enter/Manage Customer Data")
    print("2. Enter/Manage Room")
    print("3. Display Total Cost")
    print("4. EXIT")

def Sub_customer_menu():
    print("1. Enter a Customer Data")
    print("2. Display Customer Data")
    print("3. Back to main menu")


def main():
    """
    Function when main menu option selected
    """
    while True:
        Main_menu()
        try:
            choice = input("Enter your choice = ")
        except ValueError():
            print("Please Enter a number")
        else:
            os.system("cls")
            if (choice == 1 ):
                Sub_customer_menu()
                try:
                    subMenu =. input("Enter your choice = ")
                except ValueError():
                    print("Please Enter a number")
                else:
                    if (subMenu == 1):
                        CustomerObj = Customer()
                        CustomerObj.Set_customer_date()
                    elif (SubMenu == 2 ):
                        try:
                            CustomerObj.Get_customer_data()
                        except:
                            input("Customer Didn't exist yet!")
                            os.system("cls")
                            Sub_customer_menu()
                    elif(subMenu==3):
                        os.system("cls")
                        Main_menu()
                    else:
                        print("Please select a valid choice")
        if (choice == 2):
            print("Room Price")
        if (choice == 3):
            print(" Total cost")
        if (choice == 4):
            quit()
        if (choice > 4):
            print("Please select a valid choice")

main()

