# Author : virualv
# Time : 10/22/2018 2:35 PM
import socket

s = socket.socket()

address = ('127.0.0.1',5800)

s.connect(address)

while True:
    #s.send(bytes('start','utf8'))
    print('Input what want to send')
    inp = input('>>>>>>')
    if inp == 'q':
        s.send(bytes(inp, 'utf8'))
        print('stopping service')
        break

    s.send(bytes(inp,'utf8'))
    print('waiting message!')
    get = s.recv(1024)
    if str(get,'utf8') == 'q':
        print(r'server:"bye bye!"')
        break
    print(r'server:"%s"'%str(get,'utf8'))
s.close()