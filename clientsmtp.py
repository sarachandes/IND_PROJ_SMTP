
import socket
import sys
import json
import smtplib

s = socket.socket((socket.AF_INET),(socket.SOCK_STREAM))

port = 8888

s.connect(('192.168.56.102', port))

data = s.recv(1024)

s.send(b'Hi, I am from client server. Thank you!');

print (data)

s.close()

