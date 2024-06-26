our_str = bytearray(b"capitalize")
char = ord('c')
for i in range(len(our_str)):
	if char == our_str[i]:
		our_str[i] = char - 32
print(our_str.decode())
