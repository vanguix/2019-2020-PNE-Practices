class Seq:
    """A class for representing sequence objects"""
    def __init__(self, stringbases):
        for b in stringbases:
            if b not in ["A", "C", "T", "G"]:
                self.stringbases = "ERROR!"
                print("ERROR!!!!")
                return

        self.stringbases = stringbases
        print("Correct object!")

    def __str__(self):
        return self.stringbases

    def len(self):
        return len(self.stringbases)


def generate_seqs(pattern, number):
    seq_list = []
    for element in range(1, number + 1):
        sequence = pattern * element
        seq_list.append(Seq(sequence))
    return seq_list


def print_seqs(seq_list):
    index = 0
    for sequence in seq_list:
        print(f"Sequence {index}:(Length {sequence.len()}) {sequence}")
        index += 1


seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

print("List 1:")
print_seqs(seq_list1)

print()
print("List 2:")
print_seqs(seq_list2)
