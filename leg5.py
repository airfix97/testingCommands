import serial
import time

ser = serial.Serial('/dev/ttyUSB0',9600)

while True:
	ser.write(b"5")
	time.sleep(1)
	break
ser.close()
