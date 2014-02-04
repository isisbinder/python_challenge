#!python3
# Level 10

import re
def count_digits(term):
	SEQ_REGEX = r'((.)(\2*))'
	elements = re.findall(SEQ_REGEX, term)
	elements = [t[0] for t in elements]
	new_term = [str(len(t))+t[0] for t in elements]
	return ''.join(new_term)

term = '1'
for i in range(30):
	term = count_digits(term)
print(len(term))