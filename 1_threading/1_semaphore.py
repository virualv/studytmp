# author:virualv
#  date :11/1/2018

import threading,time

class Semaphore_Thread(threading.Thread):

    def run(self):
        if semaphore.acquire():
            print(self.name)
            time.sleep(5)
            semaphore.release()

if __name__ == '__main__':
    semaphore = threading.BoundedSemaphore(5)
    this = []
    for i in range(50):
        this.append(Semaphore_Thread())

    for t in this:
        t.start()