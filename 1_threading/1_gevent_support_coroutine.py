# Time    : 11/13/2018 10:07 PM
# Author  : virualv
#
# import gevent
#
#
# def func1():
#     print('\033[31;1mGo Beijing\033[0m')
#     gevent.sleep(2)
#     print('\033[31;1mBack to Shanghai\033[0m')
#
#
# def func2():
#     print('\033[32;1mTo go Shanghai\033[0m')
#     gevent.sleep(1)
#     print('\033[32;1mBack to Beijing\033[0m')
#
#
# gevent.joinall([
#     gevent.spawn(func1),
#     gevent.spawn(func2),
#     # gevent.spawn(func3),
# ])
import gevent
from gevent import monkey
monkey.patch_all()
from urllib.request import urlopen

def _collect_(url):
    print('GET:%s' % url)
    rest = urlopen(url)
    result = rest.read()
    with open('xiaomi.html','ab') as f:
        f.write(result)
    print('Get data size:%d bytes from %s' % (len(result),url))

gevent.joinall([
    gevent.spawn(_collect_,'https://www.mi.com')
])