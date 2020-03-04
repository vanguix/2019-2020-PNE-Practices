from Seq1 import Seq
from Client0 import Client

PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "127.0.0.1"
PORT = 8080

# -- Create a client object
c = Client(IP, PORT)

folder = "../Session-04/"
s = Seq()
sequence = s.read_fasta(folder + "U5.txt")

c.debug_talk("Sending U5 Gene to the server...")
c.debug_talk(str(sequence))