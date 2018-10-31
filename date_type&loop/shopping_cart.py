# author:virualv
#  date :8/24/2018

salary = int(input('Salary:'))
print('''
-------Menu-------
1.iphone 6s     $ 4999
2.macbook pro   $ 12999
3.coffee        $ 30
4.python book   $ 88
5.bicyle        $ 560
''')
a = b = c = d = e = 0
while salary > 0:
    _what = (input('>>>>>>'))
    if _what == '1':
        if salary >= 4999:
            salary -= 4999
            a += 1
            print('%d iphone 6s already append your shopping cart,current balance:%d'% (a, salary))
        else:
            print('balance is not enough,current balance:', salary)
            continue
    elif _what == '2':
        if salary >= 12999:
            salary -= 12999
            b += 1
            print('%d macbook pro already append your shopping cart,current balance:%d'%(b,salary))
        else:
            print('balance is not enough,current balance:', salary)
            continue
    elif _what == '3':
        if salary >= 30:
            salary -= 30
            c += 1
            print('%d coffee already append your shopping cart,current balance:%d'%(c,salary))

        else:
            print('balance is not enough,current balance:', salary)
            continue
    elif _what == '4':
        if salary >= 88:
            salary -= 88
            d += 1
            print('%d python books already append your shopping cart,current balance:%d'%(d,salary))
        else:
            print('balance is not enough,current balance:', salary)
            continue
    elif _what == '5':
        if salary >= 560:
            salary -= 560
            e += 1
            print('%d bicycle already append your shopping cart,current balance:%d'%(e,salary))
        else:
            print('balance is not enough,current balance:', salary)
            continue
    elif _what == 'q':
        # print('')
        break
    else:
        print('we have not your choice, please see the menu again!')
        continue
print('''
You already buy commodities in follow:
iphone 6s     %d    $%d
macbook pro   %d    $%d
coffee        %d    $%d
python book   %d    $%d
bicyle        %d    $%d
Total               $%d
Your balance is     $%d
'''%(a,4999*a,b,12999*b,c,30*c,d,80*d,e,560*e,4999*a+12999*b+30*c+80*d+560*e,salary))