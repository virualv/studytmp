# Author : virualv
# Time : 9/19/2018 2:04 PM

import re

# s = input('compute:')
# s ='
s = '1-2*((60-30+(40/5)-(4*3)/(16-3*2))'

def check(s):
    flag = True
    if re.findall('[a-zA-Z]',s):
        print('Invalid')
        flag = False
    # elif re.findall('[^1-9]',s):
    #     print('Invalid')
    #     flag = False
    elif s.count('(') != s.count(')'):
        print('Invalid')
        flag = False
    return flag

def format(s):
    s = s.replace(' ','')
    s = s.replace('+-','-')
    s = s.replace('--','+')
    s = s.replace('++','+')
    s = s.replace('-+','-')
    s = s.replace('*-','*')
    return s

def cal_mult_dev(s):
    while re.findall('\d+\.?\d*[*/]\d+\.?\d*',s):
        s_dev = re.search('\d+\.?\d*[*/]\d+\.?\d*', s)
        s1 = s_dev.group()
        if re.search('\*',s1):
            s1 = s1.split('*')
            _result_ = float(s1[0])*float(s1[1])
        else:
            s1 = s1.split('/')
            _result_ = float(s1[0])/float(s1[1])
        s = s.replace(s_dev.group(),str(_result_))
    return s
def cal_add_sub(s):
    while re.findall('\d+\.?\d*[+-]\d+\.?\d*',s):
        format(s)
        s_dev = re.search('\d+\.?\d*[+-]\d+\.?\d*',s)
        s1 = s_dev.group()
        if re.search('\+',s1):
            s1 = s1.split('+')
            _result_ = float(s1[0])+float(s1[1])
        else:
            s1 = s1.split('-')
            _result_ = float(s1[0])-float(s1[1])
        s = s.replace(s_dev.group(),str(_result_))
    return s

if check(s):
    format(s)
    while re.search('\(', s):
        if re.search('\([^()]+\)', s):
            # if re.findall('[*/]', s):
            #     sp = re.search('\([^()]+\)', s)
            #     s1 = re.findall('[^()]+', sp.group())
            #     s1 = ''.join(s1)
            #     s1 = cal_mult_dev(s1)
            # if re.findall('[+-]', s1):
            #     s1 = cal_add_sub(s1)
            s = s.replace(sp.group(), s1)
    else:
        if re.findall('[*/]', s):
            s = cal_mult_dev(s)
        if re.findall('[+-]', s):
            s = cal_add_sub(s)
    print('result is',s)
