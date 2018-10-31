# author:virualv
#  date :9/26/2018

import pickle

def foo():
    print('Hello!')
data = pickle.dumps(foo)

f = open('pickle_text','wb')
f.write(data)
f.close()