# author:virualv
#  date :11/1/2018

import threading,time
from random import randint
#
# class Produce(threading.Thread):
#     def run(self):
#         global L
#         while True:
#             val = randint(0,100)
#             print('Producer:',self.name,'Append'+str(val),L)
#             if Lock_con.acquire():
#                 L.append(val)
#                 Lock_con.notify()
#                 Lock_con.release()
#             time.sleep(3)
#
# class Consumer(threading.Thread):
#     def run(self):
#         global L
#         while True:
#             Lock_con.acquire()
#             if len(L) == 0:
#                 Lock_con.wait()
#             print('Consumer',self.name,'Delete'+str(L[0]),L)
#             del L[0]
#             Lock_con.release()
#             time.sleep(1)
#
# if __name__ == '__main__':
#     L = []
#     Lock_con = threading.Condition()
#     threads = []
#     for i in range(5):
#         threads.append(Produce())
#     threads.append(Consumer())
#     for t in threads:
#         t.start()
#     for t in threads:
#         t.join()



class Boss(threading.Thread):
    def run(self):
        print('jinwanjiabadaoshidian')
        event.isSet() or event.set()
        time.sleep(3)
        print('shijiandaole')
        event.isSet() or event.set()

class Workers(threading.Thread):
    def run(self):
        event.wait()
        print('beicuna ,ai')
        time.sleep(1)
        event.clear()
        event.wait()
        print('hao ,taibangle')

if __name__ == '__main__':

    event = threading.Event()

    threads = []

    for i in range(5):
        threads.append(Workers())
    threads.append(Boss())
    for t in threads:
        t.start()
    for t in threads:
        t.join()