from read import *
#using while loop so that program will not be terminated until user decised to
while(True):
    #printing the welcome message for users
    print('''
    ---------------------------------------
            Welcome To ABC Rental Shop
                   Kathmandu,
                     Nepal
             Tel No. +977 9877878900
    ---------------------------------------
    1. View items in stock
    2. Rent Items
    3. Return Items
    4. Exit
    ---------------------------------------
    ''')

    #taking input from user for the options given
    choice = int(input("Enter your option to go forward: "))
    if choice == 1:
        print("-"*90) 
        print("\t\t\t\tTHE ITEMS IN STOCK ARE")
        data = open("equipment.txt","r")
        items = data.readlines()
        print("-"*90)
        for item in items:
            Name,Brand, Price, Quantity = item.split(",")
            print("{0:30s}\t{1:25s}\t{2:10s}\t{3:10s}".format(Name, Brand, Price, Quantity))
        print("-"*90)
    elif choice == 2:
        try:
            equipmentName = input("Enter equipment name: ")
            quantity=int(input("Enter quantity: "))
            customerName=input("Enter customer name: ")   
        except:
            print('Enter valid input ')
    elif choice == 3:
        try:
            equipmentName = input("Enter equipment name: ")
            quantity=int(input("Enter quantity: "))
            customerName=input("Enter customer name: ")   
        except:
            print('Enter valid input ')
    elif choice == 4:
        print("\t\tThankyou for using our system!! Have a great day ahead!!")
        break
    else:
        print("Please enter the correct option.")
