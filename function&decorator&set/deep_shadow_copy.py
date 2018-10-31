import copy

husband = ["jinling",101,[15000,8000]]
wife = copy.copy(husband)                # 浅拷贝，同husband.copy一样
wife[0] = 'wulin'
wife[1] = 102
wife[2][0] -= 200
print(husband)
print(wife)

husband = ["jinling",101,[15000,8000]]
lover = copy.deepcopy(husband)          # 深拷贝
lover[0] = 'liyu'
lover[1] = 103
lover[2][0] -= 300
print(husband)
print(lover)


