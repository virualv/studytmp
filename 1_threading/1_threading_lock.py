# Time    : 10/30/2018 7:58 PM
# Author  : virualv
import time
import threading

def git():
    global num

    r.acquire()
    # num -=1
    temp = num
    # print('ok')
    time.sleep(0.001)
    num = temp -1
    r.release()

num = 100

threads_list = []
r = threading.Lock()
for i in range(100):
    t = threading.Thread(target=git)
    t.start()
    threads_list.append(t)

for t in threads_list:
    t.join()
print('finalnum:',num)


