import math

if __name__ == '__main__':
    ab = float(input())
    cd = float(input())
    r = ab / 2 + cd * cd / 8 / ab
    print('%.2f' % r)
    round = math.asin(ab / 2 / r) * 2
    area = round / 2 * r * r
    tangle = ab * (r - cd)
    print('%.2f' % (area - tangle))
