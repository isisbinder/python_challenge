#!python3
# Level 8

#1- Get source from http://www.pythonchallenge.com/pc/def/integrity.html
#2- Copy strings from us and pw.

username = 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pwd = 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

import bz2
username = bz2.decompress(username)
pwd = bz2.decompress(pwd)

# Click on bee and use data above.