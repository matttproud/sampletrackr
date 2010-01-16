#!/usr/bin/python2.4

import sys

from google.appengine.ext import db
from google.appengine.tools import bulkloader

import models

def _DecodeString(string):
  return str(string).decode('utf-8')

def _DecodeToNone(incoming):
  return None

class SampleSourceLoader(bulkloader.Loader):
  def __init__(self):
    mapping_specification = [
        ('title', _DecodeString),
        ('classification', _DecodeString),
        ]
    super(SampleSourceLoader, self).__init__(
        'SampleSource', mapping_specification)


class ContentClassificationLoader(bulkloader.Loader):
  def __init__(self):
    mapping_specification = [
        ('title', _DecodeString),
        ('description', lambda x: 'Unknown'.decode('utf-8')),
        ('creator', lambda x: None),
        ]
    super(ContentClassificationLoader, self).__init__(
        'ContentClassification', mapping_specification)

def _GetContentClassificationByName(classification_name):
  classifications = db.GqlQuery(
    'SELECT * FROM ContentClassification WHERE title = :1', classification_name)
  if classifications.count() == 0:
    classification = models.ContentClassification(title=classification_name)
    db.put(classification)
    return classification
  else:
    return classifications[0]

def _GetSampleSourceByName(sample_source_name):
  sample_source_name = _DecodeString(sample_source_name)
  samples = db.GqlQuery(
    'SELECT * FROM SampleSource WHERE title = :1', sample_source_name)
  if samples.count() == 0:
    raise Exception('Non-existent sample source %s' % sample_source_name)
  else:
    return samples[0]


class SampleSourceLoader(bulkloader.Loader):
  def __init__(self):
    mapping_specification = [
        ('title', _DecodeString),
        ('classification', _GetContentClassificationByName),
        ('creator', lambda x: None),
        ]
    super(SampleSourceLoader, self).__init__(
        'SampleSource', mapping_specification)

class CueClassificationLoader(bulkloader.Loader):
  def __init__(self):
    mapping_specification = [
      ('title', _DecodeString),
      ('description', _DecodeString),
      ]
    super(CueClassificationLoader, self).__init__(
      'CueClassification', mapping_specification)

class SampleConsumerLoader(bulkloader.Loader):
  _MAPPING_SPECIFICATION = [
    ('title', _DecodeString),
    ('classification', _GetContentClassificationByName),
    ('creator', _DecodeToNone),]

  def __init__(self):
    super(SampleConsumerLoader, self).__init__(
      'SampleConsumer', self._MAPPING_SPECIFICATION)

class SampleLoader(bulkloader.Loader):
  def __init__(self):
    mapping_specification = [
      ('text', _DecodeString),
      ('source', _GetSampleSourceByName),
      ('creator', _DecodeToNone),
      ]
    super(SampleLoader, self).__init__(
      'Sample', mapping_specification)

loaders = [ContentClassificationLoader, SampleSourceLoader,
           CueClassificationLoader, SampleConsumerLoader,
           SampleLoader,]
