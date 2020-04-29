import http.server
import socketserver
import termcolor
from pathlib import Path
from Seq1 import Seq
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
            if number == "":
                contents = f"""<!DOCTYPE html>
                               <html lang="en">
                               <head>
                                   <meta charset="UTF-8">
                                   <title>SPECIES</title>
                               </head>
                               <body style="background-color: lightyellow;">
                                <p>Total number of species in the ensembl is: 267</p>
                                <p>The limit you have selected is:{number}</p>
                                <p>The names of the species are:</p>
                               </body>
                               </html>"""
                for element in species:
                    contents += f"""<p> - {element["common_name"]}</p> """

            elif 267 >= int(number):
                contents=f"""<!DOCTYPE html>
                            <html lang="en">
                            <head>
                                <meta charset="UTF-8">
                                <title>SPECIES</title>
                            </head>
                            <body style="background-color: lightyellow;">
                                <p>Total number of species in the ensembl is: 267</p>
                                <p>The limit you have selected is:{number}</p>
                                <p>The names of the species are:</p>
                            </body>
                            </html>"""
                counter = 0
                for element in species:
                    if counter < int(number):
                        contents += f"""<p> - {element["common_name"]}</p> """
                    counter += 1

            else:
                contents = f"""<!DOCTYPE html>
                                   <html lang="en">
                                   <head>
                                       <meta charset="UTF-8">
                                       <title>SPECIES</title>
                                   </head>
                                   <body style="background-color: lightyellow;">
                                    <p>Total number of species in the ensembl is: 267</p>
                                    <p>The limit you have selected is:{number}</p>
                                    <p>The names of the species are:</p>
                                   </body>
                                   </html>"""
                for element in species:
                    contents += f"""<p> - {element["common_name"]}</p> """



        #elif firts_argument == "/karyotype":
        else:
            contents = Path('Error.html').read_text()
            error_code = 404

        # Generating the response message
        self.send_response(error_code)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()