#!python3
# Level 4

import urllib
from urllib import urlopen
URL = "http://www.pythonchallenge.com/pc/def/linkedlist.html"

page_source = urlopen(URL).read().strip()
print(page_source)


# Traverse linkedlist
import re
list_regex = r'nothing.+?(\d+)'
item = page_source
while True:
	URL = "http://www.pythonchallenge.com/pc/def/{0}".format(item)
	page_source = urlopen(URL).read()
	print(URL)
	print(page_source)

	try:
		item = re.findall(list_regex, page_source)[-1].strip()
		
	except IndexError:
		if item.split('=')[1] == '16044':
			item = str(int(item.split('=')[1])//2)
		else: break
	finally:
		item = 'linkedlist.php?nothing=' + item

print("http://www.pythonchallenge.com/pc/def/{0}".format(item))