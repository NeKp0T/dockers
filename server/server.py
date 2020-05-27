from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO
import sys

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"qweqew\n")
        # self.wfile.write(self.get_page())

    def get_page(self):
        res = BytesIO()
        with open("./contents/main.html", "rb") as f:
            while True:
                buf = f.read(1024)
                if buf: 
                    res.write(buf)
                else:
                    break
        return res.getvalue()
        

port = int(sys.argv[1])
print("starting server on " + str(port))
for i in range(5):
    print("qe" * 10)
httpd = HTTPServer(('localhost', port), SimpleHTTPRequestHandler)
httpd.serve_forever()

