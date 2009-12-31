#!/usr/bin/python2.4

import os

def _GetResource(resource_name, os_path_module=os.path):
  return os_path_module.join(os_path_module.dirname(__file__), resource_name)


