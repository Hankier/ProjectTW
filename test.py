import random
from PIL import Image, ImageDraw

FILE = "/home/hankier/git/PlemsyProject/img.png"

img = Image.new('RGB', (4000, 4000), (0, 0, 0))
draw = ImageDraw.Draw(img)


r = 79
g = 105
b = 22
for x in range(0,1000):
    for y in range(0,1000):
        xp = x // 100
        yp = y // 100
        #print(f"P = {xp} | {yp}")
        x1 = 4*x + xp
        y1 = 4*y + yp
        x2 = x1+4
        y2 = y1+4
        #print(f'{x},{y} - {r}, {g}, {b} ', end='')

        if ( x % 100 == 0 and y % 100 == 0):
            pass
        elif ( x % 100 == 0 or y % 100 == 0):
            pass
        else:
            draw.rectangle((x1, y1, x2, y2),fill=(r, g, b))

#print('')
img.save(FILE)


