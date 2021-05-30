#! /usr/bin/python
# slowcat.py - print a file slowly
# original author : dave w capella - http://grox.net/mailme
# original date     : Sun Feb 10 21:57:42 PST 2008
# distributed under the terms of the GNU Public license
############################################################
# this version prints character-by-character
# there is a small randomisation in the delay to each character
# that may or may not make a difference and/or make it seem better
# it is perhaps dependent on the speed of your eyeballs.
# author: andy middleton
# date: Sun May 30 2021

import sys, time, random

delay = .02

if len(sys.argv) > 1:
  arg = sys.argv[1]
  if arg != "-d":
    print ("usage: %s [-d delay]" % (sys.argv[0]))
    print ("delay: delay in seconds")
    print ("example: %s -d .02 < vtfile" % (sys.argv[0]))
    sys.exit()
  if len(sys.argv) > 2:
    delay = float(sys.argv[2])
    delay_tenth = delay * 0.1
    random_range_start = 0-(delay_tenth/2)
    random_range_stop = (delay_tenth/2)
while 1:
  try:
    line = input()
    for char in range(len(line)):
      print(line[char:char+1],end='', flush=True)
      time.sleep(delay+(random.uniform(random_range_start,random_range_stop)))
    print('')
    time.sleep(delay+(random.uniform(random_range_start,random_range_stop)))

  except:
    break

######################################################################
# eof: slowcat.py