# Author : virualv
# Time : 10/17/2018 2:24 PM
# import socketserver
#
# obj = socketserver.ThreadingTCPServer()
# u = input('>')
# u = int(u)
# i = u*(10**2)
# print(i)


# Foo = type('Foo',(object,),{'func':function})
# type('Foo',(object,),{'func':lambda x:125})	声明一个类
# Foo = type('Foo',(object,),{'func':lambda x:125})
# obj = Foo()
# print(obj())

for i in range(1,50):
    print(i)

import time,datetime

print(datetime.date.fromtimestamp(time.time()))

print(datetime.datetime.now()+datetime.timedelta(hours=6))

def foo(max):
    L = []
    n,a,b = 0,0,1
    while(n<max):
        L.append(b)
        a,b = b,a+b
        n+=1
    return L
L = foo(5)
print(type(L))
I = iter(L)
print(I)