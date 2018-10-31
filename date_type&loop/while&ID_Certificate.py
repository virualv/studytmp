# author:virualv
#  date :8/23/2018
userdf = 'vicker'
passdf = 'hzy122925'
counter = 0

while counter < 3:
    print('-----------------ID Cretification-----------------')
    user = input('Please input username:')
    pass1 = input('Please input  passwd :')

    if user != userdf or pass1 != passdf:
        print('Invalid user or password,please re-enter!')
    else:
        print('Authenticate Success,Welcome New System!')
        break
    counter += 1
    if counter == 3:
        keep_going_choice = input('Will you continue?[y/n]')
        if keep_going_choice == 'y':
            counter = 0
else:
    print('Your account is already locked!')