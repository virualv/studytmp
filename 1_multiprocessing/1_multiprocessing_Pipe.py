# Time    : 11/12/2018 10:09 PM
# Author  : virualv
import os
from multiprocessing import Process,Pipe

def info(corn):
    corn.send('You is good！')
    corn.send('this pid is :%s' % os.getpid())
    corn.close()

if __name__ == '__main__':
    corn_parent,corn_son = Pipe()
    p = Process(target=info,args=(corn_son,))
    p2 = Process(target=info,args=(corn_son,))
    p.start()
    p2.start()
    print(corn_parent.recv())
    print(corn_parent.recv())
    print(corn_parent.recv())
    print(corn_parent.recv())
    p.join( )