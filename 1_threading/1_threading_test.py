
import threading
from time import ctime,sleep
import time

def music(func):
    for i in range(2):
        print('Play Music....%s%s'%(func,ctime()))
        time.sleep(2)
        print('Ending play...%s'%ctime())

def movie(func):
    for i in range(2):
        print('Play Movie....%s%s'%(func,ctime()))
        time.sleep(5)
        print('Ending Play...%s'%ctime())

threads = []

t1 = threading.Thread(target=music,args=('JoyChou Rainbow',))
threads.append(t1)
t2 = threading.Thread(target=movie,args=('Forrest Jump',))
threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()
        t.join()
    print(threading.current_thread())
    print(threading.active_count())
    print('Ending...%s'%ctime())
