# Author : virualv
# Time : 9/15/2018 3:25 PM
import random

# print(random.random())
# print(random.randint(1,8)) # 包括8
# print(random.choice('hello'))
# print(random.choice(['123',4,[2,3,4]]))
# print(random.randrange(1,3)) # 不包括3

# a=[1,3,5,6,7]                # 将序列a中的元素顺序打乱
# random.shuffle(a)

# print( random.uniform(1.1,5.4) )     # 产生  1.1 到 5.4 之间的随机浮点数，区间可以不是整数
# print( random.randrange(1,100,2) )   # 生成从1到100的间隔为2的随机整数

# def ve_code():
#     code = ''
#     for i in range(4):
#         add_nu = str(random.randrange(1,10))
#         code += add_nu
#         #code = ''.join([code,add_nu,code])
#     return code
# print(ve_code())

# Ve_Code Professional Edition
# def ve_code():
#     _code = ''
#     i = 0
#     while i < 6:
#         random_num = random.randrange(48,123)
#         if (random_num >= 48 and random_num <= 57) or (random_num >= 65 and random_num <= 90) or (random_num >= 97 and random_num <= 122):
#             _code += chr(random_num)
#             i += 1
#
#     return _code
# print(ve_code())

# Ve_Code Professional Edition
def ve_code():
    _code = ''
    for i in range(4):
      #  random_num = random.choice([random.randrange(48,58),random.randrange(65,91),random.randrange(97,123)])
        _code += chr(random.choice([random.randrange(48,58),random.randrange(65,91),random.randrange(97,123)]))
    return _code
print(ve_code())