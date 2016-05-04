import http.server
import socketserver
import sys

import cherrypy

class StringGeneratorWebService(object):
	exposed = True

	@cherrypy.tools.accept(media='text/plain')
	
	def GET(self):
		return "Hello there"

	def POST(self, length=8):
		some_string = ''.join(random.sample(string.hexdigits, int(length)))
		cherrypy.session['mystring'] = some_string
		return some_string

	def PUT(self, another_string):
		cherrypy.session['mystring'] = another_string

	def DELETE(self):
		cherrypy.session.pop('mystring', None)

if __name__ == '__main__':
	conf = {
		'global': {
			'server.socket_host': '127.0.0.1',
		},
		'rest': {
			'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
			'tools.sessions.on': True,
			'tools.response_headers.on': True,
			'tools.response_headers.headers': [('Content-Type', 'text/plain')],
		}
	}
	
	cherrypy.quickstart(StringGeneratorWebService, '/', "server.conf")