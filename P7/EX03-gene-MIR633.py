import http.client
import json
import termcolor


server = "rest.ensembl.org"
endpoint = "/sequence/id/"
id = "ENSG00000207552"
params = "?content-type=application/json"
URL = server + endpoint + id + params

print()
print(f"Server: {server}")
print(f"URL: {URL}")

conn = http.client.HTTPConnection(server)

try:
    conn.request("GET", endpoint + id + params)
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

r1 = conn.getresponse()

print(f"Response received!: {r1.status} {r1.reason}\n")

data1 = r1.read().decode("utf-8")

response = json.loads(data1)
description = response["desc"]
bases = response["seq"]

termcolor.cprint(f"Gene: ", "green", end="")
print("MIR633")
termcolor.cprint(f"Description: ", "green", end="")
print(description)
termcolor.cprint(f"Bases: ", "green", end="")
print(bases)
