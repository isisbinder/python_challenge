#!python3
# Level 7
# 1- Download image

import urllib
from PIL import Image

urllib.urlretrieve("http://www.pythonchallenge.com/pc/def/oxygen.png", "oxygen.png")
img = Image.open("oxygen.png")
line = 45

pixels = [img.getpixel((i,45)) for i in range(0, img.size[0], 7)]
equals = [p[0] for p in pixels if p[0]==p[1]==p[2]]
message = ''.join(map(chr, equals))

import re
codes = map(int,re.findall(r'\d+', message))
print(''.join(map(chr, codes)))