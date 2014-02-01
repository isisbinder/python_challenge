#!python3
# Level 3
import urllib
from urllib import urlopen

URL = "http://www.pythonchallenge.com/pc/def/equality.html"
page_source = urlopen(URL).read()

import re
mess_regex = r'<!--(.+)-->'
group = re.findall(mess_regex, page_source, re.DOTALL)[-1].replace('\n', '')
equality_regex = r'[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]'
letters = re.findall(equality_regex, group)
print("http://www.pythonchallenge.com/pc/def/{0}.html".format(''.join(letters)))