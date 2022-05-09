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

def Main_menu():
    """
    Function to display booking systems main menu
    """
    print("1. Enter/Manage Booking")
    print("2. Display Booking Data")
    print("3. EXIT")

def Sub_booking_menu():
    """
    Function to display booking options when choose 1 in Main_menu()
    """
    print(" Standard Room Price --> £200 AND Deluxe Room Price --> £400")
    print("1. Enter a Booking")
    print("2. Display Booking")
    print("3. Delete Booking")
    print("4. Update Booking")
    print("5. Back to main menu")

def Sub_booking_Display_menu():
    """
    Function to display booking options when choose 2 in Main_menu()
    """
    print("1. Display all Booking Data")
    print("2. Display Booking Data by BookingID")
    print("3. Back to main menu")

def clearScreen():
    """
    Function to clear screen in Windows or Mac operating system
    """
    if platform.system()=="Windows":
        os.system("cls")
    elif platform.system()=="Linux" or "Darwin":
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
        self.customer_checkin_date = datetime.today().strftime('%d/%m/%Y')
        self.customer_checkout_date = datetime.today().strftime('%d/%m/%Y')
        Customer.num_of_customers += 1
        self.total_customers = Customer.num_of_customers
        self.RoomType=None
        self.NumOfGuests=0
        self.NumOfNight=0
        self.TotalPrice=0

    def Set_customer_data(self,update=False):
        """
        Function to enter customer data
        """

        self.customer_name = input("Enter Customer Name=")
        
        while True:
            self.customer_telephone = (input("Enter Customer Telephone="))
            try:
                if(len(self.customer_telephone) == 11 and self.customer_telephone.isnumeric()):
                    break
                else:
                    print("please enter a 11 digit number")
            except ValueError():
                print("please enter a number")

        while True :
            self.customer_age  = input("Enter Customer Age (day/month/year) =")
            try:
                self.customer_age = datetime.strptime(self.customer_age , "%d/%m/%Y").strftime("%d/%m/%Y")
                break
            except ValueError:
                print("Error: must be format dd/mm/yyyy ")
        while True :
            self.customer_checkin_date  = input("Enter Customer CheckInDate (day/month/year) =")
            try:
                self.customer_checkin_date = datetime.strptime(self.customer_checkin_date , "%d/%m/%Y").strftime("%d/%m/%Y")
                break
            except ValueError:
                print("Error: must be format dd/mm/yyyy ")
        while True :
            self.customer_checkout_date = input("Enter Customer CheckOutDate  (day/month/year) =")
            try:
                self.customer_checkout_date = datetime.strptime(self.customer_checkout_date, "%d/%m/%Y").strftime("%d/%m/%Y")

                break
            except ValueError:
                print("Error: must be format dd/mm/yyyy ")
        self.NumOfNight=datetime.strptime(self.customer_checkout_date,"%d/%m/%Y").date()-datetime.strptime(self.customer_checkin_date,"%d/%m/%Y").date()
        self.NumOfNight=self.NumOfNight.days
        while True:
                choice = int(input("Select Room Type (Enter 1 for Standard or 2 for Deluxe) = "))
                try:
                    if(choice==1):
                        self.RoomType="standard"
                        break
                    elif(choice==2):
                        self.RoomType="deluxe"
                        break
                    else:
                        print("\n please choice valid option!")
                except ValueError:
                    print("Please enter a number!")
        while(True):
            try:
                self.NumOfGuests=int(input("Enter Number of Guests (1-3)"))
                if(self.NumOfGuests>=1 and self.NumOfGuests<=3):
                    break
                else:
                    print("Guests must be between 1 to 3")
            except ValueError:
                print("Please enter a number!")
        if update==False:
            input("Press any key to continue...")
            clearScreen()

    def Total_num_of_customers(self):
        """
        Method to print total number of customers
        """
        print("Total Number Of Customers= "+str(self.total_customers))

    def calculations(self):
        """"
        Function to calculate room price
        """
        if(self.RoomType=="standard"):
            self.TotalPrice=int(self.NumOfNight)*200*self.NumOfGuests
        elif(self.RoomType=="deluxe"):
            self.TotalPrice=int(self.NumOfNight)*400*self.NumOfGuests
        return self.TotalPrice

    def Get_customer_data(self):
        """
        Function to display customer data
        """
        print("\n************************\n")
        print("Customer ID="+str(self.customer_id[0]))
        print("Customer Name="+self.customer_name)
        print("Customer Age="+str(self.customer_age))
        print("Customer telephone="+self.customer_telephone)
        print("Room Type="+self.RoomType)
        print("Customer CheckInDate="+str(self.customer_checkin_date))
        print("Customer CheckOutDate="+str(self.customer_checkout_date))
        print("Total Price="+str(self.calculations())+"£")
        print("\n************************\n")


    def Get_customer_id(self):
        return self.customer_id[0]


