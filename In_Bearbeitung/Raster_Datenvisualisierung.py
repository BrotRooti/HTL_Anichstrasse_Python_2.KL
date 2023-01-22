from tkinter import filedialog


file_name = filedialog.askopenfilename()
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
        try:
            data[i][x] = int(data[i][x])
            print(f"|{data[i][x]:>7}", end="")
        except ValueError:
                print(f"|{data[i][x]:<7}", end="")
    print("|")



