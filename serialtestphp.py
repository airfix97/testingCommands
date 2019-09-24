import serial
import time

ser = serial.Serial('/dev/ttyACM0', 9600)

while True:
	ser.write(b'1')
	time.sleep(1)

