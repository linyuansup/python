import numpy

x = input("")
x = x.split(' ')
row = len(x) ** 0.5
x = numpy.array(x, dtype=int)
x = x.reshape(int(row), int(row))

eig, vec = numpy.linalg.eig(x)
print("特征值：", eig)
print("特征向量", vec)
