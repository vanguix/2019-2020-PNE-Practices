import http.server
import socketserver
import termcolor
from pathlib import Path

# Define the Server's port
PORT = 8080


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
        #html_functions = arguments[1]
        #first_function = html_functions.split("&")[0]
        #second_function = html_functions.split("&")[1]
        #chk, checkpoint = second_function.split("=")


        if firts_argument == "/":
            contents = Path("form-EX02.html").read_text()
            error_code = 200

        elif firts_argument == "/echo":
            text = path.split("=")[1]
            value= text.split("&")[0]
            error_code = 200
            if "&" in text:
                contents = f"""
                        <!DOCTYPE html>
                        <html lang="en">
                        <head>
                            <meta charset="utf-8">
                            <title>RESULT</title>
                        </head>
                        <body>
                        <h2>Received message:</h2>
                        <p>{value.upper()}</p>
                        <a href="/">Main page</a>
                        </body></html>
                        """
            else:
                contents = f"""
                        <!DOCTYPE html>
                        <html lang="en">
                        <head>
                            <meta charset="utf-8">
                            <title>RESULT</title>
                        </head>
                        <body>
                        <h2>Received message:</h2>
                        <p>{value}</p>
                        <a href="/">Main page</a>
                        </body></html>
                        """
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