#!/usr/bin/env python3

# Glue ctm with Right-marked BPE tokens

import sys

i = 0
glue = ""
conf = 0
for line in sys.stdin:
    line = line.strip().split()
    word = line[4] 
    if word.endswith("+"):
      if i == 0:
        begin = float(line[2])
      glue += word[:-1]
      i += 1
      conf += float(line[5])
    else:
      if i > 0:
        last_begin = float(line[2])
        dur = float(line[3])
        glue += word[:-1]
        i += 1
        conf += float(line[5])
        dur = last_begin - begin + dur
        conf = conf / i  # take average

        ctm_parsed = [line[0], line[1], str(begin), str(dur), glue, str(conf)]

        print(" ".join(ctm_parsed))
        i = 0
        glue = ""
        conf = 0
      else:
        print(" ".join(line))

