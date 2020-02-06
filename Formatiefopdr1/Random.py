import random
number = random.randrange (0, 10)
gok = input("welk nummer tussen 0 en 10? ")
while int(gok) != number:
    print("niet goed")
    gok = input("welk nummer? ")
if int(gok) == number:
    print("goed geraden")