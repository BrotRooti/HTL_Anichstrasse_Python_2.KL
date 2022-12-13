#Formatierungen mittels Formatted Strings
i = 13
d = 12.3456
s = "Hallo"

print("Integer Zahlen")
print(f"|{i:<7}| linksbündig, 7 Zeichen")
print(f"|{i:^7}| zentriert,   7 Zeichen")
print(f"|{i:>7}| rechtsbündig 7 Zeichen")

print("Floats")
print(f"|{d:<15}| linksbündig, 15 Zeichen")
print(f"|{d:^15}| zentriert,   15 Zeichen")
print(f"|{d:>15}| rechtsbündig 15 Zeichen")

#das f am Ende bedeutet, dass es als Gleitkommazahl und nicht in Exponentialschreibweise ausgegeben wird
print(f"|{d:6.2f}| insgesamt 6 Stellen, 2 nach dem Komma")
print(f"|{d:6.3f}| insgesamt 6 Stellen, 3 nach dem Komma")

print("Text")
print(f"|{s:7}| 7 Zeichen")
print(f"|{s:<7}| linksbündig, 7 Zeichen")
print(f"|{s:^7}| zentriert,   7 Zeichen")
print(f"|{s:>7}| rechtsbündig 7 Zeichen")
print(f"|{s:>4}| rechtsbündig 4 Zeichen")