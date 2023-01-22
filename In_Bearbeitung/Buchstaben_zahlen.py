'''
Phillip 22.01.2023
'''



while True:
    length = 0  # Reset the length variable

    choice = input("Do you want to analyse a word, or a file? (w/f/c) ") # Ask the user if they want to analyse a word or a file

    if choice == "w": # If they want to analyse a word
        word = input("Enter a word: ") # Ask for the word

        for i in range(len(word)): # For each letter in the word
            character = word[i] # Set the variable words to the letter

            if character.isalpha():
                length += 1 # Add 1 to the length variable

            else:
                pass

        print(f"Ammount of Letters in the Word: {length}") # Print the amount of letters in the word

    elif choice == "f": # If they want to analyse a file

        file_name = input("Enter a file name: ") # Ask for the file name
        file = open(file_name, "r") # Opens the file
        for line in file:
            for i in range(len(line)):  # For each letter in the word
                character = line[i]  # Set the variable words to the letter

                if character.isalpha():
                    length += 1  # Add 1 to the length variable

                else:
                    pass
        file.close()

        print(f"Ammount of Letters in the Word: {length}") # Prints the amount of letters in the file

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



