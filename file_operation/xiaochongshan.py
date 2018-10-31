# author:virualv
#  date :8/28/2018

# date = open('xiaochongshan','r',encoding='utf-8').read()
#
# print(date)

# f1 = open('xiaochongshan1','w',encoding='utf-8')
# # print(f1)
# date1 = f1.write('')
# print(date1)
# f1.close()

# f = open('xiaochongshan','r',encoding='utf-8')
# date = f.read(2)
# print(date)
# f.close()

# f2 = open('xiaochongshan2','w',encoding='utf-8')
#
# f2.write('hello world')
# f2.write('joy')
# f2.close()
# f2 = open('xiaochongshan2','a',encoding='utf-8')
#
# f2.write('\nHello World\nHolle')
# f2.close()

# f = open('xiaochongshan','r',encoding='utf-8')
# a =f.readlines()
# print(f.readlines())
# print(type(a))
# f.close()
# number = 0
#
# for i in a:                  # f.readlines()
#     number += 1
#     if number == 6:
#         i = ''.join((i,'#i like it !'))
#         # i = i + '#i like it!'
#     print(i.strip())

# for i in date:
#     print(i.strip())

# print(f.tell())     # 输出光标的位置  （0）
# print(f.read(2))
# print(f.tell())     # 输出光标的位置   （6） 如果是英文则是2
# f.seek(0)           # 将光标移到第一位
# print(f.tell())     # 输出光标的位置   （0）

# f.flush()           # 刷新缓冲区字段，刷新后保存在存储器中

# with                # with代码块中的打开文件不需要关闭，即不需要f.close()。也可同时管理多个文件
# with open('xiaochongshan','r') as f:
#     f.readlines()
#     f.read()
#
# with open('file1','r') as f1,open('file2','r') as f2:
#     f1.read()
#     f2.readlines()

# import sys,time
# for i in range(30):
#     sys.stdout.write('*')
#     sys.stdout.flush()
#     time.sleep(0.5)
# import time
# for i in range(30):
#     print('*',end='',flush=True)
#     time.sleep(0.2)

# f = open('xcs','a',encoding='utf8')
# f.truncate(5)
# f.close()

