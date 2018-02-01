from PIL import Image
import datetime
import sys

img1Name = sys.argv[1]
encryptName = sys.argv[2]

def kekusDiferentus(x,y):
    r1,g1,b1 = img1.getpixel((x,y))
    r2,g2,b2 = img2.getpixel((x,y))
    r = r2 - r1
    g = g2 - g1
    b = b2 - b1
    if(r < 0):
        r += 256
    if(b < 0):
        b += 256
    if(g < 0):
        g += 256
    return r,g,b

img1 = Image.open(img1Name)
img2 = Image.open(encryptName)
width = img1.size[0]
height = img1.size[1]
img3 = Image.new("RGB", (width, height), (0,0,0))


for y in range(height):
    for x in range(width):
        img3.putpixel((x,y),kekusDiferentus(x,y))

img2.show()
img3.show()

filename = str(datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))
img3.save(filename + ".BMP", format="BMP")