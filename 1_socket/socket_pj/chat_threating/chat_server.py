# Author : virualv
# Time : 10/28/2018 3:53 PM
import socketserver

class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        print('server starting')
        while True:
            conn = self.request
            print(self.client_address)
            while True:
                get = conn.recv(1024)
                print(str(get,'utf8'))
                server_response = input('>')
                conn.sendall(bytes(server_response,'utf8'))
if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1',9999),MyServer)
    server.serve_forever()

