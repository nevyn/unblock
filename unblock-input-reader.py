import serial
import serial.tools.list_ports
from subprocess import *

pdsend1 = Popen(["pdsend", "13000", "localhost", "tcp"], stdin=PIPE)
pdsend2 = Popen(["pdsend", "13001", "localhost", "tcp"], stdin=PIPE)

serials = []

print("Looking for com ports")

for portuple in serial.tools.list_ports.comports():
	print("connecting to " + str(portuple))
	serials.append(serial.Serial(portuple[0], 9600))

print("Starting to readline from comports")

while True:
	for port in serials:
		line = port.readline()
		comps = line.split(" ")
		if len(comps) < 2:
			continue
		v1 = comps[0]
		pdsend1.stdin.write(v1 +";\n")
		v2 = comps[1]
		pdsend2.stdin.write(v2 +";\n")
