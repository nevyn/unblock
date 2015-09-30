#!/usr/bin/python
# -*- coding: utf-8 -*-


import pigpio
from subprocess import *

pins = [
  23, 24, 25, # strip 1
  16, 20, 21, # strip 2
  17, 27, 22, # strip 3
  6, 19, 26   # strip 4
]

pdrecv = Popen(["pdreceive", "3010", "udp"], stdout=PIPE)

pi = pigpio.pi()


for line in iter(pdrecv.stdout.readline,''):
  line = line.rstrip("\n ;")
  comps = line.split(" ")
  if comps[0] != "setleds":
    continue
  i = 0
  for comp in comps[1:]:
    v = min(255, max(0, int(float(comp))))
    pi.set_PWM_dutycycle(pins[i], v)
    i = i+1

