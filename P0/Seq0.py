def seq_ping():
    print("OK!")


def seq_read_fasta(filename):
    from pathlib import Path
    file_contents = Path(filename).read_text()
    body = file_contents.split("\n")[1:]
    sequence = ",".join(body).replace(",", "")
    return sequence


def seq_len(seq):
    count = 0
    for base in seq:
        count += 1
    return count


def seq_count_base(seq, base):
    counter = 0
    for element in seq:
        if element == base:
            counter += 1
    return counter


def seq_count(seq):
    d = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
    for bases in seq:
        if bases == "A":
            d["A"] += 1
        elif bases == "C":
            d["C"] += 1
        elif bases == "T":
            d["T"] += 1
        else:
            d["G"] += 1
    return d


def seq_reverse(seq):
    return seq[::-1]

def seq_complement(seq):
    d = {"A": "T", "T":"A", "C":"G", "G":"C"}
    newseq = ""
    for element in seq:
        newseq += d[element]

    return newseq
