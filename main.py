#!/usr/bin/python2.4

import handlers

from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app


application = webapp.WSGIApplication(
    [('/', handlers.Main),
     ('/about/.*', handlers.About),],
    debug=True)

def main():
  run_wsgi_app(application)

if __name__ == '__main__':
  main()
