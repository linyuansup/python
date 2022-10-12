import matplotlib
import numpy
import matplotlib.pyplot as plt


def rev(l):
    ret = list()
    for i in range(6):
        row = list()
        for j in range(24):
            row.append(l[j][i])
        ret.append(row)
    return ret


if __name__ == '__main__':
    with open("C:/Users/93601/Code/python/dzy/bz/sensor-data.txt", 'r', encoding='utf-8') as fp:
        lis = fp.read().split('\n')
    for i in range(len(lis)):
        lis[i] = lis[i].split(' ')
    reverse = rev(lis)
    arr = numpy.array(reverse)
    date = arr[0]
    time = arr[1]
    temper = arr[2].astype(float)
    wet = arr[3].astype(float)
    light = arr[4].astype(float)
    vol = arr[5].astype(float)
    print("最大值：%.2f" % max(light))
    print("最小值：%.2f" % min(light))
    print("平均值：%.2f" % numpy.mean(light))
    print("标准差：%.2f" % numpy.std(light))
    xlen = range(1, len(date) + 1)
    font = {'family': 'SimHei'}
    matplotlib.rc("font", **font)
    plt.figure(1)
    plt.xticks(xlen, time, rotation=45)
    plt.plot(xlen, temper, 'r', label='温度')
    plt.show()
    plt.figure(2)
    plt.xticks(xlen, time, rotation=45)
    plt.plot(xlen, wet, 'b', label='湿度')
    plt.show()
    plt.figure(3)
    plt.xticks(xlen, time, rotation=45)
    plt.plot(xlen, light, 'g', label='光照')
    plt.show()
    plt.figure(4)
    plt.xticks(xlen, time, rotation=45)
    plt.plot(xlen, vol, 'y', label='电压')
    plt.show()
