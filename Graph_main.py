import matplotlib.pyplot as plt
import scipy.interpolate as interp
import numpy as np
import Graph_presenter

spike = 50
stretch = 25
x_max = 1000
y_max = 500

Graph_presenter.Present(y_max/2, x_max, y_max, spike, stretch)
