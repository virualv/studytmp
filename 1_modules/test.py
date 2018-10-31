# Author : virualv
# Time : 9/19/2018 8:24 PM
import re
s = '56+5.2*2+96/2+9-5'
def cal_mult_dev(s):
    while re.findall('\d+\.?\d*[*/]\d+\.?\d*',s):
        s_dev = re.search('\d+\.?\d*[*/]\d+\.?\d*',s)
        s1 = s_dev.group()
        if s1.split('*')[0] == s1.split('*')[-1]:
            s1 = s1.split('/')
            _result_ = float(s1[0])/float(s1[1])
        else:
            s1 = s1.split('*')
            _result_ = float(s1[0])*float(s1[1])
        s = s.replace(s_dev.group(),str(_result_))
    return s
def cal_add_sub(s):
    while re.findall('\d+\.?\d*[+-]\d+\.?\d*',s):
        s_dev = re.search('\d+\.?\d*[+-]\d+\.?\d*',s)
        s1 = s_dev.group()
        if s1.split('+')[0] == s1.split('+')[-1]:
            s1 = s1.split('-')
            _result_ = float(s1[0])-float(s1[1])
        else:
            s1 = s1.split('+')
            _result_ = float(s1[0])+float(s1[1])
        s = s.replace(s_dev.group(),str(_result_))
    return s
if re.findall('[*/]',s):
    s = cal_mult_dev(s)
if re.findall('[+-]',s):
    s = cal_add_sub(s)
print('result is',s)



