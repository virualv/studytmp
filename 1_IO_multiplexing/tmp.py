# Time    : 11/21/2018 10:22 PM
# Author  : virualv
import re
def bin2dec(bina):
    bina = bina.strip()[2:]
    b_list = re.findall('[0-9]',bina)
    sum = 0
    a = 0
    b_list.reverse()
    for i in b_list:
        sum += (int(i)*(2**a))
        a += 1
    print('dec',sum)

bin2dec('0b1111011')
