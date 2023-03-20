



def Fehlstunden(Tag):
    global Stunden
    print(f"Tag: {Tag}")
    while True:
        try:
            data = input("Bitte Name und Stundenanzahl angeben oder mit Enter beenden\n")
            data = data.split(" ")
            if data[0] == "":
                break

            Stunden[data[0]] = int(data[1]) + Stunden[data[0]]

        except KeyError:
            print("Name nicht gefunden")
            print("Bitte Namen eingeben oder Enter drücken um zu beenden")
            continue
        except ValueError:
            print("Bitte eine Zahl eingeben")
            continue
        except IndexError:
            print("Bitte einen Namen eingeben und anschließend eine Zahl eingeben")
            continue
    print("")
    print("-" * 15)






while True:
    Stunden = {"Kerem": 0, "Adrian": 0, "Melvin": 0, "Julian": 0, "Maximillian": 0, "Lucas": 0,
               "Christoph": 0, "Phillip": 0, "Gianluca": 0, "Berat": 0, "Muslim": 0}
    Tage = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag"]

    for i in range(5):
        Fehlstunden(Tage[i])

    print("Fehlstunden dieser Woche")
    print("-" * 15)
    for name in Stunden:
        print(f"{name:<15} {Stunden[name]}")

    print("-" * 15)
    print("")

    repeat = input("Wollen Sie das Programm nochmals ausführen? (y/n)\n")
    if repeat == "y":
        continue
    else:
        quit()