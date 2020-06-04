from PIL import Image, ImageDraw, ImageEnhance
import RandomSmooth
import Graph_presenter
import math
from scipy import interpolate
import time

start_time = time.time()

# Keep these values odd
x = 101
y = 101

spikeness = 50
stretchness = 3
y_starting = y/9

Type = "cubic"

img = Image.new('RGB', (x, y), color='blue')
#--------------------------------All_in_one--------------------------------#
def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)


# pixelsShades = {}
# for i in range(0, x, stretchness):
#     for j in range(0, y, stretchness):
#         pixelsShades[(i, j)] = []

# for i in range(0, x, stretchness):
#     for j in range(0, y, stretchness):
#         ImageDraw.Draw(img).point((i, j), 'black')
#         Values = RandomSmooth.SmoothRand(
#             y_starting, x*stretchness, y/2, spikeness, stretchness)
#         xVert = Values[0]
#         shadeHeight = Values[1]
#         shadeHeight = [int(clamp(value, 0, 256)) for value in shadeHeight]
#         # Going upwards:
#         for k in range(j - stretchness, -1, -stretchness):
#             pixelsShades.get((i, k)).append(
#                 shadeHeight[(j-(k+stretchness))//stretchness])
#         # Going downwards:
#         for k in range(j + stretchness, y, stretchness):
#             pixelsShades.get((i, k)).append(
#                 shadeHeight[(k-(j+stretchness))//stretchness])
#             # Going left:
#         for k in range(i + stretchness, x, stretchness):
#             pixelsShades.get((k, j)).append(
#                 shadeHeight[(k-(i+stretchness))//stretchness])
#             # Going right:
#         for k in range(i - stretchness, -1, -stretchness):
#             pixelsShades.get((k, j)).append(
#                 shadeHeight[(i-(k+stretchness))//stretchness])

# # Drawing the shades:
# for i in range(0, x, stretchness):
#     for j in range(0, y, stretchness):
#         finalShade = pixelsShades.get((i, j))[0]
#         length = len(pixelsShades.get((i, j)))
#         for k in range(1, length):
#             finalShade += pixelsShades.get((i, j))[k]
#         finalShade = finalShade//length
#         ImageDraw.Draw(img).point((i, j), (finalShade, finalShade, finalShade, 0))
# print("Randomizer finished")
# print("--- %s seconds ---" % (time.time() - start_time))
# img.save("2D_noise.png")

#--------------------------------Horizontal--------------------------------#
for i in range(0, y, stretchness):
    Values = RandomSmooth.SmoothRand(
        y_starting, x*stretchness, y/2, spikeness, stretchness)
    xVert = Values[0]
    shadeHeight = Values[1]
    shade = [int(abs(value/y) * 265) for value in shadeHeight]
    for j in range(0, x, stretchness):
        ImageDraw.Draw(img).point((j, i), (shade[j], shade[j], shade[j], 0))
print("Horizontal finished")
print("--- %s seconds ---" % (time.time() - start_time))
img.save("2D_noise.png")

#---------------------------------Vertical--------------------------------#
for i in range(0, x, stretchness):
    Values = RandomSmooth.SmoothRand(
        y_starting, x*stretchness, y/2, spikeness, stretchness)
    xVert = Values[0]
    shadeHeight = Values[1]
    shade = [int(abs(value/y) * 265) for value in shadeHeight]
    for j in range(0, y, stretchness):
        currentShade = img.getpixel((i, j))[0]
        newShade = (shade[j] + currentShade)//2
        ImageDraw.Draw(img).point((i, j), (newShade, newShade, newShade, 0))
print("Vertical finished")
print("--- %s seconds ---" % (time.time() - start_time))
img.save("2D_noise.png")

#------------------------------Diagonal_left------------------------------#
# for j in range(0, y, stretchness):
#     Values = RandomSmooth.SmoothRand(y_starting, x*stretchness, y/2, spikeness, stretchness)
#     xVert = Values[0]
#     shadeHeight = Values[1]
#     shade = [int(abs(value/y) * 265) for value in shadeHeight]
#     for i in range(0, x, stretchness):
#         if (i+j < x):
#             currentShade = img.getpixel((i+j, i))[0]
#             newShade = (shade[i] + currentShade)//2
#             ImageDraw.Draw(img).point(
#                 (i+j, i), (newShade, newShade, newShade, 0))
# print("Diagonal left finished")
# print("--- %s seconds ---" % (time.time() - start_time))
# img.save("2D_noise.png")

# -----------------------------Diagonal_right-----------------------------#
# for j in range(y, 0, -stretchness):
#     Values = RandomSmooth.SmoothRand(y_starting, x*stretchness, y/2, spikeness, stretchness)
#     xVert = Values[0]
#     shadeHeight = Values[1]
#     shade = [int(abs(value/y) * 265) for value in shadeHeight]
#     for i in range(0, x, stretchness):
#         if (i+j <= y):
#             currentShade = img.getpixel((i, i+j - 1))[0]
#             newShade = (shade[i] + currentShade)//2
#             ImageDraw.Draw(img).point(
#                 (i, i+j - 1), (newShade, newShade, newShade, 0))
# print("Diagonal right finished")
# print("--- %s seconds ---" % (time.time() - start_time))
# img.save("2D_noise.png")

#------------------------------Interpolation------------------------------#
for j in range(0, y, stretchness):
    shades = []
    xVert = []
    for k in range(0, x, stretchness):
        shades.append(img.getpixel((k, j))[0])
        xVert.append(k)
    f = interpolate.interp1d(xVert, shades, kind=Type)
    for i in range(0, k):
        # Finding the values:
        shade = int(f(i))
        ImageDraw.Draw(img).point((i, j), (shade, shade, shade, 0))
print("Horizontal interpolation finished")
print("--- %s seconds ---" % (time.time() - start_time))
img.save("2D_noise.png")

for i in range(0, x):
    shades = []
    xVert = []
    for k in range(0, y, stretchness):
        shades.append(img.getpixel((i, k))[0])
        xVert.append(k)
    f = interpolate.interp1d(xVert, shades, kind=Type)
    for j in range(0, k):
        shade = int(f(j))
        ImageDraw.Draw(img).point((i, j), (shade, shade, shade, 0))
print("Interpolation finished")

enchancer = ImageEnhance.Sharpness(img)
cropAmount = 10
# img = enchancer.enhance(10)
img = img.crop((cropAmount,cropAmount,x-cropAmount,y-cropAmount))
img.save("2D_noise.png")
print("--- %s seconds ---" % (time.time() - start_time))
