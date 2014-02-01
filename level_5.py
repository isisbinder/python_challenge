#!python3
# Level 5

import urllib
from urllib import urlopen
PICKLE_SOURCE = "http://www.pythonchallenge.com/pc/def/banner.p"
page_source = urlopen(PICKLE_SOURCE).read()

import pickle
pick = pickle.loads(page_source)

new_text = ''
for line in pick:
	new_text += ''.join([char * times for char,times in line]) + '\n'
print(new_text)