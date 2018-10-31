# author:virualv
#  date :8/27/2018

menu = {
    '安徽':{
            '六安':{"寿县":'众兴镇'},
            '合肥':'肥西'
          },
    '湖北':{'武汉':'青山区'},
    '广东':{'深圳':'龙岗区'}
}
for key in menu:
    print(key)

choice = input('choice :').strip()
if choice in menu:
    for key1 in menu[choice]:
        print(key1)

    choice1 = input('choice1:').strip()
    if choice1 in menu[choice]:
        for key2 in menu[choice][choice1]:
            print(key2)
        choice2 = input('choice2:').strip()
        if choice2 in menu[choice][choice1]:
            for key3 in menu[choice][choice1][choice2]:
                print(key3)