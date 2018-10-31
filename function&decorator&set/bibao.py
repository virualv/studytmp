# Author : virualv
# Time : 9/10/2018 12:24 PM

def outer():
    x = 10
    def inner():    # 条件一 inner就是内部函数
        print(x)    # 条件二 外部环境的一个变量（非全局变量）
    return inner  # 结论 内部函数inner就是一个闭包

# outer()
# inner() 局部变量，无法全局使用

f = outer()
f()

# 关于闭包： 闭包 = 内部函数块 + 定义函数时环境
