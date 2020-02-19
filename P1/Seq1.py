class Seq:
    def __init__(self, stringbases):
        if stringbases == "":
            self.stringbases = "NULL"
            return
        for b in stringbases:
            if b not in ["A", "C", "T", "G"]:
                self.stringbases = "ERROR!"
                print("Invalid Seq Created")
                return
        self.stringbases = stringbases
        print("New sequence created!")

    def __init__(self, stringbases="NULL"):
        if stringbases == "":
            self.stringbases = "NULL"
            print("Null sequence created")
            return


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
        index += 1
        print(f"Sequence {index}:(Length {sequence.len()}) {sequence}")
