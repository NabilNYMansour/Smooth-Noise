import matplotlib.pyplot as plt
import scipy.interpolate as interp
import numpy as np
import RandomSmooth

spike = 250
stretch = 25
x_max = 500
y_max = 500

Values = RandomSmooth.SmoothRand(x_max, y_max, spike, stretch)
x = Values[0]
y = Values[1]

f = interp.interp1d(x, y, kind='quadratic')

xnew = []
for i in range(x[-1]):
    xnew.append(i)

ynew = f(xnew)

plt.ylim((0, y_max))
plt.plot(x, y, '.', xnew, ynew, '-')

plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Graph')

plt.show()
