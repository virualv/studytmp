# Author : virualv
# Time : 10/22/2018 2:36 PM

import socket
import subprocess

address = ('0.0.0.0',9999)

s = socket.socket()
s.bind(address)
s.listen(5)
while True:
    print('waiting data')
    get,addr = s.accept()
    print('connect success\n',addr)
    while True:
        print('waiting message!\n')
        try:
            info = get.recv(1024)
        except Exception as e:
            print(e)
            break
        obj = subprocess.Popen(str(info,'utf8'),shell=True,stdout=subprocess.PIPE)
        result = obj.stdout.read()
        result_len = len(result)
        get.sendall(bytes(str(result_len),'utf8'))
        get.recv(1024)
        get.sendall(result)
        print('send success!')
    get.close()