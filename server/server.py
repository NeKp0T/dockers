from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(self.get_page())

    def get_page(self):
        res = BytesIO()
        with open("main.html", "rb") as f:
            while True:
                buf = f.read(1024)
                if buf: 
                    res.write(buf)
                else:
                    break
        return res.getvalue()
        


httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()

