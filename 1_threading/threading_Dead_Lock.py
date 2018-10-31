# Time    : 10/31/2018 8:50 AM
# Author  : virualv
import threading,time

# class myThread(threading.Thread):
#     def doA(self):
#         lockA.acquire()
#         print(self.name,"gotlockA",time.ctime())
#         time.sleep(3)
#         lockB.acquire()
#         print(self.name,"gotlockB",time.ctime())
#         lockB.release()
#         lockA.release()
#
#     def doB(self):
#         lockB.acquire()
#         print(self.name,"gotlockB",time.ctime())
#         time.sleep(2)
#         lockA.acquire()
#         print(self.name,"gotlockA",time.ctime())
#         lockA.release()
#         lockB.release()
#     def run(self):
#         self.doA()
#         self.doB()
# if __name__=="__main__":
#
#     lockA=threading.Lock()
#     lockB=threading.Lock()
#     threads=[]
#     for i in range(5):
#         threads.append(myThread())
#     for t in threads:
#         t.start()
#     for t in threads:
#         t.join()#等待线程结束，后面再讲。


class MyThread(threading.Thread):
    def doA(self):
        Lock.acquire()
        print(self.name,'doA',time.ctime())
        time.sleep(0.5)
        Lock.acquire()
        print(self.name,'doA',time.ctime())
        Lock.release()
        Lock.release()
    def doB(self):
        Lock.acquire()
        print(self.name,'doB',time.ctime())
        time.sleep(0.5)
        Lock.acquire()
        print(self.name,'doB',time.ctime())
        Lock.release()
        Lock.release()

    def run(self):
        self.doA()
        self.doB()

if __name__ == '__main__':
    Lock = threading.RLock()
    threads = []
    for i in range(5):
        threads.append(MyThread())

    for t in threads:
        t.start()
    for t in threads:
        t.join()
