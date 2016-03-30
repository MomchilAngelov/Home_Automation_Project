import http.server
import socketserver
import sys

class HttpHandler(http.server.BaseHTTPRequestHandler):

	def __init__(self, host, port):
		self.PORT = int(port)
		self.Handler = http.server.SimpleHTTPRequestHandler
		self.httpd = None

	def run(self):
		self.httpd = socketserver.TCPServer(("", self.PORT), self.Handler)
		print("serving at port", self.PORT)
		self.httpd.serve_forever()

	def do_GET(self):
		if self.path=="/":
			self.path="/index.html"

	def do_POST(self):
		if self.path=="/send":
			form = cgi.FieldStorage(
				fp=self.rfile, 
				headers=self.headers,
				environ={'REQUEST_METHOD':'POST',
							'CONTENT_TYPE':self.headers['Content-Type'],
			})
			self.send_response(200)
			self.end_headers()


h = HttpHandler("localhost", sys.argv[1])
h.run()