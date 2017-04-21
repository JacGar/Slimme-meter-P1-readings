import serial
import time

ser = serial.Serial(port='/dev/ttyUSB0', baudrate=115200, parity = serial.PARITY_ODD, stopbits=serial.STOPBITS_NONE, bytesize = serial.EIGHTBITS)

for x in range(5):
  msg = []
  line = ser.readline()
  msg.append(line)
  if '!' in line:
    print msg
