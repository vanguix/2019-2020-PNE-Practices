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


# -- Main program
s1 = Seq("ACCTGC")
s2 = Seq("Hello? Am I a valid sequence?")
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")
