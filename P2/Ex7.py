from Client0 import Client
from Seq1 import Seq
PRACTICE = 2
EXERCISE = 6

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "127.0.0.1"
PORT1 = 8080
PORT2 = 8081

# -- Create a client object
c1 = Client(IP, PORT1)
c2 = Client(IP, PORT2)

# -- Create fragments
folder = "../Session-04/"
s = Seq()
sequence = s.read_fasta(folder + "FRAT1.txt")

fragment1 = str(sequence)[0:10]
fragment2 = str(sequence)[10:20]
fragment3 = str(sequence)[20:30]
fragment4 = str(sequence)[30:40]
fragment5 = str(sequence)[40:50]
fragment6 = str(sequence)[50:60]
fragment7 = str(sequence)[60:70]
fragment8 = str(sequence)[70:80]
fragment9 = str(sequence)[80:90]
fragment10 = str(sequence)[90:100]

list_fragments = [fragment1, fragment2, fragment3, fragment4, fragment5, fragment6, fragment7, fragment8, fragment9,
                  fragment10]

# Sending to servers console
index1 = 0
for element in list_fragments:
    if index1 % 2 == 0 or index1 == 0:
        c1.talk(f"Fragment {index1+1}: {list_fragments[index1]}")
    else:
        c2.talk(f"Fragment {index1+1}: {list_fragments[index1]}")

    index1 += 1

# Print on CLient console
print(f"Gene FRAT1: {sequence}")
index = 1
for element in list_fragments:
    print(f"Fragment {index}: {element}")
    index += 1
