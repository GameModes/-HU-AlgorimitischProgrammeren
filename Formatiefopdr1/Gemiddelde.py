lst = [0,2,3,6,7,8,10,5,9,20]

def gemiddelde():
    tot = 0
    for x in lst:
        tot += x
    gem = tot/len(lst)
    print(gem)

lst2 = [0,2,5,6,6,6,6,7,9,2,2,4]

def gemiddelde2():
    tot = 0
    for x in lst:
        tot += x
    for x in lst2:
        tot += x
    gem2 = tot/(len(lst) + len(lst2))
    print(gem2)

gemiddelde()
gemiddelde2()