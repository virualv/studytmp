# Author : virualv
# Time : 9/27/2018 3:15 PM
import json
dic = {'Brand 1':'htc','Brand 2':'SAMSUNG','Brand 3':'Google','Brand 4':'Nokia','Brand 5':'Motorola'}

# data = json.dumps(dic)
# fp =open('JSON_text','w')
# fp.write(data)
# fp.close()

f = open('JSON_txt','w')
json.dump(dic,f)
f.close()