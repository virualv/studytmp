# Author : virualv
# Time : 9/20/2018 12:42 PM
import re

source = '1-2*((60-30+(40/5)-(4*3)/(16-3*2))'

def check(s):
    Flag = True
    if re.findall('[a-z]+',s.lower()):
        print('Invalid')
        Flag = False
    if s.count('(')!= s.count(')'):
        print('Invalid')
        Flag = False
    return Flag
def Format(string):
    string = string.replace('--','+')
    string = string.replace('-+','-')
    string = string.replace('++','+')
    string = string.replace('+-','-')
    string = string.replace('*+','*')
    string = string.replace('/+','/')
    string = string.replace(' ','')
if check(source):
    pr
    Format(source)
    if re.search('\(',source):
        source = re.search('\([^()]+\)',source).group()
        source =
