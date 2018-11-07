# def _input_(s):
#     s = input('he is :')
#
# def _output_(s):
#     print('this is %s' % s)
# s = 'hi'
# # _input_(s)
# _output_(s)

# def print_info (name,age):
#         print('Name :%s'% name)
#         print('Age :%d'% age)
# name = input('Name :')
# age = int(input('Age :'))
# print_info(name,age)              # 必需参数
# print_info(name = 'Huli',age = 32)    # 关键字参数


# def print_info(name, age,sex = 'male'):        # 默认参数必须跟在其他参数后面，non-default argument follows default argument
#     print('Name :%s' % name)
#     print('Age :%d' % age)
#     print('Sex :%s' % sex)

# print_info('xianli',23,'female')
# print_info('hongjin',35)
# print_info('jinbin',24)

# def add(a,b):
#     print(a+b)
# add(15,35)

# 无命名不定长参数
# def add(*args):
#     print(args)
#     sum = 0
#     for i in args:
#         sum += i
#     print('sum = %d'% sum)
# add(1,2,3,5,4)
#
# def info(*args):
#     for i in args:
#         print(i)
#
# info('liming',23,'female','TI')

# 有命名不定长参数
# def print_info(*args,**kwargs):     # 参数位置固定，*args无命名参数放左边，**kwargs有命名参数放右边
#     # print(args)         # ('alex', 30, 'male')
#     # print(kwargs)       # {'job': 'IT', 'hobby': 'girls', 'height': 168}
#     for i in kwargs:
#         print('%s:%s'% (i,kwargs[i]))
#
# print_info('alex',30,'male',job = 'IT',hobby = 'girls',height = 168)


def print_info(*args,sex = 'male'):
    print(sex)
    print(args)         # ('alex', 30, 'male')
    # # print(kwargs)       # {'job': 'IT', 'hobby': 'girls', 'height': 168}
    # for i in kwargs:
    #     print('%s:%s'% (i,kwargs[i]))

print_info(30)
# 关于不定长参数的位置：*args放在左边，**kwargs参数放在右边    ******重要
# 如果有默认参数，放右边
# def func(name,age = 22,*args,**kwargs)

# 字典关键字传参,将字典用“**”拆解后再进行关键字传参的方式       ******重要
# def function(name,job,_home):
#     print('Name:',name)
#     print("Job:",job)
#     print('Home',_home)
# function(**{'name':'vicker','job':'Programmer','_home':'Luan'})

# def f(*args):
#     print(args)
# f(*[1,2,5],*[6,8,7])

# 高阶函数                                               ******重要
# def f(n):
#     return n*n
# def foo(a,b,f):
#     return f(a)+f(b)
# print(foo(2,3,f))

# def f():
#     print('ok')
# foo = f

# 1. 函数名可以进行赋值                                    ******重要
# 2. 函数名可以作为函数的参数，还可以作为函数的返回值。

# def outer():
#     def iner():
#         return 9
#     return iner()
# print(outer())
