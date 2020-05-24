import http.client
import termcolor
import json

def menu():
    print("1 - /listSpecies (limit)")
    print("2 - /karyotype ")
    print("3 - /chromosomeLength")
    print("4 - /geneSeq")
    print("5 - /geneInfo")
    print("6 - /geneCalc")
    print("7 - /geneList")
    print("8 - Exit")

def client(client_request):
    PORT = 8080
    SERVER = 'localhost'
    print(f"\nConnecting to server: {SERVER}:{PORT}\n")
    conn = http.client.HTTPConnection(SERVER, PORT)
    try:
        conn.request("GET", client_request + "&json=1")
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()
    r1 = conn.getresponse()
    print(f"Response received!: {r1.status} {r1.reason}\n")
    data1 = r1.read().decode("utf-8")
    data = json.loads(data1)
    termcolor.cprint(f"CONTENT: {data}", "blue")

options = True
while options:
    print("Client for proving API REST.")
    menu()
    option = int(input("Choose an option from the menu: "))

    if option == 1:
        limit_parameter = input("Number of species to show [optional]: ")
        request = "/listSpecies?limit=" + limit_parameter
        client(request)

    elif option == 2:
        specie_parameter = input("Choose specie: ")
        request = "/karyotype?specie=" + specie_parameter
        client(request)

    elif option == 3:
        specie_parameter = input("Choose specie: ")
        chr_parameter = input("Choose chromosome: ")
        request = f"/chromosomeLength?specie={specie_parameter}&chromo={chr_parameter}"
        client(request)

    elif option == 4:
        gene_parameter = input("Choose a human gene: ")
        request = "/geneSeq?gene=" + gene_parameter
        client(request)

    elif option == 5:
        gene_parameter = input("Choose a human gene: ")
        request = "/geneInfo?gene=" + gene_parameter
        client(request)

    elif option == 6:
        gene_parameter = input("Choose a human gene: ")
        request = "/geneCalc?gene=" + gene_parameter
        client(request)

    elif option == 7:
        chr_parameter = input("Choose a human chromosome: ")
        start_parameter = input("Choose the start point: ")
        end_parameter = input("Choose the end point: ")
        request = f"/geneList?chromo={chr_parameter}&start={start_parameter}&end={end_parameter}"
        client(request)

    elif option == 8:
        options = False
    else:
        print("Choose a valid option between 1-7 or exit the client (8)")








