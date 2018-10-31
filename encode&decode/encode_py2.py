# -*- encoding: utf-8 -*-
# author:virualv
#  date :8/27/2018

s = '特斯拉'
s_to_unicode = s.decode('utf-8')
unicode_to_gbk = s_to_unicode.encode('gbk')
print(s_to_unicode)
print(unicode_to_gbk.decode('gbk'))