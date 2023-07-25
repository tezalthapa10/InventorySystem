
def readfile():
    with open("equipment.txt","r") as file:
        items = file.readlines()

        for item in items:
            Name,Brand, Price, Quantity = item.split(",")
            print("{0:30s}\t{1:25s}\t{2:10s}\t{3:10s}".format(Name, Brand, Price, Quantity))

