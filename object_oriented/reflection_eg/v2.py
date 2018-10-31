# Author : virualv
# Time : 10/20/2018 3:51 PM

import v1

obj = v1.fuu()

inp = input(">>>")

if hasattr(obj,inp):
    k = getattr(obj,inp)
    print(k())

else:print('404')