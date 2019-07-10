# Author : virualv
# Time : 10/20/2018 12:43 PM

class koo:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show(self):
        return '%s - %s'%(self.name,self.age)

obj = koo('joy',19)



# getattr()
# hasattr()
# setattr()
# delattr()
# 通过字符串操作对象成员



# inp = input(':')
#
# v = getattr(obj,inp)
# print(v)
#
# func = input('func:')
# func = getattr(obj,func)
# print(func)
# print(func())

print(hasattr(obj,'name'))  #检测是否有

# setattr(obj,'k','keyvalue')
# print(obj.k)
obj.name
delattr(obj,'name')
obj.name
