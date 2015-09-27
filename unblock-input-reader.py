import serial
import serial.tools.list_ports

serials = []

for portuple in serial.tools.list_ports.comports():
	serials.append(serial.Serial(portuple[0], 38400))

while True:
	for port in serials:
		print port.readline()