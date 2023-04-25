import random


def doorchecker():
    global score
    while True:
        try:
            door_input = int(input("Choose a door from 1-3: "))
        except ValueError:
            print("That's not a door!")
            print("Please choose a door from 1-3")
            continue

        door = random.randint(1, 3)

        if door_input > 3 or door_input < 1:
            print("That's not a door!")
        elif door != door_input:
            print("You passed this round!")
            score += 1
        else:
            print("You failed, now get out of here!")
            break


while True:
    score = 0
    print("Welcome to the door game!")
    print("You have to choose a door, if you choose the right door you pass the round.")
    print("If you choose the wrong door you fail and have to leave the castle.")
    doorchecker()
    print("\n"*100)
    print("You got caught by the guards and have to leave the castle.")
    print(f"Your score is: {score}")
    repeat = input("Do you want to play again? (y/n)\n")
    if repeat == "y":
        continue
    else:
        quit()
