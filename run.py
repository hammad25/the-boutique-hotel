# -*- coding: utf-8 -*-
import os
import platform
import random
import re
from datetime import datetime

import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("The-Boutique-Hotel")

regex = re.compile("[@_!#$%^&*()<>?/\|}{~:]")


def main_menu():
    """
    Function to display booking systems main menu
    """
    print("\n WELCOME TO THE BOUTIQUE HOTEL \n")

    print("1. Enter/Manage Booking")
    print("2. Display Booking Data")
    print("3. EXIT")


def sub_booking_menu():
    """
    Function to display booking options when choose 1 in main_menu()
    """
    print("1. Enter a Booking")
    print("2. Display Booking")
    print("3. Back to main menu")


def sub_booking_display_menu():
    """
    Function to display booking options when choose 2 in main_menu()
    """
    print("1. Display all Booking Data")
    print("2. Display Booking Data by Booking ID")
    print("3. Back to main menu")


def clear_screen():
    """
    Function to clear screen in Windows or Mac operating system
    """
    if platform.system() == "Windows":
        os.system("cls")
    elif "Linux" or "Darwin" in platform.system():
        os.system("clear")
    else:
        print("*/ PLATFORM NOT SUPPORTED /*")


class Customer:
    """
    Create instance of Customer
    """

    num_of_customers = 0

    def __init__(self):
        self.customer_id = random.sample(range(1, 10000), 1)
        self.customer_name = None
        self.customer_age = None
        self.customer_telephone = None
        self.customer_checkin_date = datetime.today().strftime("%d/%m/%Y")
        self.customer_checkout_date = datetime.today().strftime("%d/%m/%Y")
        Customer.num_of_customers += 1
        self.total_customers = Customer.num_of_customers
        self.room_type = None
        self.num_of_guests = 0
        self.num_of_nights = 0
        self.total_price = 0
        self.standard_room_price = 200
        self.deluxe_room_price = 400

    def set_customer_name(self):
        """
        Function to set the name of the name
        """
        while True:
            self.customer_name = input("Enter Customer Name = \n")
            if self.customer_name.isalpha():
                break
            if (
                self.customer_name.isdigit() or
                regex.search(self.customer_name) is not None
            ):
                print("Error: Please enter alphabetic characters only")

    def set_customer_telephone(self):
        """
        Function to set the telephone of the user
        """
        while True:
            self.customer_telephone = input("Enter Customer Telephone = \n")
            try:
                if (
                    len(self.customer_telephone) == 11 and
                    self.customer_telephone.isnumeric()
                ):
                    break
                print("Error: please enter a 11 digit number")
            except ValueError():
                print("please enter a number")

    def set_customer_data(self, update=False):
        """
        Function to enter customer data in a While loop with validations
        until valid data is entered otherwise raise error
        """
        self.set_customer_name()

        self.set_customer_telephone()

        while True:
            self.customer_age = input(
                "Enter Customer Age (day/month/year) = \n"
            )
            try:
                self.customer_age = datetime.strptime(
                    self.customer_age, "%d/%m/%Y"
                ).strftime("%d/%m/%Y")
                break
            except ValueError:
                print("Error: must be format dd/mm/yyyy ")
        while True:
            self.customer_checkin_date = input(
                "Enter Customer CheckInDate (day/month/year) = \n"
            )
            try:
                self.customer_checkin_date = datetime.strptime(
                    self.customer_checkin_date, "%d/%m/%Y"
                ).strftime("%d/%m/%Y")
                break
            except ValueError:
                print("Error: must be format dd/mm/yyyy ")
        while True:
            self.customer_checkout_date = input(
                "Enter Customer CheckOutDate  (day/month/year) = \n"
            )
            try:
                self.customer_checkout_date = datetime.strptime(
                    self.customer_checkout_date, "%d/%m/%Y"
                ).strftime("%d/%m/%Y")

                break
            except ValueError:
                print("Error: must be format dd/mm/yyyy ")
        self.num_of_nights = (
            datetime.strptime(self.customer_checkout_date, "%d/%m/%Y").date() -
            datetime.strptime(self.customer_checkin_date, "%d/%m/%Y").date()
        )
        self.num_of_nights = self.num_of_nights.days
        while True:
            print(
                " Standard Room Price --> £200 AND Deluxe Room Price --> £400"
            )
            try:
                choice = int(
                    input(
                        "Select Room Type (Enter 1 for Standard or 2 for"
                        " Deluxe) = \n"
                    )
                )
                if choice == 1:
                    self.room_type = "standard"
                    break
                if choice == 2:
                    self.room_type = "deluxe"
                    break
                print("\n Error: please choice valid option!")
            except ValueError:
                print("Error: Please enter a number!")
        while True:
            try:
                self.num_of_guests = int(
                    input("Enter Number of Guests (1-3) = \n")
                )
                if self.num_of_guests >= 1 and self.num_of_guests <= 3:
                    break
                print("Guests must be between 1 to 3")
            except ValueError:
                print("Error: Please enter a number!")
        if update is False:
            input("Press any key to continue... \n")
            clear_screen()

    def total_num_of_customers(self):
        """
        Method to print total number of customers
        """
        print("Total Number Of Customers= " + str(self.total_customers))

    def calculations(self):
        """
        Function to calculate room price
        """
        if self.room_type == "standard":
            self.total_price = (
                int(self.num_of_nights) *
                self.standard_room_price *
                self.num_of_guests
            )
        elif self.room_type == "deluxe":
            self.total_price = (
                int(self.num_of_nights) *
                self.deluxe_room_price *
                self.num_of_guests
            )
        self.total_price = self.total_price
        return self.total_price

    def get_customer_data(self):
        """
        Function to display customer data
        """
        print("\n************************\n")
        print("Customer ID =        " + str(self.customer_id[0]))
        print("Customer Name =      " + self.customer_name)
        print("Customer Age =       " + str(self.customer_age))
        print("Customer telephone = " + self.customer_telephone)
        print("Room Type =          " + self.room_type)
        print("Customer Check-in=   " + str(self.customer_checkin_date))
        print("Customer Check-out=  " + str(self.customer_checkout_date))
        print("Total Price =        " + str(self.calculations()) + "£")
        print("\n************************\n")

    def make_booking_list(self):
        """
        Function to store data in spreadsheet
        """
        data = []
        data.append(self.customer_id[0])
        data.append(self.customer_name)
        data.append(self.customer_age)
        data.append(self.customer_telephone)
        data.append(str(self.customer_checkin_date))
        data.append(str(self.customer_checkout_date))
        data.append(self.room_type)
        if self.room_type == "standard":
            data.append(self.standard_room_price)
        elif self.room_type == "deluxe":
            data.append(self.deluxe_room_price)
        data.append(self.num_of_guests)
        data.append(self.num_of_nights)
        data.append(self.calculations())

        return data

    def get_customer_id(self):
        """
        Function to retrieve customer ID
        """
        return self.customer_id[0]


