#!/usr/bin/python3
import serial
rf = serial.Serial('/dev/ttyUSB0')
while 1:
    s = rf.read(12)
    print(s)
