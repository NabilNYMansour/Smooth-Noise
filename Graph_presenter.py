import matplotlib.pyplot as plt
import scipy.interpolate as interp
import numpy as np
import RandomSmooth


def Present(y_starting, x_max, y_max, spike, stretch):
    Values = RandomSmooth.SmoothRand(y_starting, x_max, y_max, spike, stretch)
    x = Values[0]
    y = Values[1]
    f = interp.interp1d(x, y, kind='quadratic')
    xnew = []

    for i in range(x[-1]):
        xnew.append(i)

    ynew = f(xnew)

    plt.ylim((0, y_max))
    plt.plot(xnew, ynew, '-')

    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title('Graph')

    plt.show()


def Returner(y_starting, x_max, y_max, spike, stretch):
    Values = RandomSmooth.SmoothRand(y_starting, x_max, y_max, spike, stretch)
    xVert = Values[0]
    y = Values[1]
    f = interp.interp1d(xVert, y, kind='quadratic')
    xnew = []

    for i in range(xVert[-1]):
        xnew.append(i)

    return xVert, f(xnew)
