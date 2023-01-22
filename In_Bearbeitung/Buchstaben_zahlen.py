'''
Phillip 17.01.2023
'''



while True:
    choice = input("Do you want to analyse a word, or a file? (w/f/c) ") # Ask the user if they want to analyse a word or a file

    if choice == "w": # If they want to analyse a word
        word = input("Enter a word: ") # Ask for the word
        print(f"Length: {len(word)}") # Print the length of the word

    elif choice == "f": # If they want to analyse a file
        length = 0 # Reset the length variable
        file_name = input("Enter a file name: ") # Ask for the file name
        file = open(file_name, "r") # Opens the file
        for line in file:
            length += len(line) # Calculates the length of the file
        file.close()
        print(f"Length: {length}") # Prints the length of the file

    elif choice == "c":
        print("Goodbye!")
        exit() # Exits the program

    else:
        print("Invalid input!")
        continue

    repeat = input("Do you want to analyse another word or file? (y/n) ") # Ask the user if they want to analyse another word or file

    if repeat == "y": # If they want to try again
        continue

    else : # If they don't want to try again
        print("Goodbye!")
        exit()



