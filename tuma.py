import os
import socket

c = socket.socket()

c.connect(('localhost',9998))

name = input("sema jina:\n")
c.send(bytes(name,'utf-8'))
c.send

print(c.recv(1024).decode())
