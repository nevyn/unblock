#!/usr/bin/python
# -*- coding: utf-8 -*-


import pigpio


class Strip(object):
  pins = []
  
  def __init__(self, pin1, pin2, pin3):
    self.pins = [pin1, pin2, pin3]

strips = [
  Strip(23, 24, 25),
  Strip(16, 20, 21),
  Strip(17, 27, 22),
  Strip(6, 19, 26)
]

pdrecv = Popen(["pdreceive", "3010", "localhost", "udp"])


