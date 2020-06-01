from PIL import Image, ImageDraw
import RandomSmooth
import Graph_presenter
import math

# Keep these values odd
x = 101
y = 101

spikeness = 100
stretchness = 20
y_starting = y/9

img = Image.new('RGB', (x, y), color='blue')

# Horizontal
for i in range(0, y, stretchness):
    Values = RandomSmooth.SmoothRand(
        y_starting, x*stretchness, y/2, spikeness, stretchness)
    xVert = Values[0]
    shadeHeight = Values[1]
    shade = []
    for k in range(len(shadeHeight)):
        shade.append(int(shadeHeight[k]/y * 265))
    for j in range(0, x, stretchness):
        ImageDraw.Draw(img).point((j, i), (shade[j], shade[j], shade[j], 0))
print("Horizontal finished")

# Vertical
for i in range(0, x, stretchness):
    Values = RandomSmooth.SmoothRand(
        y_starting, x*stretchness, y/2, spikeness, stretchness)
    xVert = Values[0]
    shadeHeight = Values[1]
    shade = []
    for k in range(len(shadeHeight)):
        shade.append(int(shadeHeight[k]/y * 265))
    for j in range(0, y, stretchness):
        currentShade = img.getpixel((i, j))[0]
        newShade = (shade[j] + currentShade)//2
        ImageDraw.Draw(img).point((i, j), (newShade, newShade, newShade, 0))
print("Vertical finished")

# # Diagonal_left
# for j in range(0, y, stretchness):
#     for i in range(0, x, stretchness):
#         Values = RandomSmooth.SmoothRand(
#             y_starting, x*stretchness, y/2, spikeness, stretchness)
#         xVert = Values[0]
#         shadeHeight = Values[1]
#         shade = []
#         for k in range(len(shadeHeight)):
#             shade.append(int(shadeHeight[k]/y * 265))
#         if (i+j < x):
#             # print(j, ": ", i)
#             currentShade = img.getpixel((i+j, i))[0]
#             newShade = (shade[i] + currentShade)//2
#             ImageDraw.Draw(img).point(
#                 (i+j, i), (newShade, newShade, newShade, 0))
# print("Diagonal left finished")

# # Diagonal_right
# for j in range(y, 0, -stretchness):
#     for i in range(0, x, stretchness):
#         Values = RandomSmooth.SmoothRand(
#             y_starting, x*stretchness, y/2, spikeness, stretchness)
#         xVert = Values[0]
#         shadeHeight = Values[1]
#         shade = []
#         for k in range(len(shadeHeight)):
#             shade.append(int(shadeHeight[k]/y * 265))
#         if (i+j < y):
#             currentShade = img.getpixel((i, i+j + 1))[0]
#             newShade = (shade[i] + currentShade)//2
#             ImageDraw.Draw(img).point(
#                 (i, i+j + 1), (newShade, newShade, newShade, 0))
# print("Diagonal right finished")


def CosineInterpolate(y1, y2, mu):
    'mu is the next point: 0 being the current point and 1 being the next point.'
    mu2 = (1-math.cos(mu*math.pi))/2
    return(y1*(1-mu2)+y2*mu2)


# # Vertical Interpolation
# for i in range(0, x, stretchness):
#     for j in range(0, y, stretchness):
#         if (j+stretchness < y):
#             if (img.getpixel((i, j)) != (0, 0, 255)):
#                 upperPixel = img.getpixel((i, j))[0]
#                 uY = j
#                 lowerPixel = img.getpixel((i, j+stretchness))[0]
#                 lY = j + stretchness
#             for k in range(1, stretchness):
#                 # Linear interpolation:
#                 toShade = upperPixel + ((j+k-uY) * ((lowerPixel - upperPixel)/(lY-uY)))

#                 # Cosine interpolation:
#                 # mu = (j+k - uY)/lY
#                 # toShade = CosineInterpolate(upperPixel, lowerPixel, mu)

#                 toShade = int(toShade)
#                 ImageDraw.Draw(img).point(
#                     (i, j+k), (toShade, toShade, toShade, 0))
# print("Vertical interpolation finished")

# # Horizontal Interpolation
# for i in range(0, x, stretchness):
#     for j in range(0, y):
#         if (i+stretchness < x):
#             if (img.getpixel((i, j)) != (0, 0, 255)):
#                 leftPixel = img.getpixel((i, j))[0]
#                 lX = i
#                 rightPixel = img.getpixel((i+stretchness, j))[0]
#                 rX = i+stretchness
#             for k in range(1, stretchness):
#                 # Linear interpolation:
#                 toShade = leftPixel + ((i+k-lX) * ((rightPixel - leftPixel)/(rX-lX)))

#                 # Cosine interpolation:
#                 # mu = (i+k - lX)/rX
#                 # toShade = CosineInterpolate(leftPixel, rightPixel, mu)

#                 toShade = int(toShade)
#                 ImageDraw.Draw(img).point(
#                     (i+k, j), (toShade, toShade, toShade, 0))
# print("Horizontal interpolation finished")

img.save("2D_noise.png")
