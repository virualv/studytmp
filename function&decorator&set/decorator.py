# Author : virualv
# Time : 9/10/2018 12:59 PM

import time

# 装饰器
# def show_time(f):
#     def inner():
#         start = time.time()
#         f()
#         end = time.time()
#         print('speed:%s'%(end - start))
#     return inner
#
# @show_time   # 等价于 foo = show_time(foo)
#
# def foo():
#     print('foo.....')
#     time.sleep(2)
#
# # foo = show_time(foo)
#
# @show_time
# def _man_():
#     print('123456')
#     time.sleep(2)
#
#
#
# foo()
# _man_()

# def show_time1(f):
#     def iner(x,y):
#         start = time.time()
#         f(x,y)
#         end = time.time()
#         print('speed :%s'% (end - start))
#     return iner
#
# @show_time1
# def fo(a,b):
#     print(a+b)
#
# fo(1,2)
#
# def show_time1(f):
#     def iner(*args,**kwargs):
#         start = time.time()
#         f(*args,**kwargs)
#         end = time.time()
#         print('speed :%s'% (end - start))
#     return iner
#
# @show_time1
# def fo(*args,**kwargs):
#     _sum_ = 0
#     for i in args:
#         _sum_ += i
#     print(_sum_)
#     time.sleep(1)
#
# fo(1,2,3,4,5)

def logger(flag = ''):
    def show_time1(f):
        def iner(*args,**kwargs):
            start = time.time()
            f(*args,**kwargs)
            end = time.time()
            if flag == 'true':
                print('speed :%s'% (end - start))
        return iner         # 注意位置（缩进量），注意别忘了
    return show_time1       # 注意位置（缩进量），注意别忘了

@logger()
def fo(*args,**kwargs):
    _sum_ = 0
    for i in args:
        _sum_ += i
    print(_sum_)
    time.sleep(1)
