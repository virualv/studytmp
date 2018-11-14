# Time    : 11/13/2018 9:52 PM
# Author  : virualv
from greenlet import greenlet

def test1():
    print('Test *')
    grl2.switch()
    print('Test **')
    grl2.switch()

def test2():
    print('Test &')
    grl1.switch()
    print("Test &&")

grl1 = greenlet(test1)
grl2 = greenlet(test2)

grl1.switch()