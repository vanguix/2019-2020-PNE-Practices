from Seq0 import *
listseq = ["U5", "ADA", "FRAT1", "FXN"]
bases = ["A", "C", "T", "G"]
txt = ".txt"
folder = "../Session-04/"
print("----Exercise 4----")
for element in listseq:
    dnaseq = seq_read_fasta(folder+element+txt)
    print("Gene", element, ":")
    for base in bases:
        print(base, ":", seq_count_base(dnaseq, base))
