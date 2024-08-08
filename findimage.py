#! /usr/bin/python2.7
import random
import sys
from PIL import Image, ImageDraw

username = input("Enter username:")
print("Username is: " + username)
im = "999.png"
pattern = "1.png"
samples = 5
#im, pattern, samples = sys.argv [1:]
samples = int (samples)

im = Image.open (im)
walnut = Image.open (pattern)
pixels = []
while len (pixels) < samples:
    x = random.randint (0, walnut.size [0] - 1)
    y = random.randint (0, walnut.size [1] - 1)
    pixel = walnut.getpixel ( (x, y) )
    if pixel [-1] > 200:
        pixels.append ( ( (x, y), pixel [:-1] ) )

def diff (a, b):
    return sum ( (a - b) ** 2 for a, b in zip (a, b) )

best = []

for x in range (im.size [0] ):
    for y in range (im.size [1] ):
        d = 0
        for coor, pixel in pixels:
            try:
                ipixel = im.getpixel ( (x + coor [0], y + coor [1] ) )
                d += diff (ipixel, pixel)
            except IndexError:
                d += 256 ** 2 * 3
        best.append ( (d, x, y) )
        best.sort (key = lambda x: x [0] )
        best = best [:3]

draw = ImageDraw.Draw (im)
for best in best:
    x, y = best [1:]
    print(x + walnut.size [0]/2, y + walnut.size [1]/2)
    draw.rectangle ( (x, y, x + walnut.size [0], y + walnut.size [1] ), outline = 'red')
im.save ('out.png')