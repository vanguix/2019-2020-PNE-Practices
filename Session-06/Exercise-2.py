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

    def print_seqs(self):
        return (f"Sequence :(Length {stringbases.len()}){self.stringbases}")


seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]
for sequence in seq_list:
    sequence.print_seqs()