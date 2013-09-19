#!/usr/bin/env python

import os
import webapp2
import jinja2
import headers

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), "templates")))


class GoneHandler(webapp2.RequestHandler):
    def get(self):
    	self.response.status = 410
    	headers.set_cache_headers(self.response, 5 * 60)
    	template = jinja_environment.get_template('gone.html')

        self.response.write(template.render({}))

app = webapp2.WSGIApplication([
    ('/.*', GoneHandler)
], debug=True)
