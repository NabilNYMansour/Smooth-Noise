import matplotlib.pyplot as plt
import scipy.interpolate as interp
import numpy as np
import Graph_presenter

spike = 10
stretch = 10
x_max = 100
y_max = 100

Graph_presenter.Present(y_max/2, x_max, y_max, spike, stretch)
