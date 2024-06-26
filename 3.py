our_str = bytearray(b"hello, world! are you ready?")
char1 = ord('h')
char2 = ord('w')
char3 = ord('a')
char4 = ord('y')
char5 = ord('r')
if char1 == our_str[0]:
	if char2 == our_str[7]:
		if char3 == our_str[14]:
			if char4 == our_str[18]:
				if char5 == our_str[22]:
					our_str[22] = char5 - 32
				our_str[18] = char4 - 32
			our_str[14] = char3 - 32
		our_str[7] = char2 - 32
	our_str[0] = char1 - 32
print(our_str.decode())
