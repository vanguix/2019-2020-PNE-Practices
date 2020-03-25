import http.server
import socketserver
import termcolor
from pathlib import Path
from Seq1 import Seq

# Define the Server's port
PORT = 8080

sequence_list = ["ACT\n", "TTT\n", "AAA\n", "CCC\n", "GGG\n"]
# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        path = self.requestline.split()[1]
        arguments = path.split('?')
        firts_argument = arguments[0]

        if firts_argument == "/":
            contents = Path("form-4.html").read_text()
            error_code = 200

        elif firts_argument == "/ping":
            contents = f"""
                        <!DOCTYPE html>
                        <html lang="en">
                        <head>
                            <meta charset="utf-8">
                            <title>RESULT</title>
                        </head>
                        <body>
                        <h1>PING OK!</h1>
                        <p>The SEQ02 server is running...</p>
                        <a href="/">Main page</a>
                        </body></html>
                        """
            error_code = 200
        elif firts_argument == "/get":
            second_argument = arguments[1]
            value = second_argument.split("=")[1]
            value = int(value)
            contents = f"""
                        <!DOCTYPE html>
                        <html lang="en">
                        <head>
                            <meta charset="utf-8">
                            <title>RESULT</title>
                        </head>
                        <body>
                        <h1>Sequence number {value}</h1>
                        <p>{sequence_list[value]}</p>
                        <a href="/">Main page</a>
                        </body></html>
                        """
            error_code = 200
        elif firts_argument == "/gene":
            folder = "../Session-04/"
            second_argument = arguments[1]
            value = second_argument.split("=")[1]
            gene = Seq()
            sequence = gene.read_fasta(folder + value + ".txt")
            contents = f"""
                        <!DOCTYPE html>
                        <html lang="en">
                        <head>
                            <meta charset="utf-8">
                            <title>RESULT</title>
                        </head>
                        <body>
                        <h1>Gene: {value}</h1>
                        <textarea reandonly rows="20" cols="80">{sequence}</textarea>
                        <br>
                        <a href="/">Main page</a>
                        </body></html>
                        """
            error_code = 200

        elif firts_argument == "/operation":
            second_argument = arguments[1]
            sequence, selection = second_argument.split("&")
            value_sequence = sequence.split("=")[1]
            value_selection = selection.split("=")[1]
            sequence = Seq(value_sequence)
            if value_selection == "Info":
                contents = f"""
                        <!DOCTYPE html>
                        <html lang="en">
                        <head>
                            <meta charset="utf-8">
                            <title>RESULT</title>
                        </head>
                        <body>
                        <h2>Sequence</h2>
                        <p>{value_sequence}</p>
                        <h2>Operation</h2>
                        <p>{value_selection}</p>
                        <h2>Result</h2>
                        <p>Total length: {sequence.len()}</p>
                        <p>A: {sequence.seq_count_base("A")[0]} ({sequence.seq_count_base("A")[1]}%)</p>
                        <p>C: {sequence.seq_count_base("C")[0]} ({sequence.seq_count_base("C")[1]}%)</p>
                        <p>G: {sequence.seq_count_base("G")[0]} ({sequence.seq_count_base("G")[1]}%)</p>
                        <p>T: {sequence.seq_count_base("T")[0]} ({sequence.seq_count_base("T")[1]}%)</p>
                        <br>
                        <a href="/">Main page</a>
                        </body></html>
                        """
            elif value_selection == "Comp":
                contents = f"""
                            <!DOCTYPE html>
                            <html lang="en">
                            <head>
                                <meta charset="utf-8">
                                <title>RESULT</title>
                            </head>
                            <body>
                            <h2>Sequence</h2>
                            <p>{value_sequence}</p>
                            <h2>Operation</h2>
                            <p>{value_selection}</p>
                            <h2>Result</h2>
                            <p>{sequence.complement()}</p>
                            <br>
                            <a href="/">Main page</a>
                            </body></html>
                            """
            elif value_selection == "Rev":
                contents = f"""
                            <!DOCTYPE html>
                            <html lang="en">
                            <head>
                                <meta charset="utf-8">
                                <title>RESULT</title>
                            </head>
                            <body>
                            <h2>Sequence</h2>
                            <p>{value_sequence}</p>
                            <h2>Operation</h2>
                            <p>{value_selection}</p>
                            <h2>Result</h2>
                            <p>{sequence.reverse()}</p>
                            <br>
                            <a href="/">Main page</a>
                            </body></html>
                            """
            error_code = 200

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
