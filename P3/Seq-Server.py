import socket
import termcolor
from Seq1 import Seq

IP = "127.0.0.1"
PORT = 8083

sequence_list= ["ACT\n", "TTT\n", "AAA\n", "CCC\n", "GGG\n"]
list_bases = ["A", "C", "G", "T"]
# --- Step 1: Creating the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# --- Step 2: Bind the socket to the server's IP and PORT
ls.bind((IP, PORT))

# --- Step 3: Convert into a listening socket
ls.listen()

print("SEQ Server configured!")

while True:
    print("Waiting for clients...")
    try:
        # --- Step 4: Wait for clients to connect
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server is done!")
        ls.close()
        exit()
    else:
        # --- Step 5: Receiving information from the client
        msg_raw = cs.recv(2000) #compulsory to specify the maximum number of bytes we allow to receive
        msg = msg_raw.decode() #for decoding the bytes into a text message

        if msg == "PING":
            termcolor.cprint("PING command!", "green")
            response = "OK!\n"
            cs.send(response.encode())
            print(response)

        elif msg.startswith("GET"):
            index = 0
            for i in sequence_list:
                if msg[4] == str(index):
                    cs.send(i.encode())
                    termcolor.cprint("GET", "green")
                    print(i)
                index += 1

        elif msg.startswith("INFO"):
            termcolor.cprint("INFO", "green")
            sequence = Seq(str(msg[5:]))
            print(f"Sequence: {sequence}")
            print(f"Total length: {sequence.len()}")
            for base in list_bases:
                info = f"{base} : {sequence.seq_count_base(base)[0]} ({sequence.seq_count_base(base)[1]})% \n"
                print(info)
                respond = f"Sequence: {sequence}\nTotal lenght: {sequence.len()}\n{info}"
            cs.send(respond.encode())

        elif msg.startswith("COMP"):
            termcolor.cprint("COMP", "green")
            sequence = Seq(str(msg[5:]))
            print(sequence.complement())
            cs.send(sequence.complement().encode())

        elif msg.startswith("REV"):
            termcolor.cprint("REV", "green")
            sequence = Seq(str(msg[4:]))
            print(sequence.reverse())
            cs.send(sequence.reverse().encode())

        elif msg.startswith("GENE"):
            termcolor.cprint("GENE", "green")
            gene = str(msg[5:])
            folder = "../Session-04/"
            s = Seq()
            seq_sequence = s.read_fasta(folder + gene + ".txt")
            print(seq_sequence)
            cs.send(str(seq_sequence).encode())










        cs.close()