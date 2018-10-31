# Author : virualv
# Time : 10/22/2018 2:36 PM

import socket

address = ('0.0.0.0',5800)

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
        if str(info,'utf8') == 'q':
            print(r'client:"bye bye!"')
            break
        print(r'client:"%s"'%str(info,'utf8'))
        inp = input('>>>>>>')
        if inp == 'q':
            get.send(bytes(inp,'utf8'))
            print("stopping service")
            break
        get.send(bytes(inp,'utf8'))
        print('send success!')
    get.close()