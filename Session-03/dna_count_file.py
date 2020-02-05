with open("dna.txt", "r") as file:
    countA = 0
    countC = 0
    countT = 0
    countG = 0
    totalbases = 0
    for line in file:
        for bases in line:
            totalbases += 1
            if bases == "A":
                countA += 1
            elif bases == "C":
                countC += 1
            elif bases == "T":
                countT += 1
            else:
                countG += 1

print("Total length:", totalbases)
print("A:", countA)
print("C:", countC)
print("T:", countT)
print("G:", countG)
