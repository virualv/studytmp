# Author : virualv
# Time : 10/20/2018 10:33 AM


# while True:
#     try:
#         imp = input('input n.o:')
#         i = int(imp)
#     except Exception as e:
#         print(e)
#         i = 1
#     print(i)



# try:
#     int('w3r')
# except IndexError as e:
#     print(e)
# except ValueError as e:
#     print(e)
# except Exception as e:
#     print(e)
# else:
#     print('else')
# finally:
#     print('......')


# try:
#     raise Exception('guo ge pi')
#
# except Exception as e:
#     print(e)


'''
class javaerror(Exception):

    def __init__(self,msg):
        self.message = msg

    def __str__(self):
        return self.message

# obj = javaerror('error')
# print(obj)

try:
    raise javaerror('i am error')
except javaerror as e:
    print(e)

'''


# assert条件  ,断言，用于强制用户服从，不服从就报错，可捕获，但一般不捕获

print('123')
assert 1 == True
print('85')
assert 2 == 1
print('86')
