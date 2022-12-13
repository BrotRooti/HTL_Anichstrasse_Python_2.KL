from tkinter import filedialog
from tkinter import *

file_name = filedialog.askopenfilename()
#file_name= "addresses.csv"
file = open(file_name, "r")

def count_lines(file_name):
    file = open(file_name, "r")
    line_count = len(file.readlines())
    return line_count

data = []
for line in file:
    data1 = line.strip("\n")
    data1 = data1.split(",")

    data.append(data1)

line_count = count_lines(file_name)
file.close()


print("_"*10*(len(data1)))

for i in range(line_count):
    for x in range(len(data[i])):
        print(f"|{data[i][x]:<7}" ,end="")
    print("|")




#print(f"|{data1[0]:<7}|")



