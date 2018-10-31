# Author : virualv
# Time : 10/25/2018 2:42 PM

import subprocess

get = subprocess.Popen('dir',shell=True,stdout=subprocess.PIPE)
print(get.stdout.read())