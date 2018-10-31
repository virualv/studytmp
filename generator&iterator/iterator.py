# Author : virualv
# Time : 9/15/2018 11:14 AM
# 生成器都是迭代器，迭代器不一定是生成器。
# list tuple dict string :Iteriable(可迭代对象)


from  collections.abc import Iterable   # from  collections import Iterable 将在py3.8移除
l = [1,2,3,4,5]
d = iter(l)        # l.__iter__()
print(d)           # <list_iterator object at 0x0000019ACB4272B0>
print(next(d))
print(next(d))
print(next(d))
# for i in d:
#     print(i)

# for 循环内部做了三件事：
#     1.调用可迭代对象的iter方法返回一个可迭代对象
#     2.不断调用迭代器对象的next方法
#     3.处理StopIteration
# for i in [1,5,3,4,5,6,8]:
#     iter([1,5,3,4,5,6,8])

print(isinstance(l,list))
print(isinstance(l,Iterable))
from  collections.abc import Iterator
print(isinstance(l,Iterator))
