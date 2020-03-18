from Client0 import Client

# -- Parameters of the server to talk to
IP = "127.0.0.1"
PORT = 8083

# -- Create a client object
c = Client(IP, PORT)
seq0 = "ACT"
print("-----| Practice 3, Exercise 7 |-----")

print("Testing PING...")
print(c.talk("PING"))

print("Testing GET...")
print(c.talk("GET 0"))
print(c.talk("GET 1"))
print(c.talk("GET 2"))
print(c.talk("GET 3"))
print(c.talk("GET 4"))

print("Testing INFO...")
print(c.talk(f"INFO {seq0}"))

print("Testing COMP...")
print(c.talk(f"COMP {seq0}"))

print("Testing REV...")
print(c.talk(f"REV {seq0}"))

print("Testing GENE...")
print(c.talk("GENE U5"))
print(c.talk("GENE ADA"))
print(c.talk("GENE FRAT1"))
print(c.talk("GENE FXN"))
print(c.talk("GENE RNU6_269P"))