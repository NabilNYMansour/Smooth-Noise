from PIL import Image, ImageDraw
import math
import random

x = 1000
y = 500


def SmoothRandomizer(y_starting, spikenessCoef, y_max, bias):
    randomValue = random.randrange(-spikenessCoef, spikenessCoef)
    if (y_starting < y_max/4):
        randomValue = abs(randomValue) + bias
    if (y_starting > 3*y_max/4):
        randomValue = -(abs(randomValue) + bias)
    return y_starting + randomValue


img = Image.new('RGB', (x, y), color='white')

spikenessCoef = 25
nextValue = y/2
stretchCoef = 50
bias = spikenessCoef
yMax = y

listOfXPoints = []
listOfYPoints = []
for i in range(0, x, stretchCoef):
    listOfXPoints.append(i)
    nextValue = SmoothRandomizer(nextValue, spikenessCoef, yMax, bias)
    listOfYPoints.append(nextValue)

for i in range(1,len(listOfXPoints)):
    ImageDraw.Draw(img).line((listOfXPoints[i - 1], listOfYPoints[i - 1], listOfXPoints[i], listOfYPoints[i]), fill="black")

img.save('pil_red.png')
