from Seq1 import *
print("-----| Practice 1, Exercise 5 |------")
s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")
bases = ["A", "C", "T", "G"]


print(f"Sequence 0:(Length {s1.len()}) {s1}")
for base in bases:
    print(base, ":", s1.seq_count_base(base), end=",  ")

print(f"\nSequence 1:(Length {s2.len()}) {s2}")
for base in bases:
    print(base, ":", s2.seq_count_base(base), end=",  ")

print(f"\nSequence 2:(Length {s3.len()}) {s3}",)
for base in bases:
    print(base, ":", s1.seq_count_base(base), end=",  ")
