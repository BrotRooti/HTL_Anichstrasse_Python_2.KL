'''
Phillip 22.01.2023
'''

from string import ascii_lowercase as letters
import ascii_art

ascii_art.print_art("Buchstaben_Analysieren")

print(f"The following program will analyse a file and tell you how many times each letter appears in the file.")
print("")
print(f"Please note that the program will only analyse letters and not numbers or special characters.")
print(f"Please also note that the program will not analyse the file if it is not in the same folder as the program.")
print("")










while True:
    length = 0  # Reset the length variable
    Letters = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0,
               "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0,
               "ä": 0, "ö": 0, "ü": 0, "ß": 0} # Creates a dictionary with all the letters and resets their amount

    choice = input(
        "Do you want to analyse a file? If yes input 'f' \n"
        "If no and you would like to cancel the programm input 'c'\n")  # Ask the user if they want to analyse a
    # word or a file

    if choice == "f":  # If they want to analyse a file
        while FileNotFoundError:
            file_name = input("Enter a file name: ")  # Ask for the file name
            try:
                file = open(file_name, "r")  # Opens the file
                break
            except FileNotFoundError:
                print("File not found.\n"
                      "Please type in the full name of the file including the file extension.")
                continue
        for line in file:
            counter = 0
            for c in letters:
                counter = line.count(c) + line.count(c.upper()) # Counts the amount of letters in the file
                Letters[c] = counter + Letters[c]
        file.close()

    elif choice == "c":
        print("")
        print("Goodbye!")
        exit()  # Exits the program

    else:
        print("Invalid input. Please type in 'f' for file or 'c' to cancel.")
        continue

    print(f"Ammount of each Letter in the File")
    print("-" * 15)

    for c in letters:
        print(f"|{c.upper()  :<10}", end=" ")
        print(f"{Letters[c]}", end=" ")  # Prints the amount of letters in the file
        print("|")

    print("_" * 15)

    repeat = input(
        "Would you like to analyse another file? Please input 'y' for yes or 'n' for no\n")
    if repeat == "y":  # If they want to try again
        continue

    else:  # If they don't want to try again
        print("")
        print("Goodbye!")
        exit()
