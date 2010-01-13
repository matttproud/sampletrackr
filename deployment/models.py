#!/usr/bin/python2.4

from google.appengine.ext import db


class SampleSource(db.Model):
  """Models a sample source."""
  # This is the title of the sample source.
  # Examples:
  # - "John Romero"
  # - "Doom II"
  title = db.StringProperty()
  # This is the type of the sample source---i.e., what it is.
  # It is free-form text.
  # Examples:
  # - "Video Game"
  # - "Celebutante"
  # - "Politician"
  # - "Criminal"
  # - "Text"
  classification = db.StringProperty()


class SampleUser(db.Model):
  title = db.StringProperty()
  classification = db.StringProperty()

class SampleInstance(db.Model):
  sample_source = db.ReferenceProperty(SampleSource)
  sample_user = db.ReferenceProperty(SampleUser)
  cue = db.StringProperty()
