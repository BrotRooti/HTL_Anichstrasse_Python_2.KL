import random
spalte = 1
input_questions = ["Geben Sie eine Zahl ein: ", "Wie viele Zeilen sollen generiert werden? ",
                    "Geben Sie eine Überschrift ein: ", "Geben Sie einen Dateinamen ein: "]


def werte_generator(zeilen):
    werte = []
    for zeile in range(zeilen):
        werte.append(random.randint(1, 100))
    return werte

def user_input(input_questions):
    input_return = []
    input_question = 0
    while True:
        try:
            #input_return = [int(input(input_questions[0])), int(input(input_questions[1])), input(input_questions[2]),input(input_questions[3])]
            while input_question <=3:
                if input_question <= 1:
                    input_return.append(int(input(input_questions[input_question])))
                else:
                    input_return.append(input(input_questions[input_question]))
                input_question += 1
        #spalten = int(input("Wie viele Spalten sollen generiert werden? "))
        #zeilen = int(input("Wie viele Zeilen sollen generiert werden? "))
        #ueberschrift = input("Geben Sie eine Überschrift ein: ")
        #datei_name = input("Geben Sie einen Dateinamen ein: ")

            return (spalten, zeilen, ueberschrift, datei_name)
        except ValueError:
            print("Bitte eine Zahl eingeben")
            continue


def file_output():
    pass


while True:
    user_input(input_questions)


    alle_werte = []
    for i in range(spalten):
        alle_werte.append(werte_generator(zeilen))

    file = open(datei_name, "a")

    while (spalte <= spalten):
        file.write(f"{ueberschrift} {spalte};")
        spalte += 1
    file.write("\n")

    for i in range(len(alle_werte[0])):
        for spalte in alle_werte:
            file.write(f"{spalte[i]};")
        file.write("\n")
        print("")
    file.close()

    repeat = input("Wollen Sie das Programm nochmals ausführen? (y/n)\n")
    if repeat == "y":
        continue
    else:
        quit()
