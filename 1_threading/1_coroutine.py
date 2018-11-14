# Time    : 11/13/2018 9:07 PM
# Author  : virualv

import time
import queue


def consumer(name):
    print("--->starting eating baozi...")
    while True:
        new_baozi = yield
        print("[%s] is eating baozi %s" % (name, new_baozi))
        # time.sleep(1)


def producer():
    con.__next__()
    con2.__next__()
    n = 0
    while n < 5:
        n += 1
        if n < 5:
            print("\033[32;1m[producer]\033[0m is making baozi %s" % n)
            con.send(n)
        else:break
        n += 1
        if n < 5:
            print("\033[32;1m[producer]\033[0m is making baozi %s" % n)
            con2.send(n)
        else:break



if __name__ == '__main__':
    con = consumer("c1")
    con2 = consumer("c2")
    p = producer()