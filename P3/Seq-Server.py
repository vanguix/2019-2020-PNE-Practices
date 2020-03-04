import socket
import termcolor
from Seq1 import Seq

IP = "127.0.0.1"
PORT = 8081

sequence_list= ["ACT\n", "TTT\n", "AAA\n", "CCC\n", "GGG\n"]

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


        cs.close()