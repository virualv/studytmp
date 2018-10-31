# author:virualv
#  date :8/28/2018

s = '玛莎拉蒂'
s_to_uft8 = s.encode('utf-8')
print(s_to_uft8)
utf8_to_unicode = s_to_uft8.decode('utf-8')
print(utf8_to_unicode)
unicode_to_gbk = utf8_to_unicode.encode('gbk')
print(unicode_to_gbk)
gbk_to_unicode = unicode_to_gbk.decode('gbk')
print(gbk_to_unicode)