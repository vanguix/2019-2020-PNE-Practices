from Seq0 import *

folder = "../Session-04/"
filename = "U5.txt"
print("DNA file:", filename)
print("The first 20 bases are:", seq_read_fasta(folder+filename)[:20])
