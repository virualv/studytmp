# Author : virualv
# Time : 9/18/2018 4:37 PM

import re

# ret = re.findall('jiu','heisndhspdskdsjidfnsaujiufndsjksdcsdhka')
# print(ret)

ret = re.findall('j..f','heisndhspdskdsjidfnsaujiufndsjksdcsdhka')  # 一个‘.’只能代指一个字符
print(ret)              # ‘.’可以匹配除换行符以外一切字符

# ^ 只匹配行首
ret1 = re.findall('^..H','JiHdmdisndsjasdxadHdskdsnlHukdksdHmckdc')
print(ret1)

# $ 匹配行末
ret2 = re.findall('c..c$','JiHdmdisndsjasdxadHdskdsnlHukdksdHmckdc')
print(ret2)

# * 重复匹配
ret3 = re.findall('f*y','frkdjdnfjjffffygdfidinfffdldffjkfnfjdyfebhesjffdffffydesef')
print(ret3)

# + [1,+∞]次匹配           # 等价于{1,}
ret4 = re.findall('ab+','kjssdfldfah')
print(ret4)

ret5 = re.findall('a+d','fsndjskahsisaaaadllknk')
print(ret5)

# ? [0,1]次匹配
ret6 = re.findall('a?s','ddsaaaaassdajd')
print(ret6)

# {}
ret7 = re.findall('a{3}j','xiaomiddiaaajidnsaajdsjaaaaienj')
print(ret7)
ret8 = re.findall('a{1,4}j','xiaomiddiaaajidnsaajdsjaaaajienj')
print(ret8)

# *等价于{0，+∞}   +等价于{1，+∞}       ？等价于{0,1}

# 字符集

# ret9 = re.findall('a[b,c,d]x','adx')
# print(ret9)
ret9 = re.findall('abc[b,c]','hijiu.comabccn')
print(ret9)

ret9 = re.findall('[a-z]','h1d5sd4c1')
print(ret9)

# [] 字符集    取消元字符的特殊功能
ret10 = re.findall('[w,*,.,,]','dh,si.na*i')
print(ret10)

ret10 = re.findall('[0-9 ]','dh5cs6i8na5i')
print(ret10)

# ^放在[]里，取反
ret11 = re.findall('[^4+6]','48f5d+s56+')
print(ret11)

# \
# 反斜杠后边跟元字符去除特殊功能,比如\.
# 反斜杠后边跟普通字符实现特殊功能,比如\d

# \d  匹配任何十进制数；它相当于类 [0-9]。
# \D 匹配任何非数字字符；它相当于类 [^0-9]。
# \s  匹配任何空白字符；它相当于类 [ \t\n\r\f\v]。
# \S 匹配任何非空白字符；它相当于类 [^ \t\n\r\f\v]。
# \w 匹配任何字母数字字符；它相当于类 [a-zA-Z0-9_]。
# \W 匹配任何非字母数字字符；它相当于类 [^a-zA-Z0-9_]
# \b  匹配一个特殊字符的边界，比如空格 ，&，＃等

print(re.findall('\d{5}','dddds457575d48d5d475dd7744'))
print(re.findall(r'y\b','helloyketty&,honey is goy/'))

#####################################################

# 匹配出第一个满足条件的结果
ret12 = re.search('sk','shdsbdkndnskbdjdnskdns')
print(ret12) # <re.Match object; span=(10, 12), match='sk'>
print(ret12.group())    #sk

ret13 = re.search('a\.','a.dks')
print(ret13.group())

ret13 = re.search('a\*','a.da*ks')
print(ret13.group())

ret = re.findall('\\\\g','dsjdnD\g')
print(ret)

ret = re.search(r'\bbl','blow')
print(ret)

#####################################################

# () |
print(re.search('(as)+','adssaadsaasasdsddfcaaaaaasasddeaaqasdcdsad').group())
print(re.search('(as|3)','a3das').group())

ret = re.match('sjs','dsdsjsnds')
print(ret)
ret = re.match('ds','dsdsjsnds')
print(ret)

'sdsjkd'.split('j')
ret4 = re.split('[j,k]','fmkskjdbsjkd')                  #*******
print(ret4)

ret = re.sub('h..u','sdjd','skajkdhusanshddusksla')
print(ret)

obj = re.compile('\.com')
ret = obj.findall('comdssasa.com')
print(ret)

ret=re.search('(?P<id>\d{2})/(?P<name>\w{3})','23/com')
print(ret.group())#23/com
print(ret.group('id'))#23


##################################################

#5
ret=re.sub('\d','abc','alvin5yuan6',1)
print(ret)#alvinabcyuan6
ret=re.subn('\d','abc','alvin5yuan6')
print(ret)#('alvinabcyuanabc', 2)

##################################################

ret = re.finditer('\d', 'ds3sy4784a')
print(ret)  # <callable_iterator object at 0x10195f940>

print(next(ret).group())
print(next(ret).group())

ret = re.findall('www.(baidu|oldboy).com', 'www.oldboy.com')
print(ret)  # ['oldboy']     这是因为findall会优先把匹配结果组里内容返回,如果想要匹配结果,取消权限即可

ret = re.findall('www.(?:baidu|oldboy).com', 'www.oldboy.com')
print(ret)  # ['www.oldboy.com']




ret = re.findall('[^$]','$sss')
print(ret)