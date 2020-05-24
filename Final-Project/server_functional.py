import http.server
import socketserver
import termcolor
from pathlib import Path
import http.client
import json
from Seq1 import Seq

list_bases = ["A", "C", "G", "T"]


def get_data(endpoint):
    PORT = 8080
    SERVER = 'rest.ensembl.org'
    print(f"\nConnecting to server: {SERVER}:{PORT}\n")
    conn = http.client.HTTPConnection(SERVER, timeout=100)
    try:
        conn.request("GET", endpoint)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()
    r1 = conn.getresponse()
    print(f"Response received!: {r1.status} {r1.reason}\n")
    data1 = r1.read().decode("utf-8")
    response = json.loads(data1)
    return response


def html_format(colour, title):
    return f"""<!DOCTYPE html>
           <html lang="en">
           <head>
               <meta charset="UTF-8">
               <title>{title}</title>
           </head>
           <body style="background-color: {colour};">
           </body>
           </html>"""

def dict_listSpecies(limit, list):
    contents = {
        "Total number of species": 267,
        "Limit selected": limit,
        "List of species": list
    }
    client_dict = json.dumps(contents)
    return client_dict

def dict_karyotype(list):
    contents = {
        "The names of the chromosomes are": list
    }
    client_dict = json.dumps(contents)
    return client_dict

def dict_chromosomeLength(length):
    contents = {
        "The length of the selected chromosome is": length
    }
    client_dict = json.dumps(contents)
    return client_dict

def dict_geneSeq(seq):
    contents = {
        "The sequence of the selected gen is": seq
    }
    client_dict = json.dumps(contents)
    return client_dict

def dict_geneInfo(start, end, length, id, chromo): #no me sale :(
    contents = {
        "The start point is": start,
        "The end point is": end,
        "The length of the gene is": length,
        "The ID of the gene is": id,
        "The chromosome of this gene is": chromo
    }
    client_dict = json.dumps(contents)
    return client_dict

def dict_geneCalc(length, list):
    contents = {
        "Total length of the gene is": length,
        "The percentage of each base in the sequence of this gene is"
        "A": list[0],
        "C": list[1],
        "G": list[2],
        "T": list[3]
    }
    client_dict = json.dumps(contents)
    return client_dict

def dict_geneList(list):
    contents = {
        "List of genes located in the introduced chromosome": list
    }
    client_dict = json.dumps(contents)
    return client_dict


PORT = 8080