COUNT=0
def main():
    """
    fuction for main menu
    """
    CustomerList=[]

    while True:
        Main_menu()
        try:
            choice = int(input("Enter your choice:"))
        except ValueError:
            print("Please enter a number")
        else:
            clearScreen()
            while True:
                if (choice == 1):
                    Sub_booking_menu()
                    try:
                        subMenu=int(input(("Enter your choice =")))
                    except ValueError:
                        print("Please enter a number")
                    else:
                        if(subMenu==1):
                            CustomerList.append(Customer())
                            global COUNT
                            CustomerList[COUNT].Set_customer_data()
                            COUNT=COUNT+1

                        elif(subMenu==2):
                            try:
                                if len(CustomerList)!=0:
                                    for i in range(0,len(CustomerList)):
                                        CustomerList[i].Get_customer_data()
                                    input("Press any key to continue...")
                                    clearScreen()
                                else:
                                    raise Exception("Customer Didn't exist yet!")
                            except:
                                input("Customer Didn't exist yet!")
                                clearScreen()
                                Sub_booking_menu()
                                clearScreen()
                        elif(subMenu==3):
                            # Delete a Customer
                            flag=False
                            CustomerID=input("\nEnter Customer Id = ")
                            try:
                                if len(CustomerList)!=0:
                                    for i in range(0,len(CustomerList)):
                                        if CustomerID != None and CustomerID == str(CustomerList[i].Get_customer_id()):
                                            del CustomerList[i]
                                        else:
                                            flag=True
                                else:
                                    raise Exception("Customer Didn't exist yet!")
                                if flag==True:
                                    raise Exception("Customer with this id not exist!")
                                else:
                                    input(" Deleted Successfully! ")
                                    clearScreen()
                                    Sub_booking_menu()
                                    clearScreen()
                            except:
                                input("Customer with this id not exist!!")
                                clearScreen()
                                Sub_booking_menu()
                                clearScreen()
                        elif(subMenu==4):
                            # Update a Customer
                            flag=False
                            CustomerID=input("\nEnter Customer Id = ")
                            try:
                                if len(CustomerList)!=0:
                                    for i in range(0,len(CustomerList)):
                                        if CustomerID != None and CustomerID == str(CustomerList[i].Get_customer_id()):
                                            CustomerList[i].Set_customer_data(True)
                                            break
                                        else:
                                            flag=True
                                else:
                                    raise Exception("Customer Didn't exist yet!")
                                if flag==True:
                                    raise Exception("Customer with this id not exist!")
                                else:
                                    input(" Updated Successfully! ")
                                    clearScreen()
                                    Sub_booking_menu()
                                    clearScreen()
                            except:
                                input("Customer with this id not exist!!")
                                clearScreen()
                                Sub_booking_menu()
                                clearScreen()
                        elif(subMenu==5):
                            clearScreen()
                            break
                        else:
                            print("Please select a valid choice")
                if (choice == 2):
                    clearScreen()
                    Sub_booking_Display_menu()
                    try:
                        subMenu=int(input(("Enter your choice =")))
                    except ValueError:
                        print("Please enter a number")
                    else:
                        if(subMenu==1):
                            try:
                                if len(CustomerList)!=0:
                                    for i in range(0,len(CustomerList)):
                                        CustomerList[i].Get_customer_data()
                                    input("Press any key to continue...")
                                    clearScreen()
                                else:
                                    raise Exception("Customer Didn't exist yet!")
                            except:
                                input("Customer Didn't exist yet!")
                                clearScreen()
                                Sub_booking_menu()
                                clearScreen()
                        elif(subMenu==2):
                            flag=False
                            CustomerID=input("\nEnter Customer Id = ")
                            try:
                                if len(CustomerList)!=0:
                                    for i in range(0,len(CustomerList)):
                                        if CustomerID != None and CustomerID == str(CustomerList[i].Get_customer_id()):
                                            CustomerList[i].Get_customer_data()
                                        else:
                                            flag=True
                                else:
                                    raise Exception("Customer Didn't exist yet!")
                                if flag==True:
                                    raise Exception("Customer with this id not exist!")
                                else:
                                    input(" Displayed Successfully! ")
                                    clearScreen()
                                    Sub_booking_menu()
                                    clearScreen()
                            except:
                                input("Customer with this id not exist!!")
                                clearScreen()
                                Sub_booking_menu()
                                clearScreen()
                        elif(subMenu==3):
                            clearScreen()
                            break
                if (choice == 3):
                    quit()
                if (choice > 3):
                    print("Please select a valid choice")

main()