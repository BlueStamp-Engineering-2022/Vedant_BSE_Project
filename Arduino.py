import serial
import time

if __name__=='__main__':
	ser=serial.Serial('/dev/ttyACM0',9600,timeout=1)
	ser.reset_input_buffer()
	while(True):
		ser.write(b"open\n")
		time.sleep(5)
		ser.write(b"close\n")
		time.sleep(5)
