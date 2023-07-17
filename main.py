#using while loop so that program will not be terminated until user decised to
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
        print("-"*70) #*70 will print 70 hypens(-)
        print('''
                RENTAL SHOP KATHMANDU
        THE AVAILABLE STOCKS ARE AS FOLLOW''')
        #Open the file in read mode and assign the file object to the variable 'data'
        data = open("equipment.txt","r")
        #Read all lines from the file object and store them as a list of strings in the variable
        items = data.readlines()
        print("-"*120)
        for item in items:
            ##Split the string 'item' into four separate values based on the comma delimiter and assign them to variables
            Name,Brand, Price, Quantity = item.split(",")
            #Print formatted values with specified field widths
            print("{0:30s}\t\t{1:25s}\t{2:10s}\t{3:10s}".format(Name, Brand, Price, Quantity))
        print("-"*120)
    elif choice == 2:
        try:
            equipmentName = input("Enter equipment name: ")
            quantity=int(input("Enter quantity: "))
            customerName=input("Enter customer name: ")   
        except:
            print('Enter valid input ')
    else:
        break
