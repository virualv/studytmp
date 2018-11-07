# Author : virualv
# Time : 9/16/2018 1:59 PM
import os

print(os.getcwd())    # 获取当前工作目录
# os.chdir(r'C:\Windows')   #改变当前脚本工作目录；相当于shell下cd
# print(os.getcwd())

# print(os.curdir)          # 返回当前目录: ('.')

# print(os.pardir)      # 获取当前目录的父目录字符串名：('..')

# print(os.makedirs('home\\mki\\kem'))
# os.removedirs('home\\mki\\kem')

# os.mkdir('dim')
# os.mkdir('dim\\home')

# os.rmdir('dim\\home')
# os.rmdir('dim')

# print(os.listdir(r'D:\workspace'))          # ['python_study', 'python_study.zip']
# os.remove('kit.py')              # 只能删除文件，不能删除文件夹
# os.rename('qq','pp')             # 可以重命名文件，也可以重命名文件名
# os.rename('ff','go')

# info=os.stat('.\\pp')
# print(type(os.listdir(r'D:\workspace')))
# print(info)
# print(info.st_size)
print(os.sep)
# s = os.sep        # 用os.sep代替\\或/,使程序再Linux和win上通用
print(type(os.sep))
# os.sep    # 输出操作系统特定的路径分隔符，win下为"\\",Linux下为"/"
# print(os.linesep)  # 输出当前平台使用的行终止符，win下为"\r\n",Linux下为"\n"
# print(os.pathsep)   # 输出用于分割文件路径的字符串
# print(os.name)

# os.system("bash command")  # 运行shell命令，直接显示
# print(os.environ)  # 获取系统环境变量
# print(os.path.abspath('./_time.py'))  # 返回path规范化的绝对路径

# s = os.path.split(r'D:\workspace\module\_time.py')  # 将path分割成目录和文件名二元组返回
# print(s)                    # ('D:\\workspace\\module', '1_time.py')

#print(os.path.dirname(r'D:\workspace\module\1_time.py'))  # 返回path的目录。其实就是os.path.split(path)的第一个元素
