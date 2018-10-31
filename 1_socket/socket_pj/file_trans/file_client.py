# Author : virualv
# Time : 10/26/2018 5:06 PM

import socket,os

address = ('192.168.31.66',9999)

sk = socket.socket()
sk.connect(address)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
while True:
    put = input('>>>').strip()
    cmd,path = put.split('|')

    path = os.path.join(BASE_DIR,path)
    file_size = os.stat(path).st_size
    file_name = os.path.basename(path)
    file_info = '%s|%s'%(file_name,file_size)
    sk.sendall(bytes(file_info,'utf8'))

    with open(path,'rb') as fp:
        has_send = 0
        while has_send != file_size:
            dateblock = fp.read(1024)
            sk.sendall(dateblock)
            has_send += len(dateblock)
    sk.close()
    print('send success!')