COUNT = 0


def main():
    """
    function for main menu to navigate and run menu and sub menu using
    validations
    """

    customer_list = []
    not_valid = False

    while True:
        if not_valid is False:
            main_menu()
        try:
            choice = int(input("Enter your choice: \n"))
        except ValueError:
            print("Error: Please enter a number")
        else:
            clear_screen()
            display_menus(customer_list, choice)


def display_menus(customer_list, choice):
    """
    Function to navigate the main menu and sub menus
    """
    while True:
        if choice == 1:
            not_valid = False
            sub_booking_menu()
            try:
                sub_menu = int(input("Enter your choice = \n"))
            except ValueError:
                print("Error: Please enter a valid number")
            else:
                if sub_menu == 1:
                    customer_list.append(Customer())
                    global COUNT
                    customer_list[COUNT].set_customer_data()
                    create_booking_worksheet(
                        customer_list[COUNT].make_booking_list()
                    )
                    COUNT = COUNT + 1

                elif sub_menu == 2:
                    not_valid = False
                    try:
                        if len(customer_list) != 0:
                            for i in range(0, len(customer_list)):
                                customer_list[i].get_customer_data()
                                input("Press any key to continue...")
                                clear_screen()
                        else:
                            raise Exception(
                                "Customer does not exist yet!"
                            )
                    except:
                        input("Customer does not exist yet!")
                        clear_screen()
                        sub_booking_menu()
                        clear_screen()

                elif sub_menu == 3:
                    not_valid = False
                    clear_screen()
                    break
                else:
                    print("Error: Please select a valid number")
        if choice == 2:
            not_valid = False
            clear_screen()
            sub_booking_display_menu()
            try:
                sub_menu = int(input("Enter your choice = \n"))
            except ValueError:
                print("Error: Please enter a valid number")
            else:
                if sub_menu == 1:
                    display_all_bookings()
                elif sub_menu == 2:
                    display_booking_by_id()
                    break
                elif sub_menu == 3:
                    clear_screen()
                    break
                elif sub_menu > 3:
                    input(
                        "Error: Please Enter a valid choice \nPress"
                        " enter to continue..."
                    )
                    clear_screen()
                    sub_booking_display_menu()

        if choice == 3:
            not_valid = False
            quit()
        if choice == 0 or choice > 3:
            not_valid = True
            clear_screen()
            main_menu()
            input(
                "Error: Please Enter a valid choice \n"
                "Press enter to continue..."
            )
            clear_screen()
            main_menu()
            break


def create_booking_worksheet(data):
    """
    Function to create and append booking into spreadsheet
    """
    print(" Updating bookings worksheet.....")
    bookings_worksheet = SHEET.worksheet("bookings")
    bookings_worksheet.append_row(data)
    print("\n Bookings worksheet updated successfully \n")


def display_customer_data(item):
    """
    Function to display customer booking data
    """
    print("\n************************\n")
    print("Customer ID =        " + item[0])
    print("Customer Name =      " + item[1])
    print("Customer DOB =       " + item[2])
    print("Customer telephone = " + item[3])
    print("Customer Check-in=   " + item[4])
    print("Customer Check-out=  " + item[5])
    print("Room Type =          " + item[6])
    print("Room per night =     " + item[7])
    print("No. of guests =      " + item[8])
    print("Total nights =       " + item[9])
    print("Total Price =        " + "£" + item[10])
    print("\n************************\n")


def display_all_bookings():
    """
    Function to display all created
    bookings within the spreadsheet to the terminal
    """
    bookings_worksheet_data = SHEET.worksheet("bookings")
    bookings_worksheet_data = bookings_worksheet_data.get_all_values()
    bookings_worksheet_data = bookings_worksheet_data[1:]

    for item in bookings_worksheet_data:
        display_customer_data(item)

    input("\nPress any key to continue...\n")


def display_booking_by_id():
    """
    Function to get and display a certain booking using a booking ID number
    """
    bookings_worksheet_data = SHEET.worksheet("bookings")
    bookings_worksheet_data = bookings_worksheet_data.get_all_values()
    bookings_worksheet_data = bookings_worksheet_data[1:]

    i_d = input("Enter an Id = \n")
    for item in bookings_worksheet_data:
        if i_d == item[0]:
            display_customer_data(item)
            break
    else:
        input(
            "Error:Customer does not exist with this ID \n"
            "Press enter to try again..."
        )
        display_booking_by_id()


if __name__ == '__main__':
    main()
