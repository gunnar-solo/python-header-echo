# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

hostName = "0.0.0.0"
serverPort = 8000

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        headers = {}
        for h in self.headers:
            headers[h] = self.headers[h]

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(bytes(json.dumps(headers), "utf-8"))

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")