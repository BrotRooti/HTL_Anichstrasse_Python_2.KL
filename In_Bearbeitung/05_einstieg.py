'''
Einführung in Prozeduren und Funktionen
Autor: Alexander Jäger
Datum: 20.10.2021
'''

# Eingabe der 1. Zahl. Diese muss größer als 0 sein
z1 = 0
while z1 <= 0:
    z1 = int(input("Zahl: "))
    if z1 <= 0:
        print("Die Zahl muss größer als 0 sein!")

# Eingabe der 2. zahl. Diese muss größer als 0 sein
z2 = 0
while z2 <= 0:
    z2 = int(input("Zahl: "))
    if z2 <= 0:
        print("Die Zahl muss größer als 0 sein!")

# Berechnung des größten gemeinsamen Teilers
while z2 != 0:
    if z1 > z2:
        z1 = z1 - z2
    else:
        z2 = z2 - z1

# Ausgabe des größten gemeinsamen Teilers
print('Der größte gemeinsame Teiler ist ' + str(z1))