#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys
import Serial
import time

def main(argc,argv):
	while True:
		if argc >= 2:
			serial = Serial.Serial(argv[1],int(argv[2]))
		else:
			serial = Serial.Serial('/dev/ttyACM0',115200)

		if serial.Available() == True:
			break
		#else:	
			#print "Could not open serial port."
		time.sleep(1.0)
		

	while True:
		try:
			string = serial.Receive()
			if not(string in ""):
				print string
		except KeyboardInterrupt:
			print "Finished."
			sys.exit(0)
		
	
if __name__=="__main__":
	argv = sys.argv
	argc = len(argv)
	main(argc,argv)
