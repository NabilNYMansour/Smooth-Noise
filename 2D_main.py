from PIL import Image, ImageDraw
import RandomSmooth
import Graph_presenter

x = 1000
y = 1000
img = Image.new('RGB', (x, y), color='white')

spikeness = 1
stretchness = 1
y_starting = y/3

Values = RandomSmooth.SmoothRand(y_starting, x, y/2, spikeness, stretchness)
xVert = Values[0]
shadeHeight = Values[1]

shade = []

for i in range(len(shadeHeight)):
    shade.append(int(shadeHeight[i]/y * 265))
print(shade)
Graph_presenter.Present(y_starting, x, y, spikeness, stretchness)

for i in range(len(xVert)):
    for j in range(0, y, stretchness):
        ImageDraw.Draw(img).point(
            (xVert[i], j), (shade[i], shade[i], shade[i], 0))

for i in range(x):
    for j in range(y):
        # shadeX = 
        pass

img.save("2D_noise.png")
