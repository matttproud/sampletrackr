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


class ContentClassificationLoader(bulkloader.Loader):
  def __init__(self):
    mapping_specification = [
        ('title', lambda x: x.decode('utf-8')),
        ('description', lambda x: 'Unknown'.decode('utf-8')),
        ('creator', lambda x: None),
        ]
    super(ContentClassificationLoader, self).__init__(
        'ContentClassification', mapping_specification)

def _GetClassificationFromName(classification_name):
  classifications = db.GqlQuery(
    'SELECT * FROM ContentClassification WHERE title = :1', classification_name)
  if classifications.count() == 0:
    classification = models.ContentClassification(title=classification_name)
    db.put(classification)
    return classification
  else:
    return classifications[0]


class SampleSourceLoader(bulkloader.Loader):
  def __init__(self):
    mapping_specification = [
        ('title', lambda x: x.decode('utf-8')),
        ('classification', _GetClassificationFromName),
        ('creator', lambda x: None),
        ]
    super(SampleSourceLoader, self).__init__(
        'SampleSource', mapping_specification)

loaders = [ContentClassificationLoader, SampleSourceLoader]
