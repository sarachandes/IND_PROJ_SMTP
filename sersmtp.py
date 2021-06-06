import socket
import sys
import json
import smtplib
import ssl

class Mail:

    def __init__(self):
        self.port = 465
        self.smtp_server_domain_name = "smtp.gmail.com"
        self.sender_mail = "sarahhajijimmy@gmail.com"
        self.password = "jbxopxnnqjznplzp"

    def send(self, emails, subject, content):
        ssl_context = ssl.create_default_context()
        service = smtplib.SMTP_SSL(self.smtp_server_domain_name, self.port, context=ssl_context)
        service.login(self.sender_mail, self.password)

        for email in emails:
            result = service.sendmail(self.sender_mail, email, f"Subject: {subject}\n{content}")

        service.quit()

s = socket.socket((socket.AF_INET),(socket.SOCK_STREAM))
print("Successfully created socket")

port = 8888

s.bind(('',port))
print("Successfully bind socket, port: " + str(port))

if __name__ == '__main__':
        mails = input("Enter email destinations: ").split()
        subject = input("Enter subject: ")
        content = input("Enter content: ")

        mail = Mail()
        mail.send(mails, subject, content)

s.listen(5)
print("Socket waiting...")
while True:
        c, addr = s.accept()
        print("Connected to: " + str(addr))

        c.send(b'Thank you')
        buffer = c.recv(1024)
        print(buffer)
c.close()
s.close()
