import http.client
import json
import termcolor
from Seq1 import Seq
list_bases = ["A","C","G","T"]
genes = {'FRAT1': 'ENSG00000165879',
         'ADA': 'ENSG00000196839',
         'FXN': 'ENSG00000165060',
         'RNU6_269P': 'ENSG00000212379',
         'MIR633': 'ENSG00000207552',
         'TTTY4C': 'ENSG00000228296',
         'RBMY2YP': 'ENSG00000227633',
         'FGFR3': 'ENSG00000068078',
         'KDR': 'ENSG00000128052',
         'ANK2': 'ENSG00000145362'}

gene = input("Write the gene name:")

server = "rest.ensembl.org"
endpoint = "/sequence/id/"
id = genes[gene]
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
print(gene)
termcolor.cprint(f"Description: ", "green", end="")
print(description)

sequence = Seq(bases)
termcolor.cprint(f"Total lenght: ", "green", end="")
print(sequence.len())

counter = 0

for base in list_bases:
    termcolor.cprint(f"{base}: ", "blue", end="")
    print(f"{sequence.seq_count_base(base)[0]} ({sequence.seq_count_base(base)[1]}%)")

    if sequence.seq_count_base(base)[0] > counter:
        counter = sequence.seq_count_base(base)[0]
        mostfrbase = base

termcolor.cprint(f"Most frequent Base: ", "green", end="")
print(mostfrbase)

