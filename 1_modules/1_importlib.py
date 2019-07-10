# Time    : 12/3/2018 3:50 PM
# Author  : virualv

import importlib

t = 'os'
h = 'getcwd'
o_s = importlib.import_module(t)


fuct = getattr(o_s,h)

print(fuct())