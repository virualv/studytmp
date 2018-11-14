# Time    : 11/12/2018 10:46 PM
# Author  : virualv

from multiprocessing import Process,Manager

def info(d,l):


if __name__ == '__main__':
    with Manager() as manager:
        dic = manager.dict()

        lis = manager.list(range(5))

        p_list = []
        for num in range(10):
            p = Process(target=info,args=(dic,lis))
