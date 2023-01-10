'''Programm, dass eine Liste von Zahlen quadriert
und analysiert.
'''
#Funktion, die alle Zahlen in einer Liste quadriert.
def squares(eingabeliste):
    #Ergebnis definieren
    ergebnisliste = []
    
    #jeden Eintrag in der Liste quadrieren 
    for counter in range(len(eingabeliste)):
        ergebnisliste.append(eingabeliste[counter]*eingabeliste[counter])
    
    #Ergebnis in's Hauptprogramm zurückgeben
    return ergebnisliste                   #Fehler 1 falsche liste zurückgegeben
##########################################################################
#Benutzereingabe
userlist = []
#Zaehler
counter = 1
#Zahlen vom Benutzer einlesen
while (True):
    print("Ihre " + str(counter) + ". Zahl bitte")
    number = (int(input()))
    userlist.append(number)
    counter = counter + 1
    #abbrechen, wenn der Benutzer 0 eingibt
    if (number == 0):
        userlist.remove(0)
        break                        #Fehler 2  bei break einrückung vergessen

#Funktion aufrufen und Ergebnis speichern
test = squares(userlist)
#Datei schreibend öffnen
file_output = open("quadrate.txt", "w")
#Daten schreiben:
for counter in range(len(test)):
    file_output.write("("+ str(counter+1) + "):" +
                      str(userlist[counter]) + " * " + str(userlist[counter])
                    + " = " + str(test[counter]) + "\n")
#Datenstrom schließen
file_output.close()

        
    