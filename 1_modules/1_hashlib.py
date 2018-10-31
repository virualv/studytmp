# Author : virualv
# Time : 9/17/2018 2:23 PM
import hashlib

m = hashlib.md5()
print(m)
m.update('hello world'.encode('utf8'))       # 5eb63bbbe01eeed093cb22bb8f5acdc3
print(m.hexdigest())

m.update('virualv'.encode('utf8'))      # a9bac97af7359bab2ad2f0dd24956230
print(m.hexdigest())

m2 = hashlib.md5()
m2.update('virualv'.encode('utf8'))     # d2437a2c8cc247738649706ea9c737f9
print(m2.hexdigest())

m3 = hashlib.md5()
m3.update('hello worldvirualv'.encode('utf8'))      # a9bac97af7359bab2ad2f0dd24956230
print(m3.hexdigest())

m4 = hashlib.sha256()
m4.update('hello worldvirualv'.encode('utf8'))      # a9bac97af7359bab2ad2f0dd24956230
print(m4.hexdigest())