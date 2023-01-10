'''
Matplotlib - Aufgabe 1
Phillip H.
24.10.2022
'''

import matplotlib.pyplot as plt

# Daten-Datei öffnen
file = open("daten.txt")
x = []
y = []
# Datei Zeile für Zeile auslesen
for line in file:
    # x- und y-Werte beim Leerzeichen trennen
    xy = line.split()
    # x-Wert zur Liste aller x-Werte als Gleitkommazahl hinzufügen
    x.append(float(xy[0]))
    # y-Wert zur Liste aller y-Werte als Gleitkommazahl hinzufügen
    y.append(float(xy[1]))

    print(x)

# Daten-Datei wieder schließen
file.close()

# Ausgabe der Kurve mittels matplotlib
plt.plot(x, y, label='Funktion', color='red', animated=True)
# Legende hinzufügen
plt.legend()
plt.show()
