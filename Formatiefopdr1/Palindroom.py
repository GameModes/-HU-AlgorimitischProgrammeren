palindroom = input("voeg in woord: ")
omgedraaid = str(palindroom[::-1])

if omgedraaid == palindroom:
    print("Het is een palindroom!")
else:
    print("het is geen palindroom")