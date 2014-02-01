#!python3
# Level 1

CRYPT_MESSAGE = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

from collections import deque
import string
CYPHER_MAP = deque(string.ascii_lowercase)
CYPHER_MAP.rotate(-2)
CYPHER_MAP = ''.join(CYPHER_MAP)

TRANSLATE_TABLE = string.maketrans(string.ascii_lowercase, CYPHER_MAP)
print(CRYPT_MESSAGE.translate(TRANSLATE_TABLE))
print('map'.translate(TRANSLATE_TABLE))