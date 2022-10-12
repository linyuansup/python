def isprime(n):
    for i in range(2, int(n ** 0.5 + 1)):
        if n % i == 0:
            return False
    return True


def add(a):
    b = []
    for i in range(a, 1, -1):
        if len(b) >= 10:
            break
        if isprime(i):
            b.append(i)
    return sum(b)


def testsum():
    assert add(100) == 732
    assert add(1000) == 9664
    assert add(10000) == 99308
    assert add(100000) == 999330
    assert add(1000000) == 9999336
