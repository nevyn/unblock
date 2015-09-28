import serial
import serial.tools.list_ports
from subprocess import *

pdsend1 = Popen(["pdsend", "13000", "localhost", "tcp"], stdin=PIPE)
pdsend2 = Popen(["pdsend", "13001", "localhost", "tcp"], stdin=PIPE)

serials = []

for portuple in serial.tools.list_ports.comports():
	print("connecting to " + str(portuple))
	serials.append(serial.Serial(portuple[0], 19200))

while True:
	for port in serials:
		line = port.readline()
		v1 = line.split(" ")[0]
		pdsend1.stdin.write(v1 +";\n")
		v2 = line.split(" ")[1]
		pdsend2.stdin.write(v2 +";\n")
