"""
Autor: Alexander Jäger
Datum: 6.2.2022
Analyseprogramm für Schüler, zum Üben des Debuggens

Aufgabe:
* Programm debuggen
* Kommentare dazuschreiben
* Fehler ausbessern
* den Variablen cnt1 und cnt2 sinnvolle Namen geben
* In einem Satz erklären, was das Programm macht
* Ausgabe-Text in der letzten Zeile anpassen
* Begrüßungstext für Benutzer so anpassen, dass klar ist, was das Programm macht.
"""

print("This program counts the characters and special characters in a text phrase.")
text = ""
while len(text) < 1: # <1 statt <5 damit auch kurze Texte möglich sind
    text = input("Please enter a text phrase:")
print("Thank you so much for this nice phrase!")

text = text.lower()
character = 0
special_character = 0
for letter in text:
    if letter in "abcdefghijklmnopqrstuvwxyz":
        character = character + 1
    else:
        special_character = special_character + 1 # +1 statt +2

print(f"There are {character} letters and {special_character} special characters in your Text.")
