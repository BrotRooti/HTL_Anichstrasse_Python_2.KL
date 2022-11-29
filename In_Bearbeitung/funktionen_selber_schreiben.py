'''
Einführung in Prozeduren und Funktionen
Autor: Phillip Hilscher
Datum: 29.11.2022
'''


def positive_zahl_eingeben():
    z = 0
    while z <= 0:
        z = int(input("Zahl: "))
        if z <= 0:
            print("Die Zahl muss größer als 0 sein!")
    return z
def teiler(z1,z2):
    while z2 != 0:
        if z1 > z2:
            z1 = z1 - z2
        else:
            z2 = z2 - z1
    return z1



z1 = positive_zahl_eingeben()
z2 = positive_zahl_eingeben()

z1 = teiler(z1,z2)




print('Der größte gemeinsame Teiler ist ' + str(z1))