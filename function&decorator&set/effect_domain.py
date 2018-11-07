# Author : virualv
# Time : 9/8/2018 11:09 AM
# x = int(2.9)  # int built-in
#
# g_count = 0  # global
#
#
# def outer():
#     o_count = 1  # enclosing
#
#     def inner():
#         i_count = 2  # local
#         print(o_count)
#
#     # print(i_count) 找不到
#     inner()
#
#
# outer()

# print(o_count) #找不到

# count = 10
#
# def outer():
#     global count
#     count += 10
#     print(count)
# outer()

def outer1():
    count = 10      # enclosing
    def inner():
        nonlocal count
        count = 20
        print(count)
    inner()
    print(count)
outer1()
