with open("C:/Users/93601/Code/python/sy/2/data.txt", 'r', encoding='utf-8') as fp:
    list = fp.read().split('\n')
i = 1
for l in list:
    if not l == '':
        data = l.split(',')
        total = 0
        for sorce in data:
            sorce = int(sorce[-2:])
            total += sorce
        print("第{}个学生的总成绩为{}".format(i, total))
        print("第{}个学生的平均分为{}".format(i, total / 6))
        i += 1
