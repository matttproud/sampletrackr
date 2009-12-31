#!/usr/bin/python2.4

import utilities

from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app


class Main(webapp.RequestHandler):
  def get(self):
    resource = utilities._GetResource('main.html')
    self.response.out.write(template.render(resource, {}))


class About(webapp.RequestHandler):
  def get(self):
    resource = utilities._GetResource('main.html')
    self.response.out.write(template.render(resource, {}))

