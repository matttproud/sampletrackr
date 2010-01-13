#!/usr/bin/python2.4
"""Facade around the standard logging infrastructure for style compliance."""

import logging

def _DeferToLogging(method_name):
  sanitized_name = method_name.lower()

  real_call = getattr(logging, sanitized_name, None)

  if real_call:
    def Wrapped(format, *args):
      real_call(format % tuple(args))

    return Wrapped
  
  return None
    
setattr(logging, 'Info', _DeferToLogging('info'))
setattr(logging, 'Error', _DeferToLogging('error'))
