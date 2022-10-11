import numpy
import matplotlib.pyplot as plt

x = numpy.linspace(0, 2 * numpy.pi, 100)
sin_y = numpy.sin(x)
cos_y = numpy.cos(x)

plt.plot(x, sin_y)
plt.plot(x, cos_y, '-.', color='red')
plt.show()
