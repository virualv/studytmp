# Author : virualv
# Time : 10/28/2018 3:43 PM

import socket

ip_port = ('127.0.0.1',9999)

sk = socket.socket()
sk.connect(ip_port)
print('connected')
while True:
    client_request = input('>')
    sk.sendall(bytes(client_request,'utf8'))
    serve_request = sk.recv(1024)
    print(str(serve_request,'utf8'))