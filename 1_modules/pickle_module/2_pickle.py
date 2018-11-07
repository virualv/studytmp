# author:virualv
#  date :9/26/2018

import pickle

def foo():
    print('Hello!')
data = pickle.dumps(foo)
print(data)

f = open('pickle_text','wb')
f.write(data)
f.close()

f = open('pickle_text','rb')
ad = f.read()
ad = pickle.loads(ad)
print(ad)