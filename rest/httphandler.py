import http.server
import socketserver
import sys
import os, os.path

import cherrypy

class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        return open('index.html')

class StringGeneratorWebService(object):
	exposed = True

	@cherrypy.tools.accept(media='text/plain')
	
	def GET(self):
		return cherrypy.session['mystring']

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
		'/': {
			'tools.sessions.on': True,
			'tools.response_headers.on': os.path.abspath(os.getcwd())
		},
		'/rest': {
			'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
			'tools.sessions.on': True,
			'tools.response_headers.on': True,
			'tools.response_headers.headers': [('Content-Type', 'text/plain')],
		}
	}

	webapp = StringGenerator()
	webapp.generator = StringGeneratorWebService()
	cherrypy.quickstart(webapp, '/', conf)