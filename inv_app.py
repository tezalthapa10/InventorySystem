while(True):
    #printing the welcome message for users
    print('''
    ---------------------------------------
             Welcome To Rental Shop
                   Kathmandu,
                     Nepal
             Tel No. +977 9877878900
    ---------------------------------------
    1. View items in stock
    2. Buy Items
    3. Exit
    ''')

    #taking input from user for the options given
    choice = int(input("Enter your option to go forward:"))
    if choice == 1:
        print("-"*60)
        print('''
                RENTAL SHOP KATHMANDU
        THE AVAILABLE STOCKS ARE AS FOLLOW''')
        data = open("equipment.txt","r")
        items = data.readlines()
        print("-"*60)
        for item in items:
            Name, Price, Quantity = item.split(",")
            print("{0}\t\t{1}\t{2}".format(Name, Price, Quantity))
        print("----------------------")
    elif choice == 2:
        try:
            equipmentName = input("Enter equipment name: ")
            quantity=int(input("Enter quantity: "))
            customerName=input("Enter customer name: ")    
        except:
            print('Enter valid input ')
    else:
        break
