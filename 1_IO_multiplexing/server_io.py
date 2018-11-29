# Time    : 11/17/2018 4:00 PM
# Author  : virualv

import socket,time

sk = socket.socket()

sk.bind(('127.0.0.1',9999))
sk.listen(3)
sk.setblocking(False)

while True:
    try:
        conn,addr = sk.accept()
        while True:
            date = conn.recv(1024)
            print(date.decode('utf8'))
            conn.sendall(date)
    except Exception as e:
        print('error:',e)
        time.sleep(3)
