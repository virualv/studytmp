# Author : virualv
# Time : 9/28/2018 11:07 AM
import shelve

f = shelve.open('shelve_txt')

# f['student_info'] = {'name':'vicker','mark':'kyro','hobby':'IT'}
data = f.get('student_info')
print(data)
data1 = f['student_info']['mark']
print(data1)