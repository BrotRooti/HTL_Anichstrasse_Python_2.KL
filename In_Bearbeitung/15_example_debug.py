"""
Autor: Alexander Jäger
Datum: 6.2.2022
Beispiel für das Debuggen von Programmen 
"""

import random

possible_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

for i in range(2):
    letter = random.choice(possible_letters)
    if letter == "x":
        break

    print ("_____")
    print ("|   |")
    print ("|   |")
    print (f"| {letter} |")

