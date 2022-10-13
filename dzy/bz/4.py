import math

if __name__ == '__main__':
    ab = float(input())
    cd = float(input())
    r = ab / 2 + cd * cd / 8 / ab
    print('%.2f' % r)
    print('%.2f' % (math.asin(ab / 2 / r) * r * r - ab * (r - cd)))
