# author:virualv
#  date :8/24/2018

a = ['wuchao','jinxing','yu','ta','jin','yu','jun','yun']
# 增删改查

# print(a[3])

# 查 切片
# print(a[0:])#取到最后
# print(a[1:3])#取第二个和第三个
# print(a[1:-1])#取到倒数第二个
# print(a[1:-1:2])#从左往右隔一个取(从第二个开始)
# print(a[-1:1:-2])#从右往左隔一个取
# print(a[-2:-5:-2])#从右往左隔一个取(从右边第一个开始)
# #取得方向是由第三个数的正负所决定
# print(a[3::-2])#从3（第四个）开始一直往最左边走，隔一个取一个
# b = a[-2::-1]
# print(b)

# 添加append 追加 insert插入

# a.append('xuefeng')#append 追加到最后一行
# # print(a)
#
a.insert(2,'xueyu')#insert 插入到任意一个位置
print(a)

# 修改
# a[2]='jinyu'
# print(a)
# a[1:3]=('yujin','xux')
# print(a)

# 删除 remove pop del
# a.remove('yujin')
# print(a)

# c = a.pop(1)
# print(a)
# print(c)

# del a[3]
# print(a)
# del a   #直接删除对象a

# a = ('')
# print(a)

# count计算元素出现次数

# t = ['to','or','not','to','be'].count('to')
# print(t)

# extend（延伸; 扩大; 推广）增加内容
# b = [4,5,6]
# a.extend(b)
# print(a)
# print(b)

# index检索列表的某个元素在列表中的位置
# print(a.index('jinxing'))

# 寻找第二个yu的位置
# first_yu_index = a.index('yu')
# little_list = (a[first_yu_index+1:])
# second_yu_index = little_list.index('yu') + first_yu_index
# print('second_yu_index_in_big_list',second_yu_index+1)

# reverse 将列表倒过来
# a.reverse()
# print(a)

# sort排序
# b = [1,6,5,8,9,7,3,4]
# b.sort()
# print(b)
# c = sorted(b)
# print(c)

# print(a.count('haidilaoge'))
#
# print('haidilaige' in a)