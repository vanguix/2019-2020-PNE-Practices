import http.server
import socketserver
import termcolor
from pathlib import Path
import http.client
import json

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

def html_format(colour):
    return f"""<!DOCTYPE html>
           <html lang="en">
           <head>
               <meta charset="UTF-8">
               <title>BROWSING HUMAN AND VERTEBRATES GENOME</title>
           </head>
           <body style="background-color: {colour};">
           </body>
           </html>"""

PORT = 8080


socketserver.TCPServer.allow_reuse_address = True


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        termcolor.cprint(self.requestline, 'green')

        path = self.requestline.split()[1]
        arguments = path.split('?')
        firts_argument = arguments[0]

        if firts_argument == "/":
            contents = Path("main-page.html").read_text()
            error_code = 200

        elif firts_argument == "/listSpecies":
            error_code = 200
            second_argument = arguments[1]
            number = second_argument.split("=")[1]
            data = get_data("info/species?content-type=application/json")
            species = data["species"]
            contents = html_format("lightyellow")
            contents += f"""<p>Total number of species in the ensembl is: 267</p>"""
            contents += f"""<p>The limit you have selected is:{number}</p>"""
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

        elif firts_argument == "/karyotype":
            error_code = 200
            second_argument = arguments[1]
            specie = second_argument.split("=")[1]
            data = get_data(f"/info/assembly/{specie}?content-type=application/json")
            karyotype = data["karyotype"]
            contents = html_format("lightgreen")
            contents += f"""<p>The names of the chromosomes are:</p>"""
            for chromosome in karyotype:
                contents += f"""<p> - {chromosome}</p>"""

        elif firts_argument == "/chromosomeLength":
            error_code = 200
            second_argument = arguments[1]
            specie, chromo = second_argument.split("&")
            specie_name = specie.split("=")[1]
            chromo_name = chromo.split("=")[1]
            data = get_data(f"/info/assembly/{specie_name}?content-type=application/json")
            information = data["top_level_region"]
            contents = html_format("salmon")
            for chromosome in information:
                if chromosome["coord_system"] == "chromosome":
                    if chromosome["name"] == chromo_name:
                        contents += f"""<p> The length of the chromosome is: {chromosome["length"]}</p>"""

        elif firts_argument == "/geneSeq":
            error_code = 200
            second_argument = arguments[1]
            gene = second_argument.split("=")[1]
            gene_id = get_data(f"""/xrefs/symbol/homo_sapiens/{gene}?content-type=application/json""")[0]["id"]
            data = get_data(f"""/sequence/id/{gene_id}?content-type=application/json""")
            contents = html_format("pink")
            contents += f'<p> The sequence of gene {gene} is: </p>'
            contents += f'<textarea rows = "100" "cols = 500"> {data["seq"]} </textarea>'

        else:
            contents = Path('Error.html').read_text()
            error_code = 404

        self.send_response(error_code)
        self.send_header('Content-Type', 'text/html')
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
