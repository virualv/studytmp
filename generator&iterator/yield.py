# author:virualv
#  date :11/3/2018

def th():
    i = 0
    while True:
        if i<10:
            i += 1
            yield i
        else:
            return

t = th()

for j in t:
    print(j)