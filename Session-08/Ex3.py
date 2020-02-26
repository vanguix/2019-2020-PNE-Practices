import socket

# SERVER IP, PORT
PORT = 8080
IP = "192.168.1.135"

while True:
    # -- Ask the user for the message
    print("Please enter a message\n")
    # -- Create the socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # -- Establish the connection to the Server
    s.connect((IP, PORT))
    # -- Send the user message
    msg = s.recv(2048)
    print("Please enter a message\n")
    print(msg.decode("utf-8"))
    # -- Close the socket
    s.close()
