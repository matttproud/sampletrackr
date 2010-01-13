#!/usr/bin/python2.4

import logging
import os

import log

import models
import utilities

from django import http

from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

def _RenderBaseFromContent(**expansions):
  base_resource = utilities.GetResource('template/base.template')
  return template.render(base_resource, expansions)


class Main(webapp.RequestHandler):
  def get(self):
    page = utilities.GetResource('template/main.template')
    page_content = template.render(page, {})
    entire_content = _RenderBaseFromContent(
        content=page_content, navigation_name='home')
    self.response.out.write(entire_content)


class About(webapp.RequestHandler):
  def get(self, page_name):
    page = utilities.GetResource('template/about/' + page_name + '.template')

    if page:
      page_content = template.render(page, {})

      entire_content = _RenderBaseFromContent(
          content=page_content, navigation_name=page_name)

      self.response.out.write(entire_content)

    else:
      logging.info('Requested non-existent page %s.' % page_name)
      self.error(404)


class Source(webapp.RequestHandler):
  def get(self, page_name):
    if page_name == 'search':
      sort_criterion = self.request.get('sort')
      if not sort_criterion in ('classification', 'title'):
        sort_criterion = 'title'
      sources = models.SampleSource.all()
      sources.order(sort_criterion)

      page = utilities.GetResource('template/source/search.template')

      page_content = template.render(page, {'sources':sources})

      entire_content = _RenderBaseFromContent(
          content=page_content, navigation_name=page_name)

      self.response.out.write(entire_content)
    else:
      self.error(404)


class Use(webapp.RequestHandler):
  def get(self, page_name):
    self.error(404)
