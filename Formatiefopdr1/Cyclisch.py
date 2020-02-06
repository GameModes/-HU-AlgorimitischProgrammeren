ch = input("noem bitwaarde met 7 bitjes (1010101): ")
n = int(input("noem verschuiving: "))

def schuiven (ch, n): #character & positieverschuiving
    if n > 0:
        for x in range(n):
            tempch = ""
            for o in ch[-6:]:
                tempch += o
            tempch += ch[0]
            ch = tempch
        print(ch)
    else:
        for x in range(n*-1):
            tempch = ""
            tempch += ch[-1]
            for o in ch[:6]:
                tempch += o
            ch = tempch
        print(ch)




schuiven(ch, n)