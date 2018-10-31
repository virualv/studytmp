# author:virualv
#  date :8/23/2018
exit_flag = False

for i in range(10):
    if i < 5:
        continue
    for j in range(10):
        print('layer2',j)
        if j == 5:
            #exit_flag = True
            break
    if exit_flag:
        break
    print('')