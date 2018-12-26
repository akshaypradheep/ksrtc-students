#!/usr/bin/python3
import pyrebase	
import serial
rf = serial.Serial('/dev/ttyUSB0')
#Firebase Configuration
config = {
  "apiKey":"AIzaSyAqNO9M-DW7tflQXcM81is-eSt-odISXo",
  "authDomain": "ksrtcbuss.firebaseapp.com",
  "databaseURL": "https://ksrtcbuss.firebaseio.com",
  "storageBucket": "ksrtcbuss.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
while 1:
	print("Waiting for RF Tag: ")
	s = rf.read(12)
	a = input("enter the name : ")
	b = input("enter the route:")
	db.child("Name").child(s).set(a)
	db.child("Route").child(s).set(b)
	#temp = str(s)
#
#
#	#db.child("passCods").child(a).set(temp)
#	#c = db.child("passCods").child(a).get()
	#print(c.val())
