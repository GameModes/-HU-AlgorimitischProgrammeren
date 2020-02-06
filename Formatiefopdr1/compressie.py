# with open('gegevenbestand.txt', 'r+') as r:
#     lezen = r.readlines()
#     r.seek(0)
#     for i in lezen:
#         if i != "\n" or i != "\t":
#             r.write(i)
#     r.truncate()

with open("gegevenbestand.txt", "r") as input:
    with open("nieuwbestand.txt", "w") as output:
        for line in input:
            if line.strip("\n") != "\n":
                output.write(line)

