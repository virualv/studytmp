# Time    : 12/9/2018 10:07 PM
# Author  : virualv

import socket

def main():
    addr = ('127.0.0.1',9000)

    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind(addr)
    sock.listen(6)

    while True:
        connection,address = sock.accept()
        info = connection.recv(1024)
        print(info.decode('utf8'))

        connection.sendall(bytes('HTTP/1.1 201 OK\r\n\r\n','utf8'))
        with open('hd.html','rb') as f:
            data = f.read()
        connection.sendall(data)
        connection.close()

if __name__ == '__main__':
    main()