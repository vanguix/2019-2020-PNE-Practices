from Client0 import Client

# -- Parameters of the server to talk to
IP = "127.0.0.1"
PORT = 8083

# -- Create a client object
c = Client(IP, PORT)

print(c.talk("PING"))
print(c.talk("GET 2"))
print(c.talk("INFO AGTCTT"))
print(c.talk("COMP AAAAAAA"))
print(c.talk("REV AGTCCC"))
print(c.talk("GENE U5"))