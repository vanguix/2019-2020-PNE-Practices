inputsequence = input("Introduce the sequence:")


countA = 0
countC = 0
countT = 0
countG = 0
for bases in inputsequence:
    if bases == "A":
        countA += 1
    elif bases == "C":
        countC += 1
    elif bases == "T":
        countT += 1
    else:
        countG += 1

print("Total length:", len(inputsequence))
print("A:", countA)
print("C:", countC)
print("T:", countT)
print("G:", countG)
