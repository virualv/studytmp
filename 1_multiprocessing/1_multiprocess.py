# author:virualv
#  date :11/6/2018

from multiprocessing import Process
import time

def f(n):
    time.sleep(0.5)
    print('hello',n,time.ctime())

if __name__ == '__main__':
    p_list = []

    for p in range(3):
        p = Process(target=f,args=('xiaomi',))
        p_list.append(p)
        p.start()

    for p in p_list:
        p.join()
    print('ending')