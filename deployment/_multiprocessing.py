#!/usr/bin/python2.4

# GAE does not like Python 2.6.

try:
  from _multiprocessing import *
except ImportError, e:
  import multiprocessing
