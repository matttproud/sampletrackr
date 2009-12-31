#!/usr/bin/python2.4

import os

from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

# class Artist(db.Model):
#   name = db.StringProperty()

# class Root(webapp.RequestHandler):
#   def get(self):
#     self.response.headers['Content-Type'] = 'text/plain'
#     query = db.GqlQuery('SELECT * FROM Artist WHERE name >= :1 AND name < :2',
#                         u'front', u'front ')
#     for result in query:
#       self.response.out.write('Name: %s', result.name)


def _GetResource(resource_name, os_path_module=os.path):
  return os_path_module.join(os_path_module.dirname(__file__), resource_name)


class Main(webapp.RequestHandler):
  def get(self):
    resource = _GetResource('main.html')
    self.response.out.write(template.render(resource, {}))


application = webapp.WSGIApplication(
    [('/', Main)],
    debug=True)

def main():
  run_wsgi_app(application)

if __name__ == '__main__':
  main()
