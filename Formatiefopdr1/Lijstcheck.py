lijst = [0, 0, 1, 1, 1, 2, 3, 5, 5, 10, 10, 20]
lijst12 = [0,0,0,0,0,1,1,1,1,1,1,1]
getal = int(input("welk getal? "))

def count (getal, lijst):
    vaak = 0
    for x in lijst:
        if x == getal:
            vaak += 1
    return vaak
print("het getal zit " + str(count(getal, lijst)) + ' keer erin.')

def lijstb ():
    grootverschil = 0
    for i in lijst:
        if i != lijst[-1]:
            verschil = lijst[i+1] - i
            if grootverschil < verschil :
                grootverschil = verschil
    print("het grootste verschil is: " + str(grootverschil))

def lijstc():
    if count(0, lijst12) < count(1, lijst12) and count(3, lijst12) == 0 and count(0, lijst12) < 12:
        print ("waar")
    else:
        print('niet waar')

count(getal, lijst)
lijstb()
lijstc()
