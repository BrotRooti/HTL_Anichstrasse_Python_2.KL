import random
from string import ascii_lowercase as letters_lower
from string import ascii_uppercase as letters_upper
from string import digits as digits
from string import punctuation as punctuation
symbols = letters_lower + letters_upper + digits + punctuation


def biggest_number(z1, z2, z3):
    list = [z1, z2, z3]
    list.sort(reverse=True)
    return list[0]


def is_bigger(z1, z2):
    if z1 > z2:
        return 1
    elif z2 > z1:
        return -1
    else:
        return 0


def input_float():
    while True:
        try:
            x = float(input("Geben Sie eine Zahl ein: "))
            if x < 0:
                raise ValueError
            return x
        except ValueError:
            print("Das ist keine positive Zahl!")
            continue


def if_else(condition, true, false):
    if condition == True:
        return true
    else:
        return false


def string_printer(string, number):
    print(string * number)


def draw_tree(string, number):
    for i in range(1, number + 1):
        print(f"{string * i:^{number * 2 - 1}}")


def random_number(lower, upper, number):
    while True:
        random_number = random.randint(lower, upper)
        if random_number % number == 0:
            return random_number
        else:
            continue


def letter_generator(klein):
    index = random.randint(0, 25)
    if klein:
        return letters_lower[index]
    else:
        return letters_upper[index]


def pw_gen(length):
    pw = ""
    for i in range(length):
        pw += random.choice(symbols)
    return pw

# x = biggest_number(1, 2, 3)
# print(x)
# x = biggest_number(3, 2)
# print(x)

draw_tree("*", 5)

# print(if_else(1<3, "Stimmt", "lügner"))

print(random_number(1, 100, 3))
print(letter_generator(True))
print(pw_gen(10))