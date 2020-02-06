lst = [10,4,4,8,8,2,1,3]
lst2 = []

#manier 1
lst.sort()
print(lst)

#manier 2
while lst:
    min = lst[0]
    for t in lst:
        if t < min:
            min = t
    lst2.append(min)
    lst.remove(min)
print (lst2)