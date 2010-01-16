#!/usr/bin/python2.4

from google.appengine.ext import db
from google.appengine.ext.db import polymodel

# TODO(mtp): Migrate this to a denormalized model after we are happy with the
#            fundamentals.


class ContentClassification(db.Model):
  """This describes the type of sample source."""
  # The short title of the classification.
  # Examples:
  # - "An Actor"
  # - "Video Game"
  # - "Celebutante"
  # - "Politician"
  # - "Criminal"
  # - "Text"
  title = db.StringProperty()
  # A verbose description of the classification.
  # Examples:
  # - "This type of text is not historically verified."
  description = db.StringProperty()
  #
  creator = db.UserProperty()


class SampleSource(db.Model):
  """Models a sample source."""
  # This is the title of the sample source.
  # Examples:
  # - "John Romero"
  # - "Doom II"
  title = db.StringProperty()
  #
  classification = db.ReferenceProperty(ContentClassification)
  #
  creator = db.UserProperty()


class SampleConsumer(db.Model):
  # The short title of the entity using a sample.
  # Examples:
  # - "My Band Name"
  # - "My Film Name"
  title = db.StringProperty()
  #
  classification = db.ReferenceProperty(ContentClassification)
  #
  creator = db.UserProperty()


class CueClassification(db.Model):
  #
  title = db.StringProperty()
  #
  description = db.StringProperty()



class Cue(polymodel.PolyModel):
  #
  classification = db.ReferenceProperty(CueClassification)
  #
  creator = db.UserProperty()


class TemporalCue(Cue):
  #
  offset_in_seconds = db.IntegerProperty()


class TextualCue(Cue):
  #
  offset_in_pages = db.IntegerProperty()


class Sample(db.Model):
  #
  text = db.TextProperty()
  #
  source = db.ReferenceProperty(SampleSource)
  #
  creator = db.UserProperty()

class SampleInstance(db.Model):
  # What about album and track information?
  #
  sample = db.ReferenceProperty(Sample)
  #
  sample_user = db.ReferenceProperty(SampleConsumer)
  #
  creator = db.UserProperty()
  #
  cue = db.ReferenceProperty(Cue)
