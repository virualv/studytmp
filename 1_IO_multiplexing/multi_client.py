# Time    : 11/17/2018 9:15 PM
# Author  : virualv
import socket

sk = socket.socket()
sk.connect(('127.0.0.1',9999))

while True:
    data = input('>>>>')
    sk.sendall(data.encode('utf8'))
    data1 = sk.recv(1024)
    print(data1.decode('utf8'))