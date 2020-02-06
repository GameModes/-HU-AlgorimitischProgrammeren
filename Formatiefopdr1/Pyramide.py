getal = int(input("Voer in getal: "))

print("\nFor loop: ")
for var in range (int(getal)+1):
    print("*"*var)
for var in range (int(getal)-1,0,-1):
    print("*"* var)

print("\nWhile loop: ")
var = getal
totvar = var+1
while var != 0: #1 tot 5
    calc = totvar - var
    print("*"* calc)
    var += -1

var = getal
totvar = var
while var != 0: #4 tot 1
    print("*"* var)
    var += -1

print("\nFor loop omgekeerd: ")
for var in range (int(getal)+1):
    print("*"*((int(getal)+1) - var))
for var in range (int(getal)-1,0,-1):
    print("*"* ((int(getal)+1) - var))