#!/usr/bin/python2.4

import sys

from google.appengine.ext import db
from google.appengine.tools import bulkloader

import models

class SampleSourceLoader(bulkloader.Loader):
  def __init__(self):
    mapping_specification = [
        ('title', lambda x: x.decode('utf-8')),
        ('classification', lambda x: x.decode('utf-8')),
        ]
    super(SampleSourceLoader, self).__init__(
        'SampleSource', mapping_specification)

loaders = [SampleSourceLoader]
