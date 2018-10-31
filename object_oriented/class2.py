# Author : virualv
# Time : 10/18/2018 3:57 PM

class go:
    __jva = 'joa'
    def __init__(self,name,age):
        self.name = name
        self.__age = age    # 私有，外部无法直接访问

    def show(self):
        return self.__age

    def show1(self):
        return go.__jva

    @staticmethod
    def show2():
        return go.__jva

obj = go('joy',18)

print(obj.name)

print(obj.show())

print(obj.show1())

print(go.show2())





print("---------------------------------------------------------")

class foo:

    def __f1(self):
        return 125

    def f2(self):
        r = self.__f1()
        return r

obj = foo()

ret = obj.f2()

print(ret)

print("---------------------------------------------------------------------------------------------------------------")

class F:
    def __init__(self):
        self.game = 'cs'
        self.__game = 'cf'

class S(F):
    def __init__(self,name):
        self.name = name
        self.__age = 19
        super(S,self).__init__()

    def show(self):
        print(self.name)         # 能访问
        print(self.__age)        # 能访问
        print(self.game)         # 能访问
       # print(self.__game)      # 不能访问

g = S('joy1')
g.show()




print("---------------------------------------------------------------------------------------------------------------")



class Ajour:
    def __init__(self):
        print('init')

    def __call__(self, *args, **kwargs):
        print('call')

obj = Ajour()
obj()


print("---------------------------------------------------------------------------------------------------------------")


class goo:

    def __init__(self):
        pass

    def __int__(self):
        return 256356

    def __str__(self):
        return 'joy'


obj = goo()

print(obj,type(obj))

# int(对象)，自动执行__int__方法，并将返回值赋值给int对象
re = int(obj)
res = str(obj)
print(re)
print(res)


class hoo:
    def __init__(self,name1,age1):
        self.name1 = name1
        self.age1 = age1

    def __str__(self):
        return '%s - %d'%(self.name1,self.age1)

obj = hoo('joy',17)
print(obj)




print("---------------------------------------------------------------------------------------------------------------")


# class joo:
#     def __init__(self,n,a):
#         self.name = n
#         self.age = a
#
#     def __add__(self, other):
#         return joo(obj1.name,other.age)
#
#     def __del__(self):
#         print('析构方法')       # 对象被销毁时，自动执行
#
# obj1 = joo('kit',25)
# obj2 = joo('goj',21)
# rsd = obj1 + obj2
#
# print(rsd)


print("---------------------------------------------------------------------------------------------------------------")


# class koo:
#     '''
#     what is current class?
#     '''
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
# obj = koo('koo',12)
#
# d = obj.__dict__
# print(d)
#
# ref = koo.__dict__
# print(ref)

print("---------------------------------------------------------------------------------------------------------------")

# class loo:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def __getitem__(self, item):
#         return item+10
#
#         # 如果item是基本参数，int,str 索引获取
#         # slice对象的话，切片
#
#     def __setitem__(self, key, value):
#         print(key,value)
#
#     def __delitem__(self, key):
#         print(key)
#
# li = loo('loo',18)
# l = li[9]    # 自动执行li对象的类中的__getitem__方法，8当做参数传递给item
# print(l)
#
# li[10] = 'jodded'
#
# del li[999]



class ioo:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __iter__(self):
        return iter([5,8,6,7,9])

lioo = ioo('joy',8)
# 如果类中有__iter__方法，对象-->可迭代对象
# 对象，__iter__()的返回值：迭代器
# for 循环，迭代器,next
# for 循环，可迭代对象，对象，__iter__方法，迭代器，next
# 1、执行lioo对象的类ioo类的 __iter__方法，并获取其返回值
# 2、循环上一步中返回的对象

for i in lioo:
    print(i)

print('===============================================================================\n\n')
# =============================================

################ metaclass ####################

class MyType(type):

    def __init__(self,*args,**kwargs):
        # self = foo
        print('888')
        pass

    def __call__(self, *args, **kwargs):
        # self = foo
        print('running')


class foo(object,metaclass=MyType):

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):  # 真正创建对象
        pass
        # return <object> 即obj

    def func(self):
        print('jot vol')

obj = foo()