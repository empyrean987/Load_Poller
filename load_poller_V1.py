#!/usr/local/bin/python
import os
import socket
import logging


try:
  port=1988
  host = '54.187.228.41'    # The remote host
  PORT = 8819              # The same port as used by the server
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((host, port))
  data = s.recv(1024)
  s.close()
  print 'Received', repr(data)
except Exception, e:
  print "Failure "+str(e)
