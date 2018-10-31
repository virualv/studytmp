# author:virualv
#  date :8/25/2018
product_list = [
    ('iphone 6s',4999),
    ('imacbookpro',12999),
    ('Tesla',500000),
    ('Mi8',2699),('MiA2',1799),
    ('Python Book',80),
    ('coffee',30)
]
shopping_cart = []
salary = input('Please input your salary:')

if salary.isdigit():
    salary = int(salary)
    while True:
        for i,v in enumerate(product_list,1):
            print(i,'>>>>>>\t',v[0],v[1],'')
        n = input('You choose which on follow[quit:q]:')
        if n.isdigit():
            n = int(n)
            if n > 0 and n <= len(product_list):
                item = product_list[n-1]
                if salary >= item[1]:
                    shopping_cart.append(item)
                    salary -= int(item[1])
                    print(product_list[n-1][0],product_list[n-1][1],'already add your shopping cart\nyour balance is %d'% salary)
                else:
                    print('You balance is not enough')
                    continue
            else:
                print('invalid number')
                continue
        elif n == 'q':

            print('You will quit shopping cart\n----------------End----------------\nYou already buy products in follow:')
            break
        else:
            print('invalid character')
            continue
for s in enumerate(shopping_cart):
    print(s[1][0],'  RMB ',s[1][1])
print('you balance is %d'% salary)


