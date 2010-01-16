#!/usr/bin/python

bad_lines = []

for line in open('sources.txt'):
  line = line.strip()
  
  if '(' in line and ')' in line:
    try:
      name, classification = line.split('(')
      if classification.endswith(')'):
        classification = classification[:-1]
    except ValueError:
      bad_lines.append(line)

  else:
    name, classification = line, 'Unknown'

  print '"%s","%s"' % (name, classification)

for line in bad_lines:
  print line
