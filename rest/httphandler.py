import http.server
import socketserver
import sys
import os, os.path

import cherrypy


class StringGenerator(object):
	def light_lamp(self):
		global is_lit
		is_lit = not is_lit
		GPIO.output(lamp_pin, is_lit)

	@cherrypy.expose
	def index(self):
		return open('index.html')

	@cherrypy.expose
	def activate(self):
		cherrypy.response.headers['Content-Type'] = 'text/plain'
		return("HAHAH")
		# return open('index.html')

	@cherrypy.expose
	def light(self):
		GPIO.setmode(GPIO.BOARD)

		is_lit = False
		lamp_pin = 22
		GPIO.setup(lamp_pin, GPIO.OUT)


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
		},
		'/activate': {
			'tools.sessions.on': True,
			'tools.response_headers.on': os.path.abspath(os.getcwd())
		}
	}

	webapp = StringGenerator()
	webapp.generator = StringGeneratorWebService()
	cherrypy.quickstart(webapp, '/', conf)