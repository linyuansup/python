import math


def sqrt_binary(n):
    left = 0.0
    right = float(n)
    while right - left > 1e-6:
        mid = (left + right) / 2
        if mid * mid > n:
            right = mid
        else:
            left = mid
    return left


n = int(input())
print(sqrt_binary(n))
print(math.sqrt(n))
