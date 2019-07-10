# Author : virualv
# Time : 10/25/2018 9:26 PM

import socket

address = ('127.0.0.1',9999) # set ip address and port

sk = socket.socket()

sk.connect(address) # connect server

while True:
    put = input('>>>')  # input command

    sk.send(bytes(put,'utf8'))
    lendata = sk.recv(1024)
    sk.send(bytes('..','utf8'))
    result_len = int(str(lendata,'utf8'))
    getdata = bytes()
    while len(getdata) != result_len:
        getdatablock = sk.recv(1024)
        getdata += getdatablock
    print('<%d>'%result_len)
    print(str(getdata,'utf8'))