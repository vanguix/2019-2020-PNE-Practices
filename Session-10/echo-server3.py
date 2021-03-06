import socket
import termcolor

IP = "212.128.253.141"
PORT = 8083


# --- Step 1: Creating the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# --- Step 2: Bind the socket to the server's IP and PORT
ls.bind((IP, PORT))

# --- Step 3: Convert into a listening socket
ls.listen()

print("Server is configured!")

number_connection = 0
list_clients = []
while True:

    try:
        # --- Step 4: Wait for clients to connect
        (cs, client_ip_port) = ls.accept()

    except KeyboardInterrupt:
        print("Server is done!")
        ls.close()
        exit()
    else:
        number_connection += 1
        print(f"CONNECTION {number_connection}. Client IP, PORT:{client_ip_port}")
        list_clients.append(client_ip_port)
        # --- Step 5: Receiving information from the client
        msg_raw = cs.recv(2000)  # compulsory to specify the maximum number of bytes we allow to receive
        msg = msg_raw.decode()  # for decoding the bytes into a text message

        print("Message received:", end="")
        termcolor.cprint(msg, "green")

        # -- Step 6: Send a response messsage to the client
        response = f"ECHO: {msg}  "
        cs.send(response.encode())  # you must encode the msg into bytes

        if number_connection == 5:
            print("The following clients has connecteds to the server:")
            clients = 0
            for i in list_clients:
                print(f"CLient {clients}: {i}")
                clients += 1

        cs.close()
