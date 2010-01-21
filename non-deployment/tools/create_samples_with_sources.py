#!/usr/bin/python

import csv
import re
import sys

_SOURCE_RE = re.compile(r'^\d+\.\s+(.*?)\s+\[.*?\].*')
_COMPLEX_TITLE_RE = re.compile(r'^\d+\.\s+(.*?)\s+\(.*?\)\s+\[.*?\].*')
_QUOTE_RE = re.compile(r'[^\d]".*?"')
_CITATION_RE = re.compile(r'^-.*?;.*;.*')
_WHITESPACE_RE = re.compile(r'\s+')
_DOUBLE_QUOTE_RE = re.compile(r'"+')
_SINGLE_QUOTE_RE = re.compile(r"'+")

def _GetSourceTitle(line):
  if _COMPLEX_TITLE_RE.match(line):
    source_title = _COMPLEX_TITLE_RE.match(line).group(1)
    return source_title

  if _SOURCE_RE.match(line):
    source_title = _SOURCE_RE.match(line).group(1)
    return source_title

  return None

title = None
lines = []
bad_stuff = []

def _CullNeedlessQuotes(sample):
  if sample.startswith("'") and sample.endswith("'") and sample.count("'") == 2:
    return sample[1:-1]

  if sample.startswith('"') and sample.endswith('"') and sample.count('"') == 2:
    return sample[1:-1]
  
  return sample

def _CullNeedlessWhitespace(sample):
  return _WHITESPACE_RE.sub(' ', sample)

def _CullNeedlessSingleQuotes(sample):
  return _SINGLE_QUOTE_RE.sub("'", sample)

def _CullNeedlessDoubleQuotes(sample):
  return _DOUBLE_QUOTE_RE.sub('"', sample)

_csv_writer = csv.writer(sys.stdout)

for line_number, line in enumerate(open(sys.argv[1])):
  line = line.strip()

  examined_line = _GetSourceTitle(line)

  if examined_line:
    if title:
      title = _CullNeedlessWhitespace(title)
      title = _CullNeedlessSingleQuotes(title)
      title = _CullNeedlessDoubleQuotes(title)
      title = _CullNeedlessQuotes(title)

    try:
      joined_lines = ' '.join(lines)

      samples = _QUOTE_RE.findall(joined_lines)


      samples = map(lambda x: x[2:-1], samples)
      samples = map(lambda x: x.strip(), samples)
      samples = map(_CullNeedlessWhitespace, samples)
      samples = map(_CullNeedlessSingleQuotes, samples)
      samples = map(_CullNeedlessDoubleQuotes, samples)
      samples = map(_CullNeedlessQuotes, samples)
      samples = filter(lambda x: x, samples)

      for item in samples:
        _csv_writer.writerow([item, title, 'Unknown'])

    finally:
      title = examined_line
      lines = []

  if title:
    if not _CITATION_RE.match(line):
      lines.append(line)

print bad_stuff
