from Seq1 import *
print("------| Practice 1, Exercise 9 |------")
# -- Create a Null sequence
s = Seq()
# -- Initialize the null seq with the given file in fasta format
folder = "../Session-04/"
filename = "U5.txt"
FILENAME = folder + filename
s.read_fasta(FILENAME)

print(f"Sequence :(Length {s.len()}) {s}")
print(f"Bases:  {s.count()}")
print(f"Rev:   {s.reverse()}")
print(f"Comp:  {s.complement()}")


