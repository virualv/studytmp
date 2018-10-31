# author:virualv
#  date :8/23/2018
print('my second program in pycharm.')

name = input('My name :')
age = int(input('My age :'))
job = input('My Job:')
salary = input('My salary:')
if salary.isdigit():    # 长得像不像数字
    salary = int(salary)
else:
    print('You must input digit!')
    exit()
msg = '''
======Information of %s======
Name :%s
Age :%d
Job :%s
Salary :%f
I will be retired in %d years
=============End=============
'''% (name,name,age,job,salary,65 - int(age))
print(msg)
