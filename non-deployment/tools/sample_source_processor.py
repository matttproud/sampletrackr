#!/usr/bin/python

import sys


def Main(arguments):
  requiring_intervention = []

  for line in file(arguments[0]):
    if '(' in line and ')' in line:
      if line.count(')') == 1 and line.count(')') == 1:
        title, classification = line.split('(')

        title = title.strip()
        classification = classification[:-2]
        classification.strip()

      else:
        requiring_intervention.append(line)

    else:
      title = line.strip()
      classification = 'Unclassified'

    print '"%s", "%s"' % (title, classification)

  for line in requiring_intervention:
    print >>sys.stderr, line

if __name__ == '__main__':
  Main(sys.argv[1:])
