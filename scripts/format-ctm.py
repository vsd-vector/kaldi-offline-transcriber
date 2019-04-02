#! /usr/bin/env python
'''
Created on Apr 02, 2019

'''

from __future__ import print_function
import sys
import re


if __name__ == '__main__':
  p = re.compile(r'(?:.*\/)?(.+)_(\d+.\d{3})[_-](\d+.\d{3})_([^_]+)$')
  last_segment_id = ""
  for l in sys.stdin:
    ss = l.split()
    m = p.match(ss[0])
    if m:      
    
      file_id = m.group(1)
      
      speaker_id = m.group(4)  
      start = float(m.group(2))
      end = float(m.group(3))
      utt_id = "%s-part_%0.3f-%0.3f" % (speaker_id, start, end)
      
      word = ss[4]
      score = "1"
      if len(ss) > 5:
          score = ss[5]      

      print("%s 1 %0.3f %0.3f %s %s" % (utt_id, float(ss[2]), float(ss[3]), word, score))      
    else:
      print("Cannot parse: ", ss[0], file=sys.stderr)
    
