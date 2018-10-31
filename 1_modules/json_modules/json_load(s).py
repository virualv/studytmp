# Author : virualv
# Time : 9/27/2018 3:21 PM
import json

fp = open('JSON_txt','r')
data = json.load(fp)
print(data['Brand 2'])


# fp = open('JSON_text','r')
data1 = fp.read()
data1 = json.loads(data1)
print(data['Brand 1'])