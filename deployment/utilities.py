#!/usr/bin/python2.4

import logging
import os


def GetResource(resource_name, os_path_module=os.path):
  logging.debug('Attempting to find %s...' % resource_name)

  resource_path = os_path_module.join(os_path_module.dirname(__file__),
                                      resource_name)
  if os_path_module.exists(resource_path):
    return resource_path
  else:
    logging.info('Resource %s does not exist.' % resource_name)
    return None


