lst = [0,1]
n = int(input("geef integer: "))



def verdubbeling(lst):
    for t in range (n):
        formfr = lst[-2]
        fr = lst[-1]
        lst.append(formfr+fr)
    print(lst)
    print(lst[-1])


verdubbeling(lst)

