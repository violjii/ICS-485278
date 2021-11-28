import math
import pylab
import numpy as np


def function(x):
    """
    cos(x)
    """
    if x == 0:
        return 1.0
    return math.cos(x ** 2) / x


x_min = 0
dx = 0.01
x_list = np.arange(x_min, dx)
y_list = [function(x) for x in x_list]
pylab.plot(y_list)
pylab.show()
