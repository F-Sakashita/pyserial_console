#!/usr/bin/env python
#-*- coding:utf-8 -*-

# python3 ---> need decode & encode
import serial 
from serial import SerialException
import re
import time
import sys

class Serial:
	def __init__(self,device_path,baudrate):
		self.__isopen = False
		try:
			self.__serial = serial.Serial(device_path, baudrate, timeout=0.05)
			self.__isopen = True
			for i in range(50):
				emp = self.Receive()
				time.sleep(0.01)
		except SerialException:
			print "Could not open port -> %s." % device_path
			self.__isopen = False
	
	'''
	def __del__(self):
		self.__serial.close()
	'''

	def ReceiveChar(self):
		return self.__serial.read(1)
	
	def Receive(self):
		string = self.__serial.readline()
		#return string[0:-1].decode('utf-8') # remove "\n" & decode  (python3)
		return string[0:-1]

	def BuffClear(self):
		string = self.__serial.read(100)

	def Transmit(self, send_string):
		# python3 --> encode()
		#send_string = send_string.encode()
		self.__serial.write(send_string);
	
	def Available(self):
		#return self._serial.isOpen()
		return self.__isopen and self.__serial.isOpen()

#reference: https://qiita.com/Acqua_Alta/items/9f19afddc6db1e4d4286
