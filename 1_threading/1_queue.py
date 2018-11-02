# author:virualv
#  date :11/2/2018

# import queue,threading
#
# Q = queue.Queue(5)
# Q.put('jiu')
# Q.put('xiang')
# Q.put('he')
# Q.put('ni')
# Q.put('chang')
# print(Q.get())
# print(Q.get())
# print(Q.get())

import queue,time,threading
from random import randint

class Production(threading.Thread):
    def run(self):
        while True:
            rar = randint(0,100)
            B.put(rar)
            print('生产出%d号包子'%rar)
            time.sleep(0.5)

class Consumer(threading.Thread):
    def run(self):
        while True:
            rer = B.get()
            print('消费者吃了',rer,'号')

if __name__ == '__main__':
    threads = [Production(),Production(),Production(),Production(),Consumer()]

    B = queue.Queue(10)

    for t in threads:
        t.start()
