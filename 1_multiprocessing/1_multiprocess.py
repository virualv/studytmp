# author:virualv
#  date :11/6/2018

# from multiprocessing import Process
# import time
#
# def f(n):
#     time.sleep(0.5)
#     print('hello',n,time.ctime())
#
# if __name__ == '__main__':
#     p_list = []
#
#     for p in range(3):
#         p = Process(target=f,args=('xiaomi',))
#         p_list.append(p)
#         p.start()
#
#     for p in p_list:
#         p.join()
#     print('ending')

import time,multiprocessing

class MyProcess(multiprocessing.Process):
    def __init__(self):
        super(MyProcess,self).__init__()
        # self.name = 'process'
    def run(self):
        time.sleep(1)
        print('okay',self.name,time.ctime())

if __name__ == '__main__':
    t_list = []
    for i in range(25):
        t = MyProcess()
        t_list.append(t)
    for t in t_list:
        t.start()
    for t in t_list:
        t.join()