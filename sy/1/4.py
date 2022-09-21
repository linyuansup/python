n = int(input())
stri = ""
res = 0
for itoa in range(n + 1):
    stri += str(itoa)
    res += int(stri)
print(str(res))
