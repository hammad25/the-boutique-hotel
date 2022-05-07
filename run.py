import gspread
from google.oauth2.service_account import Credentials
import os
import platform
import random
from datetime import datetime
import sys

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
    num_of_customers = 0

    def __init__(self):
        self.customer_name = None
        self.customer_address = None
        self.customer_checkin_date = None
        self.customer_checkout_date = None
        Customer.num_of_customers += 1
        self.total_customers = Customer.num_of_customers

    def Set_customer_date(self):
        self.customer_name = input("Enter Customer Name=")
        self.customer_address = input("Enter Customer Address=")
        while True :
                checkin_date = input("Enter Customer CheckInDate (%d/%m/%Y) =")
            try:
                self.customer_checkin_date = datetime.datetime.strptime(checkin_date, "%d/%m/%Y")
                break
            except ValueError:
                print("Error: must be format dd/mm/yyyy ")
        while True :
            checkout_date = input("Enter Customer CheckOutDate  (%d/%m/%Y) =")
            try:
                self.customer_checkout_date = datetime.datetime.strptime(checkout_date, "%d/%m/%Y")
                break
            except ValueError:
                print("Error: must be format dd/mm/yyyy ")


        input("Press any key to continue...")
        os.system("cls")


    def Total_num_of_customers(self):
        """
        Method to print total number of customers
        """
        print("Total Number Of Customers= "+str(self.total_customers))

    def Get_customer_date(self):
        print("Customer Name="+self.customer_name)
        print("Customer Address="+self.customer_address)
        print("Customer CheckInDate="+self.customer_checkin_date)
        print("Customer CheckOutDate="+self.customer_checkout_date)
        input("Press any key to continue...")
        os.system("cls")

def Main_menu():
    print("1. Enter/Display Customer Data")
    print("2. Enter/Display Room Price")
    print("3. Enter/Display Restaurant Bill")
    print("4. Enter/Display Laundry Bill")
    print("5. Enter/Display Spa Bill")
    print("6. Display Total Cost")
    print("7. EXIT")

def Sub_customer_menu():
    print("1. Enter a Customer Data")
    print("2. Display Customer Data")
    print("3. Back to main menu")

def main():
    """
    fuction for main menu
    """
    while True:
        Main_menu()
        try:
            choice = int(input("Enter your choice:"))
        except ValueError:
            print("Please enter a number")
        else:
            os.system("cls")
            while True:
                if (choice == 1):
                    Sub_customer_menu()
                    try:
                        subMenu=int(input(("Enter your choice =")))
                    except ValueError:
                        print("Please enter a number")
                    else:
                        if(subMenu==1):
                            CustomerObj=Customer()
                            CustomerObj.Set_customer_date()
                        elif(subMenu==2):
                            try:
                                CustomerObj.Get_customer_date()
                            except:
                                input("Customer Didn't exist yet!")
                                os.system("cls")
                                Sub_customer_menu()
                                os.system("cls")
                        elif(subMenu==3):
                            os.system("cls")
                            # Main_menu()
                            break
                        else:
                            print("Please select a valid choice")
            if (choice == 2):
                print("Room Price")
            if (choice == 3):
                print(" Restutant bill")
            if (choice == 4):
                print(" Laundry bill")
            if (choice == 5):
                print(" Spa bill")
            if (choice == 6):
                print(" Total cost")
            if (choice == 7):
                quit()
            if (choice > 7):
                print("Please select a valid choice")

main()