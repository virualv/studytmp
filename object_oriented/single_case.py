# Author : virualv
# Time : 10/20/2018 4:35 PM
# class goo:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
# obj = goo()     # obj对象，obj也成为goo类的 实例  （实例化）


class Goo:

    __v = None

    @classmethod
    def get_instance(cls):
        if cls.__v:
            return cls.__v
        else:
            cls.__v = Goo()
            return cls.__v

# 不要再使用 类()

obj1 = Goo.get_instance()
print(obj1)

obj2 = Goo.get_instance()
print(obj2)

obj3 = Goo.get_instance()
print(obj3)