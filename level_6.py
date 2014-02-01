#!python3
# Level 6
# URL = "http://www.pythonchallenge.com/pc/def/channel.html"

# 1- Download zip file: http://www.pythonchallenge.com/pc/def/channel.zip
# 2- Read readme.txt

import urllib
import zipfile
import re


def read_files(zfile):
	start = '90052'
	NOTHING_REGEX = r'nothing.+?(\d+)'
	file_sequence = []

	while True:
		try:
			file_sequence.append(start)
			fp_content = zfile.open('{0}.txt'.format(start)).read()
			#print('FILE: {0}\n\t{1}'.format(start, fp_content))
			start = re.findall(NOTHING_REGEX, fp_content, re.DOTALL)[-1]
		
		except IndexError:
			break
	return file_sequence

def read_comments(zfile, file_sequence):
	info_list = zfile.infolist()
	comments = ''

	for name in file_sequence:
		info_obj = filter(lambda x: x.filename == name+'.txt', info_list)[-1]
		comments += info_obj.comment
	return comments

print('Retrieving file...')
urllib.urlretrieve("http://www.pythonchallenge.com/pc/def/channel.zip", "channel.zip")
print('Reading file contents...')
zfile = zipfile.ZipFile('channel.zip')
file_sequence = read_files(zfile)
print('Doing as told...')
print(read_comments(zfile, file_sequence))