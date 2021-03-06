class Seq:
    """A class for representing sequence objects"""
    def __init__(self, stringbases):
        for b in stringbases:
            if b not in ["A", "C", "T", "G"]:
                self.stringbases = "ERROR!"
                print("ERROR!!!!")
                return

        self.stringbases = stringbases

    def __str__(self):
        return self.stringbases

    def len(self):
        return len(self.stringbases)


# -- Main program
def print_seqs(seq_list):
    index = 0
    for sequence in seq_list:
        print(f"Sequence {index}:(Length {sequence.len()}) {sequence}")
        index += 1


seq_lists = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]
print_seqs(seq_lists)
