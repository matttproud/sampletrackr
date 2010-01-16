#!/usr/bin/python

import sys

def Main(arguments):
  for line in open(arguments[0]):
    line = line.strip()

    print '"%s","Musician","Unknown"' % (line)

if __name__ == '__main__':
  Main(sys.argv[1:])
