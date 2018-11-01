# author:virualv
#  date :11/1/2018

import threading,time
from random import randint

class Produce(threading.Thread):
    def run(self):
        global L
        if

class Consumer(threading):


if __name__ == '__main__':
    L = []
    Lock_con = threading.Condition()
    threads = []
    for i in range(5):
        threads.append(Produce())
    threads.append(Consumer())
    for t in threads:
        t.start()
    for t in threads:
        t.join()