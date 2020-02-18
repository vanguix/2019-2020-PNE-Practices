from Seq0 import *
listseq = ["U5", "ADA", "FRAT1", "FXN","RNU6_269P"]
txt = ".txt"
folder = "../Session-04/"
print("----Exercise 3----")
for element in listseq:
    dnaseq = seq_read_fasta(folder+element+txt)
    print("Gene", element, "---->", "Length:", seq_len(dnaseq))
