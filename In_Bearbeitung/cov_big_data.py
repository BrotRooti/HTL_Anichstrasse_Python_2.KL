'''
Matplotlib - Aufgabe 2 - Covid-19 Big Data
Phillip H.
08.11.2022
'''

import matplotlib.pyplot as plt
file = open("time_series_covid19_confirmed_global.csv")

#create empty lists
austria = []
ecuador = []
chile = []
canada = []



for i in file:
    i = i.strip("\n")
    if "Austria" in i: # If Austria is in the line
        austria = i.split(",") # Saves everything in the line in a list
    elif "Ecuador" in i:
        ecuador = i.split(",")
    elif "Chile" in i:
        chile = i.split(",")
    elif "Canada" in i:
        canada = i.split(",")

file.close()

austria = austria[5:] # Deletes the first five elements of the list
ecuador = ecuador[5:]
chile = chile[5:]
canada = canada[5:]

# Convert the list elements to floats
austria = [float(i) for i in austria]
ecuador = [float(i) for i in ecuador]
chile = [float(i) for i in chile]
canada = [float(i) for i in canada]

# Plot the data
plt.style.use('dark_background') # Dark background
# Austria
plt.title("Covid-19 Infections in Austria") # Title
plt.plot(austria, label="Austria", color="red") #data
plt.show() # Show the plot

# Ecuador
plt.title("Covid-19 Infections in Ecuador") # Title
plt.plot(ecuador, label="Ecuador", color="red") #data
plt.show() # Show the plot

# Chile
plt.title("Covid-19 Infections in Chile") # Title
plt.plot(chile, label="Chile", color="red") #data
plt.show() # Show the plot

# Canada
plt.title("Covid-19 Infections in Canada") # Title
plt.plot(canada, label="Canada", color="red") #data
plt.show() # Show the plot

#Saves the infections of austria in a new file
file = open("austria_infections.txt", "w")
for i in austria:
    file.write(str(i) + "\n")

file.close() # Datei schließen
print("Gesammtinfektionen Österreich:  {:.2f} Mio.".format(austria[-1]/1000000)) # Print the total infections of Austria







