print("-"*90) 
print("\t\t\t\tTHE ITEMS IN STOCK ARE")
data = open("equipment.txt","r")
items = data.readlines()
print("-"*90)
for item in items:
    Name,Brand, Price, Quantity = item.split(",")
    print("{0:30s}\t{1:25s}\t{2:10s}\t{3:10s}".format(Name, Brand, Price, Quantity))
print("-"*90)