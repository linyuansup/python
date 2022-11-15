import random


def newString():
    a = random.randint(0, 3)
    num_str = "".join(str(random.choice(range(10))) for _ in range(a))
    return num_str


n = int(input())
s = ""
for i in range(n):
    s += newString()
print(s)
