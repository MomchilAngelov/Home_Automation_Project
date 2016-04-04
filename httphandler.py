import http.server
import socketserver
import sys

REDIRECTIONS = {"/slashdot/": "http://slashdot.org/", "/freshmeat/": "http://freshmeat.net/"}

class HttpHandler(http.server.BaseHTTPRequestHandler):

	def do_GET(self):

		self.send_response(200)
		# Send headers
		self.send_header('Content-type','text/html')
		self.end_headers()

		# Send message back to client
		# if self.path=="/":
		self.send_header("Location", REDIRECTIONS.get(self.path, "/index.html"))
		# self.path="/index.html"

		if self.path == "/configure":
			self.path = "/init_configuration.html"

		return


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



PORT = sys.argv[1]
httpd = http.server.HTTPServer(("95.111.79.35", int(PORT)), HttpHandler)
print("serving at port", PORT)

try:
	httpd.serve_forever()
except KeyboardInterrupt as e:
	pass

