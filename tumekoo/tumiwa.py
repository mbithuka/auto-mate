""
version control 1.1
""
import os, socket

s = socket.socket()
print('socket created')

s.bind(('localhost',9998))
s.listen(3)
print('waiting for connection')

while True:
    c, addr = s.accept()
    name = c.recv(1024).decode()
    print('connected with', addr, name)
    
    c.send(bytes('karibu'  ,'utf-8'))
    
    c.close()