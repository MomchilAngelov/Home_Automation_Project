import http.server
import socketserver
import sys

ENDPOINT = "/rest/"

class HttpHandler(http.server.BaseHTTPRequestHandler):
	
	def do_GET(self):

		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()

		# Send message back to client
		if self.path == ENDPOINT + "test":
			self.wfile.write(b'<h2>REST is working</h2>')

		if self.path == ENDPOINT + "configure":
			self.send_response(200)
			self.path = "init_configuration.html"

		return


	def do_POST(self):
		if self.path == ENDPOINT + "send":
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

