import math
from numpy import *
import matplotlib.pyplot as plt
x = linspace(0, 5, 1000)
y = -5 * cos(10 * x) * sin(3 * x) / x ** x
plt.plot(x, y)
plt.show()