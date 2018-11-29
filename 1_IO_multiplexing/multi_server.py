# Time    : 11/17/2018 8:55 PM
# Author  : virualv

import socket,select
import time

sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sk.bind(('127.0.0.1',9999))
sk.listen(5)
inp = [sk]
while True:
    inputs,outputs,errors = select.select(inp,[],[])
    for obj in inputs:
        if obj == sk:
            conn,addr = sk.accept()
            print(conn)
            inp.append(conn)
        else:
            try:
                data = obj.recv(1024)
                print(data.decode('utf8'))
                Inputs = input('request %s>>'% inp.index(obj))
                obj.sendall(Inputs.encode('utf8'))
            except Exception as outline:
                print('No%s already offline'% inp.index(obj))
                inp.remove(obj)