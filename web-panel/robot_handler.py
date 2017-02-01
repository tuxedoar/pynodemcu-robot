#!/usr/bin/env python

import socket

cmd = ''
IP = '192.168.1.13'
PORT = 5000

class control():
	
	def __init__(self):
		pass

	def command(self, cmd):
		s = socket.socket()
		s.connect((IP, PORT))

                print "Conexion establecida..."

                s.send(cmd)	
