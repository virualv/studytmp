# Author : virualv
# Time : 9/11/2018 10:38 AM

with open('id','r+') as _id_:
    _id_.write(str({'user':'vicker','passwd':'hzy122925'}))
    _id_.flush()
with open('wechat_id','r+') as _id_:
    _id_.write(str({'user':'vicker','passwd':'hzy122925'}))
    _id_.flush()
flag = False
def _authentication_(auth_type = 'myself'):
    def tran(func):
        def inner():
            global flag
            if not flag:
                if auth_type == 'myself':
                    while not flag:
                        _user_ = input('user:')
                        _pass_ = input('passwd:')
                        with open('id','r') as _id_:
                            identity = eval(_id_.readline())
                            if _user_ == identity['user'] and _pass_ == identity['passwd']:
                                print('Login success,Welcome to GoStore!')
                                flag = 'True'
                            else:
                                print('invalue username or password!please re-enter')
                                continue

                elif auth_type == 'wechat':
                    while not flag:
                        _user_ = input('wechat user:')
                        _pass_ = input('wechat passwd:')
                        with open('wechat_id','r') as _id_:
                            identity = eval(_id_.readline())
                            if _user_ == identity['user'] and _pass_ == identity['passwd']:
                                print('Login success,Welcome to GoStore!')
                                flag = True
                            else:
                                print('invalue username or password!please re-enter')
                                continue
            else:pass
            func()
        return inner
    return tran
@_authentication_(auth_type = 'myself')
def _home_():
    print("welcome to home!")
@_authentication_(auth_type = 'wechat')
def finance():
    print('Welcome to GoStore Finance Channel')
@_authentication_()
def book():
    print('Welcome to GoStore book channel')

while True:
    channel = input('choose channel:')
    if channel.isdigit():
        channel = int(channel)
        if channel == 1:
            _home_()
        elif channel == 2:
            finance()
        elif channel == 3:
            book()
        else:
            print('we can not find this channel!')
    else:
        print('it is a error channel number info,please re-enter channel number!')
