our_str = bytearray(b"banana")
char = ord('a')
replace_char = ord('x')
for i in range(len(our_str)):
	if char == our_str[i]:
		our_str[i] = replace_char
print(our_str.decode())
