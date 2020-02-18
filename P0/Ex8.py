from Seq0 import *

folder = "../Session-04/"
bases = ["A", "C", "T", "G"]
listseq = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
txt = ".txt"
print("-----| Exercise 8 |------")
for sequences in listseq:
    sequence = seq_read_fasta(folder + sequences + txt)
    dict_bases = seq_count(sequence)
    min_value = 0
    frc_base = ""
    for base, value in dict_bases.items():
        while value > min_value:
            min_value = value
            frc_base = base

    print("Gene", sequences, " : Most frequent Base: ", frc_base)
