import socket,os

address = ('0.0.0.0',9999)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sk = socket.socket()
sk.bind(address)
sk.listen(5)
print('waiting connect!')
while True:
    comn,addr = sk.accept()
    print(addr)
    while True:
        file_info = comn.recv(1024)
        file_info = str(file_info,'utf8').split('|')
        file_name = file_info[0]
        file_size = file_info[1]
        print(file_info[1])
        path = os.path.join(BASE_DIR,file_name)
        with open(path,'ab') as fp:
            file_size = int(file_size) 
            has_receive = 0
            while has_receive != file_size:
                datablock = comn.recv(1024)
                fp.write(datablock)
                has_receive += len(datablock)
        print('received success')
        break
    comn.close()


