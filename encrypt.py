from PIL import Image
import datetime
import sys

img1Name = sys.argv[1]
img2Name = sys.argv[2]

def kekusPixelus(x1, y1, x2, y2):
    r1,g1,b1 = img1.getpixel((x1,y1))
    r2,g2,b2 = img2.getpixel((x2,y2))
    r = r1 + r2
    g = g1 + g2
    b = b1 + b2
    if(r > 256):
        r -= 256
    if(g > 256):
        g -= 256
    if(b > 256):
        b -= 256
    return r,g,b


img1 = Image.open(str(img1Name))
img2 = Image.open(str(img2Name))
width = img1.size[0]
height = img1.size[1]
img3 = Image.new("RGB", (width,height), (0,0,0))



for y in range(height):
    for x in range(width):
       img3.putpixel((x,y),kekusPixelus(x,y,x,y))


img3.show()
filename = str(datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))
img3.save(filename + ".BMP", format="BMP")