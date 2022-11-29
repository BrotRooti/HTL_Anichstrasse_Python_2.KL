import random

def summieren(zahlen):
    result = 0
    for zahl in zahlen:
        result += zahl
    return result

def generiere_zufallszahlen(anzahl, min, max):
    result = []
    for index in range(anzahl):
        result.append(random.randint(min, max))
    return result

y = [1,5,7,3,9,8]
summme = summieren(y)
print(summme)

zufaellige_zahlen = generiere_zufallszahlen(10, 1, 10)
print(zufaellige_zahlen)
