# Author : virualv
# Time : 10/15/2018 1:27 PM
# 创建类
class Foo:
    def Bar(self):
        print('Bar')

    def Hello(self, name):
        print('i am %s' % name)


# 根据类Foo创建对象obj
obj = Foo()
obj.Bar()  # 执行Bar方法
obj.Hello('qiji')  # 执行Hello方法



print('===============================================================================================================')

#
class yoga:
    def kol(self):
        print(self.name,self.age,self.gender,self.key)
obj_yoga = yoga()
obj_yoga.name = 'mi'
obj_yoga.age = 8
obj_yoga.gender = 'male'
obj_yoga.key = 'joy'
obj_yoga.kol()

print('===============================================================================================================')





class get:
    def __init__(self,fan,j):
        '''
        构造方法    #类名加括号会自动执行构造方法
        (一般做初始化)
        '''
        self.name = 'all'
        self.age = 18
        print('mi',fan,j)
    def fo(self):
        print('four\n',self.name,self.age)
obj_key = get('jiu',16)
obj_key.fo()



print('===============================================================================================================')




class F:
    def f1(self):
        print('F.f1')
    def f2(self):
        print('F.f2')
    def f3(self):
        print('F.f3')
class S(F):
    def s1(self):
        print('S.s1')
    def f2(self):
        print('S.s2')
    def f3(self):
        print('S.s3')
        # super(S,self).f3()  # 执行父类中的f3方法
        # F.f3(self)            # 执行父类中的f3方法
obj_S = S()
obj_S.f1()
obj_S.f2()
obj_S.f3()





print('===============================================================================================================')






class F0:
    def a(self):
        print('F0.a')
class F1(F0):
    def a1(self):
        print('F1.a')

class F2:
    def a(self):
        print('F2.a')

class S(F1,F2):
    pass
obj_S = S()
obj_S.a()





print('===============================================================================================================')

class BaseRequest:
    def __init__(self):
        print('BaseRequest.__init__.go')
    pass

class RequestHandler(BaseRequest):
    def __init__(self):
        print('RequestHandler.__init__.go')
    def serve_forever(self):
        print('RequestHandler')
        self.process_request()
    def process_request(self):
        print('RequestHandler process_request')

class Minx:
    def process_request(self):
        print('Minx process_request')

class Son(Minx,RequestHandler):
    pass

obj = Son()
obj.serve_forever()





print('===============================================================================================================')





class Province:
    # 静态字段，属于类
    country = 'China'

    def __init__(self, name):
        # 普通字段，属于对象
        self.name = name


henan = Province("HeNan")
hebei = Province("HeBei")

print(hebei.country)
print(Province.country)
print(hebei.name)
# print(Province.name)  #类不能调用普通字段，只有对象 可以调用普通字段




print('===============================================================================================================')


# 普通方法、静态方法、类方法

class Foo:
    def bar(self):
        print('bar')
    @staticmethod
    def sta():
        print('barstatic')
    @staticmethod
    def star(j,k):
        print(j,k)

    @classmethod
    def classmd(cls):
        # cls是类名
        print('classmd')
obj = Foo()
obj.bar()

Foo.sta()
Foo.star(5,9)

Foo.classmd()





print('===============================================================================================================')






# 属性
class Foo:

    def __init__(self):
        self.name = 'dw'

    def bar(self):
        print('bar')

    @property   # 属性
    def sta(self):
        print('1111')
        return 2
    @sta.setter
    def sta(self,val):
        print(val)
    @sta.deleter
    def sta(self):
        print('999')
obj = Foo()
p = obj.sta
# print(p)
obj.sta = 568
del obj.sta

print('\n')



# 属性
class Foo:

    def __init__(self):
        self.name = 'dw'

    def bar(self):
        print('bar')

    def get_i(self):
        print('1')
        return 2

    def set_i(self,val):
        print(val)

    def del_i(self):
        print('6')

    star = property(fget=get_i,fset=set_i,fdel=del_i,doc='jindnd')  # 属性的第二种创建方式


obj = Foo()


j = obj.star
print(j)
obj.star = 5
del obj.star



print('===============================================================================================================')






li = list('')
for i in range(300):
    li.append(i)
# print(li)

class Page:

    def __init__(self,p):
        self.page = int(p)

    @property
    def start(self):
        return (self.page -1)*10

    @property
    def end(self):
        return self.page*10

while True:
    p = input('Page:')
    obj = Page(p)

    print(li[obj.start:obj.end])

