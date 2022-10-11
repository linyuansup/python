import math


def isPriority(n):
    if n == 1:
        return False
    if n in [2, 3]:
        return True
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


n = int(input())
for i in range(2, n + 1):
    if isPriority(i):
        print(i)
