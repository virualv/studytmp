# Author : virualv
# Time : 9/20/2018 3:45 PM
import re
def mult_dev(s):
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
def add_sub(s):
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