file = open("wh_daten.csv", "r")


for line in file:
    data = line.split("|")
    print(data[0])
    print("Alter: " + data[1])
file.close()


