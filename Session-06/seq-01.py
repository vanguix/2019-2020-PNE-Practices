class Seq:
    """A class for representing sequence objects"""
    def __init__(self, stringbases):
        self.stringbases = stringbases
        print("New sequence created!")

    def __str__(self):
        return self.stringbases

    def len(self):
        return len(self.stringbases)


class Gene(Seq):
    pass


# -- Main program
s1 = Seq("AAGCGT")
g = Gene("ACCTGA")
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {g}")
print(f"The length of the sequence 1 is {s1.len()}")
print(f"The lenght of the sequence 2 is {g.len()}")
