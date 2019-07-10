# Author : virualv
# Time : 9/9/2018 3:24 PM


def fibo(n):
    if n < 3:
        return n-1
    return fibo(n - 2) + fibo(n - 1)
print(fibo(6))

# str = ['a', 'b', 'c', 'd']
#
# def fun1(s):
#     if s != 'a':
#         return s
#
# ret = filter(fun1, str)
#
# print(list(ret))  # ret是一个迭代器对象
#
# str = ['1', '2', 'a', 'b']
#
# # def fun2(s):
# #     return s + "alvin"
# # ret = map(fun2, str)
# # print(ret)  # map object的迭代器
# # print(list(ret))  # ['aalvin', 'balvin', 'calvin', 'dalvin']
#
#
# def add(x,y):
#     return x+10
# print (list(map(add, range(10), range(10))))
#
# from functools import reduce
#
# # 匿名函数
# #
#
# # def add1(x,y):
# #     return x + y
# #
# # print(reduce(add1,range(1,9)))
#
# from functools import reduce
#
# def add1(x, y):
#     return x + y
#
# print(reduce(add1, range(1, 101)))  ## 4950 （注：1+2+...+99）
#
# print(reduce(add1, range(1, 101), 20))  ## 4970 （注：1+2+...+99+20）

