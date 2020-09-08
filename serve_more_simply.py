from http.server import HTTPServer, BaseHTTPRequestHandler
import time
hostName = "0.0.0.0"
serverPort = 8000
class MyServer(BaseHTTPRequestHandler):
    buffer = 1
    log_file = open('logfile2.txt', 'w', buffer)
    def log_message(self, format, *args):
        self.log_file.write("%s - - [%s] %s\n" %
                            (self.client_address[0],
                             self.log_date_time_string(),
                             format%args))

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))


#    def do_POST(self):
#        content_length = int(self.headers['Content-Length'])
#        body = self.rfile.read(content_length)
#        self.send_response(200)
#        self.end_headers()
#        response = BytesIO()
#        response.write(b'Thank you for that POST request.')
#        response.write(b'I received: ')
#        response.write(body)
#        self.wfile.write(response.getvalue())
if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server.close()
    print("Server stopped.")
httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()

