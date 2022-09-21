n = int(input()) + 1
maxNum = 0
a1 = 0
a2 = 0
a3 = 0
while a1 < n:
    a2 = 0
    while a2 < n:
        a3 = 0
        while a3 < n:
            if (a1 + a2) % 2 == 0 and (a2 + a3) % 3 == 0 and (a1 + a2 + a3) % 5 == 0:
                maxNum = max(maxNum, (a1 + a2 + a3))
            a3 += 1
        a2 += 1
    a1 += 1
print(maxNum)
