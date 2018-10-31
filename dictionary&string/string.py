# author:virualv
#  date :8/26/2018

# 字符转义
# a = 'Let\'s go'
# a = "Let's go"
# print(a)

# 重复输出
# var1 = "Hello World"
# print(var1*2)

# 索引，切片
print("HelloWorld"[1:-1])   # 0为开始位
# a = "Hello world"
# print(a[2:])

# 判断字符（串）在不在字符串里
# print('he' in "Hello")

# 格式化字符
# print("%s is a student"%'virualv')

# 字符串拼接
# a = 'ab'
# b = 'c123'
# c = a+b       # 效率低
# print(c)
#
# c = '***'.join([b,a])     # 效率高
# print(c)
# c = '***'.join([a,b])
# print(c)

# 字符串的内置方法
# st = "hello\tkitty"
# print(st.count("l"))                                        # 统计元素个数
# print(st.capitalize())                                      # 将首字母大写
# print(st.center(50,"-"))                                    # 居中 （as:------hello kitty-------）
# print(st.endswith('tty'))                                   # 判断是否以某个内容结尾
# print(st.startswith('he'))                                  # 判断是否以某个内容开头
# print(st.expandtabs(tabsize=5))                             # 扩大tab的长度
# st = "hello kitty"
# print(st.find('t'))                                         # 查找到该元素第一个，并将索引值返回
# a = 'hello kitty {name} is {age}'
# print(a.format(name = 'virualv',age = 22))                  # 格式化输出的另一种方式
# print(a.format_map({'name':'virualv','age':23}))            # 格式化输出的另一种方式(利用字典实现)
# print(a.index('t'))                                         # 查找字符的位置
# print('a12d1'.isalnum())                                    # 判断字符串是不是字母或数字，若为特殊字符返回False
# print('854'.isdecimal())                                    # 判断是不是十进制数
# print('2546'.isdigit())                                     # 判断是不是一个整型数字
# print('126'.isnumeric())                                    # 判断是不是一个整型数字
# print('cc3'.isidentifier())                                 # 判断是不是一个非法字符（根据变量的命名规则来判别）
# print('dkad'.islower())                                     # 判断是不是都小写
# print('SHOI'.isupper())                                     # 判断是不是都大写
# print(' da'.isspace())                                      # 判断是不是都是空格
# print('Hidle Hie'.istitle())                                # 判断是不是标题（每个单词首字母是不是大写）
# print('My Tile'.lower())                                    # 全变小写
# print('My tile'.upper())                                    # 全变大写
# print('My Tile'.swapcase())                                 # 大写变小写，小写变大写
# print('My Tile'.ljust(20,'*'))                              # 左对齐
# print('My Tile'.rjust(20,'*'))                              # 右对齐
# print('  My Title \n'.strip())                              # 用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。    注意:该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。
# print('\tMy Title \n'.lstrip())
# print('\tMy Title \n'.rstrip())
# print('My Title'.replace('Ti','ac'))                        # 替换字符（串）
# print('My title title'.rfind('t'))                          # 从右边开始找的第一个元素的位置，但位置是从做开始数的，第一个以0计数
# print('My Title'.split())                                   # 将字符串分成列表
# #  可用.join('','')的方式将列表转换成字符串
# print('My title'.title())                                   # 转换为标题，每个单词首字母变大写

# important
# print(st.count("l"))                                        # 统计元素个数
# print(st.center(50,"-"))                                    # 居中 （as:------hello kitty-------）
# print(st.startswith('he'))                                  # 判断是否以某个内容开头
# print(st.find('t'))                                         # 查找到该元素第一个，并将索引值返回
# print(a.format(name = 'virualv',age = 22))                  # 格式化输出的另一种方式
# print(a.format_map({'name':'virualv','age':23}))            # 格式化输出的另一种方式(利用字典实现)
# print('My tile'.upper())                                    # 全变大写
# print('My Tile'.lower())                                    # 全变小写
# print('  My Title \n'.strip())                              # 用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。    注意:该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。
# print('My Title'.replace('Ti','ac'))                        # 替换字符（串）
# # print('My Title'.split())                                   # 将字符串分成列表
# #  可用.join('','')的方式将列表转换成字符串
