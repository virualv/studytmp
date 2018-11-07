# author:virualv
#  date :8/26/2018

# a = 10
#
# print('0x',id(a))
#
# b = a
#
# # b = 15
#
# print('0x',id(b))

# dic = {'name':'virualv','age':22,'hobby':'IT','address':'Lu\'an'}
#
# print(dic)
# print(dic['address'])

# 字典的两大特点：无序、键唯一
# dic = {'age':'virualv','age':22,'hobby':'IT','address':'Lu\'an'}
# print(dic)

# 增
# dic1 = {'name':'joy'}
# dic1['age'] = 18
# print(dic1)
# ret = dic1.setdefault('age',32)     # ******键存在，不改动，返回字典中的相应的键值
# print(dic1,'\n',ret)
# ret1 = dic1.setdefault('hobby','girl')  # 键不存在，在字典中增加新的键值对，并返回相应的值
# print(dic1,'\n',ret1)

# 删
# dic3 = {'name':'virualv','age':22,'hobby':'IT','address':'Lu\'an'}
#
# print(dic3.pop('hobby'))
# ret6 = dic3.pop('address')  # 删除字典中指定的键值对，并返回该键值对的值
# print(ret6)

# a = dic3.popitem()  # 随机删除字典中的键值对，并返回该键值对的键和值
# print(a,dic3)
#
# del dic3['name']    # 删除字典中指定的键值对
# print(dic3)
#
# dic3.clear()    # 清空字典
# print(dic3)
#
# del dic3    # 直接删除整个字典

# 查
# dic1 = {'name':'virualv','age':22,'hobby':'IT','address':'Lu\'an'}
# print(dic1.keys())
# print(type(dic1.keys()))
# print(list(dic1.keys()))
# print(type(list(dic1.keys())))
# print(dic1.items())         # dict_items([('name', 'virualv'), ('age', 22), ('hobby', 'IT'), ('address', "Lu'an")])
# print(dic1.values())
# print(dic1.get('name'))

# 改
# dic3 = {'name':'virualv','age':22,'hobby':'IT','address':'Lu\'an'}
# dic4 = {'name':'vicker','age':22,'hobby':'IT','address':'Lu\'an','qq':589656}
#
# dic3['name'] = 'joy'
# print(dic3)
#
# dic3.update(dic4)
# print(dic3,'\n',dic4)


#******************************************IMPORTANT*******************************************
# dic6 = dict.fromkeys(['host1','host2','host3','host4'],'test')
# print(dic6) # {'host1': 'test', 'host2': 'test', 'host3': 'test', 'host4': 'test'}

# 排序
# dic8 = {1:'553',8:'865',5:'96',6:'856',4:'852',7:'86'}
# print(sorted(dic8))     # [1, 4, 5, 6, 7, 8]      比较键的大小然后按键的大小排序
# print(sorted(dic8.values()))        # ['553', '852', '856', '86', '865', '96']
# print(sorted(dic8.items()))         # [(1, '553'), (4, '852'), (5, '96'), (6, '856'), (7, '86'), (8, '865')]

# 遍历
# dic3 = {'name':'virualv','age':22,'hobby':'IT','address':'Lu\'an'}
# for i in dic3:            # 效率高，推荐
#     print(i,':',dic3[i])
# for i in dic3.items():
#     print(i)
# for i,v in dic3.items():  # 效率低，不推荐
#     print(i,v)
# for i in dic3.values():
#     print(i)
