from Client0 import Client
from Seq1 import Seq
PRACTICE = 2
EXERCISE = 6

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "127.0.0.1"
PORT = 8080

# -- Create a client object
c = Client(IP, PORT)

folder = "../Session-04/"
s = Seq()
sequence = s.read_fasta(folder + "FRAT1.txt")


c.talk("Sending FRAT1 Gene to the server...")
c.talk(f"Fragment 1: {str(sequence)[0:10]}")
c.talk(f"Fragment 2: {str(sequence)[10:20]}")
c.talk(f"Fragment 3: {str(sequence)[20:30]}")


print(f"Gene FRAT1: {sequence}")
print(f"Fragment 1: {str(sequence)[0:10]}")
print(f"Fragment 2: {str(sequence)[10:20]}")
print(f"Fragment 3: {str(sequence)[20:30]}")
