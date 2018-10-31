# author:virualv
#  date :8/23/2018


userdf = 'vicker'
passdf = 'hzy122925'
passed_authentication = False # 假 不成立 flag标志位

for i in range(3):
	print('-----------------ID Cretification-----------------')
	user = input('Please input username:')
	pass1 = input('Please input  passwd :')

	if user != userdf or pass1 != passdf:
		print('Invalid user or password,please re-enter!')
		continue
	else:
		print('Authenticate Success,Welcome New System!')
		passed_authentication = True    # 真 成立
		break
if not passed_authentication:  # 取反 当真时，不输出
	print('Your account is already locked!')

# 下面的方法也是对的，并且更加简洁
# userdf = 'vicker'
# passdf = 'hzy122925'
#
# for i in range(3):
# 	print('-----------------ID Cretification-----------------')
# 	user = input('Please input username:')
# 	pass1 = input('Please input  passwd :')
# 	if user != userdf or pass1 != passdf:
# 		print('Invalid user or password,please re-enter!')
# 	else:
# 		print('Authenticate Success,Welcome New System!')
#       break   #break for后，就不会执行最后面的else语句
# else:   #只要for循环正常执行完毕，中间未被打断，就会执行else语句
# 	print('Your account is already locked!')
