zin1= 'lalala ik eet ui voor ontbijt'
zin2= 'lalala ik eet citroen op zondag tijdens het ontbijt'
index = 0

if len(zin1) < len(zin2):
    maxindex = len(zin2)
else:
    maxindex = len(zin1)


for index in range (0,int(maxindex)+1):
    if zin1[index] != zin2[index]:
        print(index)
        break



        # if zin1 != zin2:
        #     for i range(zin2):
        #
        # if zin2[index] != a or len(zin2) > index :
        #     print(index)
        # index += 1

        # index += 1
        # if a != b:
        #     print(index)
        # else:
        #     continue
else:
    print("zinnen zijn correct")