from PIL import Image, ImageDraw
import math
import random

x = 1000
y = 500


def SmoothRand(x, y, spikenessCoef, stretchCoef):
    def SmoothRandomizer(y_starting, spikenessCoef, y_max, bias):
        randomValue = random.randrange(-spikenessCoef, spikenessCoef)
        if (y_starting < y_max/4):
            randomValue = abs(randomValue) + bias
        if (y_starting > 3*y_max/4):
            randomValue = -(abs(randomValue) + bias)
        return y_starting + randomValue

    nextValue = y/2

    listOfXPoints = []
    listOfYPoints = []
    for i in range(0, x, stretchCoef):
        listOfXPoints.append(i)
        nextValue = SmoothRandomizer(nextValue, spikenessCoef, y, spikenessCoef)
        listOfYPoints.append(nextValue)
    return listOfXPoints, listOfYPoints
