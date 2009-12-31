#!/usr/bin/python2.4

import logging

import utilities

from django import http

from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app


class Main(webapp.RequestHandler):
  def get(self):
    resource = utilities._GetResource('base.template')
    self.response.out.write(template.render(resource, {'navigation_name': 'Home'}))


class About(webapp.RequestHandler):
  def GetHistory(self, dispatch_method_name):   
    self.response.out.write(template.render(resource, {'title' : dispatch_method_name}))


  def get(self, page):
    logging.info(page)
    resource = utilities._GetResource('base.template')
    
    requested_page = str(page).lower().capitalize()
    logging.info(requested_page)
    dispatch_method_name = 'Get%s' % requested_page
    dispatch_method = getattr(self, dispatch_method_name, None)
    logging.info(dispatch_method_name)
    logging.info(dispatch_method)
    if not dispatch_method:
      logging.info('absent')
      return
    logging.info('present')

    dispatch_method(self, dispatch_method_name)

