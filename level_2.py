#!python3
# Level 2

from urllib import urlopen
page_source = urlopen("http://www.pythonchallenge.com/pc/def/ocr.html").read()

import re
mess_regex = r'<!--.+-->\s*<!--(.+)-->'
groups = re.findall(mess_regex, page_source, re.DOTALL)
mess = groups[-1].replace('\n','')

from collections import Counter
occurrences = Counter(mess)
for k,v in occurrences.viewitems():
	if v > 6:
		mess = mess.replace(k, '')
print(mess)
print("http://www.pythonchallenge.com/pc/def/{0}.html".format(mess))