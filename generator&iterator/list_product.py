# Author : virualv
# Time : 9/11/2018 1:17 PM
#
# a = [x**2 for x in range (10)]
# print(a)
#
# # 列表生成式
# def f(n):
#     return n**3
# b = [f(i) for i in range(10)]
# print(b)

# t = ['213',21,54]
#
# a,b = t
# print(a)
# print(b)


# 'list' object is not an iterator

#
s = (x*2 for x in range(4))

# print(s)    # <generator object <genexpr> at 0x00000262235CB318>

# print(next(s))     # 等价于s.__next__()      in Py2: s.next()
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))     # StopIteration

# 生成器就是一个可迭代对象（Iterable）

# for i in s:
#     print(i)

# Debug 调试查看执行顺序
# def foo():
#     print('ok')
#     yield 1
#     print('ok2')
#     yield 2
#
# g = foo()   # <generator object foo at 0x0000020D26D8B390>
# print(g)
# a = next(g)
# b = next(g)
# print(a,b)

# print(next(g))
# print(next(g))

# next(g)
# next(g)
#
# for i in foo():     # for循环遍历可迭代对象
#     print(i)    # 比较i 输出和 next(i)输出


# def fib(max):
#     n, before, after = 1, 0 ,1
#     while n < max:
#         before, after = after, before + after
#         n += 1
#     yield before
# i = int(input('which num:'))
# print(next(fib(i)))

def bar():
    print('ok')
    count = yield 1
    print(count)
    yield 2

s = bar()

t = s.send(None)    # next(s) 第一次send前如果没有next，只能传一个send(None)
print(t)
k = s.send('eewww')
print(k)
