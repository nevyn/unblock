import serial
import serial.tools.list_ports
from subprocess import *

pdsend = Popen(["pdsend", "13000", "localhost", "tcp"], stdin=PIPE)

serials = []

for portuple in serial.tools.list_ports.comports():
	serials.append(serial.Serial(portuple[0], 38400))

while True:
	for port in serials:
		line = port.readline()
		v1 = line.split(" ")[0]
		print v1
		pdsend.stdin.write(v1 +";\n")
