ipt = input()
res = []
strlist = ipt.split(",")
a = int(strlist[0])
for i in range(int(strlist[2])):
    res.append(a)
    a += int(strlist[1])
print(res)
