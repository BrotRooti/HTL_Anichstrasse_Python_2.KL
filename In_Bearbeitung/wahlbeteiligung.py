'''
Matplotlib - Aufgabe 3 - Wahlbeteiligung in Wiesing
Phillip H.
29.11.2022
'''

import matplotlib.pyplot as plt
import tkinter.simpledialog
ax = plt.gca()

def data_manager(jahr,location):
    data = []
    file = open(jahr + ".csv")
    for line in file:
        line = line.strip("\n")
        if location in line:  # If data is in the line
            data = line.split(";")  # Saves everything in the line in a list
    file.close()
    data = data[10]  # Deletes the first five elements of the list
    data = data.replace(",", ".")
    return data


location = tkinter.simpledialog.askstring("Wahlbeteiligung", "Welcher Ort?")



data = []
jahre = ["1989", "1994", "1999", "2003", "2008", "2013", "2018"]
for jahr in jahre:
    data.append(data_manager(jahr,location))





# Plot the data
plt.style.use('dark_background') # Dark background
# data
plt.title("Landtagswahl Wahlbeteiligung in {}".format(location)) # Title
plt.plot(jahre, data, color="red") #data
ax.invert_yaxis()
ax.set_facecolor("black")

plt.show() # Show the plot