socketserver.TCPServer.allow_reuse_address = True


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        termcolor.cprint(self.requestline, 'green')

        path = self.requestline.split()[1]
        arguments = path.split('?')
        firts_argument = arguments[0]

        try:
            if firts_argument == "/":
                contents = Path("main-page.html").read_text()
                self.send_response(200)

            elif firts_argument == "/listSpecies":
                second_argument = arguments[1]
                parameters = second_argument.split("&")
                data = get_data("info/species?content-type=application/json")["species"]
                if len(parameters) == 2:
                    parameter_1, json = second_argument.split("&")
                    number = parameter_1.split("=")[1]

                    if json == "json=1":
                        list = []
                        counter = 0
                        if number == "":
                            for element in data:
                                list.append(element["display_name"])
                                counter += 1
                            contents = dict_listSpecies(number, list)
                        elif 267 >= int(number):
                            for element in data:
                                if counter < int(number):
                                        list.append(element["display_name"])
                                        counter += 1
                                contents = dict_listSpecies(number, list)
                        else:
                            for element in data:
                                list.append(element["display_name"])
                                counter += 1
                            contents = dict_listSpecies(number, list)
                        self.send_response(200)
                    else:
                        contents = Path('Error.html').read_text()
                        self.send_response(404)

                elif len(parameters) == 1:
                    number = second_argument.split("=")[1]
                    species = data["species"]
                    contents = html_format("lightyellow", "List of species")
                    contents += f"""<h1> SPECIES ON DATABASE OF ENSEMBL </h1>"""
                    contents += f"""<p>Total number of species in the ensembl database is 267</p>"""
                    contents += f"""<p>The limit you have selected is: {number}</p>"""
                    contents += f"""<p>The names of the species are:</p>"""
                    if number == "":
                        for element in species:
                            contents += f"""<p> - {element["display_name"]}</p> """
                    elif 267 >= int(number):
                        counter = 0
                        for element in species:
                            if counter < int(number):
                                contents += f"""<p> - {element["display_name"]}</p> """
                            counter += 1
                    else:
                        for element in species:
                            contents += f"""<p> - {element["display_name"]}</p> """
                self.send_response(200)

            elif firts_argument == "/karyotype":
                second_argument = arguments[1]
                parameters = second_argument.split("&")
                if len(parameters) == 2:
                    parameter_1, json = second_argument.split("&")
                    specie = parameter_1.split("=")[1]
                    data = get_data(f"/info/assembly/{specie}?content-type=application/json")["karyotype"]

                    if json == "json=1":
                        list = []
                        for element in data:
                            list.append(element)
                        contents = dict_karyotype(list)
                        self.send_response(200)

                    else:
                        contents = Path('Error.html').read_text()
                        self.send_response(404)

                elif len(parameters) == 1:
                    specie = second_argument.split("=")[1]
                    data = get_data(f"/info/assembly/{specie}?content-type=application/json")
                    karyotype = data["karyotype"]
                    contents = html_format("lightgreen", "Karyotype")
                    contents += f"""<h1> KARYOTYPE </h1>"""
                    contents += f"""<p>The names of the chromosomes from {specie} are:</p>"""
                    for chromosome in karyotype:
                        contents += f"""<p> - {chromosome}</p>"""
                self.send_response(200)

            elif firts_argument == "/chromosomeLength":
                second_argument = arguments[1]
                arguments = second_argument.split("&")
                if len(arguments) == 3:
                    specie, chromo, json = second_argument.split("&")
                    specie_name = specie.split("=")[1]
                    chromo_name = chromo.split("=")[1]
                    data = get_data(f"/info/assembly/{specie_name}?content-type=application/json")

                    if json == "json=1":
                        info = data["top_level_region"]
                        contents = dict_chromosomeLength(0)
                        for element in info:
                            if element["name"] == chromo_name:
                                length = element["length"]
                                contents = dict_chromosomeLength(length)
                        self.send_response(200)

                    else:
                        contents = Path('Error.html').read_text()
                        self.send_response(404)

                elif len(arguments) == 2:
                    specie, chromo = second_argument.split("&")
                    specie_name = specie.split("=")[1]
                    chromo_name = chromo.split("=")[1]
                    data = get_data(f"/info/assembly/{specie_name}?content-type=application/json")
                    information = data["top_level_region"]
                    contents = html_format("salmon", "Chromosome length")
                    contents += "<h1> CHROMOSOME LENGTH </h1>"
                    for chromosome in information:
                        if chromosome["coord_system"] == "chromosome":
                            if chromosome["name"] == chromo_name:
                                c_lenght = chromosome['length']
                                contents += f"""<p> The length of the chromosome {chromo_name} is: {c_lenght}</p>"""
                    self.send_response(200)

            elif firts_argument == "/geneSeq":
                second_argument = arguments[1]
                parameters = second_argument.split("&")

                if len(parameters) == 2:
                    parameter_1, json = second_argument.split("&")
                    gene = parameter_1.split("=")[1]
                    gene_id = get_data(f"""/xrefs/symbol/homo_sapiens/{gene}?content-type=application/json""")[0]["id"]
                    data = get_data(f"""/sequence/id/{gene_id}?content-type=application/json""")
                    if json == "json=1":
                        contents = dict_geneSeq(data["seq"])
                        self.send_response(200)
                    else:
                        contents = Path('Error.html').read_text()
                        self.send_response(404)
                elif len(parameters) == 1:
                    gene = second_argument.split("=")[1]
                    gene_id = get_data(f"""/xrefs/symbol/homo_sapiens/{gene}?content-type=application/json""")[0]["id"]
                    data = get_data(f"""/sequence/id/{gene_id}?content-type=application/json""")
                    contents = html_format("pink", "Sequences")
                    contents += "<h1> SEQUENCES OF HUMAN GENES </h1>"
                    contents += f'<p> The sequence of gene {gene} is: </p>'
                    contents += f'<textarea rows = "100" "cols = 500"> {data["seq"]} </textarea>'
                self.send_response(200)

            elif firts_argument == "/geneInfo":
                second_argument = arguments[1]
                parameters = second_argument.split("&")
                if len(parameters) == 2:
                    parameter_1, json = second_argument.split("&")
                    gene = parameter_1.split("=")[1]
                    gene_id = get_data(f"""/xrefs/symbol/homo_sapiens/{gene}?content-type=application/json""")[0]["id"]
                    data = get_data(f"""/lookup/id/{gene_id}?content-type=application/json""")
                    if json == "json=1":
                        length = data["end"] - data["start"]
                        contents = dict_geneInfo(data["start"], data["end"], length, data["id"], data["seq_region_name"])
                        self.send_response(200)
                    else:
                        contents = Path('Error.html').read_text()
                        self.send_response(404)

                elif len(parameters) == 1:
                    gene = second_argument.split("=")[1]
                    gene_id = get_data(f"""/xrefs/symbol/homo_sapiens/{gene}?content-type=application/json""")[0]["id"]
                    data = get_data(f"""/lookup/id/{gene_id}?content-type=application/json""")
                    contents = html_format("plum", "Information")
                    contents += f'<h1>INFORMATION ABOUT HUMAN GENE {gene} </h1>'
                    contents += f'<p> The start point is: {data["start"]}</p>'
                    contents += f'<p> The end point is: {data["end"]}</p>'
                    contents += f'<p> The length of the gene is: {data["end"] - data["start"]}</p>'
                    contents += f'<p> The id of the gene is: {gene_id}</p>'
                    contents += f'<p> The gene is on chromosome {data["seq_region_name"]}</p>'
                    self.send_response(200)

            elif firts_argument == "/geneCalc":
                second_argument = arguments[1]
                parameters = second_argument.split("&")
                if len(parameters) == 2:
                    parameter_1, json = second_argument.split("&")
                    gene = parameter_1.split("=")[1]
                    gene_id = get_data(f"""/xrefs/symbol/homo_sapiens/{gene}?content-type=application/json""")[0]["id"]
                    data = get_data(f"""/sequence/id/{gene_id}?content-type=application/json""")
                    sequence = Seq(data["seq"])
                    if json == "json=1":
                        bases = []
                        for base in list_bases:
                            bases.append(sequence.seq_count_base(base)[1])
                        contents = dict_geneCalc(sequence.len(), bases)
                        self.send_response(200)
                    else:
                        contents = Path('Error.html').read_text()
                        self.send_response(404)

                elif len(parameters) == 1:
                    gene = second_argument.split("=")[1]
                    gene_id = get_data(f"""/xrefs/symbol/homo_sapiens/{gene}?content-type=application/json""")[0]["id"]
                    data = get_data(f"""/sequence/id/{gene_id}?content-type=application/json""")
                    sequence = Seq(data["seq"])
                    contents = html_format("lightblue", "Calculations")
                    contents += F"<h1> CALCULATIONS OF GENE {gene}</h1>"
                    contents += f"<p> Total length: {sequence.len()} </p>"
                    contents += "<p> Percentage of its bases: </p>"
                    for base in list_bases:
                        contents += f"<p>- {base}: {sequence.seq_count_base(base)[1]}%</p>"
                self.send_response(200)

            elif firts_argument == "/geneList":
                second_argument = arguments[1]
                parameters = second_argument.split("&")
                if len(parameters) == 4:
                    chromo, start, end, json = second_argument.split("&")
                    chromo_name = chromo.split("=")[1]
                    start_point = start.split("=")[1]
                    end_point = end.split("=")[1]
                    data = get_data(f"""/overlap/region/human/{chromo_name}:{start_point}-{end_point}?feature=gene;content-type=application/json""")
                    if json == "json=1":
                        list = []
                        for gene in data:
                            list.append(gene["external_name"])
                        contents = dict_geneList(list)
                        self.send_response(200)
                    else:
                        contents = Path('Error.html').read_text()
                        self.send_response(404)

                elif len(parameters) == 3:
                    chromo, start, end = second_argument.split("&")
                    chromo_name = chromo.split("=")[1]
                    start_point = start.split("=")[1]
                    end_point = end.split("=")[1]
                    data = get_data(f"""/overlap/region/human/{chromo_name}:{start_point}-{end_point}?feature=gene;content-type=application/json""")
                    contents = html_format("peachpuff", "List of genes")
                    contents += "<h1> LIST OF GENES </h1>"
                    contents += f"<p> Here is the list of some genes from chromosome {chromo_name}:</p>"
                    for gene in data:
                        contents += f'<p> - {gene["external_name"]}</p>'
                self.send_response(200)

        except (KeyError, TypeError, ValueError, IndexError):
            contents = Path('Error.html').read_text()
            self.send_response(404)

        endpoints = ["/", "/listSpecies", "/karyotype", "/chromosomeLength",
                     "/geneSeq", "/geneInfo", "/geneCalc", "/geneList"]

        if firts_argument in endpoints:
            if "json=1" in path:
                type = "application/json"
            else:
                type = "text/html"

        self.send_header('Content-Type', type)
        self.send_header('Content-Length', len(str.encode(contents)))
        self.end_headers()
        self.wfile.write(str.encode(contents))
        return


Handler = TestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()