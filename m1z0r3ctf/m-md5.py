from Crypto.Util.number import *
from hashlib import md5

flag = "m1z0r3{toooo_E4sy_f0r_yoU?}"
assert len(flag) == 27
pad = bytes_to_long(md5(flag).digest())
print len(str(pad))

hack = 0

for char in flag:
	hack+= pad
	hack*= ord(char)
	
print hack
#hack = 8213242002076053911181908692341986030919593545361549673265676083814813944695092587591375250
