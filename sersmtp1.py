import socket
import sys
import json
import smtplib
import ssl

s = socket.socket((socket.AF_INET),(socket.SOCK_STREAM))
print("Successfully created socket")

port = 8888

s.bind(('',port))
print("Successfully bind socket, port: " + str(port))

s.listen(5)
print("Socket waiting...")
while True:
        c, addr = s.accept()
        print("Connected to: " + str(addr))

        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login("sarahhajijimmy@gmail.com","jbxopxnnqjznplzp")
        server.sendmail(
                "sarahhajijimmy@gmail.com",
                "bokunoaisan@gmail.com",
                "ITT440 INDIVIDUAL PROJECT SMTP")
        server.quit()


        c.send(b'Thank you')
        buffer = c.recv(1024)
        print(buffer)
c.close()

