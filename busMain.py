import pyrebase
import serial
rf = serial.Serial('/dev/ttyUSB0')
busRoute = "thrissur-chlkara"
#Firebase Configuration
config = {
  "apiKey":"AIzaSyAqNO9M-DW7tflQXcM81is-eSt-odISXo",
  "authDomain": "ksrtcbuss.firebaseapp.com",
  "databaseURL": "https://ksrtcbuss.firebaseio.com",
  "storageBucket": "ksrtcbuss.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
#-------------------------------------------------------------
def fireRead(barcod):
	_name = db.child("Name").child(barcod).get()
	_route = db.child("Route").child(barcod).get()
	return _name.val(), _route.val()

def inRead():
	a = rf.read(12)
	#a = input("enter the user ID:")
	return a

def display(name,route):
	print(name)
	print(route)

def timeStamp():
	import datetime
	now = datetime.datetime.now()
	a = str(now.day) + "-" + str(now.month) + "-" + str(now.year)
	return a 
	pass

def mark(_usr):
		_us = str(_usr)
		a = db.child("date").child(_us).child(timeStamp()).child(busRoute).child("up").get()
		_a = a.val()
		print(_a)
		if _a == "1":
			return "not allowed"
			pass
		else:	
			db.child("date").child(_usr).child(timeStamp()).child(busRoute).child("up").set("1")
			return "happy journy"

#--------------------------------------------------------------
while True:
	_u = inRead()
	a,b = fireRead(_u)
	if a is None:
		display("not allowed","card not registered")
	else:
		display(a,b)
		print(mark(_u))
		pass
